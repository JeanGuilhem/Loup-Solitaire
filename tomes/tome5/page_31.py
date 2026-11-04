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

check_inventory(current_page_number=31, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Alors que vous commencez à grimper, deux guerriers
Sharnazims surgissent soudain du tunnel infesté d'insectes. Les
deux hommes se jettent sur vous, les bras en avant et les mains
prêtes à vous saisir les chevilles pour vous tirer au bas de
l'échelle. Vous réussissez à les repousser et vous donnez un
violent coup de pied en plein visage à l'un des deux Sharnazims.
Celui-ci porte les mains à sa gorge endolorie et tombe à la
renverse dans l'eau boueuse en poussant un cri étranglé. Vous
parvenez à atteindre la trappe, mais entre-temps, le second
Sharnazim a tiré son cimeterre et il commence à monter à
l'échelle. Apparemment, il ne se soucie plus de vous capturer
vivant ! Vous soulevez avec l'épaule la lourde dalle couverte de
toiles d'araignées et vous réussissez à vous hisser dehors, vous
retrouvant soudain dans une rue bruyante où de nombreux
chalands déambulent devant les étalages d'un marché. La bouche
d'égout d'où vous sortez se trouve tout près d'une table en osier
où sont empilées de nombreuses torches.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous possédez une Pierre de Feu de Kalte, ou bien un Briquet, rendez-vous au :'))
    if has_item("SPHÈRE DE FEU") or has_item("BRIQUET À AMADOU"):
        st.page_link("tomes/tome5/page_143.py", label="143", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_143.py", label="143", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous n'avez ni l'un ni l'autre de ces objets, rendez-vous au :"))
    if has_item("SPHÈRE DE FEU") or has_item("BRIQUET À AMADOU"):
        st.page_link("tomes/tome5/page_183.py", label="183", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_183.py", label="183", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
