import streamlit as st
from inventory import (
    POISONED,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    set_flag,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=63, book=5)

fr_text = """
Vous découpez de longues lanières dans votre manteau Kaï et
vous vous efforcez de panser au mieux votre plaie. Vous
réussissez à arrêter l'hémorragie, mais vous avez perdu une
grande quantité de sang et vous craignez, de plus, que la blessure
s'infecte. Désormais, vous perdrez 2 points d'ENDURANCE par
paragraphe jusqu'à ce que vous trouviez et buviez une dose de
Potion de Laumspur. Si votre total d'ENDURANCE tombe à zéro
avant que vous n'ayez pu vous procurer cette potion, vous
mourrez d'un empoisonnement du sang.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        set_flag(POISONED)
    st.warning("Blessure infectée : vous perdrez 2 points d'ENDURANCE par paragraphe jusqu'à ce que vous buviez une Potion de Laumspur.")
    st.write_stream(stream_text("A présent, si vous désirez fouiller le cadavre des Gardes que vous avez tués, rendez-vous au :"))
    st.page_link("tomes/tome5/page_102.py", label="102", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous enfuir par le couloir, sans vous soucier de vos victimes, rendez-vous au :"))
    st.page_link("tomes/tome5/page_150.py", label="150", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
