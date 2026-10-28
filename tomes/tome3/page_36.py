import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=36, book=3)

fr_text = """
Vous montez plus de cinquante marches avant d'atteindre
l'arcade. Tandis que vous reprenez votre souffle, vous remarquez
que des volutes de brume virevoltant et serpentant dans les airs
dissimulent l'ouverture et ce qui se trouve derrière. Vous vous
apercevez également que la température est beaucoup plus
fraîche aux environs de cette porte voûtée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            'Si vous maîtrisez la Discipline Kaï du Sixième Sens et si vous avez le titre Kaï de '
            'Gardien (ce qui signifie que vous maîtrisez 7 Disciplines Kaï), rendez-vous au :'
        )
    )
    if has_kai("Le Sixième Sens") and kai_rank() >= 7:
        st.page_link("tomes/tome3/page_341.py", label="341", icon="📄")
    else:
        st.write_stream(stream_text("Il vous faut le Sixième Sens et le rang de Gardien (7 Disciplines Kaï)."))
        st.page_link("tomes/tome3/page_341.py", label="341", icon="📄", disabled=True)

    st.write_stream(
        stream_text(
            'Si vous maîtrisez la Discipline Kaï du Sixième Sens sans avoir le rang de Gardien, '
            'rendez-vous au :'
        )
    )
    if has_kai("Le Sixième Sens") and kai_rank() < 7:
        st.page_link("tomes/tome3/page_124.py", label="124", icon="📄")
    else:
        st.write_stream(stream_text("Ce choix est réservé au Sixième Sens sans le rang de Gardien."))
        st.page_link("tomes/tome3/page_124.py", label="124", icon="📄", disabled=True)

    st.write_stream(
        stream_text(
            'Enfin, si vous ne maîtrisez pas la Discipline Kaï du Sixième Sens, préparez-vous à '
            "passer à l'attaque et franchissez l'arcade en vous rendant au :"
        )
    )
    st.page_link("tomes/tome3/page_264.py", label="264", icon="📄", disabled=has_kai("Le Sixième Sens"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
