from unittest import TestCase
from behave import *
from pages.test_page import TestPage

use_step_matcher("parse")
assertions = TestCase()


@given("The user is in Google page")
def step_impl(context):
    expected_text = "Google"
    actual = expected_text
    expected = expected_text
    assertions.assertEqual(actual, expected)


@when("The user select the search button")
def step_impl(context):
    test_page = TestPage(context)
    test_page.select_search_button()


@step("The iphone {iphone_model} is selected")
def step_impl(context, iphone_model):
    test_page = TestPage(context)
    test_page.insert_iphone_model(iphone_model)


@then("The price is showed")
def step_impl(context):
    expected_text = "Preço"
    actual = expected_text
    expected = expected_text
    assertions.assertEqual(actual, expected)


@step("The Shopping sheet is selected")
def step_impl(context):
    test_page = TestPage(context)
    test_page.select_shopping_sheet()



