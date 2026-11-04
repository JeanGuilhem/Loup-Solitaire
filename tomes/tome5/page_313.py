import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=313, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Au pied du clocher, vous remarquez un espace où sont alignés plusieurs enclos à Itikars possédant chacun une aire
d'atterrissage personnelle. Les Itikars sont de grands oiseaux
noirs qui nichent dans les plus hauts sommets du Dahir et des
monts Vakar. Les Vassagoniens ont depuis longtemps réussi à
apprivoiser ces géants du ciel. Ils les utilisent couramment
comme monture pour les déplacements des chefs militaires, des
éclaireurs, des messagers et des envoyés spéciaux. Soudain, un
cavalier monté sur un Itikar surgit du ciel rougeoyant et vient
atterrir sur la plate-forme jouxtant le clocher. Des esclaves
tendent une corde au cavalier qui l'attache à son tour à l'anneau
de la selle avant de mettre pied à terre. L'Itikar croasse en faisant
battre ses larges et puissantes ailes tandis qu'un treuil l'emporte
de force vers son enclos. Le cavalier et les esclaves quittent la
plate-forme et il ne reste plus à présent qu'une seule sentinelle à
l'entrée de l'enclos. Si vous réussissez à la maîtriser, vous pourrez
alors fuir sur le dos de l'oiseau géant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous possédez une sarbacane et une Flèche de Sommeil, rendez-vous au :'))
    if has_item("SARBACANE") and has_item("FLÈCHE DE SOMMEIL"):
        st.page_link("tomes/tome5/page_325.py", label="325", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_325.py", label="325", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous ne possédez pas ces objets, rendez-vous au :'))
    if has_item("SARBACANE") and has_item("FLÈCHE DE SOMMEIL"):
        st.page_link("tomes/tome5/page_282.py", label="282", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_282.py", label="282", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
