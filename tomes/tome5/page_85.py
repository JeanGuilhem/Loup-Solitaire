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

check_inventory(current_page_number=85, book=5)

fr_text = """
Les geôliers ouvrent brusquement la porte et font irruption dans
la cellule, l'arme au poing, prêts à l'attaque. Ce sont de véritables
brutes au visage cruel et couturé de cicatrices. Le premier
mouvement de surprise qu'ils esquissent en vous voyant soudain
apparaître se mue rapidement en fureur aveugle : ils se ruent sur
vous et vous collent dos au mur. « On dirait que nous avons
affaire à un petit farceur, n'est-ce pas Sefrou ! » siffle le plus
grand des Gardes. « Un illusionniste des Contrées du Nord qui a
perdu son chemin, sans doute », dit le second d'une voix rauque.
Les deux hommes ricanent de leurs bons mots tandis que dans
leurs yeux brille une lueur malveillante. « Nous allons donner
une leçon à notre ami ! » reprend le premier Garde en vous
mettant sa lame sous la gorge. « Va chercher les poucettes ! »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez attaquer le Garde qui vous tient sous la menace de son épée, rendez-vous au :"))
    st.page_link("tomes/tome5/page_59.py", label="59", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous abstenir, rendez-vous au :"))
    st.page_link("tomes/tome5/page_163.py", label="163", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
