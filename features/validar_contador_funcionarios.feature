@allure.label.epic:HomePage
Feature: Validar contador de funcionários

    @ok
    @allure.label.story:Labels
    Scenario: Validar contador de funcionários
        Given O usuário está na página do portal de testes SEA Tecnologia
        When O filtro Ver apenas ativos é selecionado
        And O número de funcionários ativos é verificado
        And O botão Limpar filtros é pressionado
        And O número total de funcionários é verificado
        Then O contador é validado com sucesso


