import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, handle_repas, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=137, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous n'avez pas mangé depuis longtemps et vous devez prendre
un Repas tout de suite ou perdre 3 points d'ENDURANCE.
"""

fr_text_2 = """
Vous vous faufilez sans être vu à travers les plantes exotiques qui
poussent partout en abondance, puis vous suivez une allée de
gravier qui passe à travers une étrange pelouse où pousse une
herbe violette. Au bout de cette allée, se trouve une magnifique
fontaine. Un jet d'eau d'un bleu clair accroche la lumière du soleil
qui s'y réfracte et crée un arc-en-ciel aux couleurs éclatantes.
Vous regardez, par-delà la fontaine, les tours du Palais s'élancer
dans le ciel et vous notez de manière précise les positions des
portes et fenêtres. Côté jardin, il y a deux entrées vers le Grand
Palais. Vous avez la possibilité d'entrer soit par la porte des
cuisines, soit par le Vizu-Diar : la galerie des Trophées du
Zakhan. Mais cependant, une seule de ces entrées vous mènera à
l'Herboristerie Impériale où se trouve la précieuse herbe d'Oede.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write(fr_text_2)

    st.write_stream(stream_text("Si vous voulez entrer dans le Palais par les cuisines, rendez-vous au :"))
    st.page_link("tomes/tome5/page_66.py", label="66", icon="📄")

    st.write_stream(stream_text("Si vous préférez passer par le Vizu-Diar, rendez-vous au :"))
    st.page_link("tomes/tome5/page_149.py", label="149", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de l'Orientation ou celle du Sixième Sens, rendez-vous au :"))
    if has_kai("L'Orientation") or has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_37.py", label="37", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_37.py", label="37", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
