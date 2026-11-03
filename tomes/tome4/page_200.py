import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=200, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
La forêt grouille de brigands, mais vos réflexes sont prompts et
votre habileté de Seigneur Kaï vous permet de ne pas être repéré.
Vous arrivez enfin de l'autre côté de la forêt touffue. Au-delà
s'étendent des plaines dépourvues d'arbres qu'il faut traverser
pour atteindre Ruanon. Le spectacle qui s'offre à vos yeux est
singulièrement inquiétant. Une grande partie de la ville minière
a été en effet incendiée. Les boutiques, les maisons, les tavernes
qui s'alignaient le long des rues ne sont plus que des tas de
cendres fumantes. Vous craignez alors que Ruanon n'ait été
entièrement détruite. Une faible brise, cependant, dissipe bientôt les nuages de fumée qui masquent les
ruines comme des rideaux gris, et vous apercevez une barricade
dressée autour d'une tour de pierre. Une bannière en lambeaux
flotte au sommet de la tour et une lueur d'espoir s'allume aussitôt
en vous. Il s'agit là, en effet, du drapeau du Sommerlund.
L'habituel soleil qui symbolise votre pays est ici bordé d'une
soutache blanche indiquant que ce drapeau appartient à un
régiment de la cavalerie royale. Soudain, un craquement retentit
derrière vous. Vous faites aussitôt volte-face et vous apercevez
trois brigands qui s'avancent dans votre direction. La pointe
d'acier de leurs lances scintille. On dirait que ces armes ont été
trempées dans un liquide clair et gluant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Chasse ou s'il vous est déjà arrivé de visiter Crique-en-Gorn, rendez-vous au :"))
    gorn = st.checkbox("Vous avez déjà visité Crique-en-Gorn (au cours d'une aventure précédente)", key="crique_en_gorn")
    if has_kai("La Chasse") or gorn:
        st.page_link("tomes/tome4/page_45.py", label="45", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_45.py", label="45", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous souhaitez affronter les brigands, rendez-vous au :'))
    st.page_link("tomes/tome4/page_133.py", label="133", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre la fuite, vous devrez traverser la plaine en courant pour essayer d'atteindre Ruanon qui se trouve à 800 mètres de distance. Rendez-vous pour cela au :"))
    st.page_link("tomes/tome4/page_307.py", label="307", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
