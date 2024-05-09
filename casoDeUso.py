import transformToAlternativeText as tTAT

text = "Explique a imagem para um cego. Ele receberá esta imagem, e deve entende-la. Sua explicação será utilizada como alternative text, portanto, siga boas praticas de alternative text e retorne somente um alternative text."

# criação de um objeto iTAT, passando apikey do google e texto de prompt
object_tTAT = tTAT.ImageToAltertiveText("AIzaSyCO22iUMe3Jzj46Np7_apLqpAmEhMwanJA",textPrompt=text)

imageLink = "https://tfcprw.vtexassets.com/arquivos/ids/173459-800-auto?v=638382826036400000&width=800&height=auto&aspect=true"

imagePath = "/home/fernando/Desktop/imagens/input.jpg"

alternativeText = object_tTAT.gerarTextoAlternativo(imageLink=imageLink)
print(alternativeText)