import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=320, book=2)

fr_text = """
En ouvrant son sac, vous y découvrez avec horreur un parchemin en
peau humaine sur lequel un message a été tracé dans une étrange
écriture runique. Le seul mot que vous parvenez à reconnaître est « Kaï
». Vous trouvez également dans le sac un poignard à la lame noire dont
la seule vue vous fait frissonner, ainsi qu'un bloc d'obsidienne. Ces
objets portent la marque des Maîtres des Ténèbres, et il n'est pas
étonnant que vous vous sentiez soudain fort inquiet. Vous jetez le sac à
terre comme s'il s'agissait d'un charbon ardent et vous vous hâtez de
rejoindre votre cheval. Hélas, le malheur veut qu'il ait disparu: sans
doute les Squalls l'ont-ils volé. Vous poussez alors un soupir de
découragement et vous vous résignez à poursuivre votre route à pied.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_138.py", label="138", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
