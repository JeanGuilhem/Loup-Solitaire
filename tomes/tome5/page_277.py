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

check_inventory(current_page_number=277, book=5)

fr_text = """
Vous vous accroupissez le plus possible en attendant que la
chance vous sourie pour vous précipiter sur la porte. Des flèches,
de plus en plus nombreuses, viennent rebondir sur le mur et le
parapet. Les Drakkars se ruent dans l'escalier et le bruit de leurs
bottes ferrées vous glace d'effroi. C'est le moment ou jamais :
vous vous relevez rapidement, puis vous courez vers la porte en
tirant le gros verrou en fer d'une main tremblante. Un projectile
à pointe d'acier fait éclater une pierre à quelques centimètres de
votre main et une flèche, après avoir rebondi sur le mur, vous fait
une entaille juste au-dessus de l'œil. Une fois le verrou tiré vous
poussez la porte en pierre et vous vous précipitez, inconscient
des dangers qui vous attendent derrière...
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_352.py", label="352", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
