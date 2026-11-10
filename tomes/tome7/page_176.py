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

check_inventory(current_page_number=176, book=7)

fr_text = """
Vous avancez lentement et prudemment, tout en vous efforçant
de percer l'obscurité. Devant vous, le tunnel vire brusquement à
gauche, mais avant que vous n'ayez atteint le tournant, un
hurlement terrifiant retentit derrière vous et se répercute le long
du tunnel. Vous restez figé sur place, paralysé par la peur
pendant un instant, puis vous vous retournez lentement. Vous
apercevez alors avec horreur la silhouette d'un gigantesque loup
noir qui s'avance en bondissant dans votre direction. Il se
rapproche très rapidement, ses yeux rouges brillant d'une lueur
féroce et sa gueule grande ouverte laissant voir de redoutables
crocs prêts à mordre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez rester sur place pour combattre le loup vorace, rendez-vous au :"))
    st.page_link("tomes/tome7/page_8.py", label="8", icon="📄")

    st.write_stream(stream_text("Si vous préférez courir vers le tournant et fuir le plus vite possible, rendez-vous au :"))
    st.page_link("tomes/tome7/page_140.py", label="140", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
