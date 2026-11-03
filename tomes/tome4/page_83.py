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

check_inventory(current_page_number=83, book=4)

fr_text = """
L'escalier mène à un niveau inférieur où un passage vous permet
de vous diriger vers le sud. Vous venez juste de pénétrer dans ce
tunnel, lorsqu'une patrouille de Gardes surgit soudain,
franchissant une porte dissimulée dans la paroi, un peu plus loin.
Vous vous ruez parmi eux en les bousculant de tous côtés et vous
parvenez à vous enfuir avant qu'ils n'aient eu le temps de
dégainer leurs armes. Leurs cris de fureur retentissent à vos
oreilles tandis que vous courez à toutes jambes en direction
d'une faible lueur aperçue au loin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_199.py", label="199", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
