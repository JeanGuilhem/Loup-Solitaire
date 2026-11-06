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

check_inventory(current_page_number=133, book=6)

fr_text = """
« Vous voyez bien devant vous le Trou de l'Enfer, dit un Ogron.
Lorsque le siège de la ville commença, le prince Ewewin envoya
dix éclaireurs afin qu'ils découvrent où ce passage menait. Mais
les dix hommes ne revinrent jamais ; alors on envoya dix Ogrons,
aucun d'eux n'en est jamais revenu non plus ! » Un autre Ogron,
qui était en train de fendre un tronc d'arbre à mains nues,
vient se mêler à la conversation : « On entend de curieux bruits
dans le Trou de l'Enfer, très tard dans la nuit, dit-il d'un air
entendu... Des bruits horribles ! » ajoute-t-il en passant un
doigt épais sur sa gorge bleu foncé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez demander aux Ogrons la permission d'utiliser l'un de leurs pontons flottants pour vous rendre jusqu'au Trou de l'Enfer, rendez-vous au :"))
    st.page_link("tomes/tome6/page_179.py", label="179", icon="📄")

    st.write_stream(stream_text("Si vous préférez y aller à la nage, rendez-vous au :"))
    st.page_link("tomes/tome6/page_171.py", label="171", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
