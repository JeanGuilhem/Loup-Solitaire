import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=22, book=6)

fr_text = """
Les fers de lance ne sont plus qu'à quelques centimètres de votre
poitrine, lorsque vous parvenez enfin à dégainer votre arme et à
les faire dévier d'un formidable coup qui brise net toutes les
hampes. Les gardes reculent vivement, les yeux agrandis par la
stupeur et la mâchoire tombante. Vous profitez de leur
ébahissement pour lancer votre cheval au galop et gagner l'ombre
protectrice de la rue qui s'ouvre devant vous. Tandis que les cris
d'alerte du corps de garde s'évanouissent derrière vous, vous
arrivez à un endroit où la rue bifurque. L'ombre du soir commence
à étendre son noir manteau sur la ville-frontière, et vous êtes
impatient de trouver, pour vous-même et pour votre monture, un
lieu sûr pour y passer la nuit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez continuer par la gauche, rendez-vous au :"))
    st.page_link("tomes/tome6/page_151.py", label="151", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller sur la droite, rendez-vous au :"))
    st.page_link("tomes/tome6/page_289.py", label="289", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Intuition, rendez-vous au :"))
    if has_magnakai("Intuition"):
        st.page_link("tomes/tome6/page_41.py", label="41", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_41.py", label="41", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
