import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=234, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Dans une hébétude totale, vous tombez en tournoyant sans
même savoir si c'est la tête la première ou les pieds en avant.
L'air chaud qui vous cingle le visage souffle si fort qu'il vous
maintient les yeux grands ouverts et vous desserre les mâchoires.
Vous respirez avec difficulté et vous continuez à tomber en
hurlant de terreur jusqu'à ce que vous heurtiez les branches
supérieures d'un Toab ; quelques secondes après, vous tombez à
l'eau. Vous refaites rapidement surface et vous commencez
instinctivement à faire des battements de jambes. Vous n'avez
aucune idée de la direction où vous allez, mais en quelques
brasses vous vous retrouvez près du bord d'un bassin d'eau
claire. Encore sous le choc, vous tremblez de tous vos membres
mais vous parvenez néanmoins à vous hisser sur le rebord
couvert de mousse. Par miracle, vous n'avez pas été blessé lors de
votre chute, mais votre épreuve est loin d'être terminée, car les
Drakkars et les Gardes du Palais vous ont vu tomber et ils sont
déjà en train de dévaler l'escalier de la tour. A présent, ils
traversent le pont en courant, vers les jardins du Palais. Un peu
plus loin, derrière une colonnade bordée d'arbres, un escalier
grimpe jusqu'à un petit portail donnant accès au Palais
supérieur. A votre droite, un étroit sentier s'enfonce dans l'épais
feuillage des arbres et des arbustes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez gravir les marches qui mènent au petit portail, rendez-vous au :"))
    st.page_link("tomes/tome5/page_352.py", label="352", icon="📄")

    st.write_stream(stream_text("Si vous préférez suivre le sentier sinueux, rendez-vous au :"))
    st.page_link("tomes/tome5/page_391.py", label="391", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome5/page_220.py", label="220", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_220.py", label="220", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
