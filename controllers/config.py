import yaml


class Config:
    @staticmethod
    def get_config() -> dict:
        """Lê arquivo de configuração

        Returns:
            dict: dicionario com as configurações
        """
        with open("config.yaml", "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
            return data
