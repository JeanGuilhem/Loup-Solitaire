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

check_inventory(current_page_number=360, book=5)

fr_text = """
Deux Gardes en uniforme noir surgissent en bas des marches.
Cette brusque rencontre les prend au dépourvu, mais vous-même
êtes lent à réagir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï de la Chasse, ajoutez 1 point au chiffre obtenu."))
    roll = hazard_roll(key="premier")
    if roll is not None:
        bonus = 1 if has_kai("La Chasse") else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Bonus de la Chasse : +1, soit un résultat de {total}.*")
        st.write_stream(stream_text("Maintenant, utilisez à nouveau la Table de Hasard pour obtenir un autre chiffre."))
        second = hazard_roll(key="second", label="Utilisez à nouveau la Table de Hasard.")
        if second is not None and second < total:
            st.write_stream(stream_text("Si ce second chiffre est inférieur au résultat que vous avez obtenu, rendez-vous au :"))
            st.page_link("tomes/tome5/page_226.py", label="226", icon="📄")
        elif second is not None and second > total:
            st.write_stream(stream_text("S'il est supérieur à votre résultat, rendez-vous au :"))
            st.page_link("tomes/tome5/page_297.py", label="297", icon="📄")
        elif second is not None:
            st.write_stream(stream_text("Si les chiffres sont égaux, rendez-vous au :"))
            st.page_link("tomes/tome5/page_334.py", label="334", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
