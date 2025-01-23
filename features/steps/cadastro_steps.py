from unittest import TestCase
from behave import *
from selenium.common import TimeoutException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import datetime
import random
import string

from selenium.webdriver.support.wait import WebDriverWait

from lib.selenium_helper import Helpers
from pages.cadastro_page import CadastroPage

use_step_matcher("parse")
assertions = TestCase()


@when("O botão adicionar funcionário é selecionado")
def step_impl(context):
    cadastro_page = CadastroPage(context)
    cadastro_page.selecionar_add_funcionario()


@step("O status {status} do trabalhador é informado")
def step_impl(context, status):
    cadastro_page = CadastroPage(context)
    cadastro_page.informar_status_funcionario(status)


@step("O campo nome {nome} é preenchido")
def step_impl(context, nome):
    cadastro_page = CadastroPage(context)
    cadastro_page.inserir_nome(nome)


@step("O gênero {genero} é informado")
def step_impl(context, genero):
    cadastro_page = CadastroPage(context)
    cadastro_page.informar_genero(genero)


@step("O campo CPF {cpf} é preenchido")
def step_impl(context, cpf):
    cadastro_page = CadastroPage(context)
    cadastro_page.inserir_cpf(cpf)


@step("A data de nascimento {data_nascimento} é informada")
def step_impl(context, data_nascimento):
    cadastro_page = CadastroPage(context)
    cadastro_page.inserir_data(data_nascimento)


@step("O RG {rg} é informado")
def step_impl(context, rg):
    cadastro_page = CadastroPage(context)
    cadastro_page.inserir_rg(rg)


@step("O cargo {cargo} é selecionado")
def step_impl(context, cargo):
    cadastro_page = CadastroPage(context)
    cadastro_page.selecionar_cargo(cargo)


@step("A atividade {atividade} é selecionada para o uso de epi {uses_epi}")
def step_impl(context, atividade, uses_epi):
    cadastro_page = CadastroPage(context)
    cadastro_page.selecionar_atividade(atividade, uses_epi)


@step("O CA {ca} é informado para a seleção de uso do EPI {uses_epi}")
def step_impl(context, ca, uses_epi):
    cadastro_page = CadastroPage(context)
    cadastro_page.inserir_ca(ca, uses_epi)


@step("O EPI {epi} é adicionado")
def step_impl(context, epi):
    cadastro_page = CadastroPage(context)
    cadastro_page.adicionar_epi(epi)


@step("O arquivo do atestado de saúde é inserido")
def step_impl(context):
    cadastro_page = CadastroPage(context)
    cadastro_page.adicionar_atestado()


@then("O cadastro do funcionário é finalizado e consta na lista da página inicial")
def step_impl(context):
    cadastro_page = CadastroPage(context)
    cadastro_page.validar_cadastro_funcionario()


@step("O cadastro é salvo")
def step_impl(context):
    cadastro_page = CadastroPage(context)
    cadastro_page.salvar_cadastro()


@then(
    "O cadastro é validado via API {nome} {status} {genero} {cpf} {rg} {ca} {data_nascimento} {cargo} {atividade} {uses_epi} {epi}")
def step_impl(context, nome, status, genero, cpf, rg, ca, data_nascimento, cargo, atividade, uses_epi, epi):
    cadastro_page = CadastroPage(context)
    cadastro_page.validar_cadastro_api(nome, status, genero, cpf, rg, ca, data_nascimento, cargo, atividade, uses_epi,
                                       epi)


@step("A opção uso de EPI {uses_epi} é selecionada")
def step_impl(context, uses_epi):
    cadastro_page = CadastroPage(context)
    cadastro_page.selecionar_uso_epi(uses_epi)


@step("O equipamento {epi} é selecionado {uses_epi}")
def step_impl(context, epi, uses_epi):
    cadastro_page = CadastroPage(context)
    cadastro_page.selecionar_equipamento_epi(epi, uses_epi)


@step("O campo nome é preenchido com valor aleatório e timestamp para validação")
def step_impl(context):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    letras_aleatorias = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    nome_aleatorio = f"{timestamp}_{letras_aleatorias}"
    context.nome_aleatorio = nome_aleatorio
    cadastro_page = CadastroPage(context)
    cadastro_page.preencher_nome_aleatorio()


@step("O cadastro é salvo com os campos vazios")
def step_impl(context):
    cadastro_page = CadastroPage(context)
    cadastro_page.salvar_cadastro()


