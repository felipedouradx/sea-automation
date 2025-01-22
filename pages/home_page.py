from selenium.webdriver.common.by import By

from lib.selenium_helper import Helpers


class HomePage:
    def __init__(self, context):
        self.context = context
        self.helper = Helpers(context)

        # WebElements
        self.botao_filtro_ativos = '#root > main > div.c-ijpWJD > div.c-ctDlKA > div.c-jqbATT > div.c-hfAyug > button.isActive'
        self.botao_limpar_filtros = '#root > main > div.c-ijpWJD > div.c-ctDlKA > div.c-jqbATT > div.c-hfAyug > button.clear'
        self.botao_opcoes_funcionario = 'na#root > main > div.c-ijpWJD > div.c-ctDlKA > div.c-jqbATT > div.c-kGuehp > div > div:nth-child(1) > div.c-jyZWAyme'
        self.building_button_menu_lateral = '#root > main > div.c-eFRCyV > div.c-juSleU > div:nth-child(1)'
        self.home_button_menu = '/html/body/div[1]/main/div[1]/div[2]/div[1]'
        self.edit_button_menu = '/html/body/div[1]/main/div[1]/div[2]/div[2]'
        self.tree_button_menu = '/html/body/div[1]/main/div[1]/div[2]/div[3]'
        self.notifications_button_menu = '/html/body/div[1]/main/div[1]/div[2]/div[4]'
        self.history_button_menu = '/html/body/div[1]/main/div[1]/div[2]/div[5]'
        self.profile_button_menu = '/html/body/div[1]/main/div[1]/div[2]/div[6]'

    def selecionar_filtros_ativos(self):
        self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR, self.botao_filtro_ativos)
        botao_filtro_ativos = self.context.browser.find_element(By.CSS_SELECTOR, self.botao_filtro_ativos)
        botao_filtro_ativos.click()

    def selecionar_limpar_filtros(self):
        botao_limpar_filtrosos = self.context.browser.find_element(By.CSS_SELECTOR, self.botao_limpar_filtros)
        botao_limpar_filtrosos.click()

    def selecionar_menu_opcoes_perfil(self):
        self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR, self.botao_opcoes_funcionario)
        botao_opcoes_funcionario = self.context.browser.find_element(By.CSS_SELECTOR, self.botao_opcoes_funcionario)
        botao_opcoes_funcionario.click()

    def selecionar_item_menu_lateral(self, item):
        if item == 'home':
            self.helper.selenium_wait_clickable(2, By.XPATH, self.home_button_menu)
            home_button_menu = self.context.browser.find_element(By.XPATH, self.home_button_menu)
            home_button_menu.click()
        elif item == 'edit':
            self.helper.selenium_wait_clickable(2, By.XPATH, self.edit_button_menu)
            edit_button_menu = self.context.browser.find_element(By.XPATH, self.edit_button_menu)
            edit_button_menu.click()
        elif item == 'tree':
            self.helper.selenium_wait_clickable(2, By.XPATH, self.tree_button_menu)
            tree_button_menu = self.context.browser.find_element(By.XPATH, self.tree_button_menu)
            tree_button_menu.click()
        elif item == 'notifications':
            self.helper.selenium_wait_clickable(2, By.XPATH, self.notifications_button_menu)
            notifications_button_menu = self.context.browser.find_element(By.XPATH, self.notifications_button_menu)
            notifications_button_menu.click()
        elif item == 'history':
            self.helper.selenium_wait_clickable(2, By.XPATH, self.history_button_menu)
            history_button_menu = self.context.browser.find_element(By.XPATH, self.history_button_menu)
            history_button_menu.click()
        elif item == 'profile':
            self.helper.selenium_wait_clickable(2, By.XPATH, self.profile_button_menu)
            profile_button_menu = self.context.browser.find_element(By.XPATH, self.profile_button_menu)
            profile_button_menu.click()
        else:
            print('Invalid item.')
            raise Exception('Invalid item.')
