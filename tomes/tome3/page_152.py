import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=152, book=3)

fr_text = """
Vous décidez d'essayer de distraire son attention en jetant
quelques Pièces d'Or dans un renfoncement du mur situé en face
de lui.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Tout d'abord, déterminez le nombre de Pièces d'Or que vous allez lancer. Utilisez ensuite la Table "
            "de Hasard pour obtenir un autre chiffre (exceptionnellement, vous considérez que 0 = 10)."
        )
    )
    thrown = st.session_state.get("visibility_coins_152", False)
    if thrown is False:
        if st.session_state.purse == 0:
            st.warning("Vous n'avez aucune Pièce d'Or à lancer : le garde ne bouge pas.")
            st.page_link("tomes/tome3/page_181.py", label="181", icon="📄")
        else:
            coins = st.number_input(
                "Nombre de Pièces d'Or à lancer",
                min_value=1,
                max_value=st.session_state.purse,
                value=1,
                step=1,
                key="coins_152",
            )
            if st.button("Lancer les Pièces d'Or", key="throw_152"):
                if spend_gold(int(coins)):
                    st.session_state["visibility_coins_152"] = int(coins)
                    st.rerun()
    else:
        st.write(f"*Vous avez lancé {thrown} Pièce(s) d'Or.*")
        roll = hazard_roll(key="coins")
        if roll is not None:
            value = roll if roll != 0 else 10
            st.write(f"*Chiffre retenu : {value}.*")
            if value <= thrown:
                st.write_stream(
                    stream_text(
                        "Le chiffre est égal ou inférieur au nombre de Pièces que vous avez jetées, rendez-vous au :"
                    )
                )
                st.page_link("tomes/tome3/page_319.py", label="319", icon="📄")
            else:
                st.write_stream(stream_text("Le chiffre est supérieur au nombre de Pièces, rendez-vous au :"))
                st.page_link("tomes/tome3/page_181.py", label="181", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
