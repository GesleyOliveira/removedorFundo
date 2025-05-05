
# 🖼️ Removedor de Fundo de Imagens

Este projeto permite **remover automaticamente o fundo de imagens** usando inteligência artificial, através das bibliotecas **rembg**, **Pillow** e uma interface gráfica simples feita com **Streamlit**.

---

## 📦 Requisitos

- **Python 3.8 ou superior**
- Recomendado usar **ambiente virtual** (`venv`)

### 📚 Dependências Python

- `streamlit`
- `rembg`
- `pillow`
- `onnxruntime`

Instale tudo com:
```bash
pip install streamlit rembg pillow onnxruntime
```

---

## ⚙️ Configuração do Ambiente Virtual

1️⃣ Crie o ambiente virtual:
```bash
python -m venv venv
```

2️⃣ Ative o ambiente virtual:
- Windows:
    ```bash
    venv\Scripts\activate
    ```
- macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

3️⃣ Instale as dependências no ambiente virtual:
```bash
pip install streamlit rembg pillow onnxruntime
```

---

## 🚀 Como Rodar o Aplicativo

Execute o aplicativo com:
```bash
streamlit run app.py
```

Isso abrirá uma página no navegador (geralmente em [localhost:8501](http://localhost:8501)).

---

## 🖥️ Como Usar

1️⃣ Abra o navegador na página do Streamlit.

2️⃣ Faça o upload de uma imagem (`.jpg`, `.jpeg`, `.png`).

3️⃣ O app mostrará:
- A **imagem original**.
- A **imagem sem fundo** gerada automaticamente.

4️⃣ Clique no botão **"Baixar Imagem Sem Fundo"** para salvar o resultado como `.png`.

---

## 📂 Estrutura do Projeto

```
removedorFundo/
├── app.py              # Código principal do aplicativo Streamlit
├── imagens/            # Pasta para armazenar imagens de entrada e saída
├── venv/               # Ambiente virtual Python (opcional, mas recomendado)
├── README.md           # Este arquivo
```

---

## 💡 Recursos Usados

- **rembg** → IA para remoção de fundo.
- **Pillow** → Processamento e manipulação de imagens.
- **Streamlit** → Interface gráfica interativa no navegador.

---

## ⚠️ Avisos

- A saída sempre será salva como `.png` para preservar a transparência.
- Verifique se o arquivo carregado está em formato suportado (`.jpg`, `.jpeg`, `.png`).
- Em Windows, certifique-se de ter o Visual C++ Runtime instalado para evitar erros do `onnxruntime`.

