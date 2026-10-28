import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=245, book=3)

fr_text = """
La bête, avant de mourir, pousse un dernier cri d'agonie et une
odeur pestilentielle vous frappe aussitôt les narines. Même les
chiens Kanu froncent le museau en signe de dégoût et se
détournent pour essayer d'échapper à l'effroyable puanteur. Irian
s'approche alors du cadavre avec un couteau à la main et
entreprend de dépecer la créature. Vous faites une grimace en le
voyant découper la peau de l'animal, de la gorge au ventre pour
l'arracher ensuite de sa chair. Mais vous n'êtes pas au bout de
votre écœurement : Irian, en effet, plonge les mains dans la
carcasse béante et en retire une graisse épaisse dont il s'enduit le
visage et le corps.
« C'est de l'huile de Bakanal, s'écrie-t-il avec enthousiasme, elle
protège du froid et de l'humidité ; c'est encore mieux que la
fourrure pour se préserver des glaces de Kalte. » En même
temps, il tend vers vous une main pleine de graisse immonde
dont il vous invite à vous enduire la peau à votre tour.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous acceptez de l'imiter en vous appliquant de l'huile de Bakanal sur le corps, rendez-vous "
            "au :"
        )
    )
    st.page_link("tomes/tome3/page_91.py", label="91", icon="📄")
    st.write_stream(
        stream_text(
            "Si, en revanche, l'idée de sentir à peu près aussi bon qu'une cuve remplie de roquefort rance ne "
            "vous séduit guère, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome3/page_172.py", label="172", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
