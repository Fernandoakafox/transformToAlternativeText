import transformToAlternativeText as tTAT

# caso queira dar como prompt uma string
stringPrompt = "Explique a imagem para uma pessoa cega. Esta pessoa receberá esta imagem, e deve entende-la. Sua explicação será utilizada como alternative text, portanto, siga boas praticas de alternative text e retorne somente um alternative text."

apiKey = "Digite sua apo key aqui"

# criação de um objeto iTAT, passando apikey do google e texto de prompt
object_tTAT = tTAT.ImageToAltertiveText(apiKey)

imageUrl = "https://images.pexels.com/photos/312839/pexels-photo-312839.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"

imagePath = "/home/fernando/Desktop/imagens/input.jpg"

alternativeText = object_tTAT.gerarTextoAlternativo(imageUrl=imageUrl)
print(alternativeText)
