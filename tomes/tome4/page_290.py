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

check_inventory(current_page_number=290, book=4)

fr_text = """
Les ruines sont envahies de racines et de mauvaises herbes, mais
vous parvenez cependant à distinguer les contours du sanctuaire
qui constitue le centre du temple. L'immense dôme de marbre
est toujours intact et vous offrira un excellent abri. Tandis que
vous attachez votre cheval à un arbre rabougri, vous apercevez
deux hommes vêtus de longues capes noires, cachés sous le
dôme. Vous leur donnez aussitôt l'ordre de sortir du sanctuaire et
de décliner leur identité, mais ni l'un ni l'autre ne vous répond ni
ne bouge.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez faire signe à vos hommes d'attaquer ces deux étrangers, rendez-vous au :"))
    st.page_link("tomes/tome4/page_44.py", label="44", icon="📄")
    st.write_stream(stream_text('Si vous préférez essayer de les capturer vivants, rendez-vous au :'))
    st.page_link("tomes/tome4/page_102.py", label="102", icon="📄")
    st.write_stream(stream_text("Enfin, si vous décidez plutôt de remettre votre arme au fourreau et de vous approcher d'eux la main tendue en signe d'amitié, rendez-vous au :"))
    st.page_link("tomes/tome4/page_78.py", label="78", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
