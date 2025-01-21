@allure.label.epic:CadastroFuncionário
Feature: Cadastro de funcionário sem uso de EPI

    @test
    @allure.label.story:Labels
    Scenario Outline: Cadastro de funcionário
        Given O usuário está na página do portal de testes SEA Tecnologia
        When O botão adicionar funcionário é selecionado
        And O status <status> do trabalhador é informado
        And O campo nome <nome> é preenchido
        And O gênero <genero> é informado
        And O campo CPF <cpf> é preenchido
        And A data de nascimento <data_nascimento> é informada
        And O RG <rg> é informado
        And A opção uso de EPI <epi> é selecionada
        And O cargo <cargo> é selecionado
        And A atividade <atividade> é selecionada
        And O CA <ca> é informado para a seleção de uso do EPI <epi>
        And O CA <ca> é informado para a seleção de uso do EPI <epi>
        And O cadastro é salvo
        Then O cadastro é validado via API <nome> <status> <genero> <cpf> <rg> <ca> <data_nascimento> <cargo> <atividade>


    Examples:
      | nome      | cpf         | data_nascimento | rg      | ca    | status | genero    | cargo | atividade |
      | Tester    | 11122233344 | 01012000        | 1234567 | 00001 | Ativo  | feminino  | 01    | 02        |
      | Tester    | 11122233344 | 01012000        | 1234567 | 00001 | Ativo  | feminino  | 02    | 01        |
      | Tester    | 11122233344 | 01012000        | 1234567 | 00001 | Ativo  | masculino | 02    | 02        |
      | Tester    | 11122233344 | 01012000        | 1234567 | 00001 | Ativo  | masculino | 03    | 03        |
      | Tester    | 11122233344 | 01012000        | 1234567 | 00001 | Ativo  | masculino | 04    | 05        |


