import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    lose_everything,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=194, book=2)

fr_text = """
Lorsque vous vous réveillez, vous avez la désagréable surprise de vous
retrouver étendu sous une jetée en bois, dans une puanteur
insupportable qui monte des eaux environnantes. Vous vous relevez
avec une douleur lancinante dans la tête, comme si on vous avait
assommé. C'est d'ailleurs très exactement ce qui vous est arrivé ; mais,
plus grave encore, les pêcheurs vous ont tout volé : Or, Sac à Dos,
Armes, ainsi que tous vos Objets Spéciaux, y compris, hélas, le Sceau
d'Hammardal. Avec un gémissement désespéré, vous vous arrachez à la
puanteur des eaux croupies et vous vous hissez sur la jetée. En levant
les yeux, vous apercevez alors un écriteau délavé qui porte ces mots :
BIENVENUE À RAGADORN
Pour votre malheur, toutes les rumeurs qui circulent au sujet de cette
ville maudite se sont révélées exactes ; il fait presque noir, à présent, et
la pluie s'est mise à tomber. Dans l'immédiat, il vous faut à tout prix
retrouver le Sceau d'Hammardal si vous voulez convaincre le Roi de
Durenor de vous confier le Glaive de Sommer. Vous jetez un coup
d'œil autour de vous et vous apercevez une place sur laquelle est
installé un marché. Au centre de cette place, un poteau indicateur en
pierre signale diverses rues qui mènent dans toutes les directions.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        lose_everything()

    st.write_stream(stream_text("Si vous voulez aller vers l'est le long de la rue de la Bernicle, rendez-vous au :"))
    st.page_link("tomes/tome2/page_215.py", label="215", icon="📄")

    st.write_stream(stream_text("Si vous voulez aller au sud, le long du Dock de la rive Ouest, rendez-vous au :"))
    st.page_link("tomes/tome2/page_303.py", label="303", icon="📄")

    st.write_stream(stream_text("Si vous voulez aller au nord, en empruntant la rue du Butin, rendez-vous au :"))
    st.page_link("tomes/tome2/page_129.py", label="129", icon="📄")

    st.write_stream(
        stream_text(
            "Si enfin vous préférez retourner vers la jetée, en direction de l'ouest, et chercher le "
            "bateau de pêche, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_86.py", label="86", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
