@allure.label.epic:CadastroFuncionário
Feature: Cadastro de funcionário

    @test
    @allure.label.story:Labels
    Scenario: Cadastro de funcionário com campos vazios
        Given O usuário está na página do portal de testes SEA Tecnologia
        When O botão adicionar funcionário é selecionado
        And O cadastro é salvo com os campos vazios
        Then Um alerta de preenchimento é apresentado

