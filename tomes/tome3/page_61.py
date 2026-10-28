import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=61, book=3)

fr_text = """
Vous pénétrez dans une galerie couverte qui entoure une cour
intérieure. Soudain, vous entendez le tintement sourd d'une
cloche de pierre que l'on sonne dans une tour de guet située au-
dessus de la forteresse ; c'est une cloche d'alarme. La galerie et la
cour intérieure sont complètement vides ; vous n'apercevez
qu'un traîneau à voile rangé près de l'entrée. Vous décidez alors
de prendre le risque d'aller voir et vous descendez l'escalier qui
mène dans la cour. Quelques instants plus tard, vous découvrez
que le traîneau est chargé de vivres et de matériel en provenance
de Liouk. Toute la forteresse est à présent alertée de votre arrivée
et il ne vous est donc plus possible d'accomplir votre mission. La
seule chose qui vous reste à faire, c'est de vous enfuir sur le
traîneau à voile pendant qu'il en est encore temps. Dans dix
jours, vous aurez rejoint le navire Cardonal et vous n'aurez plus
qu'à reconnaître l'échec de votre mission.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.error("Votre mission a échoué : votre aventure dans le tome 3 s'achève ici.")
    st.page_link("tomes/tome1/crafting_hero.py", label="Démarrer une nouvelle aventure", icon="⚔️")
    st.page_link("accueil.py", label="Retour à l'accueil", icon="🏠")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
