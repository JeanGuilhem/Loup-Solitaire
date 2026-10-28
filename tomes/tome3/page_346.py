import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=346, book=3)

fr_text = """
Dyce saute de l'autre côté sans difficulté. Irian, lui, glisse et
tombe, mais vous parvenez à le remonter à la surface grâce à la
corde attachée à sa ceinture. Fenor et vous-même êtes toujours
de ce côté de la crevasse et c'est à votre tour de sauter.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï de la Chasse, vous pouvez ajouter 2 au chiffre que vous aurez tiré."))
    roll = hazard_roll()
    if roll is not None:
        total = roll + (2 if has_kai("La Chasse") else 0)
        if has_kai("La Chasse"):
            st.write(f"*Chasse : +2, soit un total de {total}.*")
        if total <= 3:
            st.write_stream(stream_text("Si le total obtenu est de 0 à 3, rendez-vous au :"))
            st.page_link("tomes/tome3/page_195.py", label="195", icon="📄")
        else:
            st.write_stream(stream_text("De 4 à 11, rendez-vous au :"))
            st.page_link("tomes/tome3/page_232.py", label="232", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
