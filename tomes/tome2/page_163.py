import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=163, book=2)

fr_text = """
« Nous avons le vaisseau le plus rapide de toutes les mers du Nord, il
n'est pas de navire qui puisse rattraper le Sceptre Vert », affirme le
capitaine. Il a raison en effet, car bientôt le bateau pirate disparaît à
l'horizon. « Depuis vingt-cinq ans que je navigue, je n'ai jamais vu les
pirates Lakuri s'aventurer si loin au nord, dit le capitaine en se caressant
la barbe d'un air songeur, ils doivent être sur la piste d'un bien riche
butin pour s'éloigner ainsi de leurs îles tropicales. » Et tandis que le
capitaine descend dans sa cabine, vous pensez avec inquiétude que ce «
riche butin » pourrait bien être vous-même.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_240.py", label="240", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
