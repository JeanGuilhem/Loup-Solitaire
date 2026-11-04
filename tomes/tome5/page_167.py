import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=167, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous passez la porte et vous vous hâtez vers la fraîcheur
accueillante qui règne dans la pièce. Vous remarquez une grande
barre de fer au-dessus de la porte que vous baissez
instinctivement afin de retarder d'éventuels poursuivants. La
pièce est vide, excepté quelques vêtements posés sur le dossier
d'une chaise en fer forgé. A en juger par leur coupe et leur taille,
ces habits doivent probablement appartenir à l'Armurier. Vous
entendez des bruits en provenance d'un couloir allant vers l'est :
vous distinguez le tintement caractéristique d'assiettes qui
s'entrechoquent puis les voix de Gardes affamés. Vous grimpez
un large escalier et vous suivez un réseau de couloirs allant vers
l'ouest. Ils sont bordés de nombreuses niches contenant des
bustes en marbre et de belles tapisseries représentant un ancien
Zakhan ou une bataille oubliée depuis longtemps.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :'))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_105.py", label="105", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_105.py", label="105", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous ne maîtrisez pas cette Discipline, rendez-vous au :'))
    if not has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_158.py", label="158", icon="📄")
    else:
        st.page_link("tomes/tome5/page_158.py", label="158", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
