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

check_inventory(current_page_number=94, book=5)

fr_text = """
Vous tombez la tête la première dans le cloaque. L'eau viciée
vous entre par le nez et les oreilles et vous suffoquez à moitié.
Vous remontez à la surface et vous vous hissez péniblement sur
l'étroit trottoir qui longe l'égout. C'est alors que vous constatez
que l'un de vos bras ne réagit plus. La blessure que la trappe vous
avait faite à l'épaule en se rabattant est encore douloureuse mais,
en outre, tout votre bras est maintenant ankylosé et paralysé.
L'angoisse vous oppresse lorsque vous réalisez soudain de quoi il
s'agit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_81.py", label="81", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
