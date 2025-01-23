from selenium.webdriver.common.by import By

from lib.selenium_helper import Helpers


class HomePage:
    def __init__(self, context):
        self.context = context
        self.helper = Helpers(context)

        # WebElements
        self.botao_filtro_ativos = '/html/body/div/main/div[2]/div[2]/div[2]/div[1]/button[1]'
        self.botao_limpar_filtros = '/html/body/div/main/div[2]/div[2]/div[2]/div[1]/button[2]'
        self.botao_opcoes_funcionario = '/html/body/div/main/div[2]/div[2]/div[2]/div[2]/div/div/div[2]'
        self.botao_etapa_concluida = '/html/body/div[1]/main/div[2]/div[2]/div[2]/div[3]/button'
        self.nova_atividade_button = '/html/body/div/main/div[2]/div[2]/form/div[4]/div/button'
        self.home_button_menu = '/html/body/div[1]/main/div[1]/div[2]/div[1]'
        self.edit_button_menu = '/html/body/div[1]/main/div[1]/div[2]/div[2]'
        self.tree_button_menu = '/html/body/div[1]/main/div[1]/div[2]/div[3]'
        self.notifications_button_menu = '/html/body/div[1]/main/div[1]/div[2]/div[4]'
        self.history_button_menu = '/html/body/div[1]/main/div[1]/div[2]/div[5]'
        self.profile_button_menu = '/html/body/div[1]/main/div[1]/div[2]/div[6]'
        self.next_button = '/html/body/div[1]/main/div[2]/div[3]/button'
        self.top_button_item_1 = '/html/body/div[1]/main/div[2]/div[1]/div[2]/div'
        self.top_button_item_2 = '/html/body/div[1]/main/div[2]/div[1]/div[3]/div'
        self.top_button_item_3 = '/html/body/div[1]/main/div[2]/div[1]/div[4]/div'
        self.top_button_item_4 = '/html/body/div[1]/main/div[2]/div[1]/div[5]/div'
        self.top_button_item_5 = '/html/body/div[1]/main/div[2]/div[1]/div[6]/div'
        self.top_button_item_6 = '/html/body/div[1]/main/div[2]/div[1]/div[7]/div'
        self.top_button_item_7 = '/html/body/div[1]/main/div[2]/div[1]/div[8]/div'
        self.top_button_item_8 = '/html/body/div[1]/main/div[2]/div[1]/div[9]/div'
        self.top_button_item_9 = '/html/body/div[1]/main/div[2]/div[1]/div[10]/div'

    def selecionar_filtros_ativos(self):
        botao_filtro_ativos = self.context.browser.find_element(By.XPATH, self.botao_filtro_ativos)
        botao_filtro_ativos.click()

    def selecionar_limpar_filtros(self):
        botao_limpar_filtrosos = self.context.browser.find_element(By.XPATH, self.botao_limpar_filtros)
        botao_limpar_filtrosos.click()

    def selecionar_menu_opcoes_perfil(self):
        self.helper.selenium_wait_clickable(2, By.XPATH, self.botao_opcoes_funcionario)
        botao_opcoes_funcionario = self.context.browser.find_element(By.XPATH, self.botao_opcoes_funcionario)
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

    def selecionar_item_menu_superior(self, item):
        pass

    def selecionar_botao_etapa_concluida(self):
        self.helper.selenium_wait_clickable(2, By.XPATH, self.botao_etapa_concluida)
        botao_etapa_concluida = self.context.browser.find_element(By.XPATH, self.botao_etapa_concluida)
        botao_etapa_concluida.click()

    def selecionar_proximo_passo(self):
        self.helper.selenium_wait_clickable(2, By.XPATH, self.next_button)
        next_button = self.context.browser.find_element(By.XPATH, self.next_button)
        next_button.click()

    def selecionar_item_1_menu_superior(self):
        top_button_item_1 = self.context.browser.find_element(By.XPATH, self.top_button_item_1)
        top_button_item_1.click()

    def selecionar_item_2_menu_superior(self):
        top_button_item_2 = self.context.browser.find_element(By.XPATH, self.top_button_item_2)
        top_button_item_2.click()

    def selecionar_item_3_menu_superior(self):
        next_button = self.context.browser.find_element(By.XPATH, self.top_button_item_3)
        next_button.click()

    def selecionar_item_4_menu_superior(self):
        next_button = self.context.browser.find_element(By.XPATH, self.top_button_item_4)
        next_button.click()

    def selecionar_item_5_menu_superior(self):
        next_button = self.context.browser.find_element(By.XPATH, self.top_button_item_5)
        next_button.click()

    def selecionar_item_6_menu_superior(self):
        next_button = self.context.browser.find_element(By.XPATH, self.top_button_item_6)
        next_button.click()

    def selecionar_item_7_menu_superior(self):
        next_button = self.context.browser.find_element(By.XPATH, self.top_button_item_7)
        next_button.click()

    def selecionar_item_8_menu_superior(self):
        next_button = self.context.browser.find_element(By.XPATH, self.top_button_item_8)
        next_button.click()

    def selecionar_item_9_menu_superior(self):
        next_button = self.context.browser.find_element(By.XPATH, self.top_button_item_9)
        next_button.click()



