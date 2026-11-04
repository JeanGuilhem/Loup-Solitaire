import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=64, book=5)

fr_text = """
Vous avez à peine fait quelques pas le long du trottoir lorsque
vous entendez un grognement rauque et inhumain. Puis le son se
transforme soudain en un épouvantable crissement suraigu
tandis qu'apparaît l'énorme masse d'un Kwaraz. Celui-ci fond sur
vous avant même que vous ne puissiez prendre la fuite.
Ce reptile géant est très sensible au pouvoir psychique. Si vous
maîtrisez la Discipline Kaï de la Puissance Psychique, ajoutez 4
points (au lieu des 2 points habituels) à votre total d'HABILETÉ
pour toute la durée de l'affrontement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # Puissance psychique : +4 au lieu de +2 (le moteur compte déjà les 2 points habituels)
    outcome = combat([("KWARAZ", 20, 30)], hability_modifier=2 if has_kai("Puissance psychique") else 0)
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur du combat, rendez-vous au :"))
        st.page_link("tomes/tome5/page_177.py", label="177", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
