import streamlit as st
from streamlit_option_menu import option_menu
import about_us, chat, home

class MultiApp:
    
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
                menu_title='Medibot',
                options=['Home','Chat','About Us'],
                icons=['house-fill','chat-text-fill','info-circle-fill'],
                menu_icon='robot',
                default_index=0,
                styles={
                        "container": {"padding": "5!important","background-color":"#262730"},
                        "icon": {"color": "white", "font-size": "15px"},
                        "nav-link": {"color": "white", "font-size": "15px", "text-align": "left", "margin": "opx", "--hover-color": "blue"},
                        "nav-link-selected": {"background-color": "#02ab21"},
                }
            )
            
        if app== 'Home':
            home.app()
        if app== 'Chat':
            chat.app()
        if app== 'About Us':
            about_us.app()
    
    run()