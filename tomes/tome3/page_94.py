import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=94, book=3)

fr_text = """
Vous avez glissé et vous êtes tombé dans l'eau glacée, vous hurlez
de douleur tandis que le froid vous saisit jusqu'à la moelle des os.
Vous luttez de toutes vos forces pour essayer de regagner la rive,
mais c'est une entreprise désespérée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll()
    if roll is not None and roll <= 6:
        st.write_stream(
            stream_text(
                "Vous avez de la chance : vous parvenez en effet à vous hisser hors de l'eau glacée et vous "
                "vous écroulez épuisé sur la rive. Vous perdez 3 points d'ENDURANCE."
            )
        )
        if not st.session_state.get("visibility_cold_water"):
            st.session_state["visibility_cold_water"] = True
            change_endurance(-3)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)
        st.write_stream(stream_text("Rendez-vous au :"))
        st.page_link("tomes/tome3/page_176.py", label="176", icon="📄")
    elif roll is not None:
        st.write_stream(
            stream_text(
                "L'eau glacée a tôt fait de vous paralyser les bras et quelques minutes plus tard vous vous "
                "êtes noyé. Votre mission s'achève donc ici."
            )
        )
        show_illustrations()
        ls_death()

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
