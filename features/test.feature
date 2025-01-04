@allure.label.epic:CadastroDeProcesso
Feature: Check the iPhone price
    #Test

    @test
    @allure.label.story:Labels
    Scenario Outline: Check the iPhone price
        Given The user is in Google page
        When The user select the search button
        And The iphone <iphone_model> is selected
        And The Shopping sheet is selected
        Then The price is showed

    Examples:
      | iphone_model      |
      | iPhone 15 Pro Max |

