@allure.label.epic:HomePage
Feature: Validar opção Adicionar outra atividade
    #SEA-09

    @ok
    @allure.label.story:Labels
    Scenario Outline: Validar opção Adicionar outra atividade
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
        Then O opção Adicionar outra atividade é selecionada

    Examples:
      | nome      | cpf         | data_nascimento | rg      | ca    | status  | genero    | cargo | atividade | uses_epi | epi               |
      | Tester    | 11122233344 | 01012000        | 1234567 | 00001 | Inativo | feminino  | 02    | 02        | True     | Protetor auditivo |