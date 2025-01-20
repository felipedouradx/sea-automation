from unittest import TestCase
from behave import *

use_step_matcher("parse")
assertions = TestCase()


@given("O usuário está na página do portal de testes SEA Tecnologia")
def step_impl(context):
    pass
