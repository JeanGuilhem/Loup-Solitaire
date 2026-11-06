import streamlit as st
from inventory import (
    buy_button,
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_magnakai,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

# Repas à la main (et non handle_repas) : le joueur doit pouvoir acheter du pain avant de manger.

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=307, book=6)

fr_text = """
Un peu plus loin, vous apercevez un chariot chargé de grosses
miches de pain frais qui s'arrête près d'une fontaine asséchée.
Aussitôt, une nuée de soldats affamés se précipite sur le chariot
comme des mouches sur un pot de confiture. Vous n'avez pas
déjeuné aujourd'hui et la délicieuse odeur de pain frais vous met
en appétit. Une miche coûte 2 Pièces d'Or et équivaut à un
Repas. Vous pouvez en acheter autant que vous le désirez. Si
vous ne prenez pas un Repas maintenant, vous perdez 3 points
d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write("**Miches de pain** (1 Repas chacune) :")
    cols = st.columns(4)
    for i, col in enumerate(cols):
        with col:
            buy_button("REPAS", 2, key=f"pain_{i}", label="Acheter une miche (2 Pièces d'Or)")

    meal = st.session_state.get("visibility_repas_307", False)
    if has_magnakai("Art de la Chasse"):
        st.success("*Grâce à votre Discipline Magnakaï de l'Art de la Chasse, vous trouvez votre nourriture par vous-même.*")
    elif not meal:
        col1, col2 = st.columns(2)
        if col1.button("Manger un Repas", disabled=not has_item("REPAS")):
            remove_from_inventory("REPAS")
            st.session_state.visibility_repas_307 = "mangé"
            st.rerun()
        if col2.button("Ne pas manger (-3 ENDURANCE)"):
            change_endurance(-3)
            st.session_state.visibility_repas_307 = "jeûne"
            st.rerun()
    elif meal == "mangé":
        st.success("Vous avez mangé. 1 Repas vous a été retiré.")
    else:
        st.error("Vous n'avez pas mangé : vous perdez 3 points d'ENDURANCE.")
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    if meal or has_magnakai("Art de la Chasse"):
        st.write_stream(stream_text('Rendez-vous au :'))
        st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
