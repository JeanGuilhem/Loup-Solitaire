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

check_inventory(current_page_number=309, book=7)

fr_text = """
La descente est lente et difficile. De nombreuses marches ont été
emportées lors de l'effondrement des remparts et vous devez
lutter contre une pluie de cendres et de roches volcaniques qui
jaillissent du cœur du donjon. Vous vous abritez comme vous le
pouvez, mais vous ne restez jamais longtemps au même endroit
de peur d'être pris dans une faille ou sous un éboulis de pierres.
Lorsque vous arrivez enfin à la plage, votre manteau et votre
capuchon sont brûlants, et les semelles de vos bottes ont
pratiquement fondu. Un grand nombre de créatures ont réussi à
s'échapper avant vous et elles se pressent sur la plage en se
mordant et en se griffant les unes les autres dans une terreur
panique. De nombreux corps flottent sur le lac, et le sable noir
est presque entièrement recouvert de cadavres et de carcasses.
Vous vous frayez un chemin à travers tous ces êtres affolés, mais
rester sur la plage serait suicidaire.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez escalader les rochers pour plonger dans le lac, rendez-vous au :"))
    st.page_link("tomes/tome7/page_254.py", label="254", icon="📄")
    st.write_stream(stream_text("Si vous préférez vous frayer un chemin jusqu'à la vieille jetée, rendez-vous au :"))
    st.page_link("tomes/tome7/page_122.py", label="122", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
