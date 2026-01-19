import streamlit as st
from components.sidebar import sidebar_ui
from components.chat_ui import chat_ui
from components.pdf_handler import handle_pdf_upload

# -------- DARK SKY THEME --------
st.markdown(
    """
    <style>

    /* Full page dark sky background */
    .stApp {
        background: linear-gradient(180deg, #020617, #0b1235, #1a1f5c);
        font-family: 'Segoe UI', sans-serif;
    }

    /* Make main containers transparent (removes white) */
    .block-container,
    .stMain,
    section[data-testid="stSidebar"],
    .css-1d391kg,
    .css-12oz5g7 {
        background: transparent !important;
    }

    /* Sidebar with subtle dark glass effect */
    section[data-testid="stSidebar"] {
        background: rgba(10, 15, 40, 0.6) !important;
        backdrop-filter: blur(6px);
    }

    /* Headings in sky style */
    h1, h2, h3 {
        color: #e6f2ff;
        text-shadow: 1px 1px 6px #3b82f6;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #2563eb, #6d28d9);
        color: white;
        border-radius: 10px;
        border: none;
    }

    /* Input boxes — dark glass look */
    .stTextInput>div>div>input,
    .stTextArea>div>textarea {
        background: rgba(255,255,255,0.15);
        color: white;
        border-radius: 8px;
        border: 1px solid #3b82f6;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------- CUSTOM THEME (BACKGROUND & FONT) ----------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f4ff;   /* change this for background */
        font-family: 'Segoe UI', sans-serif;
    }

    h1, h2, h3 {
        color: #1f3b4d;              /* change heading color */
        font-family: 'Poppins', sans-serif;
    }

    .stButton>button {
        background-color: #4f46e5;
        color: white;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="StudyBuddy", page_icon="🧠", layout="wide")

# Initialize session state
if "pdf_content" not in st.session_state:
    st.session_state.pdf_content = None
if "user_focus" not in st.session_state:
    st.session_state.user_focus = ""

# Unpack the tuple returned by sidebar_ui()
selected_mode, selected_sub_mode = sidebar_ui()

# Header
st.title("🧠 StudyBuddy - Your Smart Study Assistant")

# PDF Handler (optional upload)
st.markdown("### 📚 Upload a PDF (Optional)")
pdf_text, user_focus, summarize_clicked = handle_pdf_upload()

if summarize_clicked and pdf_text:
    st.session_state.pdf_content = pdf_text
    st.session_state.user_focus = user_focus
    st.divider()
    st.success("✅ PDF loaded! Starting summary chat...")

st.divider()

# Pass mode and sub_mode separately to chat_ui
chat_ui(selected_mode, selected_sub_mode)