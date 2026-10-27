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

check_inventory(current_page_number=243, book=2)

fr_text = """
Voyant que leur maître est mort, les Gloks désemparés battent en
retraite vers la poupe du navire. Le capitaine Kelman rassemble alors
ses hommes et se lance à l'attaque, repoussant les immondes créatures
qui, dans un concert de grognements rageurs, sont contraintes de sauter
par-dessus bord pour éviter d'être taillées en pièces. Constatant qu'il ont
perdu la bataille, les Kraans s'envolent des mâts et s'enfuient en
direction de la côte qu'on aperçoit à l'horizon. « Merci, Seigneur Kaï,
dit le capitaine en vous serrant la main, nous sommes fiers et
reconnaissants de vous avoir avec nous. » Une longue ovation retentit
sur le pont du navire : ce sont les marins qui vous rendent hommage en
même temps que leur capitaine. Vous aidez ensuite à soigner les
blessés tandis qu'on répare la mâture endommagée ; et deux heures plus
tard, le navire est prêt à repartir, les voiles gonflées de vent : vous voici
à nouveau en route pour Durenor.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_240.py", label="240", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
