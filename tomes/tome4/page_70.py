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

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=70, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Les feux de camp allumés le long de la grand-route vous
permettent de repérer votre chemin dans la forêt. Les Guerriers
Pillards sont rassemblés autour des flammes cherchant quelque
réconfort dans leur chaleur. De toute évidence ils négligent leur
tour de garde et vous n'avez aucune difficulté à éviter leurs
patrouilles. Au matin, vous avez atteint la lisière de la forêt.
Devant vous s'étendent des champs de blé ; vous apercevez au-delà
un petit village niché au fond d'une vallée peu profonde.
Quelques sentiers étroits traversent les champs et vous
distinguez des essaims d'insectes qui volettent çà et là. Vous
marchez le long d'un de ces sentiers, lorsque vous apercevez
soudain des brigands qui se dirigent vers vous, leurs lances jetées
sur l'épaule. Ils avancent d'un pas insouciant, comme s'ils se
promenaient.
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

    st.write_stream(stream_text("Si vous souhaitez vous cacher parmi les épis de blé, rendez-vous au :"))
    st.page_link("tomes/tome4/page_159.py", label="159", icon="📄")

    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï du Camouflage et que vous ayez atteint le rang Kaï de Gardien (ou un rang supérieur), rendez-vous au :"))
    if has_kai("Le Camouflage") and kai_rank() >= 7:
        st.page_link("tomes/tome4/page_49.py", label="49", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_49.py", label="49", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
