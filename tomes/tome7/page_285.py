import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=285, book=7)

fr_text = """
Les chauves-souris sont affamées, et l'odeur inattendue de leur
nourriture favorite, du sang humain bien chaud, les a
complètement affolées. Il est trop tard pour éviter le combat, et
vous devez vous battre si vous ne voulez pas devenir leur proie. Si
vous ne maîtrisez pas la Discipline Magnakaï de la Science
Médicale, doublez tous les points d'ENDURANCE que vous
perdez au cours du combat, à cause de leur salive empoisonnée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # la salive empoisonnée des Vampires double vos blessures, sauf avec la Science Médicale
    outcome = combat([("VAMPIRES", 19, 32)], ls_loss_multiplier=1 if has_magnakai("Science Médicale") else 2)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_161.py", label="161", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
