import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
fr_unknown_item = "Vous ne possédez pas cet objet."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=258, book=4)

fr_text = """
Vous vous éloignez de la cabane et vous poursuivez votre chemin
parmi les arbres. Au matin, vous avez atteint la lisière de la forêt.
Contemplant alors les champs de blé qui s'étendent au-delà, vous
apercevez un petit village niché au creux d'une vallée peu
profonde. Quelques sentiers étroits apparaissent parmi les blés et
vous distinguez des essaims d'insectes qui volettent çà et là. Vous
avancez le long d'un des sentiers lorsque des brigands
apparaissent soudain un peu plus loin. La lance jetées sur
l'épaule, ils marchent dans votre direction d'un pas insouciant,
comme s'ils se promenaient.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un Médaillon d'Onyx, rendez-vous au :"))
    if has_item("MÉDAILLON D'ONYX"):
        st.page_link("tomes/tome4/page_305.py", label="305", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_305.py", label="305", icon="📄", disabled=True)
    st.write_stream(stream_text('Si vous souhaitez vous cacher parmi les blés, rendez-vous au :'))
    st.page_link("tomes/tome4/page_159.py", label="159", icon="📄")
    st.write_stream(stream_text('Enfin, si vous maîtrisez la Discipline Kaï du Camouflage et que vous ayez atteint le rang Kaï de Gardien (ou un rang supérieur), rendez-vous au :'))
    if has_kai("Le Camouflage") and kai_rank() >= 7:
        st.page_link("tomes/tome4/page_49.py", label="49", icon="📄")
    else:
        if not has_kai("Le Camouflage"):
            st.write_stream(stream_text(fr_unkown_kai))
        else:
            st.write_stream(stream_text("Vous n'avez pas atteint le rang Kaï de Gardien."))
        st.page_link("tomes/tome4/page_49.py", label="49", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
