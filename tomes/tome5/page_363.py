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

check_inventory(current_page_number=363, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous plongez dans le jardin en contrebas; une fraction de
seconde plus tard, vous étiez mort. Les flèches viennent ricocher
sur les pointes empoisonnées qui surmontent la porte, puis
rebondissent vers le ciel en sifflant. Le jardin clos est parfumé
par les senteurs des plantes exotiques et des fleurs qui bordent
un bassin sculpté rempli d'eau bleue. C'est un spectacle
ravissant, mais vous n'avez pas le temps de vous y arrêter, car les
Gardes du Palais sont à vos trousses et vous devez continuer à
avancer. En face de vous, au-delà d'une colonnade bordée
d'arbres, une volée de marches monte jusqu'à un petit portail
encastré dans le mur du Palais supérieur. A votre droite, un
sentier sinueux s'enfonce dans l'épais feuillage des arbustes et
des arbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome5/page_220.py", label="220", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_220.py", label="220", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline, vous pouvez monter les marches vers le petit portail, rendez-vous dans ce cas au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome5/page_352.py", label="352", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_352.py", label="352", icon="📄")
    st.write_stream(stream_text("ou bien suivre le sentier sinueux, rendez-vous alors au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome5/page_391.py", label="391", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_391.py", label="391", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
