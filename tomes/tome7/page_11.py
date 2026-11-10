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

check_inventory(current_page_number=11, book=7)

fr_text = """
Après avoir descendu l'escalier, vous arrivez à un couloir étroit
ressemblant à un tunnel, pris entre deux parois dont la
maçonnerie est à moitié désagrégée. Une eau noire et
nauséabonde s'écoule le long d'un canal creusé au centre, en
direction d'un passage voûté que vous distinguez au loin. En vous
approchant, vous découvrez que la voie en question est barrée
par une grosse herse en fer noir. Une plaque de métal est rivetée
sur les barreaux et un curieux dessin y est gravé :
Par ailleurs, vous découvrez sur votre gauche un cadran rouillé
muni d'une aiguille en cuivre. Des chiffres, de 1 à 40, sont
disposés tout autour. Il y a un levier sous le cadran. Votre
instinct infaillible de Maître Kaï vous fait penser qu'en
choisissant le - ou les - bon numéro, et en abaissant ensuite le
levier, la herse se soulèvera.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Intuition, rendez-vous au :"))
    if has_magnakai("Intuition"):
        st.page_link("tomes/tome7/page_167.py", label="167", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_167.py", label="167", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Exploration, rendez-vous au :"))
    if has_magnakai("Exploration"):
        st.page_link("tomes/tome7/page_306.py", label="306", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_306.py", label="306", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous ne maîtrisez aucune de ces deux disciplines, rendez-vous au :'))
    st.page_link("tomes/tome7/page_329.py", label="329", icon="📄", disabled=has_magnakai("Intuition") or has_magnakai("Exploration"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
