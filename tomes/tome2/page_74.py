import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=74, book=2)

fr_text = """
Vous posez vos mains sur sa poitrine et vous essayez de refermer sa
blessure. Il a perdu beaucoup de sang et bien qu'il transpire
abondamment, il a la peau froide. Ses yeux s'ouvrent alors et il
prononce quelques mots à peine audibles. « Les pirates... Les pirates de
Lakuri... Attention aux voiles rouges... Repoussez les pirates... » Le
capitaine perd à nouveau connaissance. Vous l'enveloppez dans des
couvertures et vous glissez un coussin sous sa tête, mais il a déjà
plongé dans un sommeil dont il ne reviendra jamais. Pendant ce temps,
les cadavres des membres de l'équipage ont été rassemblés sur le pont.
Le capitaine Kelman s'approche de vous et vous tend un cimeterre noir
qui semble particulièrement redoutable. « Ce n'est pas une épée de
pirate, Loup Solitaire, dit-il, cette lame vient des forges de Helgedad.
C'est une épée de Maître des Ténèbres. » On ne pouvait vous annoncer
plus mauvaise nouvelle car, si les Maîtres des Ténèbres ont rallié les
pirates de Lakuri à leur cause, le voyage jusqu'à Durenor sera plus
périlleux encore que vous ne le pensiez. Vous jetez à l'eau le cimeterre
noir et vous revenez à bord du Sceptre Vert. Et tandis que vous mettez
le cap à l'est, le navire marchand de Durenor s'enfonce dans les
profondeurs de la mer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_240.py", label="240", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
