@allure.label.epic:HomePage
Feature: Listar funcionário por filtro

    @test
    @allure.label.story:Labels
    Scenario: Cadastro de funcionário sem EPI e sem Atestado de Saúde
        Given O usuário está na página do portal de testes SEA Tecnologia
        When O filtro Ver apenas ativos é selecionado
        Then Os funcionários com status ativo são listados

