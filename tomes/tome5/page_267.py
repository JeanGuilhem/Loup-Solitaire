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

check_inventory(current_page_number=267, book=5)

fr_text = """
Les Drakkars chancellent, aveuglés par l'éclair. Norlim profite de
l'occasion pour pousser ses compagnons à résister aux
envahisseurs, menant l'attaque de sa puissante hache de guerre,
affûtée comme un rasoir. La hache fend l'air en sifflant et vient
frapper les armures noires de l'ennemi en faisant jaillir des
gerbes d'étincelles, causant des ravages dans leurs rangs
clairsemés, comme une faux coupant des blés mûrs. Vous
regrimpez sur la plate-forme et vous voyez un Drakkar sur le
point de frapper Banedon. Loin d'être impressionné par le
guerrier mugissant qui menace de le décapiter avec son épée
noire à double tranchant, le jeune magicien pointe son doigt vers
le Drakkar prêt à frapper.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez attaquer le Drakkar avant qu'il ne touche Banedon à la tête, rendez-vous au :"))
    st.page_link("tomes/tome5/page_330.py", label="330", icon="📄")

    st.write_stream(stream_text("Si vous ne souhaitez pas intervenir, rendez-vous au :"))
    st.page_link("tomes/tome5/page_394.py", label="394", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
