import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=306, book=6)

fr_text = """
Vous luttez de toutes vos forces contre le courant et essayez de
vous diriger vers l'autre rive. Finalement le souffle coupé et
tremblant de froid, vous sortez de l'eau et vous vous effondrez
comme une masse sur les rochers. Il fait un froid extrême et, à
moins que vous ne possédiez la Discipline Magnakaï de Nexus,
vous perdez 1 point d'ENDURANCE. Vous reprenez peu à peu
conscience et découvrez que vous vous trouvez tout près du
confluent de la Quarle et la Storn. Vous apercevez une grotte au
pied du mur d'enceinte de la ville, à moins de dix mètres de
l'endroit où vous vous trouvez. Elle est fermée par une grille de
fer aux barreaux rouillés, et une odeur épouvantable se dégage
des eaux qui s'écoulent vers la rivière. Lorsque vous comprenez
qu'il s'agit d'un égout, une lueur d'espoir s'allume dans vos yeux :
grâce à cet égout, vous pourrez peut-être vous introduire au cœur
de Tekaro !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if has_magnakai("Nexus"):
        st.write("*Votre Discipline Magnakaï de Nexus vous protège du froid.*")
    else:
        if is_new_page():
            change_endurance(-1)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome6/page_249.py", label="249", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
