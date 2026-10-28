import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=190, book=3)

fr_text = """
Vous ne relâchez l'enfant qu'au dernier moment, juste avant
d'empoigner les fouets et d'en cingler l'échine des chiens qui
s'élancent aussitôt, de toute la puissance de leurs muscles. Des
volées de flèches vous sifflent aux oreilles et plusieurs d'entre
elles viennent se ficher avec un bruit mat dans l'armature de bois
du traîneau. Deux éclaireurs Barbares vous donnent la chasse,
mais vos chiens ont à présent atteint leur pleine vitesse et vous
avez tôt fait de distancer vos poursuivants en restant désormais
hors de portée de leurs flèches. A la nuit tombée, vous arrivez au
pied des monts de Viad. Cette immense chaîne de granit dresse
au-dessus de la glace ses flancs escarpés, gigantesque barrière de
roc qu'il est inutile d'espérer franchir par cette nuit sans lune.
Bientôt, le vent se lève à l'ouest, annonçant une tempête
nocturne et il vous faut à tout prix trouver un endroit où vous
abriter, sinon, vous ne survivrez pas au blizzard.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de l'Orientation ou celle du Sixième Sens, rendez-vous au :"))
    if has_kai("L'Orientation") or has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome3/page_348.py", label="348", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_348.py", label="348", icon="📄", disabled=True)
    st.write_stream(stream_text('Si vous ne possédez aucune de ces deux Disciplines, vous pouvez chercher un abri en marchant vers le nord ; rendez-vous pour cela au :'))
    st.page_link("tomes/tome3/page_27.py", label="27", icon="📄")
    st.write_stream(stream_text('Si vous préférez prendre la direction du sud pour essayer de trouver cet abri, rendez-vous au :'))
    st.page_link("tomes/tome3/page_314.py", label="314", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
