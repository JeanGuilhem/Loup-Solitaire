import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=300, book=2)

fr_text = """
En arrivant à proximité du bateau, vous constatez que l'échelle de
coupée a été relevée. Un marin à la mine peu engageante est accoudé
au bastingage et vous lance des injures. De toute évidence, il croit que
vous êtes un réfugié qui essaie de monter à bord comme passager
clandestin. Mais lorsque vous lui criez que vous êtes le Loup Solitaire
et que vous venez d'être trompé par un imposteur, l'échelle est à
nouveau baissée. En prenant pied sur le pont, vous êtes accueilli par un
homme de haute taille vêtu d'un uniforme passementé d'or. Son visage
est presque entièrement caché par une abondante tignasse de cheveux
roux et une grande barbe également rousse. « Levez l'ancre ! »
ordonne-t-il d'une voix tonitruante. Les hommes d'équipage se
précipitent aussitôt à leurs postes comme si leur vie en dépendait et se
mettent au travail. Le capitaine vous conduit ensuite à sa cabine et vous
offre un verre de Wanlo, l'un des alcools les plus forts qu'on puisse
boire dans cette région. Vous lui faites alors le récit de ce qui vient
d'arriver et vous remarquez que son visage prend une expression
soucieuse. « Tout cela sent la trahison, dit-il d'un air sombre, il est clair
que l'ennemi a déjà dressé des plans pour faire échouer votre mission. Il
ne faut plus compter sur l'effet de surprise et, quant à moi, j'ai perdu un
courageux second. Espérons au moins que la traversée jusqu'au
royaume de Durenor sera sans histoire... » Vous le quittez quelques
instants plus tard et vous remontez sur le pont juste à temps pour voir
disparaître à l'horizon les tours de la capitale ; vous descendez ensuite
dans votre propre cabine en éprouvant un sentiment mêlé d'orgueil et
d'appréhension.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre. Si vous tirez 0 ou 1, rendez-vous au 224. Avec 2 ou 3, rendez-vous au 316 ; 4 ou 5, rendez-vous au 81 ; 6 ou 7, rendez-vous au 22 ; 8 ou 9, rendez-vous au 99.'))
    number = hazard_roll()
    if number is not None:
        if number <= 1:
            st.page_link("tomes/tome2/page_224.py", label="224", icon="📄")
        elif number <= 3:
            st.page_link("tomes/tome2/page_316.py", label="316", icon="📄")
        elif number <= 5:
            st.page_link("tomes/tome2/page_81.py", label="81", icon="📄")
        elif number <= 7:
            st.page_link("tomes/tome2/page_22.py", label="22", icon="📄")
        else:
            st.page_link("tomes/tome2/page_99.py", label="99", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
