# 🖼️ Removedor de Fundo de Imagens

Este script usa a biblioteca **rembg** para remover o fundo de uma imagem automaticamente. Ele também usa **Pillow** para manipulação de imagens.

---

## 📦 Requisitos

**Python 3.8 ou superior**

### Bibliotecas Python:

- `rembg`
- `Pillow`

### Instale as dependências com:

```bash
pip install streamlit rembg pillow onnxruntime

Instalando o Python 3.10 (se necessário):

1. python3.10 -m venv venv
2. venv\Scripts\activate
3. pip install rembg pillow onnxruntime


🚀 Como usar
Passos:
1️⃣ Coloque sua imagem no diretório do script (ou tenha o caminho completo dela).

2️⃣ Execute o script: streamlit run app.py

3️⃣ Quando solicitado:

Informe o caminho da imagem de entrada (ex.: imagem.jpg)

Opcionalmente, informe o nome do arquivo de saída (ou deixe vazio para gerar automaticamente)

O script criará uma nova imagem .png com fundo removido.

💻 Exemplo
Entrada:

🖼️ Entre com o caminho da imagem de entrada: imagem.jpg

💾 Entre com o nome do arquivo de saída (ou deixe vazio para padrão):

Saída:

✅ Imagem 'ElonMusk.jpg' carregada com sucesso.

✅ Imagem sem fundo salva como 'ElonMusk_sem_fundo.png'.

📂 Recursos
rembg: ferramenta de remoção de fundo baseada em inteligência artificial.

Pillow: biblioteca para processamento de imagens no Python.

⚠️ Avisos
O script aceita imagens nos formatos comuns (.jpg, .png).

A saída sempre será .png para preservar a transparência.

Certifique-se de fornecer caminhos corretos, principalmente em sistemas Windows (use \\ ou r"C:\caminho\imagem.jpg").
