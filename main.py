import streamlit as st
from streamlit_option_menu import option_menu

import index, about, contact

st.set_page_config(
    page_title="Narcisse",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
)

class Menu:
    def __init__(self):
        self.apps = []
        
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title="Narcisse",
                options=["Index", "About", "Contact"],
                icons=["house", "book", "envelope"],
                menu_icon="cast",
                default_index=1,
                orientation="vertical",
                styles={
                    "container": {"padding": "5!important", "background-color": "black"},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color":"white", "font-size": "23px", "text-align": "left", "margin": "0px", "--hover-color": "white"},
                    "nav-link-selected": {"background-color": "green"},
                }
            )

        if app == "Index":
            index.app()
        if app == "About":
            about.app()
        if app == "Contact":
            contact.app()


    run()