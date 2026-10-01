import io
from PIL import Image
import streamlit as st
from config.logging_config import logger
from controllers.main_controller import MainController
from database.connection import check_db_connection, init_db

# Configuração da página Streamlit
st.set_page_config(
    page_title="Visão Computacional - Neon.tech",
    page_icon="📷",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inicializa as tabelas no banco de dados se necessário
try:
    init_db()
except Exception as e:
    logger.error(f"Falha ao rodar init_db: {e}")

controller = MainController()

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("📌 Menu & Status")
st.sidebar.markdown("---")

# Verificação de status da conexão com Neon.tech
db_status = check_db_connection()
if db_status:
    st.sidebar.success("🟢 Banco de Dados: Conectado (Neon.tech)")
else:
    st.sidebar.error("🔴 Banco de Dados: Desconectado")

st.sidebar.markdown("---")
st.sidebar.info(
    "Navegue pelo menu lateral para acessar o **Histórico** e os **Dashboards**."
)

# --- CABEÇALHO PRINCIPAL ---
st.title("📷 Visão Computacional em Tempo Real")
st.write(
    "Captação de imagem via webcam, processamento automático com OpenCV e persistência na nuvem com PostgreSQL (Neon.tech)."
)

col_cam, col_result = st.columns([1, 1])

with col_cam:
    st.subheader("📹 Câmera")
    # Componente nativo do Streamlit para captura via Webcam
    camera_input = st.camera_input("Acesse sua webcam e clique para capturar")

if camera_input is not None:
    # Converter a entrada da câmera em imagem PIL
    image_bytes = camera_input.getvalue()
    pil_img = Image.open(io.BytesIO(image_bytes))

    with col_cam:
        st.success("Foto capturada com sucesso!")

    # Processamento Automático
    with st.spinner("Analisando imagem e salvando no Neon.tech..."):
        try:
            results = controller.process_and_save_capture(pil_img)

            with col_result:
                st.subheader("🔍 Resultado da Análise Automática")
                st.markdown(f"**ID da Análise:** `{results['id']}`")
                st.markdown(f"**Descrição:** {results['descricao']}")

                # Grade de Métricas
                m1, m2 = st.columns(2)
                m1.metric("Pessoas Detectadas", results["quantidade_pessoas"])
                m2.metric("Rostos Encontrados", results["rostos"])

                m3, m4 = st.columns(2)
                m3.metric("Luminosidade", f"{results['luminosidade']}")
                m4.metric("Nitidez", f"{results['nitidez']}")

                st.markdown(f"**Objetos Identificados:** {results['objetos']}")
                st.markdown(f"**Cores Predominantes:** {results['cores']}")
                st.markdown(f"**Idade Aproximada:** {results['idade']}")
                st.markdown(f"**Emoção Predominante:** {results['emocao']}")

                st.success("Análise persistida com sucesso!")

        except Exception as e:
            st.error(f"Erro no processamento da imagem: {e}")