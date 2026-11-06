import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=101, book=6)

fr_text = """
Vous faites un nœud coulant au bout de la corde puis vous la
faites lentement descendre au fond du trou béant. Si vous
parvenez à glisser le nœud autour de la tête du marteau, il se
resserrera lorsque vous tirerez sur la corde et vous pourrez
alors remonter l'arme. Utilisez la Table de Hasard pour obtenir
un chiffre. Si vous maîtrisez la Discipline Magnakaï de l'Art de
la Chasse, ajoutez 3 au chiffre tiré.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll(key="corde")
    if roll is not None:
        bonus = 3 if has_magnakai("Art de la Chasse") else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Art de la Chasse : {roll} + 3 = **{total}**.*")
        # le livre dit « supérieur à 5 » : on prend 5 et plus (le 5 n'aurait sinon aucune issue)
        st.write_stream(stream_text("Si le résultat obtenu est compris entre 0 et 4, rendez-vous au :"))
        st.page_link("tomes/tome6/page_348.py", label="348", icon="📄", disabled=total > 4)
        st.write_stream(stream_text("Si ce résultat est supérieur à 4, rendez-vous au :"))
        st.page_link("tomes/tome6/page_207.py", label="207", icon="📄", disabled=total <= 4)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
