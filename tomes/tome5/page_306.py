import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=306, book=5)

fr_text = """
« Tenez-vous bien, Loup Solitaire ! » crie Banedon en reprenant
le contrôle de sa barre de cristal. Vous lui obéissez et vous
saisissez le garde-fou tout en bloquant vos pieds contre le bas du
bastingage pour plus de sûreté, car vous avez deviné la
manœuvre que le jeune sorcier a l'intention d'effectuer. 
« Attention : coup du pirate ! » crie alors Banedon à ses Nains qui
sont toujours en train de livrer bataille. Puis il tourne
brusquement la barre à gauche. La Nef du ciel réagit
immédiatement à son geste et bascule jusqu'à ce que le pont se
retrouve presque à la verticale. Les Nains obéissent à l'ordre
donné et se jettent à plat ventre sur le pont, s'agrippant aux
planches comme des patelles sur la quille d'un galion. Les
Drakkars, eux, perdent l'équilibre, culbutent sur le pont et la
passerelle, puis ils tombent dans le vide en hurlant de terreur.
Banedon redresse alors le vaisseau et des cris de victoire
retentissent tandis que la Nef du ciel file à vive allure vers les
Foos. « Œil pour œil, dent pour dent ! » clament les Nains à l'unisson.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_247.py", label="247", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
