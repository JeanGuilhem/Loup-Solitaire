import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=102, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Le tunnel de Tarnalin est une véritable merveille. Il fait plus de 30
mètres de hauteur et de largeur et traverse les montagnes de la chaîne
d'Hammardal en donnant accès à la capitale. D'ordinaire, chariots et
piétons s'y pressent, car c'est la voie obligée entre Port Bax et
Hammardal. Mais lorsque vous y pénétrez, vous avez la surprise de
constater qu'il est désert ; vous n'y découvrez qu'une carriole de fruits
renversée sur la chaussée. La route qui s'enfonce dans les profondeurs
du tunnel éclairé par des torches est vide et silencieuse. Et tandis que
vous avancez sur la chaussée recouverte de pavés, un sentiment
d'inquiétude vous saisit : et si les Monstres d'Enfer étaient arrivés à
Tarnalin avant vous ? Vous marchez pendant une heure et vous arrivez
alors à une bifurcation.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez prendre la voie de gauche, rendez-vous au :"))
    st.page_link("tomes/tome2/page_64.py", label="64", icon="📄")
    st.write_stream(stream_text("Si vous préférez aller à droite, rendez-vous au :"))
    st.page_link("tomes/tome2/page_164.py", label="164", icon="📄")
    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï du Sens de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome2/page_325.py", label="325", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_325.py", label="325", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
