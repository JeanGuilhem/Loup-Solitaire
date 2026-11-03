import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=344, book=4)

fr_text = """
Votre coup a fait voler en éclats la lance du cavalier. Il tire alors
sur ses rênes, se débarrasse de son arme brisée et dégaine un
cimeterre. Avec un sourire diabolique qui découvre deux rangées
de dents noires et pointues, il lance un cri de guerre en
éperonnant son cheval qui se précipite à nouveau sur vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous avez atteint le rang Kaï d'Aspirant (ou un rang supérieur), rendez-vous au :"))
    if kai_rank() >= 6:
        st.page_link("tomes/tome4/page_111.py", label="111", icon="📄")
    else:
        st.write_stream(stream_text("Vous n'avez pas atteint le rang Kaï d'Aspirant."))
        st.page_link("tomes/tome4/page_111.py", label="111", icon="📄", disabled=True)

    st.write_stream(stream_text("Sinon, rendez-vous au :"))
    if kai_rank() >= 6:
        st.page_link("tomes/tome4/page_43.py", label="43", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome4/page_43.py", label="43", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
