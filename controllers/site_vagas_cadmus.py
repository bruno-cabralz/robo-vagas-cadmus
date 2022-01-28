from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class SiteCadmus:
    def __init__(self, caminho_driver: str) -> None:
        """Instancia a classe com as configurações iniciais

        Args: 
            caminho_driver (str): caminho do executavel do chromedriver 
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument('--log-level=3')

        self.driver = webdriver.Chrome(caminho_driver,
                                       options=chrome_options)

    def acessar_vagas(self) -> None:
        """Acessa página de vagas da cadmus
        """
        self.driver.get('https://cadmus.com.br/vagas-tecnologia/')
        time.sleep(5)

    def pegar_vagas(self) -> dict:
        """Essa função é responsável por buscar os elemetos na página

        Returns:
            dict: retorna um dicionário com as vagas contendo titulo e local
        """

        vagas = self.driver.find_elements(By.XPATH, '//div[@class="box"]')
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,1000);")
        time.sleep(2)

        dados_vagas = {}

        for vaga in vagas:

            titulo_el = vaga.find_element(By.TAG_NAME, 'h3')
            local_el = vaga.find_element(By.CLASS_NAME, 'local')
            titulo = titulo_el.text
            local = local_el.text

            dados_vagas.update({titulo: {
                'local': local,
                'descricao': None
            }})

        return dados_vagas

    def pegar_descricao_vagas(self, dados_vagas: dict) -> dict:
        """Função responsável por pegar as descrições das vagas

        Args:
            dados_vagas (dict): dicicionário das vagas

        Returns:
            dict: retorna o dicionário atualizado com as descrições
        """
        for vaga in dados_vagas:
            self.driver.execute_script("window.scrollTo(0,1000);")
            time.sleep(1)
            btn_descricao = '//div[@class="box"]/h3[contains(text(), "{}")]/../p/a'.format(
                vaga)
            link = self.driver.find_element(
                By.XPATH, btn_descricao)
            link.send_keys(Keys.RETURN)
            descricao = self.driver.find_element(
                By.XPATH, '//div[@class="box z-depth-1"]/p')

            dados_vagas[vaga]['descricao'] = descricao.text
            self.driver.back()

        return dados_vagas
