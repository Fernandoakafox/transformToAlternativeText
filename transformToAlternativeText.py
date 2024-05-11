import google.generativeai as genai
import PIL.Image
import requests
import os

def readTextArchive(archivePath):
  """Recebe o caminho de um arquivo txt e retorna uma string contendo o conteudo do texto

  Parametros:
  - archivePath (str): Caminho do arquivo .txt

  """
  with open(archivePath, "r") as file:
    text = file.read()
    return text

def downloadImagem(url:str, nome_arquivo:str):
    """Recebe uma url de uma imagem e o nome do arquivo, contendo o formato, em que a imagem deverá ser arquivada.

    Parametros:
    - url(str): url da imagem que será baixada
    -nome_arquivo(str): nome que a imagem terá

    Retorno:
    -Boolean: True caso foi feito o download e False caso não foi possivel


    """
    # Faz o request da URL da imagem
    resposta = requests.get(url)

    # Verifica se o request foi bem-sucedido
    if resposta.status_code == 200:
        # Abre o arquivo em modo de escrita binária
        with open(nome_arquivo, 'wb') as arquivo:
            # Escreve o conteúdo da resposta no arquivo
            arquivo.write(resposta.content)
        return True
    else:
        return None

class ImageToAltertiveText:
    def __init__(self, chaveApiGoogleGemini, archiveTxtPromptPath=None, stringPrompt=None):
        """Recebe a chave API do Google Gemini e o caminho para um arquivo de texto ou uma string que deve conter as orientações de como o modelo deve gerar o texto alternativo(EX: arquivo de texto contendo o texto Appropriate Use of Alternative Tex + diretrizes especificas do seu uso: Imagem de blogspot ou Imagem de marketplace...)

        Parametros:
        - chaveApiGoogleGemini (str): chave API do Google Gemini
        - stringPrompt (str): texto no formato string contendo o texto Appropriate Use of Alternative Tex + diretrizes especificas do seu uso: Imagem de blogspot ou Imagem de marketplace...
        - archiveTxtPrompt (.txt): arquivo de texto contendo o texto Appropriate Use of Alternative Tex + diretrizes especificas do seu uso: Imagem de blogspot ou Imagem de marketplace...

        """
        self.apiKey = chaveApiGoogleGemini
        genai.configure(api_key=self.apiKey)

        # verificando se o usuario deu algum prompt especifico, do contrario é utilizado o prompt padrao com diretrizes para criação de alternative text
        if stringPrompt:
          self.stringPrompt = stringPrompt
        elif archiveTxtPromptPath:
          self.stringPrompt = readTextArchive(archiveTxtPromptPath)
        else:
          self.stringPrompt = readTextArchive("diretrizes_para_criacao_de_alternative_text.txt")

        # defini a temperatura do modelo
        self.modelTemperature = 1, #Defini a temperatura do modelo como 1 caso o usuario não especifique,

        # configura o modelo
        self.model = self.configureGenerativeModel()



    def configureGenerativeModel(self):
      # configurações do modelo relacionadas a "criatividade" (abaixo criamos um dicionario de opções)
      generation_config = {
        "candidate_count": 1, #as vezes o modelo retorna diversos candidatos a resposta, estamos especificando que queremos apenas 1 resposta
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
      }

      # configurações do modelo relacionadas a segurança
      safety_settings = [
        {
          "category": "HARM_CATEGORY_HARASSMENT",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
          "category": "HARM_CATEGORY_HATE_SPEECH",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
          "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
          "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
      ]

      # modelo do gemini que vamos utilizar
      model_name = "gemini-1.5-pro-latest"

       # retorna as configurações do modelo
      return genai.GenerativeModel(model_name=model_name, generation_config=generation_config, safety_settings=safety_settings)


    def gerarTextoAlternativo(self, imageUrl: str = None, imageArchive: str = None):
        """Recebe a URL de uma imagem ou caminho e faz o download da imagem. A imagem é aberta e enviada para a API Google generativeai junto com o prompt textual que foi solicitado na construção do objeto. O retorno é um texto alternativo que segue as orientações definidas pelo prompt textual.

        Parametros:
        - imageUrl (string, optional): string da imagem que necessita um alternative text
        - imagePath (string, optional): caminho da imagem que necessita um alternative text

        Retorno:
        - None: caso o link da imagem esteja quebrado
        - str: string contendo o alternative text
        """

        if imageUrl:
            downloadImagem(imageUrl, "tempImage.png")
            imagePath = "tempImage.png"
        elif imageArchive:
            imagePath = imageArchive

        # abre a imagem e armazena-a na variavel img. Após aberta, ela fica na memoria.
        img = PIL.Image.open(imagePath)

        # faz uma solicitação enviando uma imagem e um texto. Armazena a resposta em response
        response = self.model.generate_content([self.stringPrompt, img])

        # fecha a imagem
        img.close()

        # se tivemos que baixar a imagem, agora excluimos ela
        if imageUrl:
            # exclui a imagem temporaria
            os.remove("tempImage.png")

        # retorna o alternative text em formato de texto
        return response.text