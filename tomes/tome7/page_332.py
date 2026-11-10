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

check_inventory(current_page_number=332, book=7)

fr_text = """
Vous bondissez au milieu des gardes surpris et vous vous frayez
un chemin en frappant d'estoc et de taille. Deux gardes tombent,
et le troisième s'avance vers vous, son épée toujours au fourreau.
Vous le frappez en dessous du menton ; du sang s'écoule de son
casque, ses yeux de bête roulent dans leurs orbites, et il tombe à
genoux en gémissant horriblement. Le quatrième guerrier
disparaît dans le couloir en poussant des cris d'alarme qui se
répercutent le long du passage.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous lancer à sa poursuite, rendez-vous au :"))
    st.page_link("tomes/tome7/page_195.py", label="195", icon="📄")
    st.write_stream(stream_text("Si vous préférez entrer dans la pièce et tenter de fuir par le couloir du fond, rendez-vous au :"))
    st.page_link("tomes/tome7/page_69.py", label="69", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
