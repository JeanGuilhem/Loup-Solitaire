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

check_inventory(current_page_number=167, book=6)

fr_text = """
En poussant la porte de la taverne du Beaurivage, vous êtes
accueilli par des rires gras et rauques. Une foule hétéroclite de
buveurs, habillés de façon voyante et exhibant leurs armes avec
vanité, est agglutinée autour du comptoir. Soudain, une voix
tonitruante crie votre nom. Parcourant rapidement la bruyante
assemblée des yeux, vous reconnaissez alors le Capitaine, le chef
des mercenaires, que vous aviez rencontré à l'Auberge des Épées
Croisées. « Salut, mon ami, quelle bonne surprise ! s'écrie-t-il en
vous donnant amicalement une grande tape dans le dos. Ainsi, tu
as changé d'avis, te voilà décidé à te joindre à ma valeureuse
troupe. » Avant même que vous ayez le temps de répondre, il
vous place une chope de bière mousseuse dans la main en
clamant : « A la bataille et à mon butin ! » Une vingtaine de voix
éraillées par l'alcool font écho à son toast. Le Capitaine vous
explique ensuite que ses hommes et lui doivent partir pour Eula
à bord d'un bateau de rivière qui lèvera l'ancre à minuit. Si vous
souhaitez faire le voyage avec eux, il paiera lui-même votre billet.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez aller jusqu'à Eula par bateau, ainsi que vous l'offre le Capitaine, rendez-vous au :"))
    st.page_link("tomes/tome6/page_341.py", label="341", icon="📄")

    st.write_stream(stream_text("Si vous préférez voyager seul et aller à Tekaro par la route, rendez-vous au :"))
    st.page_link("tomes/tome6/page_118.py", label="118", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
