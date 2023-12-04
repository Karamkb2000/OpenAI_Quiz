import openai
import streamlit as st

from app.app import get_app

OPENAI_TOKEN = "OPENAI_TOKEN"

def initial_config():
    """
    Initial configuration of OpenAI API and streamlit
    """
    try:
        openai.api_key = st.secrets[OPENAI_TOKEN]
    except KeyError:
        st.error("OpenAI API key not found in secrets.toml.")
        st.stop()

    st.set_page_config(
        page_title="Exam generator",
        page_icon=":pencil2:",
    )

def main():
    initial_config()

    app = get_app()
    app.render()

if __name__ == '__main__':
    main()
