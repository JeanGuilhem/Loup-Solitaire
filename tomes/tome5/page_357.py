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

check_inventory(current_page_number=357, book=5)

fr_text = """
La passerelle oscille dangereusement sous votre poids et vous
devez ralentir, de peur de passer par-dessus la rambarde. Alertée
par le bruit des planches qui craquent, la sentinelle fait volte-face
et se précipite vers vous en brandissant un javelot pour contrer
votre attaque. Vous ne pouvez pas éviter le combat et vous devrez
vous battre jusqu'à ce que mort s'ensuive. Diminuez de 2 points
votre total d'HABILETÉ pour toute la durée de ce combat, car il
vous est difficile de garder l'équilibre sur ces planches instables.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # un 1 tiré sur la Table de Hasard au cours d'un assaut : chute (le journal du combat garde les chiffres)
    fight = st.session_state.get("combat_sentinelle")
    fallen = fight is not None and fight.get("outcome") != "dead" and any(entry["dice"] == 1 for entry in fight["log"])
    st.write_stream(stream_text("Si, à un moment quelconque du combat, vous tirez un 1 dans la Table de Hasard, vous perdez l'équilibre et vous tombez."))
    if fallen:
        st.error("*Vous avez tiré un 1 : vous perdez l'équilibre et vous tombez !*")
        st.write_stream(stream_text("Rendez-vous alors au :"))
        st.page_link("tomes/tome5/page_293.py", label="293", icon="📄")
    else:
        outcome = combat([("SENTINELLE DE LA PLATE-FORME", 15, 23)], key="sentinelle", hability_modifier=-2)
        if outcome == "win":
            st.write_stream(stream_text("Si vous sortez vainqueur et que vous désiriez fouiller le corps de la sentinelle, rendez-vous au :"))
            st.page_link("tomes/tome5/page_207.py", label="207", icon="📄")
            st.write_stream(stream_text("Si vous êtes vainqueur, mais si vous préférez laisser le corps pour vous hâter vers l'enclos de l'Itikar, rendez-vous dans ce cas au :"))
            st.page_link("tomes/tome5/page_224.py", label="224", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
