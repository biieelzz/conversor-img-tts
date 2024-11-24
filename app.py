# Passo 0: Criar uma interface para o usuário
# (Utilizar a biblioteca "streamlit")

# Passo 1: Solicitar que o usuário tire uma foto ou envie um print do texto a ser lido
# (Utilizar a biblioteca "cv")

# Passo 2: Fazer a conversão da imagem para texto
# (Utilizar a biblioteca "easyocr")

# Passo 3: Mostrar o texto na tela

# Passo 4: Fazer a convesão de texto para fala
# (Utilizar a biblioteca "pyttsx3")

# Passo 5: Tocar a fala convertida

############################################################################################

import cv2 as cv
import easyocr
import pyttsx3
import streamlit as st
from PIL import Image
import io

# Função para carregar a imagem
def carregar_imagem():
    uploaded_file = st.file_uploader("Escolha uma imagem", type=["png", "jpg", "jpeg", "bmp", "gif"])
    
    if uploaded_file is not None:
        # Carrega a imagem com a biblioteca Pillow
        imagem = Image.open(uploaded_file)
        
        # Exibe a imagem na interface
        st.image(imagem, caption="Imagem selecionada", use_column_width=True)
        
        # Retorna a imagem carregada para armazená-la em uma variável
        return imagem
    else:
        st.warning("Nenhuma imagem foi carregada.")
        return None

# Cabeçalho da interface
st.title("Conversor de imagem")

# Chama a função para carregar e armazenar a imagem
imagem_carregada = carregar_imagem()

# Exemplo de como acessar e usar a imagem carregada
if imagem_carregada:
    st.write("Imagem carregada com sucesso!")
    st.write(f"Tamanho da imagem: {imagem_carregada.size}")
    st.write(f"Modo da imagem: {imagem_carregada.mode}")
    