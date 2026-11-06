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

check_inventory(current_page_number=89, book=6)

fr_text = """
« Esmond, montre-toi, vieux brigand ! C'est moi, Cyrilus, ton
frère ! Je suis avec quelqu'un que j'aimerais bien te présenter.
Ouvre vite ! » crie le magicien en frappant à la porte avec son
bâton de chêne. Mais personne ne répond. Le vieil homme sourit
et lève ses maigres épaules en reprenant : « Allons,
réveille-toi, vieux frère, je sais que tu es là ! » Toujours
rien.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Intuition, rendez-vous au :"))
    if has_magnakai("Intuition"):
        st.page_link("tomes/tome6/page_7.py", label="7", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_7.py", label="7", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline, rendez-vous au :"))
    if has_magnakai("Intuition"):
        st.page_link("tomes/tome6/page_258.py", label="258", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome6/page_258.py", label="258", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
