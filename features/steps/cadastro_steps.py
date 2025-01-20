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


@step("O status do trabalhador Ativo é informado")
def step_impl(context):
    cadastro_page = CadastroPage(context)
    cadastro_page.informar_status_funcionario()


@step("O campo nome {nome} é preenchido")
def step_impl(context, nome):
    cadastro_page = CadastroPage(context)
    cadastro_page.inserir_nome(nome)


@step("O sexo é informado")
def step_impl(context):
    cadastro_page = CadastroPage(context)
    cadastro_page.informar_sexo()


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


@step("O cargo 2 é selecionado")
def step_impl(context):
    cadastro_page = CadastroPage(context)
    cadastro_page.selecionar_cargo()


@step("A atividade é selecionada")
def step_impl(context):
    cadastro_page = CadastroPage(context)
    cadastro_page.selecionar_atividade()


@step("O CA {ca} é informado")
def step_impl(context, ca):
    cadastro_page = CadastroPage(context)
    cadastro_page.inserir_ca(ca)


@step("O EPI {epi} é adicionado")
def step_impl(context, epi):
    cadastro_page = CadastroPage(context)
    cadastro_page.adicionar_epi(epi)


@step("O arquivo do atestado de saúde é inserido")
def step_impl(context):
    cadastro_page = CadastroPage(context)
    cadastro_page.adicionar_atestado()


@then("O cadastro do funcionário é realizado com sucesso")
def step_impl(context):
    elemento = context.browser.find_element(By.XPATH, "//p[contains(text(),'Hello')]")
    actual_text = elemento.text
    assert partial_text in actual_text, f"Expected text to contain '{partial_text}', but found '{actual_text}'"