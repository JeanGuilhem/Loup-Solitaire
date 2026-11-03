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

check_inventory(current_page_number=180, book=4)

fr_text = """
Au fond du hangar à bateaux, une cale étroite descend vers une
porte à hauteur d'eau. L'un de vos hommes se précipite pour
soulever la lourde barre qui la verrouille, tandis que les autres
patrouilleurs portent le bateau vers la rampe. Vous poussez
l'embarcation dans l'eau de la rivière puis vous montez à bord,
émergeant du hangar dans une brusque secousse qui vous jette
pêle-mêle les uns sur les autres. Lorsque vous parvenez enfin à
vous relever, le courant de la rivière emporte le bateau. Vous
empoignez un aviron et vous essayez de maintenir l'embarcation
au milieu des eaux bouillonnantes qui s'enfoncent dans les
contreforts de la chaîne de Maaken. Mais, à peine avez-vous pris
le contrôle du bateau qu'un danger inattendu surgit devant vous :
un peu plus loin, en effet, la rivière disparaît soudain dans la
paroi rocheuse d'un énorme bloc de granite. Il est trop tard pour
éviter d'être emporté dans les ténèbres de la grotte qui s'ouvre de
l'autre côté de la paroi. Tandis que l'embarcation plonge dans
l'obscurité, vous vous préparez à affronter les périls qui vous
attendent peut-être.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_241.py", label="241", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
