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

check_inventory(current_page_number=168, book=5)

fr_text = """
Tel un tigre, vous sautez au milieu des Gardes pris au dépourvu.
Une des sentinelles s'apprête à lever sa sarbacane, mais un coup
de poing bien ajusté au visage l'en empêche. Il tombe en arrière
et sa tête va heurter le mur avec un bruit sourd et effrayant. Le
deuxième Garde veut vous planter son trident dans la poitrine,
mais vous esquivez son coup d'un saut de côté et, de votre main
libre, vous saisissez son arme que vous tirez violemment. Le
Garde perd l'équilibre et tombe la tête la première. Vous vous
retournez juste à temps pour affronter le troisième Garde qui
s'apprête à vous lancer son trident.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GARDE DU VESTIBULE", 15, 23)], max_rounds=3)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez ce combat en 3 Assauts ou moins, rendez-vous au :"))
        st.page_link("tomes/tome5/page_101.py", label="101", icon="📄")
    elif outcome == "rounds_over":
        st.write_stream(stream_text("Si le combat dure plus de 3 Assauts, rendez-vous au :"))
        st.page_link("tomes/tome5/page_46.py", label="46", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
