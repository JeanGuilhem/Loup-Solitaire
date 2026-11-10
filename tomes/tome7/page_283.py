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

check_inventory(current_page_number=283, book=7)

fr_text = """
Le reste de la horde se jette, pour les dévorer, sur les cadavres
mutilés des rats qui gisent autour de vous. Cependant quelques-uns
ont réussi à percer par endroits votre formidable défense et à
enfoncer leurs petites dents acérées dans votre chair. Vos bras,
vos jambes et vos mains sont ensanglantés par de nombreuses
petites morsures et égratignures. Votre victoire vous a donné le
temps de réfléchir mais, dans quelques secondes, les rats
passeront de nouveau à l'attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez escalader le récif de rochers déchiquetés se dressant à votre gauche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_336.py", label="336", icon="📄")

    st.write_stream(stream_text("Si vous préférez remettre votre coracle à l'eau et vous éloigner de la baie, rendez-vous au :"))
    st.page_link("tomes/tome7/page_117.py", label="117", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
