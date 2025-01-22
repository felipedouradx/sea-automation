@allure.label.epic:HomePage
Feature: Validar campo CPF

    @ok
    @allure.label.story:Labels
    Scenario Outline: Validar formato e tamanho de caracteres do campo CPF
      Given O usuário está na página do portal de testes SEA Tecnologia
      When O botão adicionar funcionário é selecionado
      And O campo CPF <cpf> é preenchido
      Then O formato do CPF <cpf> é validado

    Examples:
      | cpf                   |
      | 8888 |




