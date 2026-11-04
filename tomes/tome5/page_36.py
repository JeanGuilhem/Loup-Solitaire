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

check_inventory(current_page_number=36, book=5)

fr_text = """
Les Sharnazims au visage cruel et menaçant vous encerclent et
les lames aiguisées de leurs cimeterres luisent à la lumière du
soleil. « Attrapez-le ! s'écrie Maouk. Mais prenez-le vivant ! » Les
guerriers rengainent alors leurs armes à contrecœur avant de se
ruer sur vous. Vous parvenez à en éliminer six avant de vous
laisser finalement surpasser par le nombre de vos adversaires. «
Vous êtes courageux, Seigneur Kaï, dit Maouk d'une voix
ironique, mais à partir de maintenant, il vous faudra plus que du
courage pour vous sauver ! »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_176.py", label="176", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
