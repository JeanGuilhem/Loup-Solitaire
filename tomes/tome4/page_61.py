import streamlit as st
from inventory import (
    check_inventory,
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

check_inventory(current_page_number=61, book=4)

fr_text = """
La promptitude de vos réflexes vous a permis de ne pas tomber
dans la rivière. Vous avez en effet évité le tentacule en faisant un
pas de côté et vous lui portez aussitôt un coup. Sous le choc, une
profonde blessure apparaît laissant échapper un jet de sang vert
qui se répand au fond du bateau. Il n'y a plus que deux rescapés
parmi vos hommes. L'un est en train de frapper de son arme un
autre tentacule qui s'est enroulé autour de son pied, le second est
étendu sans connaissance, le bras cassé à hauteur du coude.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez frapper à votre tour le tentacule enroulé autour du pied du patrouilleur, rendez-vous au :"))
    st.page_link("tomes/tome4/page_304.py", label="304", icon="📄")

    st.write_stream(stream_text("Si vous préférez porter secours au patrouilleur évanoui, rendez-vous au :"))
    st.page_link("tomes/tome4/page_136.py", label="136", icon="📄")

    st.write_stream(stream_text("Enfin, si vous estimez plus judicieux d'empoigner les rames et d'essayer de gagner la rive, rendez-vous au :"))
    st.page_link("tomes/tome4/page_189.py", label="189", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
