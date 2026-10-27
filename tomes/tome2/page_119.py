import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=119, book=2)

fr_text = """
Des débris de bois, des planches, des madriers et des voiles déchirées
flottent sur les vagues parsemées d'écume. C'est là tout ce qui reste d'un
navire marchand. Mais soudain, vous apercevez un homme cramponné
à un panneau d'écoutille. Une échelle de corde lui est aussitôt jetée et le
malheureux est ramené à bord. « Les pirates ! » dit-il simplement avant
de s'écrouler sur le pont, à bout de force. Après qu'on l'a enveloppé
dans une couverture, l'homme est emmené dans une cabine. Il a reçu de
nombreuses blessures et sa fin est proche. « Voici un forfait qui porte la
signature des pirates Lakuri, vous confie le capitaine, mais il est rare
qu'on les croise dans ces eaux ; ils doivent être sur la piste d'un riche
butin pour s'être ainsi éloignés de leurs îles tropicales. » Et tandis que
votre navire reprend sa route en direction de Durenor, vous ne pouvez
vous empêcher de penser que ce « riche butin » pourrait bien être vous-
même.
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
