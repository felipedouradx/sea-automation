from unittest import TestCase
from behave import *
from selenium.webdriver.common.by import By

from pages.home_page import  HomePage

use_step_matcher("parse")
assertions = TestCase()


@given("O usuário está na página do portal de testes SEA Tecnologia")
def step_impl(context):
    pass


@when("O filtro Ver apenas ativos é selecionado")
def step_impl(context):
    home_page = HomePage(context)
    home_page.selecionar_filtros_ativos()


@step("O botão Limpar filtros é pressionado")
def step_impl(context):
    home_page = HomePage(context)
    home_page.selecionar_limpar_filtros()


@then("Os filtros são limpos")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Os filtros são limpos')


@then("Os funcionários com status ativo são listados")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Os funcionários com status ativo são listados')


@when("O menu de opções do funcionário é selecionado")
def step_impl(context):
    home_page = HomePage(context)
    home_page.selecionar_menu_opcoes_perfil()


@then("A opção Editar funcionário é selecionada")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then A opção Editar funcionário é selecionada')


@then("A opção Excluir funcionário é selecionada")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then A opção Excluir funcionário é selecionada')


@when("O item {item} do menu lateral é selecionado")
def step_impl(context, item):
    home_page = HomePage(context)
    home_page.selecionar_item_menu_lateral(item)


@then("A navegação pelo item {item} do menu lateral é validada")
def step_impl(context, item):
    if item == 'edit':
        text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), 'Funcionário(s)')]")
        text = text_element.text
        assert 'Funcionário(s)' == text, f"Expected text 'Funcionário(s)' but got '{text}'"
    else:
        text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), 'Em Breve')]")
        text = text_element.text
        assert 'Em Breve' == text, f"Expected text 'Em Breve' but got '{text}'"