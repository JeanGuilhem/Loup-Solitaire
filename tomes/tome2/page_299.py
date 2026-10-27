import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

fr_unknown_item = "Vous ne possédez pas cet objet."
check_inventory(current_page_number=299, book=2)

fr_text = """
Vous courez pendant six heures sans vous arrêter. Les Monstres d'Enfer
vous attendent sur le grand chemin et il vous faut les éviter en passant
par les forêts escarpées qui s'étendent au flanc des collines. Souvent,
vous vous sentez si fatigué, vos jambes vous font si mal que vous avez
la tentation de tout abandonner. Mais chaque fois que vous faiblissez, le
Lieutenant Général Rhygar parvient à vous redonner courage. Son
endurance vous émerveille car ce n'est plus un jeune homme et il porte
par surcroît la lourde armure des chevaliers du Sommerlund. A la nuit
tombée, vous arrivez à l'entrée du tunnel de Tarnalin qui traverse les
monts d'Hammardal. Il y a en tout trois tunnels qui mènent à la capitale
de Durenor. Tous trois ont été creusés au temps de la Lune Noire et
chacun d'eux fait plus de 60 kilomètres de long. Ils constituent les
seules voies d'accès à la ville qui est entièrement encerclée par les
montagnes. Vous pouvez à présent faire une courte halte et le
Lieutenant Général Rhygard s'assied à côté de vous en prenant dans son
sac du pain et des viandes. « Mangez, Loup Solitaire, dit-il alors en
vous tendant cette nourriture, car vous allez avoir besoin de forces ; il
vous faudra en effet parcourir seul ce tunnel qui mène à Hammardal,
tandis que je resterai ici pour contenir l'ennemi aussi longtemps que je
pourrai combattre. Et ne protestez pas, le succès de votre mission est la
seule chose qui compte. » Mais si Rhygard veut arrêter les Monstres
d'Enfer, il lui faudra une arme magique car sa propre épée ne lui servira
à rien contre ces créatures.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez lui donner votre Lance Magique pour qu'il puisse défendre l'entrée du tunnel, rendez-vous au :"))
    if has_item("LANCE MAGIQUE"):
        st.page_link("tomes/tome2/page_102.py", label="102", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_102.py", label="102", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous ne possédez pas cette Lance Magique ou si vous ne voulez pas vous en séparer, rendez-vous au :'))
    st.page_link("tomes/tome2/page_118.py", label="118", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
