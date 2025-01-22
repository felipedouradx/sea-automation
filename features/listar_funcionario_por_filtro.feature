@allure.label.epic:HomePage
Feature: Listar funcionário por filtro

    @ok
    @allure.label.story:Labels
    Scenario: Listar funcionário por filtro
        Given O usuário está na página do portal de testes SEA Tecnologia
        When O filtro Ver apenas ativos é selecionado
        And O número de funcionários ativos é verificado
        Then Os funcionários ativos são listados