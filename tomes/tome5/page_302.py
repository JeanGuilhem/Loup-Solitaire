import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=302, book=5)

fr_text = """
Banedon prend la barre tandis que son extraordinaire vaisseau,
la Nef du ciel, ainsi que le nomment les Nains, fait route à travers
les ténèbres grandissant vers le passage du Dahir. La visibilité
diminue de minute en minute jusqu'à ce que vous ne puissiez
plus rien distinguer au-delà de la passerelle qui borde le
vaisseau. Vous vous sentez plutôt mal à l'aise, car si la Nef du ciel
dévie de sa route, ne serait-ce que d'un pouce, vous irez vous
écraser contre les parois abruptes de la montagne. « Ne vous
inquiétez pas, Loup Solitaire, dit Nolrim, le Nain à la sacoche de
velours, le capitaine s'en sortira ! » Banedon, quant à lui, se tient
debout, la main délicatement posée sur le cristal étincelant, et
l'air absent, comme s'il était en transes. Ses yeux sont fermés et
une série de pulsations nerveuses tracent de fugitifs sillons sur
son front et ses tempes. Le Nain vous conduit à une cabine située
à l'arrière du vaisseau où les membres de l'équipage se racontent
avec grande excitation leur victoire sur les Kraans et leurs
cavaliers. Ils sont tous assis autour d'une table jonchée
d'assiettes fumantes et de bocks de bière mousseuse. L'odeur
alléchante des plats épicés et de la bière de Bor vous chatouille
les narines et vous fait soudain réaliser que mourez de faim.
Vous dévorez en un clin d'œil la viande à la moelle que l'on vous
sert. Ce copieux repas vous fait gagner 3 points d'ENDURANCE.
Cependant, vous hésitez avant d'accepter un bock de bière, car la
bière de Bor est une boisson si forte qu'elle a été proscrite dans
maintes villes du Magnamund en raison des ravages qu'elle peut occasionner.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=3)

    st.write_stream(stream_text('Si vous voulez boire un peu de cette bière de terrible réputation, rendez-vous au :'))
    st.page_link("tomes/tome5/page_392.py", label="392", icon="📄")

    st.write_stream(stream_text("Si vous préférez décliner l'offre et vous en abstenir, rendez-vous au :"))
    st.page_link("tomes/tome5/page_283.py", label="283", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
