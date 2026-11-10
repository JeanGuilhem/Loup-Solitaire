import streamlit as st
from combat import combat
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

check_inventory(current_page_number=8, book=7)

fr_text = """
Vous attaquez la bête féroce dès qu'elle surgit de l'obscurité.
Votre lame s'enfonce dans son épaisse fourrure et vous lui
infligez une profonde blessure à l'épaule, mais le choc de la
rencontre vous fait rouler à terre. Le Loup en profite aussitôt
pour vous attraper le bras, et vous hurlez de douleur sous la
morsure de ses puissants crocs. Mû par un réflexe désespéré,
vous frappez à nouveau au moment où il plonge pour vous saisir
le mollet. Cette créature est insensible à la Puissance Psychique,
mais non au Foudroiement Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("LOUP DE LA MORT", 22, 40)], psychic_power_immune=True)
    if outcome == "win":
        st.write_stream(stream_text('Si vous sortez vainqueur de ce combat, rendez-vous au :'))
        st.page_link("tomes/tome7/page_194.py", label="194", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
