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

check_inventory(current_page_number=312, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Les Nains sont à présent en train de nettoyer le pont de tous les
débris de bataille. Un guerrier Drakkar mort gît sur le ventre, au
sommet d'un empilement de caisses et de sacs regroupés sous la
grand-voile. Alors que les Nains le tirent par les pieds pour le
jeter par-dessus bord, il revient subitement à la vie et les envoie
culbuter. Le Drakkar hurle comme un fou tout en faisant
tournoyer sa hache qui décrit autour de lui une courbe
sanguinolente. Un juron de malédiction retentit depuis son
masque à tête de mort, puis il lève le bras pour lancer sa hache.
De toute évidence, c'est vous qu'il prend pour cible !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï de la Chasse ou celle du Sixième Sens, rendez-vous au :'))
    if has_kai("La Chasse") or has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_210.py", label="210", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_210.py", label="210", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous ne maîtrisez aucune de ces Disciplines, utilisez la Table de Hasard pour obtenir un chiffre.'))
    if not (has_kai("La Chasse") or has_kai("Le Sixième Sens")):
        roll = hazard_roll(key='hazard')
        if roll is not None:
            if 0 <= roll <= 4:
                st.write_stream(stream_text('Si vous avez tiré un chiffre compris entre 0 et 4, rendez-vous au :'))
                st.page_link("tomes/tome5/page_354.py", label="354", icon="📄")
            elif 5 <= roll <= 8:
                st.write_stream(stream_text('Si vous avez tiré un chiffre compris entre 5 et 8, rendez-vous au :'))
                st.page_link("tomes/tome5/page_371.py", label="371", icon="📄")
            elif 9 <= roll <= 9:
                st.write_stream(stream_text('Si vous avez tiré un 9, rendez-vous au :'))
                st.page_link("tomes/tome5/page_232.py", label="232", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
