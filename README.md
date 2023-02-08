# QR Generator

Esse código foi desenvolvido para facilitar o processo de geração de códigos QR, por pessoas que tenham dificuldades na realização desse processo. 


## 🔧 Ferramentas Utilizadas

-   qrcode: para criar a lógica da função que produz a conversão de texto em um QR Code.
-   tkinter: para criar toda a parte visual da aplicação (telas, botões, menus de entrada de informação e textos visíveis).

## ⚙️ Como Funciona

-   Inicialização da aplicação demonstra a tela com uma label(QR Generator), logo abaixo o menu de entrada de informação e um botão(QR).
-   O Usuário deve colar um link no menu de entrada de informação.
-   Após concluída a entrada de informação, o botão "QR" deve ser pressionado.
-   Um menu filedialog será exibido na tela do usuário indicando que este, deve escolher o diretório no qual deseja gerar a imagem.
-   Com o diretório selecionado, o usuário deverá pressionar o botão escrito "Salvar".
-   Ao clickar em salvar, o filedialog será automáticamente fechado, o usuário deve esperar um sinal verde (✅) na tela da aplicação.
-   Após a apresentação do sinal verde na tela, o usuário poderá verificar o sua imagem QR que estará disponível no diretório indicado e fechar o aplicativo.

## 💻 Como executar o código

- Instalar Python
- Para executar esse código, você precisa ter as seguintes bibliotecas instaladas: qrcode, gTTS e tkinter. Elas podem ser instaladas usando o gerenciador de pacotes Python pip com os seguinte comandos: (pip install) 
- Para executar o arquivo (python **qrgenerator_screenV2.py**)
