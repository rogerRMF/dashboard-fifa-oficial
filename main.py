import streamlit as st
from pages import home
from pages import players
from pages import teams

def main():
    st.sidebar.title("Menu de Navegação")
    opcao = st.sidebar.selectbox("Escolha a Página", ["home", "players", "teams"])

    if opcao == "home":
        home.run()  
    elif opcao == "players":
        players.run()  # A função run() deve existir no arquivo players.py
    elif opcao == "teams":
        teams.run()

if __name__ == "__main__":
    main()
