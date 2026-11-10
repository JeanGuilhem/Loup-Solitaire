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

check_inventory(current_page_number=95, book=7)

fr_text = """
Le guerrier a parcouru la moitié du pont quand, soudain, un cri
de bête affamée retentit derrière lui. Il fait aussitôt volte-face et
se met en position de combat. Peu après, un grommellement
sourd provenant de l'arche vous glace le sang. Trois créatures
surgissent sournoisement de l'ombre ; leur peau luisante est d'un
bleu sombre comme la nuit, et elles vous fixent d'un air féroce en
sifflant de façon menaçante entre leurs dents. Dès qu'il les
aperçoit, le guerrier a un mouvement de recul, et vous voyez
l'épée trembler au bout de son bras. Quand les créatures se
mettent à avancer, ses nerfs craquent ; il tourne les talons et se
précipite vers vous en hurlant : « Sauvez-vous, étranger ! Nous
allons être dévorés vivants ! »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez suivre son conseil et fuir les créatures en vous échappant par le tunnel opposé, rendez-vous au :"))
    st.page_link("tomes/tome7/page_87.py", label="87", icon="📄")

    st.write_stream(stream_text("Si vous décidez d'attaquer le guerrier dès qu'il sera à votre portée, rendez-vous au :"))
    st.page_link("tomes/tome7/page_345.py", label="345", icon="📄")

    st.write_stream(stream_text("Si vous préférez le laisser passer et vous préparer à affronter, seul, les trois créatures qui se rapprochent, rendez-vous au :"))
    st.page_link("tomes/tome7/page_249.py", label="249", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
