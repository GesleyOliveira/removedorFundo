import streamlit as st
from rembg import remove
from PIL import Image
import os

# Função para processar a imagem
def process_image(input_path, output_path):
    try:
        inp = Image.open(input_path)
        output = remove(inp)
        output.save(output_path)
        return True, f"Imagem processada com sucesso! Salva em: {output_path}"
    except Exception as e:
        return False, f"Erro ao processar a imagem: {e}"

# Interface com o usuário usando Streamlit
def main():
    st.title("🖼️ Remoção de Fundo de Imagem")

    st.write(
        "Esse aplicativo permite remover o fundo de uma imagem usando IA. Selecione uma imagem e clique em 'Processar'."
    )

    # Upload de imagem
    uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Imagem Original", use_column_width=True)
        st.write("")
        st.write("Processando...")

        # Definindo o caminho de saída
        output_path = "./imagens/Foto_sem_fundo.png"

        # Processando a imagem
        success, message = process_image(uploaded_file, output_path)

        # Mostrando o resultado
        if success:
            st.success(message)
            st.image(output_path, caption="Imagem Sem Fundo", use_column_width=True)
            st.download_button(
                label="Baixar Imagem Sem Fundo",
                data=open(output_path, "rb").read(),
                file_name="Foto_sem_fundo.png",
                mime="image/png",
            )
        else:
            st.error(message)

if __name__ == "__main__":
    main()
