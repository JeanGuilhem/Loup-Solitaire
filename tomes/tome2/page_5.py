import streamlit as st
from combat import combat
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=5, book=2)

fr_text = """
La porte s'ouvre à la volée et un MONSTRE d'ENFER se rue sur vous
en brandissant son épée. Vous frappez la créature dès qu'elle a pénétré
dans la cale et sous l'effet du coup, une longue et profonde entaille
apparaît sur sa poitrine. Le Monstre pousse un cri épouvantable, mais,
malgré sa blessure, il a encore la force de bondir sur vous. Il vous faut
engager un combat à mort.
Le Monstre d'Enfer est un être de l'au-delà, un mort vivant, et la
puissance du Glaive de Sommer vous permet de multiplier par deux
tous les points d'ENDURANCE qu'il perdra au cours du combat. Il est
cependant insensible à la Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("MONSTRE BLESSÉ", 22, 20)], psychic_immune=True, undead=True)
    if outcome == "win":
        st.write_stream(stream_text("Vous avez tué le Monstre : vous pouvez vous enfuir de la cale par l'écoutille. Rendez-vous alors au :"))
        st.page_link("tomes/tome2/page_166.py", label="166", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
