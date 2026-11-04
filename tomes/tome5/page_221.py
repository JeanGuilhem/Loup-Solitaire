import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=221, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Emergeant d'un banc de nuages, vous apercevez un vaisseau
volant : c'est une petite embarcation, pas plus grande qu'une
péniche de la rivière Unoram, avec deux voiles triangulaires qui
claquent au vent de chaque côté de la proue incurvée. Dans la
lumière décroissante du crépuscule, vous voyez un long étendard
flottant en haut du mât et un vrombissement sourd parvient
jusqu'à vos oreilles. Vous regardez, incrédule, ce spectacle
insolite : êtes-vous victime d'une hallucination trompeuse créée
par les Seigneurs des Ténèbres, ou bien est-ce un mirage dû à un
jeu de lumières ? Mais tandis que l'embarcation se rapproche,
force vous est de constater qu'il s'agit bel et bien d'un vaisseau
volant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez le Pendentif à l'Etoile de Cristal, rendez-vous au :"))
    if has_item("PENDENTIF À L'ÉTOILE DE CRISTAL"):
        st.page_link("tomes/tome5/page_336.py", label="336", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_336.py", label="336", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne possédez pas cet Objet Spécial, rendez-vous au :"))
    if has_item("PENDENTIF À L'ÉTOILE DE CRISTAL"):
        st.page_link("tomes/tome5/page_275.py", label="275", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_275.py", label="275", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
