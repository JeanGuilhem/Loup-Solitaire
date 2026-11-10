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

check_inventory(current_page_number=13, book=7)

fr_text = """
Un grincement strident de métal rouillé retentit dans le tunnel
tandis que les rouages en fer se mettent en action. Lentement, la
herse se soulève. Sans perdre un instant, vous vous glissez sous
les pointes acérées et vous partez en courant dans le passage qui
s'ouvre devant vous. Une ribambelle de rats vous file entre les
jambes en couinant, tandis que vous courez sur les dalles
glissantes du souterrain. Vous frémissez de dégoût en entendant
leurs pattes griffer la pierre et leur queue dénudée fendre le
limon verdâtre et puant qui recouvre le sol. Heureusement, le
passage finit par s'élargir, et vous débouchez sur un escalier
menant vers le bas. Vous dévalez les marches mais, dans votre
course, vous dérangez une colonie de chauves-souris qui se
mettent à voler furieusement autour de vous, vous frôlant de
leurs ailes membraneuses tout en essayant de vous mordre de
leurs petites dents pointues comme des aiguilles.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Magnakaï du Contrôle Animal ou du Foudroiement Psychique, rendez-vous au :'))
    if has_magnakai("Contrôle Animal") or has_magnakai("Foudroiement Psychique"):
        st.page_link("tomes/tome7/page_180.py", label="180", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_180.py", label="180", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez ni l'une ni l'autre de ces disciplines, rendez-vous au :"))
    st.page_link("tomes/tome7/page_285.py", label="285", icon="📄", disabled=has_magnakai("Contrôle Animal") or has_magnakai("Foudroiement Psychique"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
