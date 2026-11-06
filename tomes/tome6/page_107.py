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

check_inventory(current_page_number=107, book=6)

fr_text = """
La trappe est lourde et massive, mais vous sentez que les gonds
scellés par la rouille cèdent progressivement sous la pression.
Vous parvenez à soulever la dalle centimètre par centimètre, et
vous découvrez alors qu'elle s'ouvre sur une grande place pavée.
La cathédrale de Tekaro se dresse tout au bout, juste en face de
vous. Mais l'endroit pullule de gardes et vous vous empressez de
refermer la trappe, pour ne pas être repéré. Selon votre
estimation, la cathédrale se trouve environ à deux cents mètres
à l'est. Vous redescendez les marches et vous continuez à longer
le passage souterrain, espérant trouver une issue qui débouchera
dans la crypte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_120.py", label="120", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
