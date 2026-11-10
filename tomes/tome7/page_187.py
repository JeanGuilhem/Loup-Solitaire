import streamlit as st
from inventory import (
    can_shoot,
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

check_inventory(current_page_number=187, book=7)

fr_text = """
Le tunnel descend dans une caverne vaste et profonde. Des
volutes de fumée s'élèvent de part et d'autre d'un étroit pont en
pierre qui mène au centre de cet antre immense, où il rejoint un
autre chemin orienté d'est en ouest. Prudemment, vous avancez
sur le pont, l'estomac soulevé par l'odeur âcre des fumées
sulfureuses et la vue du vide noir et béant qui s'ouvre de chaque
côté de vous. Arrivé au centre, vous entendez des bruits de pas
précipités provenant du passage voûté sur votre droite.

Les bruits se rapprochent rapidement et, soudain, un homme
vêtu d'une armure en cuir surgit de l'obscurité. En vous
apercevant, il s'arrête si brusquement qu'il semble, l'espace d'un
instant, transformé en statue de pierre ! Son visage maigre,
ruisselant de sueur, est déformé par la peur. Après avoir jeté un
regard anxieux par-dessus son épaule, il dégaine son arme et
s'avance dans votre direction.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un arc et que vous souhaitiez l'utiliser contre ce guerrier, rendez-vous au :"))
    st.page_link("tomes/tome7/page_79.py", label="79", icon="📄", disabled=not can_shoot())

    st.write_stream(stream_text("Si vous préférez dégainer votre arme pour vous défendre, rendez-vous au :"))
    st.page_link("tomes/tome7/page_95.py", label="95", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Intuition, rendez-vous au :"))
    if has_magnakai("Intuition"):
        st.page_link("tomes/tome7/page_205.py", label="205", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_205.py", label="205", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
