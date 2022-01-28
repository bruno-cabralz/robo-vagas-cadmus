from controllers.site_vagas_cadmus import SiteCadmus
from controllers.relatorio_vagas import Planilha
from controllers.email import Email
from controllers.config import Config
import time
import schedule


def start():
    config = Config.get_config()
    site_cadmus = SiteCadmus(config['site']['driver'])
    site_cadmus.acessar_vagas()
    vagas = site_cadmus.pegar_vagas()

    vagas = site_cadmus.pegar_descricao_vagas(vagas)
    planilha = Planilha()
    planilha.formatar_planilha()
    planilha.escreve_dados(vagas)

    email = Email(config['email']['destinatario'],
                  config['email']['remetente'], config['email']['senha'])
    email.enviar_email()


if __name__ == '__main__':
    start()
    schedule.every().day.at("14:19").do(start)

    while True:
        schedule.run_pending()
        time.sleep(1)
