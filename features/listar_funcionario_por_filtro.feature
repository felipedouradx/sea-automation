@allure.label.epic:CadastroFuncionário
Feature: Cadastro de funcionário com uso de EPI e sem Atestado de Saúde

    @test
    @allure.label.story:Labels
    Scenario: Cadastro de funcionário sem EPI e sem Atestado de Saúde
        Given O usuário está na página do portal de testes SEA Tecnologia
        When O filtro Ver apenas ativos é selecionado
        And O botão Limpar filtros é pressionado
        Then Os filtros são limpos


