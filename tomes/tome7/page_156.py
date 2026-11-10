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

check_inventory(current_page_number=156, book=7)

fr_text = """
Il y a longtemps que Tavig a cessé de crier quand vous parvenez
enfin à faire lâcher prise à la main. Vous emportez le corps
ensanglanté de votre compagnon dans la pénombre du tunnel et
vous l'allongez délicatement sur le sol. Il reste inerte, le regard
fixe : vous ne pouvez plus rien faire pour lui. Vous vous
agenouillez tristement pour lui fermer les yeux, puis vous posez
son épée sur sa poitrine, ainsi que le veut la coutume de son pays
pour les guerriers morts au champ de bataille.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("A présent, si vous souhaitez fouiller rapidement le corps de Tavig avant de reprendre votre chemin, rendez-vous au :"))
    st.page_link("tomes/tome7/page_227.py", label="227", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne pas y toucher et partir immédiatement, rendez-vous au :"))
    st.page_link("tomes/tome7/page_323.py", label="323", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
