# Aumentando a Acessibilidade na Web com Gemini

Este projeto foi desenvolvido com o objetivo de aumentar a acessibilidade na web através da automatização da criação de "Alternative Text" (texto alternativo) para imagens. O Alternative Text é um campo fundamental para audiodescritores, permitindo que pessoas cegas compreendam o conteúdo das imagens ao navegar na internet. Infelizmente muitos sites deixam o alternative text em branco, isto é, sem a real descrição da imagem. Este projeto visa diminuir, e quem sabe eliminar, a falta de alternative text.

## Mas o que é um Audio Descritor?
Um audio descrito é um software ou aplicativo que converte texto em áudio, permitindo que os usuários ouçam o conteúdo em vez de lê-lo. No momento em que o software encontra uma imagem em uma página da web, por exemplo, ele pode usar o texto alternativo para descreve-la.
 
![E se você estivesse comprando roupas, mas na hora (10)](https://github.com/Fernandoakafox/transformToAlternativeText/assets/124198375/e45f94be-7d5d-440f-a72c-61a87de88685)

## Funcionamento do projeto
Com o envio de uma imagem e um texto contendo diretrizes de boas práticas para a criação de texto alternativo, este projeto é capaz de gerar automaticamente um texto alternativo preciso e de alta qualidade. A automação deste processo pode ser feita atravez deste projeto, que contém codigo no paradigma de orientação a objetos. Deste modo, você só precisa inicializar o objeto uma vez, passando como argumento a sua API-Key do Google Cloud e o seu texto de boas práticas. Apartir dai, é só chamar a função "gerarTextoAlternativo()" passando como parametro uma imagem.

![E se você estivesse comprando roupas, mas na hora (9)](https://github.com/Fernandoakafox/transformToAlternativeText/assets/124198375/a2a58783-2318-49e6-a0eb-0262f6bf7f98)

## Veja exemplos de textos alternativos criados pelo projeto
![5](https://github.com/Fernandoakafox/transformToAlternativeText/assets/124198375/b9a2950a-1731-44db-a294-a1212eade8eb)



## No exemplo abaixo, veja a riqueza de detalhes
![3](https://github.com/Fernandoakafox/transformToAlternativeText/assets/124198375/b54f030e-7a7a-43a4-be86-0ff45db49c25)

## No exemplo abaixo, veja como o texto consegue passar a nossão do ambiente da imagem
![4](https://github.com/Fernandoakafox/transformToAlternativeText/assets/124198375/edfe4bac-3866-430b-a88d-e313ea08b334)

## Como faço para testar o programa?
### 1. Clone o repositório:

   ![image](https://github.com/Fernandoakafox/transformToAlternativeText/assets/124198375/129dff52-53d5-4dde-a65d-d3f3b277b221)


### 2. Instale as dependências do projeto:

   ![image](https://github.com/Fernandoakafox/transformToAlternativeText/assets/124198375/cd44aa99-eb9b-447b-9238-efb0da55aa95)


### 3. Utilize o arquivo casoDeUso.py como guia:

![Captura de tela 2024-05-10 115945](https://github.com/Fernandoakafox/transformToAlternativeText/assets/124198375/8203a597-6a70-48e9-88d3-69b47dd19ae7)




