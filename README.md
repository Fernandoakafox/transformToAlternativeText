# Aumentando a Acessibilidade na Web com Gemini

Este projeto foi desenvolvido com o objetivo de aumentar a acessibilidade na web através da automatização da criação de "Alternative Text" (texto alternativo) para imagens. O Alternative Text é um campo fundamental para audiodescritores, permitindo que pessoas cegas compreendam o conteúdo das imagens ao navegar na internet. Infelizmente muitos sites deixam o alternative text em branco, isto é, sem a real descrição da imagem. Este projeto visa diminuir, e quem sabe eliminar, a falta de alternative text.

## Mas o que é um Audio Leitor?
Um audio leitor é um software ou aplicativo que converte texto em áudio, permitindo que os usuários ouçam o conteúdo em vez de lê-lo. No momento em que o software encontra uma imagem em uma página da web, por exemplo, ele pode usar o texto alternativo para descreve-la.
 
![Design sem nome](https://github.com/Fernandoakafox/transformToAlternativeText/assets/124198375/e889b03e-86cd-4b2c-b698-638e01b4664d)

## Funcionamento do projeto
Com o envio de uma imagem e um texto contendo diretrizes de boas práticas para a criação de texto alternativo, este projeto é capaz de gerar automaticamente um texto alternativo preciso e de alta qualidade. A automação deste processo pode ser feita atravez deste projeto, que contém codigo no paradigma de orientação a objetos. Deste modo, você só precisa inicializar o objeto uma vez, passando como argumento a sua API-Key do Google Cloud e o seu texto de boas práticas. Apartir dai, é só chamar a função "gerarTextoAlternativo()" passando como parametro uma imagem.

![E se você estivesse comprando roupas, mas na hora (2)](https://github.com/Fernandoakafox/transformToAlternativeText/assets/124198375/33d4edb4-5fa4-4731-b803-20a3c0e57d9c)

## Veja exemplos de textos alternativos criados pelo projeto

![E se você estivesse comprando roupas, mas na hora (5)](https://github.com/Fernandoakafox/transformToAlternativeText/assets/124198375/b02e42dd-95ec-4019-a1a9-f89d2b22b39b)


## No exemplo abaixo, veja a riqueza de detalhes
![E se você estivesse comprando roupas, mas na hora (6)](https://github.com/Fernandoakafox/transformToAlternativeText/assets/124198375/7a83d4ed-e12e-4737-9dfd-ea7435e90143)

## No exemplo abaixo, veja como o texto consegue passar a nossão do ambiente da imagem
![E se você estivesse comprando roupas, mas na hora (7)](https://github.com/Fernandoakafox/transformToAlternativeText/assets/124198375/0cc9bc6a-9fa4-4c51-90dd-c9b1ea8ddc21)


## Como faço para testar o programa?
1. Clone o repositório:

   git clone git@github.com:Fernandoakafox/transformToAlternativeText.git
   cd seu-projeto

2. Instale as dependências do projeto:

   pip install -r requirements.txt


3. Utilize o arquivo casoDeUso.py como guia:

   Abra e modifique o arquivo casoDeUso.py





