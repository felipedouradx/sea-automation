@allure.label.epic:HomePage
Feature: Validar itens do menu lateral

    @ok
    @allure.label.story:Labels
    Scenario Outline: Validar itens do menu lateral
        Given O usuário está na página do portal de testes SEA Tecnologia
        When O item <item> do menu lateral é selecionado
        Then A navegação pelo item <item> do menu lateral é validada

    Examples:
      | item          |
      | home          |
      | edit          |
      | tree          |
      | notifications |
      | history       |
      | profile       |


