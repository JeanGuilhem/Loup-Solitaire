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

fr_unknown_item = "Vous ne possédez pas cet objet."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=67, book=3)

fr_text = """
L'homme rejette soudain la tête en arrière comme si on venait de
l'éveiller brusquement d'une transe. « Qui est là ? murmure-t-il
en scrutant l'obscurité de ses yeux profondément enfoncés dans
leurs orbites. Y a-t-il quelqu'un ici ou est-ce la folie qui me visite ? »
Vous tendez alors la main à travers l'ouverture et vous lui faites
un signe pour montrer où vous êtes. « Loués soient les dieux !
s'écrie l'homme en se levant d'un bond. Je m'appelle Tygon et je
suis un marchand de Radagorn. Les Barbares des Glaces m'ont
capturé, ils ont volé ma marchandise et m'ont amené ici.
J'attends maintenant d'être reçu par leur nouveau Brumalmarc,
le mage Vonotar du Sommerlund. C'est lui, semble-t-il, qui doit
décider de mon sort. Si vous me libérez, je ferai tout ce qui sera
en mon pouvoir pour vous aider. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous disposez d'une Corde, vous pouvez la descendre à travers l'ouverture et aider l'homme à sortir de sa cellule ; rendez-vous pour cela au :"))
    if has_item("CORDE"):
        st.page_link("tomes/tome3/page_328.py", label="328", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_328.py", label="328", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous n'avez pas de Corde, ou si vous ne souhaitez pas aider cet homme, vous reprendrez votre chemin le long du tunnel en direction de l'escalier. Rendez-vous alors au :"))
    st.page_link("tomes/tome3/page_166.py", label="166", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
