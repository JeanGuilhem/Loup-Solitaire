import streamlit as st
from inventory import (
    bow_bonus,
    check_inventory,
    display_inventory,
    end_page,
    has_flag,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

# Compétition : les flèches du tournoi ne sont pas rayées (hazard_roll + bow_bonus, pas bow_shot).

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=340, book=6)

fr_text = """
Un petit homme à la figure bouffie, vêtu d'un pourpoint à galons
d'argent, fait irruption dans la tente et demande l'attention de
tous. Rapidement, il explique les règles qui régissent le tournoi
puis il vous conduit vers le champ clos. A l'autre bout du terrain
ont été dressées une dizaine de cibles comportant chacune dix
cercles de couleurs différentes numérotés de 0 à 9. Chaque
archer dispose de trois flèches et doit obtenir un total minimal de
8 points pour la qualification pour le tour suivant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir trois chiffres et faites-en le total. Si vous maîtrisez la Discipline Magnakaï de la Science des Armes pour l'Arc, ajoutez 3 à ce total."))
    first = hazard_roll(key="tournoi_1", label="Première flèche (Table de Hasard)")
    second = hazard_roll(key="tournoi_2", label="Deuxième flèche (Table de Hasard)") if first is not None else None
    third = hazard_roll(key="tournoi_3", label="Troisième flèche (Table de Hasard)") if second is not None else None
    # Fait testé : « arc Jakan » (paragraphe 298) : -2 HABILETÉ pour le tournoi, se brise sur un 0
    if has_flag("arc Jakan") and 0 in (first, second, third):
        st.write("*Vous avez tiré un 0 : votre arc fêlé se brise !*")
        st.page_link("tomes/tome6/page_335.py", label="335", icon="📄")
    elif third is not None:
        bonus = bow_bonus()
        total = first + second + third + bonus
        detail = f" + {bonus} (Science des Armes)" if bonus else ""
        st.write(f"*Total : {first} + {second} + {third}{detail} = **{total}**.*")
        if total <= 7:
            st.write_stream(stream_text('Si votre dernier total est égal ou inférieur à 7, rendez-vous au :'))
            st.page_link("tomes/tome6/page_103.py", label="103", icon="📄")
        else:
            st.write_stream(stream_text('Si votre dernier total est supérieur ou égal à 8, rendez-vous au :'))
            st.page_link("tomes/tome6/page_26.py", label="26", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
