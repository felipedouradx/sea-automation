import http
import os
import json
import re
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from lib.selenium_helper import Helpers


class CadastroPage:
    def __init__(self, context):
        self.context = context
        self.helper = Helpers(context)

        # WebElements
        self.botao_add_funcionario_selector = '#root > main > div.c-ijpWJD > div.c-ctDlKA > div.c-jqbATT > button'
        self.botao_status_funcionario_selector = '#root > main > div.c-ijpWJD > div.c-ctDlKA > form > div:nth-child(2) > button > span'
        self.nome_input_name = 'name'
        self.genero_f_radio_xpath = '/html/body/div[1]/main/div[2]/div[2]/form/div[3]/div/div[2]/div/label[2]/span[1]/input'
        self.genero_m_radio_xpath = '/html/body/div/main/div[2]/div[2]/form/div[3]/div/div[2]/div/label[1]/span[1]/input'
        self.cpf_input_name = 'cpf'
        self.birthDay_input_name = 'birthDay'
        self.rg_input_name = 'rg'
        self.cargo_dropdown = 'ant-select-selection-item'
        self.cargo_1_option = '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]'
        self.cargo_2_option = '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[2]'
        self.cargo_3_option = '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[3]'
        self.cargo_4_option = '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[4]'
        self.cargo_5_option = '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[5]'
        self.atividade_dropdown = '/html/body/div[1]/main/div[2]/div[2]/form/div[4]/div/div/div[1]/div/div/span[2]'
        self.atividade_1_option = '/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[1]'
        self.atividade_2_option = '/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[2]'
        self.atividade_3_option = '/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[3]'
        self.atividade_4_option = 'body > div:nth-child(3) > div > div > div.rc-virtual-list > div.rc-virtual-list-holder > div > div > div:nth-child(4)'
        self.atividade_5_option = '/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[5]'
        self.epi_1_dropdown = '/html/body/div[1]/main/div[2]/div[2]/form/div[4]/div/div/div[2]/div/div[1]/div/div/span[2]'
        self.epi_1_option = '/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[1]'
        self.epi_2_option = '/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[2]'
        self.epi_3_option = '/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[3]'
        self.epi_4_option = '/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[4]'
        self.epi_5_option = '/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[5]'
        self.ca_input_name = 'caNumber'
        self.epi_dropdown_xpath = '/html/body/div[1]/main/div[2]/div[2]/form/div[4]/div/div/div[2]/div/div[1]/div'
        self.epi_option_xpath = '/html/body/div[4]/div/div/div[2]/div[1]/div/div/div[2]'
        self.add_epi_button_xpath = '/html/body/div[1]/main/div[2]/div[2]/form/div[4]/div/div/div[2]/span'
        self.atestado_input_class = 'c-iQPyMC'

    def selecionar_add_funcionario(self):
        self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR, self.botao_add_funcionario_selector)
        botao_add_funcionario = self.context.browser.find_element(By.CSS_SELECTOR, self.botao_add_funcionario_selector)
        botao_add_funcionario.click()

    def informar_status_funcionario(self, status):
        if status == 'Ativo':
            self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR, self.botao_status_funcionario_selector)
            botao_status_funcionario = self.context.browser.find_element(By.CSS_SELECTOR,
                                                                         self.botao_status_funcionario_selector)
            botao_status_funcionario.click()
        if status == 'Inativo':
            pass
        elif status != 'Ativo' and status == 'Inativo':
            print('Expected status Ativo or Inativo, but got {}'.format(status))

    def inserir_nome(self, nome):
        nome_text_box = self.context.browser.find_element(By.NAME, self.nome_input_name)
        nome_text_box.send_keys(nome)

    def informar_genero(self, genero):
        if genero == 'feminino':
            genero_f_radio = self.context.browser.find_element(By.XPATH, self.genero_f_radio_xpath)
            genero_f_radio.click()
        elif genero == 'masculino':
            genero_m_radio = self.context.browser.find_element(By.XPATH, self.genero_m_radio_xpath)
            genero_m_radio.click()
        else:
            print('Gênero incorreto.')
            raise

    def inserir_cpf(self, cpf):
        cpf_text_box = self.context.browser.find_element(By.NAME, self.cpf_input_name)
        cpf_text_box.send_keys(cpf)

    def inserir_data(self, data_nascimento):
        birthDay_text_box = self.context.browser.find_element(By.NAME, self.birthDay_input_name)
        birthDay_text_box.send_keys(data_nascimento)

    def inserir_rg(self, rg):
        rg_text_box = self.context.browser.find_element(By.NAME, self.rg_input_name)
        rg_text_box.send_keys(rg)

    def selecionar_cargo(self, cargo):
        cargo_dropdown = self.context.browser.find_element(By.CLASS_NAME, self.cargo_dropdown)
        cargo_dropdown.click()
        if cargo == '01':
            self.helper.selenium_wait_clickable(2, By.XPATH, self.cargo_1_option)
            cargo_1_option = self.context.browser.find_element(By.XPATH, self.cargo_1_option)
            cargo_1_option.click()
        elif cargo == '02':
            self.helper.selenium_wait_clickable(2, By.XPATH, self.cargo_2_option)
            cargo_2_option = self.context.browser.find_element(By.XPATH, self.cargo_2_option)
            cargo_2_option.click()
        elif cargo == '03':
            self.helper.selenium_wait_clickable(2, By.XPATH, self.cargo_3_option)
            cargo_3_option = self.context.browser.find_element(By.XPATH, self.cargo_3_option)
            cargo_3_option.click()
        elif cargo == '04':
            self.helper.selenium_wait_clickable(2, By.XPATH, self.cargo_4_option)
            cargo_4_option = self.context.browser.find_element(By.XPATH, self.cargo_4_option)
            cargo_4_option.click()
        elif cargo == '05':
            self.helper.selenium_wait_clickable(2, By.XPATH, self.cargo_5_option)
            cargo_5_option = self.context.browser.find_element(By.XPATH, self.cargo_5_option)
            cargo_5_option.click()
        else:
            print('Cargo inválido.')
            raise

    def selecionar_atividade(self, atividade, uses_epi):
        time.sleep(1)
        if uses_epi == 'True':
            atividade_dropdown = self.context.browser.find_element(By.XPATH, self.atividade_dropdown)
            atividade_dropdown.click()
            if atividade == '01':
                self.helper.selenium_wait_clickable(2, By.XPATH, self.atividade_1_option)
                atividade_1_option = self.context.browser.find_element(By.XPATH, self.atividade_1_option)
                atividade_1_option.click()
            elif atividade == '02':
                self.helper.selenium_wait_clickable(2, By.XPATH, self.atividade_2_option)
                atividade_2_option = self.context.browser.find_element(By.XPATH, self.atividade_2_option)
                atividade_2_option.click()
            elif atividade == '03':
                self.helper.selenium_wait_clickable(2, By.XPATH, self.atividade_3_option)
                atividade_3_option = self.context.browser.find_element(By.XPATH, self.atividade_3_option)
                atividade_3_option.click()
            elif atividade == '04':
                self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR, self.atividade_4_option)
                atividade_4_option = self.context.browser.find_element(By.CSS_SELECTOR, self.atividade_4_option)
                atividade_4_option.click()
            elif atividade == '05':
                self.helper.selenium_wait_clickable(2, By.XPATH, self.atividade_5_option)
                atividade_5_option = self.context.browser.find_element(By.XPATH, self.atividade_5_option)
                atividade_5_option.click()
            else:
                print('Atividade inválida.')
                raise
        elif uses_epi == 'False':
            pass
        else:
            print('O valor deve ser boolean.')

    def inserir_ca(self, ca, uses_epi):
        if uses_epi == 'True':
            ca_text_box = self.context.browser.find_element(By.NAME, self.ca_input_name)
            ca_text_box.send_keys(ca)
        elif uses_epi == 'False':
            print('O funcionário não utiliza API')
            pass

    def adicionar_epi(self, epi):
        epi_dropdown = self.context.browser.find_element(By.XPATH, self.epi_dropdown_xpath)
        epi_dropdown.click()
        self.helper.selenium_wait_clickable(2, By.XPATH, self.epi_option_xpath)
        epi_option = self.context.browser.find_element(By.XPATH, self.epi_option_xpath)
        epi_option.click()
        add_epi_button = self.context.browser.find_element(By.XPATH, self.add_epi_button_xpath)
        add_epi_button.click()

    def adicionar_atestado(self):
        file_path = os.path.join(os.getcwd(), "lib/assets/teste_atestado.pdf")
        file_input = self.context.browser.find_element(By.CLASS_NAME, self.atestado_input_class)
        file_input.send_keys(file_path)

    def salvar_cadastro(self):
        save_button = self.context.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/form/button')
        save_button.click()

    def validar_cadastro_api(self, nome, status, genero, cpf, rg, ca, data_nascimento, cargo, atividade, uses_epi, epi):
        conn = http.client.HTTPSConnection("analista-teste.seatecnologia.com.br")
        conn.request("GET", "/employees")

        response = conn.getresponse()
        data = response.read()

        errors = []

        try:
            json_data = json.loads(data)

            if isinstance(json_data, list) and len(json_data) > 0:
                last_entry = json_data[-1]

                if "isActive" in last_entry["state"]["employee"]:
                    try:
                        if status == 'Ativo':
                            status = True
                        elif status == 'Inativo':
                            status = False
                        is_active_value = last_entry["state"]["employee"]["isActive"]
                        assert isinstance(is_active_value,
                                          bool), f"isActive should be a boolean but got {type(is_active_value)}"
                        assert is_active_value == status
                    except AssertionError as e:
                        errors.append(f"isActive validation failed: {e}")

                if "cpf" in last_entry["state"]["employee"]:
                    try:
                        cpf_value = last_entry["state"]["employee"]["cpf"]
                        assert len(cpf_value) == 11, f"CPF should be 11 digits but got {cpf_value}"
                        assert cpf_value.isdigit()
                        assert cpf_value == cpf
                    except AssertionError as e:
                        errors.append(f"CPF validation failed: {e}")

                if "name" in last_entry["state"]["employee"]:
                    try:
                        name_value = last_entry["state"]["employee"]["name"]
                        assert len(name_value) < 100, f"Name should be less than 100 characters."
                        assert re.fullmatch(r"[A-Za-z\s]+",
                                            name_value), f"Name should contain only letters and spaces but got {name_value}"
                        assert name_value == nome
                    except AssertionError as e:
                        errors.append(f"Name validation failed: {e}")

                if "gender" in last_entry["state"]["employee"]:
                    try:
                        gender_value = last_entry["state"]["employee"]["gender"]
                        assert gender_value == genero
                    except AssertionError as e:
                        errors.append(f"Gender validation failed: {e}")

                if "usesEpi" in last_entry["state"]["employee"]:
                    try:
                        uses_epi_value = last_entry["state"]["employee"]["usesEpi"]
                        assert uses_epi_value == uses_epi
                    except AssertionError as e:
                        errors.append(f"usesEpi validation failed: {e}")

                if "rg" in last_entry["state"]["employee"]:
                    try:
                        rg_value = last_entry["state"]["employee"]["rg"]
                        assert rg_value.isdigit()
                        assert rg_value == rg
                    except AssertionError as e:
                        errors.append(f"RG validation failed: {e}")

                if "birthDay" in last_entry["state"]["employee"]:
                    try:
                        parsed_date = datetime.strptime(data_nascimento, "%d%m%Y")
                        formatted_date = parsed_date.strftime("%Y-%m-%d")
                        birthday_value = last_entry["state"]["employee"]["birthDay"]
                        assert birthday_value == formatted_date
                    except AssertionError as e:
                        errors.append(f"BirthDay validation failed: {e}")

                if uses_epi == 'True':
                    if "caNumber" in last_entry["state"]["employee"]:
                        try:
                            ca_value = last_entry["state"]["employee"]["caNumber"]
                            assert ca_value.isdigit()
                            assert ca_value == ca
                        except AssertionError as e:
                            errors.append(f"CA Number validation failed: {e}")

                    if "activity" in last_entry["state"]["employee"]:
                        try:
                            activity_value = last_entry["state"]["employee"]["activity"]
                            expected_activity_value = f"Ativid {atividade}"
                            assert activity_value == expected_activity_value, f"Expected activity '{expected_activity_value}' but got '{activity_value}'"
                        except AssertionError as e:
                            errors.append(f"Activity validation failed: {e}")

                    if "epi" in last_entry["state"]["employee"]:
                        try:
                            epi_value = last_entry["state"]["employee"]["epi"]
                            formatted_epi_value = re.sub(r'\s+', '-', epi.lower().strip())
                            assert epi_value == formatted_epi_value, f"Expected epi '{formatted_epi_value}' but got '{epi_value}'"
                        except AssertionError as e:
                            errors.append(f"EPI validation failed: {e}")
                    if not "epi" in last_entry["state"]["employee"]:
                        print(f"Erro: Valor epi '{epi}' não enviado para o endpoint.")
                        raise

                if "role" in last_entry["state"]["employee"]:
                    try:
                        role_value = last_entry["state"]["employee"]["role"]
                        expected_role_value = f"Cargo {cargo}"
                        assert role_value == expected_role_value, f"Expected role '{expected_role_value}' but got '{role_value}'"
                    except AssertionError as e:
                        errors.append(f"Role validation failed: {e}")

            else:
                errors.append("JSON response is not a list or is empty.")

        except json.JSONDecodeError:
            errors.append("Failed to decode JSON from response.")
        finally:
            conn.close()

        if errors:
            raise AssertionError("Validation errors occurred:\n" + "\n".join(errors))

    def selecionar_uso_epi(self, uses_epi):
        if uses_epi == 'True':
            pass
        elif uses_epi == 'False':
            epi_checkbox = self.context.browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/form/div[4]/div/label/span[1]/input')
            epi_checkbox.click()

    def selecionar_equipamento_epi(self, epi, uses_epi):
        if uses_epi == 'True':
            time.sleep(2)
            epi_dropdown = self.context.browser.find_element(By.XPATH, self.epi_1_dropdown)
            epi_dropdown.click()
            time.sleep(1)
            if epi == 'Capacete de segurança':
                self.helper.selenium_wait_clickable(2, By.XPATH, self.epi_1_option)
                epi_1_option = self.context.browser.find_element(By.XPATH, self.epi_1_option)
                epi_1_option.click()
            elif epi == 'Luvas descartáveis':
                self.helper.selenium_wait_clickable(2, By.XPATH, self.epi_2_option)
                epi_2_option = self.context.browser.find_element(By.XPATH, self.epi_2_option)
                epi_2_option.click()
            elif epi == 'Oculos de proteçao':
                self.helper.selenium_wait_clickable(2, By.XPATH, self.epi_3_option)
                epi_3_option = self.context.browser.find_element(By.XPATH, self.epi_3_option)
                epi_3_option.click()
            elif epi == 'Calçado de Segurança':
                self.helper.selenium_wait_clickable(2, By.XPATH, self.epi_4_option)
                epi_4_option = self.context.browser.find_element(By.XPATH, self.epi_4_option)
                epi_4_option.click()
            elif epi == 'Protetor auditivo':
                self.helper.selenium_wait_clickable(2, By.XPATH, self.epi_5_option)
                epi_5_option = self.context.browser.find_element(By.XPATH, self.epi_5_option)
                epi_5_option.click()
            else:
                print('Epi inválido.')
                raise
            actions = ActionChains(self.context.browser)
            actions.move_to_element(epi_dropdown).send_keys(Keys.ESCAPE).perform()

        elif uses_epi == 'False':
            pass
        else:
            print('O valor deve ser boolean.')






