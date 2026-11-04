import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=208, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
« Par tous les Dieux ! crie Banedon, un lépreux ! » Le visage du
vieil homme n'est plus qu'un horrible masque couvert de
pustules verdâtres et purulentes. Ses pupilles ont viré au jaune et
ses lèvres ne sont plus que des lambeaux de chair grisâtre qui
pendent lamentablement. Banedon vous écarte du pauvre
malade puis vous dit à l'oreille : « Il a la lèpre, Loup Solitaire ;
une maladie terrible, extrêmement contagieuse, qui pourrit la
peau. Nos vies sont en danger. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un peu d'herbe d'Oede, vous pouvez en donner au malheureux lépreux. Rendez-vous en ce cas au :"))
    if has_item("HERBE D'OEDE"):
        st.page_link("tomes/tome5/page_321.py", label="321", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_321.py", label="321", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous n'en possédez pas, ou si vous ne souhaitez pas en donner au malade, fuyez la caverne avec Banedon et rendez-vous au :"))
    st.page_link("tomes/tome5/page_270.py", label="270", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
