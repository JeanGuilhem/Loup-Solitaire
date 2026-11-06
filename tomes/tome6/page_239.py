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

check_inventory(current_page_number=239, book=6)

fr_text = """
Mais alors que vous vous apprêtez à partir, Cyrilus se récrie,
inquiet : « Attendez, vous devez aller à Varetta, n'est-ce pas ? Je
dois moi-même m'y rendre demain matin, je connais très bien la
route et ses moindres dangers, et je sais qu'il ne serait pas
prudent que vous vous y aventuriez seul. » Vous comprenez
qu'après sa rencontre avec Roark il est effrayé à l'idée de rester
seul. Voyagerez-vous avec le vieil homme ? Vous pesez le pour et
le contre. D'un côté, vous pensez qu'en sa compagnie le voyage
vous paraîtra moins long, mais de l'autre, sa présence pourrait
vous ralentir. Finalement, vous vous apprêtez à refuser lorsqu'il
vous dit quelque chose qui vous fait changer d'avis.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_319.py", label="319", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
