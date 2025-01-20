from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from lib.selenium_helper import Helpers


class CadastroPage:
    def __init__(self, context):
        self.context = context
        self.helper = Helpers(context)

    def selecionar_add_funcionario(self):
        self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR,
                                            '#root > main > div.c-ijpWJD > div.c-ctDlKA > div.c-jqbATT > button')
        botao_add_funcionario = self.context.browser.find_element(By.CSS_SELECTOR,
                                                                  '#root > main > div.c-ijpWJD > div.c-ctDlKA > div.c-jqbATT > button')
        botao_add_funcionario.click()

    def informar_status_funcionario(self):
        self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR,
                                            '#root > main > div.c-ijpWJD > div.c-ctDlKA > form > div:nth-child(2) > button > span')
        botao_add_funcionario = self.context.browser.find_element(By.CSS_SELECTOR,
                                                                  '#root > main > div.c-ijpWJD > div.c-ctDlKA > form > div:nth-child(2) > button > span')
        botao_add_funcionario.click()

    def inserir_nome(self, nome):
        nome_text_box = self.context.browser.find_element(By.NAME, 'name')
        nome_text_box.send_keys(nome)

    def informar_sexo(self):
        ratio_sexo = self.context.browser.find_element(By.XPATH,
                                                       '/html/body/div[1]/main/div[2]/div[2]/form/div[3]/div/div[2]/div/label[2]/span[1]/input')
        ratio_sexo.click()

    def inserir_cpf(self, cpf):
        cpf_text_box = self.context.browser.find_element(By.NAME, 'cpf')
        cpf_text_box.send_keys(cpf)

    def inserir_data(self, data_nascimento):
        cpf_text_box = self.context.browser.find_element(By.NAME, 'birthDay')
        cpf_text_box.send_keys(data_nascimento)

    def inserir_rg(self, rg):
        rg_text_box = self.context.browser.find_element(By.NAME, 'rg')
        rg_text_box.send_keys(rg)

    def selecionar_cargo(self):
        cargo_dropdown = self.context.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/form/div[3]/div/div[6]/div')
        select = Select(cargo_dropdown)
        select.select_by_index(1)

    def selecionar_atividade(self):
        atividade_dropdown = self.context.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/form/div[4]/div/div/div[1]/div/div/span[2]')
        select = Select(atividade_dropdown)
        select.select_by_index(2)

    def inserir_ca(self, ca):
        ca_text_box = self.context.browser.find_element(By.NAME, 'caNumber')
        ca_text_box.send_keys(ca)

    def adicionar_epi(self, epi):
        epi_text_box = self.context.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/form/div[4]/div/div/div[2]/div/div[1]/div/divumber')
        epi_text_box.send_keys(epi)
        botao_add_epi = self.context.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/form/div[4]/div/div/div[2]/span')
        botao_add_epi.click()

    def adicionar_atestado(self):
        file_path = "/lib/assets/teste_atestado.pdf"
        file_input = self.context.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/form/div[5]/div/label')
        file_input.send_keys(file_path)



