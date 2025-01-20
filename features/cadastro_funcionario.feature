@allure.label.epic:CadastroFuncionário
Feature: Cadastro de funcionário com dados válidos

    @test
    @allure.label.story:Labels
    Scenario Outline: Cadastro de funcionário com dados válidos
        Given O usuário está na página do portal de testes SEA Tecnologia
        When O botão adicionar funcionário é selecionado
        And O status do trabalhador Ativo é informado
        And O campo nome <nome> é preenchido
        And O sexo é informado
        And O campo CPF <cpf> é preenchido
        And A data de nascimento <data_nascimento> é informada
        And O RG <rg> é informado
        And O cargo 2 é selecionado
        And A atividade é selecionada
        And O CA <ca> é informado
        And O EPI <epi> é adicionado
        And O arquivo do atestado de saúde é inserido
        Then O cadastro do funcionário é realizado com sucesso


    Examples:
      | nome      | cpf         | data_nascimento | rg      | ca    | epi               |
      | Equipe QA | 11122233344 | 01/01/2000      | 1234567 | 00001 | Protetor auditivo |

