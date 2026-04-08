import threading

import customtkinter
from CTkMessagebox import CTkMessagebox
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


options = Options()
options.add_argument(r"user-data-dir=C:\selenium_profile")

# Tema correto (fora da classe)
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("Automação LinkedIn")
        self.geometry("420x520")
        

        # Fundo geral
        self.configure(fg_color="#f5f7fa")

        # Layout
        self.grid_columnconfigure(0, weight=1)

        # FRAME CENTRAL
        self.frame = customtkinter.CTkFrame(
            self,
            fg_color="white",
            corner_radius=15
        )
        
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.frame.grid_columnconfigure(0, weight=1)
        
        self.tela_principal()

    # Telas
    def tela_principal(self):
        
        self.limpar_tela()
        
        # TÍTULO
        titulo = customtkinter.CTkLabel(
            self.frame,
            text="Automação LinkedIn",
            font=("Arial", 22, "bold"),
            text_color="#0A66C2"  # cor do LinkedIn
        )
        titulo.grid(row=0, column=0, pady=20, sticky="n") 

        # DESCRIÇÃO
        descricao = customtkinter.CTkLabel(
            self.frame,
            text="Automatize seu networking no LinkedIn\ncom envio de mensagens e conexões\n\nEscolha uma opção abaixo:",
            justify="center",
            text_color="#333333"
        )
        descricao.grid(row=1, column=0, pady=(0, 25))
        # BOTÃO MENSAGEM
        btn_mensagem = customtkinter.CTkButton(
            self.frame,
            text="Enviar Mensagens",
            height=45,
            fg_color="#f0f0f0",
            hover_color="#d9d9d9",
            text_color="black",
            border_width=1,
            border_color="#a0a0a0",
            corner_radius=5,
            command=self.tela_mensagem
        )
        btn_mensagem.grid(row=2, column=0, padx=30, pady=10, sticky="ew")
        # BOTÃO CONEXÃO
        btn_conexao = customtkinter.CTkButton(
            self.frame,
            text="Enviar Conexões",
            height=45,
            fg_color="#f0f0f0",
            hover_color="#d9d9d9",
            text_color="black",
            border_width=1,
            border_color="#a0a0a0",
            corner_radius=5,
            command=self.tela_conexao
        )
        btn_conexao.grid(row=3, column=0, padx=30, pady=10, sticky="ew")
        # BOTÃO FECHAR
        btn_fechar = customtkinter.CTkButton(
            self.frame,
            text="FECHAR",
            height=45,
            font=("Arial",12, "bold"),
            fg_color="#ff0000",
            hover_color="#a30202",
            text_color="white",
            border_width=1,
            border_color="#ff0000",
            corner_radius=5,
            command=self.fechar_programa
        )
        btn_fechar.grid(row=4, column=0, padx=30, pady=10, sticky="ew")

    def tela_mensagem(self):
        
        self.limpar_tela()  # limpa o frame

        # TÍTULO
        titulo = customtkinter.CTkLabel(
            self.frame,
            text="Mensagem",
            font=("Arial", 22, "bold"),
            text_color="#0A66C2"
        )
        titulo.grid(row=0, column=0, padx=30, pady=(25, 10))

        # DESCRIÇÃO adaptada para a tela de mensagens
        descricao = customtkinter.CTkLabel(
            self.frame,
            text="Aqui você pode enviar mensagens automáticas \n para quem aceitou seu convite no LinkedIn.",
            justify="center",
            text_color="#333333"
        )
        descricao.grid(row=1, column=0, padx=30, pady=(0, 10))

        placeholder = customtkinter.CTkLabel(
            self.frame,
            text="Digite a quantidade de mensagens que deseja enviar",
            justify="left",
            text_color="#333333"
        )
        placeholder.grid(row=2, column=0, padx=30, pady=0, sticky="w")

        self.quantidade = customtkinter.CTkEntry(
            self.frame,
            height=45,
            border_width=1,
            border_color="#a0a0a0",
            placeholder_text="",
        )
        self.quantidade.grid(row=3, column=0, padx=30, pady=0, sticky="ew")

        # PlaceHolder adaptada para a tela de mensagens
        placeholder  = customtkinter.CTkLabel(
            self.frame,
            text="Digite a sua mensagem genérica",
            justify="left",
            text_color="#333333"
        )
        placeholder.grid(row=4, column=0, padx=30, pady=0, sticky="w")

        # Caixa de texto pra envido de messsagem
        self.mensagem = customtkinter.CTkTextbox(
            self.frame,
            height=150,
            width=300,
            border_width=1,
            border_color="#a0a0a0",
        )
        self.mensagem.grid(row=5, column=0, padx=30, pady=(0, 10), sticky="ew")

        # Exemplo de botão para enviar mensagem
        btn_enviar = customtkinter.CTkButton(
            self.frame,
            text="Iniciar Envio de Mensagens",
            height=45,
            fg_color="#f0f0f0",
            hover_color="#d9d9d9",
            text_color="black",
            border_width=1,
            border_color="#a0a0a0",
            corner_radius=5,
            command=self.enviar_mensagem
        )
        btn_enviar.grid(row=6, column=0, padx=30, pady=10, sticky="ew")

        # Botão voltar para a tela principal
        btn_voltar = customtkinter.CTkButton(
            self.frame,
            text="Voltar",
            height=45,
            command=self.tela_principal
        )
        btn_voltar.grid(row=7, column=0, padx=30, pady=10, sticky="ew")

    def tela_conexao(self):
        self.limpar_tela()

        # TÍTULO
        titulo = customtkinter.CTkLabel(
            self.frame,
            text="Conexões",
            font=("Arial", 22, "bold"),
            text_color="#0A66C2"
        )
        titulo.grid(row=0, column=0, pady=(25, 10))

        # DESCRIÇÃO adaptada para a tela de mensagens
        descricao = customtkinter.CTkLabel(
            self.frame,
            text= "Expanda sua rede no LinkedIn de forma prática e automatizada.",
            justify="center",
            text_color="#333333"
        )
        descricao.grid(row=2, column=0, pady=(0, 25))

        self.caixa_texto = customtkinter.CTkEntry(
            self.frame,
            height=45,
            border_width=1,
            border_color="#a0a0a0",
            placeholder_text="Digite aqui o cargo que deseja se conectar",
        )
        self.caixa_texto.grid(row=3, column=0, padx=30, pady=10, sticky="ew")

        self.quantidade = customtkinter.CTkEntry(
            self.frame,
            height=45,
            border_width=1,
            border_color="#a0a0a0",
            placeholder_text="Digite quantas vezes deseja conectar",
        )
        self.quantidade.grid(row=4, column=0, padx=30, pady=10, sticky="ew")

        # Exemplo de botão para enviar Conexões
        btn_enviar = customtkinter.CTkButton(
            self.frame,
            text="Iniciar Envio de Conexões",
            height=45,
            fg_color="#f0f0f0",
            hover_color="#d9d9d9",
            text_color="black",
            border_width=1,
            border_color="#a0a0a0",
            corner_radius=5,
            command=self.enviar_conexao
        )
        btn_enviar.grid(row=5, column=0, padx=30, pady=10, sticky="ew")

        # Botão voltar para a tela principal
        btn_voltar = customtkinter.CTkButton(
            self.frame,
            text="Voltar",
            height=45,
            command=self.tela_principal
        )
        btn_voltar.grid(row=6, column=0, padx=30, pady=10, sticky="ew")

    # Envios
    def enviar_mensagem(self):
        mensagem = self.capturar_mensagem()
        quantidade = self.quantidade.get()

        self.limpar_tela()

        # TÍTULO
        titulo = customtkinter.CTkLabel(
            self.frame,
            text="Enviando mensagens...",
            font=("Arial", 22, "bold"),
            text_color="#0A66C2"
        )
        titulo.grid(row=0, column=0, pady=(25, 10))

        # Label de progresso
        self.label_progresso = customtkinter.CTkLabel(
            self.frame,
            text="Iniciando...",
            font=("Arial", 16),
            text_color="#333"
        )
        self.label_progresso.grid(row=1, column=0, pady=(10, 10))

        # Barra de progresso
        self.progressbar = customtkinter.CTkProgressBar(self.frame, width=300)
        self.progressbar.grid(row=2, column=0, pady=(10, 10), )
        self.progressbar.set(0)

        espaco = customtkinter.CTkLabel(self.frame, text="")
        espaco.grid(row=3, column=0, pady=(10, 10))
        espaco = customtkinter.CTkLabel(self.frame, text="")
        espaco.grid(row=3, column=0, pady=(10, 10))
        # Dispara processo em thread

        threading.Thread(target=self._processar_mensagem, args=(mensagem,int(quantidade))).start()

    def enviar_conexao(self):

        texto = self.capturar_texto()
        quantidade = int(self.quantidade.get())
        self.limpar_tela()

        # TÍTULO
        titulo = customtkinter.CTkLabel(
            self.frame,
            text="Enviando Conexão...",
            font=("Arial", 22, "bold"),
            text_color="#0A66C2"
        )
        titulo.grid(row=0, column=0, pady=(25, 10))

        # Label de progresso
        self.label_progresso = customtkinter.CTkLabel(
            self.frame,
            text="Iniciando...",
            font=("Arial", 16),
            text_color="#333"
        )
        self.label_progresso.grid(row=1, column=0, pady=(10, 10))

        # Barra de progresso
        self.progressbar = customtkinter.CTkProgressBar(self.frame, width=300)
        self.progressbar.grid(row=2, column=0, pady=(10, 10),)
        self.progressbar.set(0)

        espaco = customtkinter.CTkLabel(self.frame, text="")
        espaco.grid(row=3, column=0, pady=(10, 10))
        espaco = customtkinter.CTkLabel(self.frame, text="")
        espaco.grid(row=3, column=0, pady=(10, 10))
        # Dispara processo em thread

        threading.Thread(target=self._processar_conexoes, args=(texto, quantidade)).start()

    # Metodos
    def _processar_mensagem(self, mensagem, quantidade):

        contador_de_mensagens = 0
        contador_de_processos = 0
        total_de_processos = quantidade + 4
        nome_pessoa = ""

        self.atualizar_label_processo(f"Abrindo LinkedIn.")
        self.atualizar_status_processbar(contador_de_processos, total_de_processos)

        driver = self.iniciar_driver()
        contador_de_processos += 1

        self.atualizar_label_processo(f"Filtrando conexões")
        self.atualizar_status_processbar(contador_de_processos, total_de_processos)

        driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
        time.sleep(2)
        contador_de_processos += 1

        elementos = driver.find_elements(By.XPATH, "//a[contains(@aria-label, 'Enviar mensagem')]")

        for elemento in elementos:

            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento)
            # abre caixa de mensagem
            driver.execute_script("arguments[0].click();", elemento)
            time.sleep(2)

            # Coleta o nome da pessoa
            shadown_root = driver.find_element(By.ID, "interop-outlet")
            busca_nome = driver.execute_script(
                "return arguments[0].shadowRoot.querySelector('.artdeco-pill__text')", shadown_root)
            if busca_nome:
                nome_pessoa = busca_nome.get_attribute("innerHTML").strip()
            else:
                pass

            #localiza msg-form
            shadown_root = driver.find_element(By.ID, "interop-outlet")
            formulario_de_mensagem = driver.execute_script(
                "return arguments[0].shadowRoot.querySelectorAll('p')", shadown_root)

            self.atualizar_label_processo(f"Verificando conversa.")
            self.atualizar_status_processbar(contador_de_processos, total_de_processos)

            #verifica se e um conversa nova
            nova_conversa = self.verifica_se_possui_conversa(driver)
            contador_de_processos += 1

            if(nova_conversa):
                #Enviar msg para novo contato
                #Escreve a mensagem no msg_form
                self.atualizar_label_processo(f"Escrevendo mensagem.")
                self.atualizar_status_processbar(contador_de_processos, total_de_processos)

                for item in formulario_de_mensagem:
                    if item.get_attribute("innerHTML") == "<br>" :
                        item.send_keys(f"Olá {nome_pessoa}!\n\n{mensagem}")
                time.sleep(2)
                ###
                contador_de_processos += 1
                contador_de_mensagens += 1
                # Atualiza label e progressbar
                self.atualizar_label_processo(f"Enviando mensagem a {nome_pessoa}.")
                self.atualizar_status_processbar(contador_de_processos, total_de_processos)
                time.sleep(2)

                # localiza m
                shadown_root = driver.find_element(By.ID, "interop-outlet")
                botao_enviar = driver.execute_script(
                    "return arguments[0].shadowRoot.querySelector('.msg-form__send-button')", shadown_root)
                botao_enviar.click()
                time.sleep(2)
                # fecha a conversa
                self.fechar_popup_conversa(driver)
            else:
                #fecha a conversa
                self.fechar_popup_conversa(driver)

            # Verifica se e o ultimo loop
            if elementos.index(elemento) == (len(elementos) - 1):
                self.carrega_mais_itens(driver)
            time.sleep(2)
            # busca e adiciona novo itens a lista
            nova_busca = driver.find_elements(By.XPATH, "//a[contains(@aria-label, 'Enviar mensagem')]")
            add_itens = [x for x in nova_busca if x not in elementos]  # mantém a ordem
            elementos.extend(add_itens)

            if contador_de_mensagens == quantidade:
                break

        self.atualizar_label_processo(f"Finalizando processo..")
        print(f"Foram enviadas {contador_de_mensagens} mensagens para novas conexões.")
        self.mostrar_popup(f"Foram enviadas {contador_de_mensagens} mensagens para novas conexões.","check")

        contador_de_processos += 1
        time.sleep(2)
        driver.quit()
        self.after(0, self.tela_principal)

    def _processar_conexoes(self,texto,quantidade):

        contador_de_conexao = 0
        contador_de_processos = 0
        total_de_processos = quantidade +  3
        nome_pessoa = ""

        driver = self.iniciar_driver()

        # Busca por cargo
        pesquisa = driver.find_element("id", ":r4:")
        pesquisa.send_keys(texto + Keys.RETURN)

        self.atualizar_label_processo(f"Pesquisando por {texto}")
        contador_de_processos += 1
        self.atualizar_status_processbar(contador_de_processos, total_de_processos)

        time.sleep(4)
        driver.find_element(By.XPATH, "//div[contains(@aria-label,'Filtrar Pessoas')]").click()

        # Atualiza label e progressbar
        self.atualizar_label_processo("Filtrando por Pessoas")

        contador_de_processos += 1
        self.atualizar_status_processbar(contador_de_processos, total_de_processos)

        time.sleep(4)
        driver.find_element(By.XPATH, "//div[contains(@aria-label,'Filtrar conexões de 2º')]").click()

        # Atualiza label e progressbar
        self.atualizar_label_processo("Filtrando conexões de 2º")
        contador_de_processos += 1
        self.atualizar_status_processbar(contador_de_processos, total_de_processos)

        time.sleep(4)
        botoes = driver.find_elements(By.XPATH, "//a[contains(@aria-label,'se conectar')]")
        nomes = driver.find_elements(By.XPATH, "//a[contains(@aria-label,'Convidar')]")

        # Atualiza label e progressbar
        self.atualizar_label_processo("Inciando conexões..")

        for botao in botoes:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao)
            time.sleep(2)

            botao.click()
            time.sleep(2)

            # Captura o nome
            for nome in nomes:
                if nomes.index(nome) == botoes.index(botao):
                    nome_pessoa = nome.get_attribute("aria-label").split()

            # Localiza e click no botao enviar sem nota dentro do shadownRoot
            shadown_root = driver.find_element(By.ID, "interop-outlet")
            Botao_enviar = driver.execute_script("return arguments[0].shadowRoot.querySelector('button.artdeco-button--primary')",shadown_root)
            Botao_enviar.click()
            time.sleep(2)

            # Atualiza label e progressbar
            self.atualizar_label_processo(f"Conectando a {nome_pessoa[1]} {nome_pessoa[2]}...")
            self.atualizar_status_processbar(contador_de_processos, total_de_processos)

            if botoes.index(botao) == (len(botoes)) - 1:
                self.carrega_conexoes(driver)
                time.sleep(2)

            novos_nomes = driver.find_elements(By.XPATH, "//a[contains(@aria-label,'Convidar')]")
            time.sleep(2)
            add_nomes = [x for x in novos_nomes if x not in nomes]  # mantém a ordem
            botoes.extend(add_nomes)

            # busca e adiciona novo itens a lista
            nova_busca = driver.find_elements(By.XPATH, "//a[contains(@aria-label,'se conectar')]")
            time.sleep(2)
            add_itens = [x for x in nova_busca if x not in botoes]  # mantém a ordem
            botoes.extend(add_itens)

            contador_de_conexao += 1
            contador_de_processos += 1

            if contador_de_conexao == quantidade:
                break

        self.atualizar_label_processo(f"Finalizando processo..")
        print(f"Foram enviadas {contador_de_conexao} conexões para o cargo '{texto}'.")
        self.mostrar_popup(f"Foram enviadas {contador_de_conexao} conexões para o cargo de '{texto}'.", "check")

        time.sleep(3)
        driver.quit()
        self.after(0, self.tela_principal)

    def carrega_mais_itens(self, driver):
        try:
            carregar_mais = driver.find_element(By.XPATH, "//button//span[contains(text(),'Carregar mais')]")
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", carregar_mais)
            driver.execute_script("arguments[0].click();", carregar_mais)
        except NoSuchElementException:
            print("Botão 'Carregar mais' não encontrado")

    def carrega_conexoes(self, driver):
        try:
            carrega_conexoes = driver.find_element(By.XPATH, "//button//span[contains(text(),'Próxima')]")
            driver.execute_script("arguments[0].scrollIntoView(true);", carrega_conexoes)
            driver.execute_script("arguments[0].click();", carrega_conexoes)
        except NoSuchElementException:
            print("Botão 'Próxima' não encontrado")

    def limpar_tela(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def capturar_mensagem(self):
       return self.mensagem.get("1.0", "end-1c")

    def capturar_texto(self):
       return self.caixa_texto.get()

    def captura_quantidade(self):
        return self.quantidade.get()

    def fechar_programa(self):
        self.destroy()

    def mostrar_popup(self,message,icon):
        CTkMessagebox(
            title="Processo Concluído",
            message=message,
            icon= icon,
            bg_color = "#F5F7FA",
            fg_color="white",
            button_height=45,
            border_color="#a0a0a0",
            border_width=1,
            button_color="#f0f0f0",
            button_text_color="black",
            corner_radius = 5,
            )

    def iniciar_driver(self):
        url_inicial = "https://www.linkedin.com/feed/"

        driver = webdriver.Chrome( options = options )
        time.sleep(2)
        driver.get(url_inicial)
        driver.maximize_window()
        url_atual = driver.current_url

        # Verifica se está logado e muda o tempo pra que pessoa possa fazer login
        if url_atual == url_inicial:
            time.sleep(2)
        else:
            time.sleep(28)

        return driver

    def atualizar_status_processbar(self, contador_de_processos, total_de_processos):
        progresso = contador_de_processos / total_de_processos
        self.progressbar.set(progresso)
        self.frame.update_idletasks()

    def atualizar_label_processo(self, mensagem):
        self.label_progresso.configure(
            text = mensagem)
        print(mensagem)

    def fechar_popup_conversa(self,driver):
        # Fechar rascunho da conversa
        try:
            shadown_root = driver.find_element(By.ID, "interop-outlet")
            lista_de_botoes = driver.execute_script(
                "return arguments[0].shadowRoot.querySelectorAll('span.artdeco-button__text')", shadown_root)
            for botao in lista_de_botoes:
                if botao.get_attribute(
                        "innerText") == "Fechar rascunho da conversa" or "Fechar conversa com" in botao.get_attribute(
                        "innerText"):
                    driver.execute_script("arguments[0].click();", botao)
        except StaleElementReferenceException:
            pass

    def verifica_se_possui_conversa(self, driver):
        nova_conversa = False
        try:
            shadown_root = driver.find_element(By.ID, "interop-outlet")
            lista_de_mensagens = driver.execute_script(
                "return arguments[0].shadowRoot.querySelectorAll('.msg-s-event-listitem__body')", shadown_root)

            if lista_de_mensagens == []:
                nova_conversa = True
            else:
                nova_conversa = False

        except StaleElementReferenceException:
            pass
        return nova_conversa


app = App()
app.mainloop()