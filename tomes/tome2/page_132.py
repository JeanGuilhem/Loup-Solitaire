import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=132, book=2)

fr_text = """
Vous atterrissez dans la rue boueuse au milieu d'une pluie de verre
brisé. La chute vous a quelque peu secoué mais vous êtes indemne. Un
villageois furieux, armé d'une matraque, essaie de vous fracasser le
crâne, mais vous roulez sur vous-même et vous vous relevez d'un bond
; avant qu'il ait eu le temps de vous atteindre, vous êtes déjà en train de
courir le long de la rue sinueuse ; vous n'êtes pas au bout de vos peines
cependant, car un Squall à cheval se précipite sur vous, sa lance levée.
Il s'apprête à vous frapper lorsque vous faites un pas de côté qui vous
permet d'éviter le coup. Vous saisissez alors la hampe de son arme et
vous déséquilibrez le Squall qui glisse de sa selle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous décidez de garder la lance, n'oubliez pas de l'inscrire sur votre Feuille d'Aventure."))
    pickup_button("LANCE", key="lance", label="Garder la lance du Squall")
    st.write_stream(stream_text("Si vous souhaitez frapper le Squall à l'aide de sa propre lance, rendez-vous au :"))
    st.page_link("tomes/tome2/page_317.py", label="317", icon="📄")
    st.write_stream(stream_text("Si vous préférez vous emparer de son cheval pour prendre la fuite, rendez-vous au :"))
    st.page_link("tomes/tome2/page_150.py", label="150", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
