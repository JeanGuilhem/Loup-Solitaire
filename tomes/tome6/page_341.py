import streamlit as st
from inventory import (
    check_inventory,
    completed_lore_circles,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=341, book=6)

fr_text = """
Votre cheval est en sécurité dans la cale, et il ne vous reste plus
qu'à trouver votre propre cabine. C'est une pièce minuscule à
l'avant du bateau, mais la couchette est confortable et vous vous
endormez aussitôt après avoir posé la tête sur l'oreiller. Vous
vous réveillez une heure après le lever du soleil et vous regardez
par le hublot le rivage ombragé. Le ciel est gris et une petite pluie
fine tombe sur la rivière ; un peu plus tard dans la matinée, un
brouillard épais se lève et vous montez sur le pont. Le Capitaine
s'y tient seul, accoudé au bastingage, son manteau de cuir trempé
par la petite pluie froide et pénétrante. Il hoche la tête en signe
de salut et vous désigne au loin les montagnes du Cener, noyées
dans la brume. « Ce mauvais temps nous prive de points de
repères, mais d'après mes calculs nous devrions être à Luyen vers
midi. » Vous regardez au loin le ciel obscurci et vous remontez le
col de votre manteau.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    solaris = "Cercle de Solaris" in completed_lore_circles()
    st.write_stream(stream_text("Si vous avez accompli le Cercle du Savoir de Solaris (ce qui signifie que vous maîtrisez les Disciplines Magnakaï de l'Invisibilité, de l'Art de la Chasse et de l'Exploration), rendez-vous au :"))
    if solaris:
        st.page_link("tomes/tome6/page_131.py", label="131", icon="📄")
    else:
        st.page_link("tomes/tome6/page_131.py", label="131", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous n'avez pas la pratique complète de ce Cercle du Savoir, rendez-vous au :"))
    if solaris:
        st.page_link("tomes/tome6/page_44.py", label="44", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome6/page_44.py", label="44", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
