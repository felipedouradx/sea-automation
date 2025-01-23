@allure.label.epic:HomePage
Feature: Limpar filtros
    #SEA-06

    @ok
    @allure.label.story:Labels
    Scenario: Limpar filtros de busca
        Given O usuário está na página do portal de testes SEA Tecnologia
        When O filtro Ver apenas ativos é selecionado
        And O número de funcionários ativos é verificado
        And O botão Limpar filtros é pressionado
        And O número total de funcionários é verificado
        Then Os filtros são limpos

