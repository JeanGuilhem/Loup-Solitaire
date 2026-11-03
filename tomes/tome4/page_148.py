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

check_inventory(current_page_number=148, book=4)

fr_text = """
« Rassemblement ! lance la voix du capitaine Gayal dominant le
fracas de la bataille. Rassemblez-vous autour de moi, soldats du
Sommerlund ! » Le courageux capitaine regroupe ses soldats
protégés par des boucliers et charge le flanc des cavaliers
ennemis qui vacillent et reculent. Le capitaine et sa troupe
parviennent à semer la panique dans les rangs adverses et,
bientôt, un héraut vassagonien, son armure écarlate cabossée et
le visage éclaboussé de sang, s'éloigne de la bataille pour sonner
la retraite. Vous voyez alors les brigands survivants lancer leurs
montures au galop, cherchant désespérément à s'échapper par la
brèche ouverte dans la barricade. Submergés par la peur et la
fatigue, ils s'élancent sur leur propre troupe d'infanterie qui
s'avançait en renfort. Les soldats à pied sont ainsi renversés et
écrasés par la cavalerie qui les piétine. Le capitaine Gayal mène
ses hommes jusqu'à la barricade et une volée de flèches mortelles
s'abat alors sur l'ennemi en déroute. Pour les Vassagoniens c'est
le coup fatal. Ils jettent leurs armes et s'enfuient à toutes jambes
pour essayer d'échapper à la pluie de flèches qui tombe d'un ciel
envahi de fumée. Un cri de guerre fier et strident les poursuit à
travers la plaine : « Vive le Sommerlund ! »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_137.py", label="137", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
