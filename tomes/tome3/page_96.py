import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_flag,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=96, book=3)

fr_text = """
Vous vous enveloppez dans votre cape blanche et vous vous
cachez derrière une stalagmite, à quelques mètres de la rive du
lac. Retenant votre souffle, le corps parfaitement immobile, vous
entendez les pas et les grognements du Languabarb s'approcher
de plus en plus près.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Pour savoir si la mise en pratique de votre Discipline Kaï vous a permis de passer inaperçu, "
            "utilisez la Table de Hasard. Si vous vous êtes enduit le torse d'huile de Bakanal, vous ajouterez 2 "
            "au chiffre obtenu."
        )
    )
    roll = hazard_roll()
    if roll is not None:
        bonus = 2 if has_flag("huile de Bakanal") else 0
        total = roll + bonus
        if bonus:
            st.write(f"*L'huile de Bakanal vous donne +{bonus} : total {total}.*")
        if total <= 8:
            st.write_stream(stream_text("Le total se situe entre 0 et 8, rendez-vous au :"))
            st.page_link("tomes/tome3/page_59.py", label="59", icon="📄")
        else:
            st.write_stream(stream_text("Le total se situe entre 9 et 11, rendez-vous au :"))
            st.page_link("tomes/tome3/page_214.py", label="214", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
