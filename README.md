# Relatório Vagas Cadmus
Essa solução foi desenvolvida utilizando puramente a linguagem de programação Python com algumas biblioteca afim de automatizar o envio de relatórios da relação de vagas do dia da Cadmus.
  

## Integrantes

<table align="center">
  <tr>
	<td  align="center"><a  href="https://github.com/bruno-cabralz"><img  style="border-radius: 50%;"  src="https://avatars.githubusercontent.com/u/76916533?v=4"  width="100px;"  alt=""/><br /><sub><b>Bruno Cabral</b></sub></a><br />
	</td>
    <td align="center"><a href="https://github.com/MariaClaraSanchez"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/57421273?v=4" width="100px;" alt=""/><br /><sub><b>Maria Clara Sanchez</b></sub></a><br />
	<td  align="center"><a  href="https://github.com/Cad-Renata"><img  style="border-radius: 50%;"  src="https://avatars.githubusercontent.com/u/96484353?v=4"  width="100px;"  alt=""/><br /><sub><b>Renata Ferreira</b></sub></a><br />
</td>
</table>

  

# Configuração

## Máquina Virtual
Caso queira executar o projeto separadamente da onde fica seus documentos python é preciso cria uma máquina virtual e para isso precisa da os seguintes passos :
<br>
1º Instalar o env em sua máquina para isso utilize o comando :
```
pip install venv
```
2º Criar sua máquina virtual:
```
python3 -m venv nome_maquina_virtual-env
```
3º Escolha o comando de acordo com seu sistema opercional:
#### Para Windows:
```
nome_maquina_virtual-env\Scripts\activate.bat
```
#### Para Unix ou no MacOS:
```
source nome_maquina_virtual-env/bin/activate
```

## Instalando Dependências
Use o gerenciado de pacote [pip](https://pip.pypa.io/en/stable/) para instalar as dependências.
```bash
pip install -r requirements.txt
```

## Arquivo de Configuração
Para executar o projeto é necessário criar um arquivo `config.yaml` na raiz do projeto. Segue exemplo de estrutura do arquivo:

```yaml

email:
  remetente: '' # endereço do remetente
  senha: '' # senha do remetente
  destinatario: '' # endereço do destinatario

site:
  driver: '' # caminho do driver (chromedriver.exe)

```

# Inicializando

Para executar o robô basta executar o comando :

```
pyhton main.py
```
