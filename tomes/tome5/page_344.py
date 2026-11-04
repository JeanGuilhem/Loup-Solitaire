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

check_inventory(current_page_number=344, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Le visage du vieil homme n'est plus qu'un masque hideux couvert
de pustules purulentes. Ses pupilles ont viré au jaune et ses
lèvres grises pendent en lambeaux. Il est atteint de la lèpre, une
maladie infectieuse qui pourrit la peau, attaque les nerfs et laisse
le corps atrocement mutilé et déformé. L'homme a été rejeté de
la communauté et exilé dans cette grotte où il finira ses jours
dans la solitude et la misère.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un peu d'herbe d'Oede et si vous souhaitez en donner un peu au pauvre lépreux, rendez-vous au :"))
    if has_item("HERBE D'OEDE"):
        st.page_link("tomes/tome5/page_321.py", label="321", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_321.py", label="321", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous n'en avez pas, ou si vous ne voulez pas en donner à ce malheureux malade, sortez de la grotte et rendez-vous au :"))
    st.page_link("tomes/tome5/page_270.py", label="270", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
