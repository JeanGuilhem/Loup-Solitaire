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

check_inventory(current_page_number=239, book=4)

fr_text = """
« Il ne s'agit pas là de brigands ordinaires, vous répond le
tenancier de la taverne. Ils appartiennent en fait à une armée
privée. Leur chef est un aristocrate renégat de Vassagonie du
nom de Barraka. Ses hommes, cependant, l'appellent le Tueur du
Destin. Après avoir lancé leur première attaque, nous pensions
que les brigands nous laisseraient tranquilles. Après tout, cette
province n'est pas riche, même lorsque des convois en
provenance des mines la traversent. Pourtant, le Tueur du Destin
et ses hommes sont restés. On dirait... on dirait qu'ils ont décidé
de nous tuer à tout prix. » Cette nuit-là, les trois jeunes gens, qui
sont en fait les fils du tenancier, prennent des tours de garde,
postés derrière les meurtrières aménagées dans les murs. Vos
hommes et vous pourrez ainsi dormir pendant quelques heures.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_324.py", label="324", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
