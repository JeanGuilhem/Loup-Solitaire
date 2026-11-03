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

check_inventory(current_page_number=25, book=4)

fr_text = """
Après avoir traversé les riches champs de blé situés au sud du
Sommerlund, le spectacle qui s'offre à présent à vos yeux vous
paraît singulièrement morne et sinistre. Un paysage plat et
désolé, parsemé çà et là de fougères rabougries et de tertres
rocheux, s'étend devant vous. Au cours de l'après-midi, des
nuages d'orage s'amoncellent au sommet des monts Durncrag, à
l'ouest, et un lointain grondement de tonnerre annonce l'arrivée
imminente de la pluie. En début de soirée, vos éclaireurs vous
annoncent qu'ils ont découvert les ruines d'un ancien temple à
moins d'un kilomètre et demi de la grand-route.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez établir votre campement à l'abri de ces ruines, rendez-vous au :"))
    st.page_link("tomes/tome4/page_290.py", label="290", icon="📄")

    st.write_stream(stream_text("Si vous préférez éviter ce temple et poursuivre votre chemin, rendez-vous au :"))
    st.page_link("tomes/tome4/page_141.py", label="141", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
