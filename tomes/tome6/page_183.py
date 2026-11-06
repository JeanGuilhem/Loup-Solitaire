import streamlit as st
from inventory import (
    check_inventory,
    clear_flag,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

# fait testé : « arc emprunté » (Arc prêté pour le tournoi, à rendre ici)

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=183, book=6)

fr_text = """
Au moment où la flèche victorieuse d'Altan s'enfonce dans la
cible, une immense clameur s'élève de la foule. Les villageois,
ravis d'avoir assisté à un tel tournoi, se ruent sur le champ de tir
pour féliciter Altan. Noyé dans la foule nombreuse qui se presse
autour de lui, il disparaît bientôt de votre vue, et vous en profitez
pour quitter les lieux discrètement. Si vous aviez emprunté un
arc pour le tournoi, vous devez le rapporter à la tente avant
d'aller rejoindre Cyrilus.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # l'arc emprunté pour le tournoi (faits « arc emprunté », « arc Jakan », « arc de Kalte ») est rendu
    if is_new_page():
        for flag in ("arc emprunté", "arc Jakan", "arc de Kalte"):
            clear_flag(flag)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_33.py", label="33", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
