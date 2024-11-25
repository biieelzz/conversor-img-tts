import streamlit as st
import cv2
import easyocr
import pyttsx3
from PIL import Image
import numpy as np
import os


# Função para carregar e exibir a imagem
def carregar_imagem():
    with st.container(border=True):
        st.subheader("Envio de imagem 🖼️", divider="rainbow", anchor=False)
        st.write('\n')
        # Prompt para o usuário carregar a imagem
        imagem_enviada = st.file_uploader("Envie uma imagem ou capture uma foto para extrair texto e ouvir sua conversão em fala",
                                          type=["jpg", "jpeg", "png",
                                                "bmp", "tiff", "webp"]
                                          )

        # Exibindo a imagem na tela
        if imagem_enviada:
            imagem = Image.open(imagem_enviada)
            st.image(imagem, caption="Imagem carregada", use_column_width=False)

            # Convertendo a imagem carregada do formato PIL (utilizado pelo Streamlit) para o formato OpenCV (matriz NumPy)
            # Alterando o espaço de cores de RGB para BGR, que é o padrão utilizado pelo OpenCV
            return cv2.cvtColor(np.array(imagem), cv2.COLOR_RGB2BGR)

        return None


# Função para extrair texto da imagem
def extrair_texto_imagem(imagem):
    st.write('\n')
    st.write('\n')
    with st.container(border=True):
        # Subtítulo dentro do streamlit
        st.subheader("Extração de texto 📄", divider="rainbow", anchor=False)
        st.write('\n')

        # Iniciando o leitor do easyocr
        # Suporte para português e inglês
        leitor = easyocr.Reader(['pt', 'en'])

        # Salvando o texto em uma variável
        resultados = leitor.readtext(imagem)

        # Concatenando os textos detectados
        texto_extraido = " ".join([resultado[1] for resultado in resultados])

        # Mostrando em tela o texto extraído
        st.write(texto_extraido)

        return texto_extraido


# Função para converter texto em fala e salvar localmente
def converter_texto_fala(texto):
    # Convertendo o texto em fala e salvando em um arquivo de áudio local
    # Retornando o caminho do arquivo de áudio gerado
    if not texto.strip():
        st.error(
            "O texto está vazio. Certifique-se de que a imagem contém texto legível.")
        return None

    try:
        # Iniciando o conversor de texto para fala
        engine = pyttsx3.init()

        # Definindo diretório onde o áudio será salvo
        diretorio_audio = "audios"
        if not os.path.exists(diretorio_audio):
            # Criando o diretório caso ele não exista
            os.makedirs(diretorio_audio)

        # Definindo o nome do arquivo de áudio
        arquivo_audio = os.path.join(
            diretorio_audio, "audio_convertido.mp3")

        # Salvando o áudio no diretório local
        engine.save_to_file(texto, arquivo_audio)
        engine.runAndWait()

        return arquivo_audio

    except Exception as e:
        st.error(f"Erro ao converter texto para fala: {e}")
        return None


# Função main do app
def main():
    # Configuração da página
    st.set_page_config(
       page_title="Conversor IMG > TEXT/TTS",
        page_icon="💻",
    )

    # Informações da barra lateral
    avatar = "images/Gabriel.jpg"
    with st.sidebar:
        st.image(avatar, use_column_width=False)
        st.markdown("Desenvolvido por :violet[**Gabriel Oliveira**]")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.markdown("**LinkedIn:** https://bit.ly/3Op4te9")
        st.markdown("**GitHub:** https://bit.ly/4g1kNOe")

    st.header("Conversor de :red-background[imagens] para :blue-background[texto] e :violet-background[fala]", anchor=False)
    st.write('\n')
    st.write('\n')

    # Carregando imagem
    imagem = carregar_imagem()

    if imagem is not None:
        # Extraindo texto da imagem
        texto_extraido = extrair_texto_imagem(imagem)

        if texto_extraido:
            # Convertendo texto em fala e criando um player no streamlit
            caminho_audio = converter_texto_fala(texto_extraido)

            if caminho_audio:
                # Lendo o arquivo de áudio salvo localmente em modo binário
                with open(caminho_audio, "rb") as audio_file:
                    audio_bytes = audio_file.read()

                st.write('\n')
                st.write('\n')
                with st.container(border=True):
                    # Subtítulo dentro do streamlit
                    st.subheader("Conversão para Fala 🗣️", divider="rainbow", anchor=False)
                    st.write('\n')

                    # Criando o player de áudio
                    st.audio(audio_bytes, format="audio/mp3")

            else:
                st.warning("Não foi possível gerar o áudio.")


# Execução do app
if __name__ == "__main__":
    main()
