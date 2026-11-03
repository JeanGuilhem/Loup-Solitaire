import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=35, book=4)

fr_text = """
Mettant en pratique votre Discipline Kaï, vous vous dissimulez
dans les ombres qui se projettent contre les murs et vous avancez
prudemment en direction du pont. Soudain, le Garde pose son
morceau de bois et vous tourne le dos. Il est en train de fouiller
dans son sac à dos pour y chercher quelque nourriture. C'est là
l'occasion ou jamais de vous précipiter vers le pont en
brandissant votre arme dont vous frapperez le Garde par
surprise.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï de la Chasse ou si vous avez atteint le rang Kaï de Gardien (ou un rang supérieur), vous ajouterez 3 au chiffre que vous aurez tiré."))
    roll = hazard_roll()
    if roll is not None:
        bonus = 3 if has_kai("La Chasse") or kai_rank() >= 7 else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Bonus : +3, soit un total de {total}.*")
        if total <= 7:
            st.write_stream(stream_text("Si vous obtenez un total de 0 à 7, rendez-vous au :"))
            st.page_link("tomes/tome4/page_147.py", label="147", icon="📄")

        else:
            st.write_stream(stream_text("De 8 à 12, rendez-vous au :"))
            st.page_link("tomes/tome4/page_231.py", label="231", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
