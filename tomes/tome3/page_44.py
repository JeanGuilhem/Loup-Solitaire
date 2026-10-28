import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=44, book=3)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
« Suivez-moi, dit Loi-Kymar, j'ai écouté attentivement tous les
bruits de la forteresse pendant plus d'un an et je connais à
présent toutes les portes dérobées, tous les passages cachés. Du
fond de ma cellule, j'en ai appris davantage sur ces couloirs que
Vonotar lui-même avec toute sa ruse. » Vous suivez alors le
magicien à travers un réseau de tunnels et de passages secrets,
d'escaliers et de salles froides et obscures. Au sommet d'un
escalier particulièrement raide, vous arrivez devant une porte de
pierre. Une odeur étrange et écœurante filtre à travers un petit
judas. « Ce sont les cuisines », murmure Loi-Kymar en faisant
une grimace éloquente pour exprimer tout le dégoût que lui
inspire la pitance servie dans la forteresse. Cette porte secrète est
située juste à côté d'une cheminée dans laquelle brûle un feu
d'enfer. Un grand chaudron de pierre rempli de gruau est
suspendu au-dessus du feu. Deux Barbares des Glaces sont assis
à une table proche, devant des bols vides.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous avez une Potion Noire de Ronces des Cimetières, rendez-vous au :'))
    if has_item("POTION DE RONCES DES CIMETIÈRES"):
        st.page_link("tomes/tome3/page_79.py", label="79", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_79.py", label="79", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous avez une Potion Verte de Brosse à Potences, rendez-vous au :'))
    if has_item("POTION DE BROSSE À POTENCES"):
        st.page_link("tomes/tome3/page_157.py", label="157", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_157.py", label="157", icon="📄", disabled=True)

    st.write_stream(
        stream_text(
            'Si vous ne possédez aucune de ces deux potions, il vous reste à ouvrir la porte pour '
            'attaquer par surprise les Barbares désarmés ; rendez-vous pour cela au :'
        )
    )
    has_potion = has_item("POTION DE RONCES DES CIMETIÈRES") or has_item("POTION DE BROSSE À POTENCES")
    st.page_link("tomes/tome3/page_270.py", label="270", icon="📄", disabled=has_potion)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
