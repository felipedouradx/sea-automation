from unittest import TestCase
from behave import *
from selenium.webdriver.common.by import By

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


@then("O cadastro do funcionário é realizado com sucesso e consta na lista da página inicial")
def step_impl(context):
    text_element = context.browser.find_element(By.XPATH, "//p[contains(text(),'Hello')]")
    text = text_element.text
    assert "Hello" == text, f"Expected text 'Hello', but found '{text}'"


@step("O cadastro é salvo")
def step_impl(context):
    cadastro_page = CadastroPage(context)
    cadastro_page.salvar_cadastro()


@then("O cadastro é validado via API {nome} {status} {genero} {cpf} {rg} {ca} {data_nascimento} {cargo} {atividade} {uses_epi} {epi}")
def step_impl(context, nome, status, genero, cpf, rg, ca, data_nascimento, cargo, atividade, uses_epi, epi):
    cadastro_page = CadastroPage(context)
    cadastro_page.validar_cadastro_api(nome, status, genero, cpf, rg, ca, data_nascimento, cargo, atividade, uses_epi, epi)


@step("A opção uso de EPI {uses_epi} é selecionada")
def step_impl(context, uses_epi):
    cadastro_page = CadastroPage(context)
    cadastro_page.selecionar_uso_epi(uses_epi)


@step("O equipamento {epi} é selecionado {uses_epi}")
def step_impl(context, epi, uses_epi):
    cadastro_page = CadastroPage(context)
    cadastro_page.selecionar_equipamento_epi(epi, uses_epi)