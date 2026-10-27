import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=251, book=2)

fr_text = """
Il fait presque nuit lorsque le petit bateau de pêche entre dans le port de
Ragadorn. Vous n'avez toujours pas rencontré le moindre survivant au
naufrage et le pire est à craindre. Vous remarquez bientôt que trois des
pêcheurs ont un comportement suspect. Ils se parlent à l'oreille et
jettent de fréquents regards à votre bourse. Et tandis que le bateau
vogue dans l'estuaire du fleuve Dorn, ils vous encerclent soudain et
vous ordonnent de leur donner votre or. Vous vous apprêtez à passer à
l'attaque lorsque quelqu'un vous pousse par-derrière en vous projetant à
plat ventre sur le pont. L'un des marins lève alors le pied et un instant
plus tard, tout devient noir dans votre tête.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_194.py", label="194", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
