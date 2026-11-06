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

check_inventory(current_page_number=287, book=6)

fr_text = """
Vous attachez votre cheval à un poteau près de la cabane et
avancez vers la porte. De son côté, Cyrilus annonce son arrivée en
tambourinant à la porte de Denka et demande à son frère de lui
ouvrir. N'obtenant aucune réponse, il frappe de plus belle, de
plus en plus impatient. Vous souriez : si son frère lui ressemble,
il doit avoir le sommeil facile ! Finalement, vous poussez la
porte et vous entrez dans la cabane. Une délicieuse odeur de pain
frais vous met l'eau à la bouche. Vous apercevez une rangée de
grands paniers pleins de miches dorées, et regardez avec envie les
nombreux plateaux de tartes, de flans et de biscuits disposés sur
le comptoir. Il n'y a personne, mais au fond de la pièce une porte
s'ouvre sur une autre pièce.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez demander s'il y a quelqu'un, rendez-vous au :"))
    st.page_link("tomes/tome6/page_43.py", label="43", icon="📄")

    st.write_stream(stream_text("Si vous voulez vous servir vous-même de pain et de gâteaux, rendez-vous au :"))
    st.page_link("tomes/tome6/page_157.py", label="157", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
