import time
from unittest import TestCase
from behave import *
from selenium.webdriver.common.by import By

from pages.home_page import HomePage

use_step_matcher("parse")
assertions = TestCase()


@given("O usuário está na página do portal de testes SEA Tecnologia")
def step_impl(context):
    time.sleep(1)
    expected_url = "https://analista-teste.seatecnologia.com.br/"
    assert context.browser.current_url == expected_url, f"Expected URL to be {expected_url} but got {context.current_url}"


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
    if context.lista_ativos == context.lista_todos:
        assert True
    elif context.lista_ativos < context.lista_todos:
        assert True
    else:
        assert False


@when("O menu de opções do funcionário é selecionado")
def step_impl(context):
    home_page = HomePage(context)
    home_page.selecionar_menu_opcoes_perfil()


@then("A opção Editar funcionário é selecionada")
def step_impl(context):
    text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), 'Alterar')]")
    text = text_element.text
    assert 'Alterar' == text, f"Expected text 'Alterar' but got '{text}'"


@then("A opção Excluir funcionário é selecionada")
def step_impl(context):
    text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), 'Excluir')]")
    text = text_element.text
    assert 'Excluir' == text, f"Expected text 'Excluir' but got '{text}'"


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


@when("O item {item} do menu superior é selecionado")
def step_impl(context, item):
    home_page = HomePage(context)
    home_page.selecionar_item_menu_superior(item)


@then("A navegação pelo item {item} do menu superior é validada")
def step_impl(context, item):
    expected_texts = {
        '1': 'Funcionário(s)',
        '2': 'Em Breve',
        '3': 'Em Breve',
        '4': 'Em Breve',
        '5': 'Em Breve',
        '6': 'Em Breve',
        '7': 'Em Breve',
        '8': 'Em Breve',
        '9': 'Em Breve'
    }

    if item not in expected_texts:
        raise ValueError(f"Unexpected item '{item}' received. Expected values: {list(expected_texts.keys())}")

    expected_text = expected_texts[item]
    text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), '{expected_text}')]")
    actual_text = text_element.text

    assert expected_text == actual_text, f"Expected text '{expected_text}' but got '{actual_text}'"


@when("A opção Etapa concluída é selecionada")
def step_impl(context):
    home_page = HomePage(context)
    home_page.selecionar_botao_etapa_concluida()


@then("O status Concluído é definido no item 1")
def step_impl(context):
    text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), 'CONCLUIDO')]")
    text = text_element.text
    assert 'CONCLUIDO' == text, f"Expected text 'CONCLUIDO' but got '{text}'"


@step("O botão Próximo passo é selecionado")
def step_impl(context):
    home_page = HomePage(context)
    home_page.selecionar_proximo_passo()


@then("O item 2 é acessado")
def step_impl(context):
    home_page = HomePage(context)
    home_page.selecionar_item_2_menu_superior()
    text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), 'Em Breve')]")
    text = text_element.text
    assert 'Em Breve' == text, f"Expected text 'Em Breve' but got '{text}'"
    text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), 'Concluído')]")
    text = text_element.text
    assert 'Concluído' == text, f"Expected text 'Concluído' but got '{text}'"


@then("O item 3 é acessado")
def step_impl(context):
    home_page = HomePage(context)
    home_page.selecionar_item_3_menu_superior()
    text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), 'Em Breve')]")
    text = text_element.text
    assert 'Em Breve' == text, f"Expected text 'Em Breve' but got '{text}'"
    elements_count = len(context.browser.find_elements_by_xpath("//*[contains(text(), 'CONCLUIDO')]"))
    if elements_count == 2:
        print("More than one 'Concluído' exists.")
    else:
        print("One or no 'Concluído' exists.")
        raise Exception


@then("O item 4 é acessado")
def step_impl(context):
    home_page = HomePage(context)
    home_page.selecionar_item_4_menu_superior()
    text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), 'Em Breve')]")
    text = text_element.text
    assert 'Em Breve' == text, f"Expected text 'Em Breve' but got '{text}'"
    elements_count = len(context.browser.find_elements_by_xpath("//*[contains(text(), 'CONCLUIDO')]"))
    if elements_count == 3:
        print("More than one 'Concluído' exists.")
    else:
        print("One or no 'Concluído' exists.")
        raise Exception


@then("O item 5 é acessado")
def step_impl(context):
    home_page = HomePage(context)
    home_page.selecionar_item_5_menu_superior()
    text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), 'Em Breve')]")
    text = text_element.text
    assert 'Em Breve' == text, f"Expected text 'Em Breve' but got '{text}'"
    elements_count = len(context.browser.find_elements_by_xpath("//*[contains(text(), 'CONCLUIDO')]"))
    if elements_count == 4:
        print("More than one 'Concluído' exists.")
    else:
        print("One or no 'Concluído' exists.")
        raise Exception


@then("O item 6 é acessado")
def step_impl(context):
    home_page = HomePage(context)
    home_page.selecionar_item_6_menu_superior()
    text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), 'Em Breve')]")
    text = text_element.text
    assert 'Em Breve' == text, f"Expected text 'Em Breve' but got '{text}'"
    elements_count = len(context.browser.find_elements_by_xpath("//*[contains(text(), 'CONCLUIDO')]"))
    if elements_count == 5:
        print("More than one 'Concluído' exists.")
    else:
        print("One or no 'Concluído' exists.")
        raise Exception


@then("O item 7 é acessado")
def step_impl(context):
    home_page = HomePage(context)
    home_page.selecionar_item_7_menu_superior()
    text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), 'Em Breve')]")
    text = text_element.text
    assert 'Em Breve' == text, f"Expected text 'Em Breve' but got '{text}'"
    elements_count = len(context.browser.find_elements_by_xpath("//*[contains(text(), 'CONCLUIDO')]"))
    if elements_count == 6:
        print("More than one 'Concluído' exists.")
    else:
        print("One or no 'Concluído' exists.")
        raise Exception


@then("O item 8 é acessado")
def step_impl(context):
    home_page = HomePage(context)
    home_page.selecionar_item_8_menu_superior()
    text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), 'Em Breve')]")
    text = text_element.text
    assert 'Em Breve' == text, f"Expected text 'Em Breve' but got '{text}'"
    elements_count = len(context.browser.find_elements_by_xpath("//*[contains(text(), 'CONCLUIDO')]"))
    if elements_count == 7:
        print("More than one 'Concluído' exists.")
    else:
        print("One or no 'Concluído' exists.")
        raise Exception


@then("O item 9 é acessado")
def step_impl(context):
    home_page = HomePage(context)
    home_page.selecionar_item_9_menu_superior()
    text_element = context.browser.find_element(By.XPATH, f"//*[contains(text(), 'Em Breve')]")
    text = text_element.text
    assert 'Em Breve' == text, f"Expected text 'Em Breve' but got '{text}'"
    elements_count = len(context.browser.find_elements_by_xpath("//*[contains(text(), 'CONCLUIDO')]"))
    if elements_count == 8:
        print("More than one 'Concluído' exists.")
    else:
        print("One or no 'Concluído' exists.")
    raise Exception


@then("Os funcionários ativos são listados")
def step_impl(context):
    assert context.lista_ativos > 0, f"'É esperado funcionários ativos, conforme o protótipo. Found: {context.lista_ativos}'"
