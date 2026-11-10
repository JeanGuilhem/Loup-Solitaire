import streamlit as st
from inventory import (
    can_shoot,
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

check_inventory(current_page_number=79, book=7)

fr_text = """
Le visage déformé par l'horreur, le guerrier regarde la flèche
arriver sur lui en fendant l'air. Il ouvre la bouche pour hurler,
mais son cri lui reste dans la gorge, car le projectile se plante
profondément dans sa poitrine. Il chancelle, bat l'air de ses
mains comme pour s'agripper à quelque chose et bascule du pont
dans le gouffre enfumé. Soudain, un cri féroce s'élève de l'arche.
Vous prenez une autre flèche et vous visez au jugé, lorsque vous
parvient un murmure sourd qui va en s'amplifiant. Ce bruit vous
fait frémir. C'est alors que trois créatures à la peau bleu nuit
émergent de l'ombre en sifflant et en jacassant entre leurs dents.
Elles vous fixent d'un œil féroce et avancent par bonds, sans
cesser de ricaner de façon horripilante.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez essayer de tuer ces trois créatures à l'aide de votre arc, rendez-vous au :"))
    st.page_link("tomes/tome7/page_328.py", label="328", icon="📄", disabled=not (can_shoot()))

    st.write_stream(stream_text("Si vous préférez ranger votre arme et tenter d'échapper à vos adversaires en fuyant par le passage voûté qui se trouve de l'autre côté, rendez-vous au :"))
    st.page_link("tomes/tome7/page_241.py", label="241", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
