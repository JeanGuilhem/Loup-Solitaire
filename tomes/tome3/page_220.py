import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=220, book=3)

fr_text = """
Le lendemain, il règne un froid polaire. Un fort vent d'ouest
souffle sans relâche tandis que vous conduisez votre traîneau en
direction de la plaine de Hrod. Vous avez de la neige dans les
yeux et vos lèvres gercées saignent. Vers midi cependant, vous
atteignez la bordure de la plaine. Le traîneau de Dyce et d'Irian
arrive le premier devant le mur de glace, et ils vous encouragent
à les rejoindre le plus vite possible. Mais soudain, sans que rien
ne l'ait laissé prévoir, une grande fissure apparaît entre les deux
traîneaux, accompagnée d'un craquement terrifiant : quelques
instants plus tard, une immense crevasse aux profondeurs
obscures s'est formée devant vous. Vous tirez frénétiquement sur
les rênes, mais il est trop tard : les chiens Kanu n'ont pas le
temps de s'arrêter et disparaissent dans le vide. Votre traîneau
reste en équilibre au bord de la crevasse, tandis que les chiens
hurlent, suspendus dans le gouffre, retenus par leur harnais.
Avec d'infinies précautions, vous vous risquez à jeter un coup
d'œil dans la crevasse. Le harnais des deux premiers chiens a
cédé et les deux malheureux animaux se sont écrasés 50 mètres
plus bas, sur une surface glacée. L'un d'eux semble mort. L'autre
est gravement blessé et gémit à côté du corps immobile de son
congénère. Tout d'un coup, le traîneau se met à basculer un peu
plus, dans une brusque secousse et vous êtes saisi d'épouvante.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez vous glisser précautionneusement vers l'arrière du traîneau, en compagnie de "
            "Fenor, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome3/page_146.py", label="146", icon="📄")
    st.write_stream(stream_text("Si vous préférez sauter hors du traîneau, sur la glace fissurée, rendez-vous au :"))
    st.page_link("tomes/tome3/page_29.py", label="29", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
