import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
    use_arrow,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=56, book=6)

fr_text = """
Vous chargez votre arc, visez et tirez une fraction de seconde
avant que la décharge d'énergie vous frappe en pleine poitrine.
Vous atteignez le chef de la secte en plein cœur, et l'homme
s'écroule raide mort. Cependant, vous êtes vous-même
sérieusement ébranlé par le choc : vous vacillez et vous tombez à
terre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        use_arrow()

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Le chiffre tiré correspond au nombre de points d'ENDURANCE que la décharge d'énergie vient de vous faire perdre."))
    roll = hazard_roll()
    if roll is not None:
        # perte appliquée une seule fois par visite
        if not st.session_state.get("visibility_t6_56_decharge"):
            st.session_state["visibility_t6_56_decharge"] = True
            change_endurance(-roll)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-roll)
        st.write_stream(stream_text("Si vous êtes encore en vie, vous parvenez à vous remettre sur pied et à courir sous le couvert du sous-bois pour y rejoindre votre cheval. Mais entretemps, l'un des disciples a récupéré la baguette d'or et il se prépare à l'utiliser de nouveau contre vous ! Rendez-vous au :"))
        st.page_link("tomes/tome6/page_182.py", label="182", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
