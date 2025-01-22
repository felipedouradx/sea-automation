@allure.label.epic:CadastroFuncionário
Feature: Cadastro de funcionário com uso de EPI e sem Atestado de Saúde

    @test
    @allure.label.story:Labels
    Scenario Outline: Cadastro de funcionário sem EPI e sem Atestado de Saúde
        Given O usuário está na página do portal de testes SEA Tecnologia
        When O botão adicionar funcionário é selecionado
        And O status <status> do trabalhador é informado
        And O campo nome <nome> é preenchido
        And O gênero <genero> é informado
        And O campo CPF <cpf> é preenchido
        And A data de nascimento <data_nascimento> é informada
        And O RG <rg> é informado
        And A opção uso de EPI <uses_epi> é selecionada
        And O cargo <cargo> é selecionado
        And O equipamento <epi> é selecionado <uses_epi>
        And O CA <ca> é informado para a seleção de uso do EPI <uses_epi>
        And A atividade <atividade> é selecionada para o uso de epi <uses_epi>
        And O cadastro é salvo
        Then O cadastro é validado via API <nome> <status> <genero> <cpf> <rg> <ca> <data_nascimento> <cargo> <atividade> <uses_epi> <epi>


    Examples:
      | nome      | cpf         | data_nascimento | rg      | ca    | status  | genero    | cargo | atividade | uses_epi | epi                   |
      | Tester    | 11122233344 | 01012000        | 1234567 | 00001 | Inativo | feminino  | 02    | 00        | False    | **                    |
      | Tester    | 11122233344 | 01012000        | 1234567 | 00001 | Ativo   | masculino | 03    | 04        | True     | Luvas descartáveis    |
      | Tester    | 11122233344 | 01012000        | 1234567 | 00001 | Ativo   | masculino | 02    | 00        | False    | **                    |
      | Tester    | 11122233344 | 01012000        | 1234567 | 00001 | Ativo   | masculino | 03    | 01        | True     | Protetor auditivo     |
      | Tester    | 11122233344 | 01012000        | 1234567 | 00001 | Ativo   | masculino | 04    | 05        | True     | Capacete de segurança |
