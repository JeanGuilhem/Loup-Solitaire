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

check_inventory(current_page_number=161, book=2)

fr_text = """
La boutique est déserte. Vous attendez en examinant pendant cinq
minutes les articles exposés, mais personne ne vient. Vous vous
apprêtez à repartir lorsque vous remarquez une carte accrochée derrière
la porte. C'est un plan du port de Ragadorn. Les écuries et le relais de la
diligence sont clairement indiqués à proximité de la porte Est de la
ville. C'est là que vous trouverez un moyen de transport qui vous
permettra d'atteindre Port Bax. Vous repérez le trajet qui mène à la
porte Est et vous quittez la boutique. Vous rebroussez chemin au pas de
course dans la rue de la Hache puis vous tournez vers l'est, dans la rue
du Sage. Le pont de Ragadorn se trouve tout au bout de cette voie
sinueuse ; c'est là le seul point de passage qui relie les parties Est et
Ouest de la ville. Vous vous frayez un chemin dans la foule qui se
presse sur le pont, puis, dès que vous êtes arrivé de l'autre côté, vous
vous mettez à courir sur les pavés le long du boulevard du Commerce,
section Est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_186.py", label="186", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
