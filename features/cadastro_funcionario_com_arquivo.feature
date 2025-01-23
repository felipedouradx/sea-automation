@allure.label.epic:CadastroFuncionário
Feature: Cadastro de funcionário com inserção de arquivo
    #SEA-02

    @ok
    @allure.label.story:Labels
    Scenario Outline: Cadastro de funcionário com Atestado de Saúde
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
        And O arquivo do atestado de saúde é inserido
        Then O arquivo é anexado ao cadastro com sucesso
        And O cadastro é salvo
        Then O cadastro de funcionário com atestado de saúde <file_name> é validado via API


    Examples:
      | nome      | cpf         | data_nascimento | rg      | ca    | status  | genero    | cargo | atividade | uses_epi | epi | file_name          |
      | Tester    | 11122233344 | 01012000        | 1234567 | 00001 | Inativo | feminino  | 02    | 00        | False    | **  | teste_atestado.pdf |