@then("Um alerta de preenchimento é apresentado")
def step_impl(context):
    try:
        wait = WebDriverWait(context, 2)
        wait.until(EC.alert_is_present())
    except NoAlertPresentException:
        print('Mensagem de erro não visível')
        raise NoAlertPresentException


@then("O cadastro de funcionário com atestado de saúde {file_name} é validado via API")
def step_impl(context, file_name):
    cadastro_page = CadastroPage(context)
    cadastro_page.validar_cadastro_funcionario_com_arquivo(file_name)


@then("O arquivo é anexado ao cadastro com sucesso")
def step_impl(context):
    helpers = Helpers(context)
    helpers.selenium_wait_presence(2, By.XPATH, f"//*[contains(text(), 'teste_atestado.pdf')]")
    text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), 'teste_atestado.pdf')]")
    text = text_element.text
    assert 'teste_atestado.pdf' == text, f"Expected text 'teste_atestado.pdf' but got '{text}'"


@then("O formulário de cadastro é apresentado")
def step_impl(context):
    text_element = context.browser.find_element(By.XPATH,
                                                f"//*[contains(text(), 'O trabalhador está ativo ou inativo?')]")
    text = text_element.text
    assert 'O trabalhador está ativo ou inativo?' == text, f"Expected text 'O trabalhador está ativo ou inativo?' but got '{text}'"


@then("O opção Adicionar outra atividade é selecionada")
def step_impl(context):
    cadastro_page = CadastroPage(context)
    cadastro_page.selecionar_nova_atividade()
    nova_atividade_element = context.browser.find_elements(By.XPATH, "//*[contains(text(), 'Selecione a atividade:')]")
    elements_count = len(nova_atividade_element)
    if elements_count == 2:
        print("More than one 'Selecione a atividade:' exists.")
    else:
        print("One or no 'Selecione a atividade:' exists.")
        raise AssertionError


@then("O opção Adicionar EPI é selecionada")
def step_impl(context):
    cadastro_page = CadastroPage(context)
    cadastro_page.selecionar_adicionar_epi()
    adicionar_epi_element = context.browser.find_elements(By.XPATH, "//*[contains(text(), 'Selecione o EPI:')]")
    elements_count = len(adicionar_epi_element)
    if elements_count == 2:
        print("More than one 'Selecione o EPI:' exists.")
    else:
        print("One or no 'Selecione o EPI:' exists.")
        raise AssertionError


@when("O número de funcionários ativos é verificado")
def step_impl(context):
    lista_ativos_element = context.browser.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div[2]/div[2]/div')
    child_elements = lista_ativos_element.find_elements(By.XPATH, './*')
    context.lista_ativos = len(child_elements)


@step("O número total de funcionários é verificado")
def step_impl(context):
    lista_todos_element = context.browser.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div[2]/div[2]/div')
    child_elements = lista_todos_element.find_elements(By.XPATH, './*')
    context.lista_todos = len(child_elements)


@then("O contador é validado com sucesso")
def step_impl(context):
    helpers = Helpers(context)
    helpers.selenium_wait_presence(2, By.XPATH, '/html/body/div/main/div[2]/div[2]/div[2]/div[2]/span')
    contador_element = context.browser.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div[2]/div[2]/span')
    span_text = contador_element.text.strip()

    lista_ativos_str = str(context.lista_ativos)
    lista_todos_str = str(context.lista_todos)

    assert lista_ativos_str in span_text and lista_todos_str in span_text, \
        f"Assertion failed! Expected 'Ativos {lista_ativos_str}/{lista_todos_str}' in '{span_text}'"


@then('O formato do CPF {cpf} é validado')
def step_validar_formato_cpf(context, cpf):
    cpf_field = context.browser.find_element(By.XPATH, "//input[@name='cpf']")
    cpf_value = cpf_field.get_attribute("value").strip()
    num_digits = len([digit for digit in cpf_value if digit.isdigit()])
    if num_digits < 11:
        raise AssertionError(
            f"CPF has only {num_digits} digits. Please add {11 - num_digits} more digit(s) to make it exactly 11."
        )
    if num_digits > 11:
        truncated_value = ''.join([digit for digit in cpf_value if digit.isdigit()])[:11]
        raise AssertionError(
            f"CPF has {num_digits} digits. Only the first 11 digits '{truncated_value}' have been saved. "
            "Please ensure the CPF has exactly 11 digits."
        )
    assert num_digits == 11, f"Expected 11 digits, but got {num_digits} in '{cpf_value}'"
    assert cpf_value.isdigit(), f"CPF contains invalid characters: {cpf_value}"

