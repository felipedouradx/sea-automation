@allure.label.epic:CadastroFuncionário
Feature: Cadastro de funcionário
    #Teste falha, novo cadastro nao consta na lista.. após clicar em add novo funcionario e voltar para a pagina
    # iniciall o nome aparece

    @ok
    @allure.label.story:Labels
    Scenario Outline: Cadastro de funcionário com validação na lista da página inicial
        Given O usuário está na página do portal de testes SEA Tecnologia
        When O botão adicionar funcionário é selecionado
        And O status <status> do trabalhador é informado
        And O campo nome é preenchido com valor aleatório e timestamp para validação
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
        Then O cadastro do funcionário é finalizado e consta na lista da página inicial


    Examples:
      | cpf         | data_nascimento | rg      | ca    | status  | genero    | cargo | atividade | uses_epi | epi                   |
      | 99999999999 | 03031993        | 7654321 | 00002 | Ativo   | masculino | 03    | 02        | True     | Protetor auditivo     |
