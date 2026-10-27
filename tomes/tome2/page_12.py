import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=12, book=2)

fr_text = """
Le capitaine Kelman ouvre la porte d'une vitrine et en retire le damier
d'un jeu de Samor. Les magnifiques figurines d'ivoire sculpté sont déjà
disposées sur les cases lorsque le capitaine dépose avec précaution le
damier sur la table. Vous acceptez, à contrecœur, de miser 10 Pièces
d'Or et le jeu commence.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour savoir qui va l'emporter. Si vous maîtrisez la Discipline Kaï du Sixième Sens, vous avez le droit d'ajouter 2 au chiffre obtenu. Si le total est de 0, 1, 2 ou 3, rendez-vous au 58. 4, 5 ou 6, rendez-vous au 167. 7, 8, 9, 10 ou 11, rendez-vous au 329."))
    number = hazard_roll()
    if number is not None:
        total = number + (2 if has_kai("Le Sixième Sens") else 0)
        if has_kai("Le Sixième Sens"):
            st.write(f"*Sixième Sens : +2, total {total}.*")
        if total <= 3:
            st.page_link("tomes/tome2/page_58.py", label="58", icon="📄")
        elif total <= 6:
            st.page_link("tomes/tome2/page_167.py", label="167", icon="📄")
        else:
            st.page_link("tomes/tome2/page_329.py", label="329", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
