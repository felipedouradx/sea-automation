@allure.label.epic:HomePage
Feature: Validar botão Adicionar Funcionário
    #SEA-10

    @ok
    @allure.label.story:Labels
    Scenario: Validar botão Adicionar Funcionário
        Given O usuário está na página do portal de testes SEA Tecnologia
        When O botão adicionar funcionário é selecionado
        Then O formulário de cadastro é apresentado


