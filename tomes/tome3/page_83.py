import streamlit as st
from combat import combat
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

check_inventory(current_page_number=83, book=3)

fr_text = """
Les Barbares des Glaces mutants semblent contrôlés par une
hideuse créature qui se cache dans l'ombre d'une porte, un peu
plus loin. Ce monstre est doté d'une grosse tête humaine qui
repose sur deux pieds. Il n'a ni torse ni membres, mais il est doté
en revanche d'une longue queue de reptile qui lui permet de
conserver son équilibre. Les Barbares des Glaces mutants vous
attaquent simultanément et vous devrez les combattre comme
s'il s'agissait d'une seule et même créature. Ils sont insensibles à
la Puissance Psychique, mais l'être étrange auquel ils obéissent
est doué, quant à lui, d'une redoutable Force Mentale qui vous
fait perdre 2 points d'ENDURANCE, à moins que vous ne
maîtrisiez la Discipline Kaï du Bouclier Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("BARBARES DES GLACES MUTANTS", 18, 24)], psychic_immune=True, psychic_damage=2)
    if outcome == "win":

        st.write_stream(stream_text('Si vous sortez vainqueur de ce combat, rendez-vous au :'))
        st.page_link("tomes/tome3/page_313.py", label="313", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
