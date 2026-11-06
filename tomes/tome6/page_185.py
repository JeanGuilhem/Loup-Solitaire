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

check_inventory(current_page_number=185, book=6)

fr_text = """
Vous attachez votre cheval à un poteau et gravissez les marches
inégales jusqu'à la porte de la cabane de la bière. Pendant ce
temps, Cyrilus annonce son arrivée en frappant à la porte de
Denka avec son bâton et demande à son frère de lui ouvrir.
N'obtenant aucune réponse, il se met à frapper de plus belle, et
vous souriez en le voyant perdre patience. Si son frère lui
ressemble un tant soit peu, il doit avoir le sommeil facile ! Sans
plus attendre, vous pénétrez dans la cabane. Tout semble désert
mais, en approchant du comptoir, vous apercevez un homme à
moitié endormi, affalé sur un tabouret, une chope à la main.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez le réveiller, rendez-vous au :"))
    st.page_link("tomes/tome6/page_93.py", label="93", icon="📄")

    st.write_stream(stream_text("Si vous préférez tirer vous-même de la bière à l'un des fûts, rendez-vous au :"))
    st.page_link("tomes/tome6/page_266.py", label="266", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
