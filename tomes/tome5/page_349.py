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

check_inventory(current_page_number=349, book=5)

fr_text = """
Un rayon d'énergie pure jaillit en sifflant le long de la lame effilée
du glaive doré. Vous assénez un violent coup sur la tête du
Vordak, lui fracturant le crâne jusqu'aux dents. Votre victime
pousse un hurlement surnaturel de terreur, de douleur et
d'agonie. Son squelette tombe et se transforme en un fluide vert
et fumant qui désintègre aussitôt les plantes qui poussent aux
alentours. Les Drakkars hésitent à la vue du Glaive de Sommer
dont les rayons vifs se réfléchissent sur leurs masques à tête de
mort. Vous en profitez pour passer à l'attaque, donnant des
coups à droite et à gauche pour vous ouvrir le chemin. Un
guerrier Drakkar lève alors son bouclier, mais votre lame
transperce le bois recouvert d'acier et le blesse à l'épaule.
L'instant suivant, vous faites volte-face et vous levez votre Glaive
sur un autre Drakkar qui s'apprêtait à vous frapper. Vous
déchirez son armure noire comme s'il s'agissait d'un morceau de
parchemin. Le Drakkar pousse un cri d'agonie, mais vous
disparaissez dans l'épais feuillage avant même que son corps
inerte ne tombe à terre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_228.py", label="228", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
