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

check_inventory(current_page_number=341, book=3)

fr_text = """
Vous sentez la présence d'une force puissante derrière cette
arcade baignée de brume. Et, tandis que vous vous concentrez, le
souvenir vous revient d'une légende qu'on vous avait racontée
dans votre enfance: la « Légende de la Porte de Vagadyn ».
C'était l'histoire de Démons de Glace qui avaient mené une
guerre pour pouvoir quitter leur monde et venir à Kalte. Ces
créatures n'avaient pas de corps, pas de forme, pas de substance,
elles n'étaient que pure énergie dans une autre dimension, au-
delà des limites du temps et de l'espace. Or, les Démons de
Glaces avaient découvert la Porte de Vagadyn, un seuil qui reliait
leur monde à celui de Magnamund et ils se battaient entre eux
pour passer cette Porte sans se douter du sort qui les attendait de
l'autre côté. Car les Anciens, eux aussi, connaissaient l'existence
du seuil de Vagadyn et, chaque fois qu'un Démon le franchissait,
ils l'emprisonnaient dans un cristal, pour utiliser son énergie à
bâtir la forteresse d'Ikaya. Les coupes de M'iare qui éclairent
d'une lumière éternelle les souterrains d'Ikaya contiennent ainsi
les esprits de Démons de Glace inférieurs qui y sont enfermés.
Vous vous rappelez également que, dans ce conte, on promettait
les pires malheurs à quiconque détruirait la prison de cristal d'un
de ces Démons car alors, la créature immatérielle chercherait à
s'emparer du corps de son sauveur. Averti par la mise en
pratique de votre Discipline Kaï, vous franchissez l'arcade
baignée de brume.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_264.py", label="264", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
