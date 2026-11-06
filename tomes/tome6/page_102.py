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

check_inventory(current_page_number=102, book=6)

fr_text = """
La nuit est déjà tombée lorsque vous atteignez Soren. Le ciel
est pur et des milliers d'étoiles brillent au firmament. Vous
vous engagez dans la rue principale, en direction du quai où une
vingtaine de bateaux sont ancrés. Les fanaux rouges et bleus
accrochés en haut des mâts se reflètent dans les eaux sombres de
la Storn. Votre œil est attiré par un grand panneau de bois posé
sur le quai, à côté d'une passerelle menant à une caravelle de
transport. Les prix des différentes destinations y sont inscrits
à la craie : Luyen: 10 Pièces d'Or Rhem : 15 Pièces d'Or Eula:
20 Pièces d'Or La quatrième escale - Tekaro - a été barrée d'une
croix et l'on a écrit en regard : « Annulé pour cause de guerre.
»
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez acheter un billet pour l'une des trois destinations proposées, rendez-vous au :"))
    if st.session_state.purse >= 10:
        st.page_link("tomes/tome6/page_10.py", label="10", icon="📄")
    else:
        st.page_link("tomes/tome6/page_10.py", label="10", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne le souhaitez pas, ou si vous n'en avez pas les moyens, rendez-vous au :"))
    st.page_link("tomes/tome6/page_68.py", label="68", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
