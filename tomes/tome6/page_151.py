import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

# « temple souterrain de Maaken » : le temple de Vashna du tome 4, visité par un héros qui a fini ce tome

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=151, book=6)

fr_text = """
La ruelle descend en pente raide vers les quais et les immenses
entrepôts qui bordent la Quarle. Le soleil a disparu derrière
l'horizon et on allume peu à peu les lanternes dans les allées
tortueuses et les passages étroits de cette ville compliquée. Par
les portes grandes ouvertes, la lumière rougeoyante des feux de
bois se reflète sur les pavés noirs de la rue. Vous avancez
encore de quelques mètres, mais la voie est tout à coup bloquée
par le passage d'une procession qui vient dans votre direction.
Les hommes qui la composent sont habillés de longs manteaux
rouges ; ils portent tous une cagoule noire sur la tête et tiennent
à la main un cierge écarlate dont la flamme vacille dans la brise
de la nuit. Leur chef est un homme de haute stature, aux yeux
gris et durs. Il vous dévisage froidement, puis il lève lentement
une main. La procession fait halte. « Etes-vous croyant ou non-
croyant ? » vous demande-t-il d'une voix aussi glaciale que son
regard.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez répondre « croyant », rendez-vous au :"))
    st.page_link("tomes/tome6/page_108.py", label="108", icon="📄")

    st.write_stream(stream_text("Si vous préférez répondre « non-croyant », rendez-vous au :"))
    st.page_link("tomes/tome6/page_67.py", label="67", icon="📄")

    st.write_stream(stream_text("Si vous vous êtes déjà rendu au temple souterrain de Maaken, rendez-vous au :"))
    st.page_link("tomes/tome6/page_294.py", label="294", icon="📄", disabled=4 not in st.session_state.completed_books)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
