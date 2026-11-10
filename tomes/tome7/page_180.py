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

check_inventory(current_page_number=180, book=7)

fr_text = """
Vous concentrez tout le pouvoir que vous confère votre
Discipline Magnakaï puis, après avoir pris une profonde
inspiration, vous poussez un cri aigu et continu. Bientôt des
gouttes de sueur perlent sur votre front alors que vous haussez le
ton à un point tel que votre cri en devient inaudible. Soudain, les
chauves-souris se mettent à crier à l'unisson. Elles tournent et
virevoltent en tous sens, s'assommant contre les murs, les sens
paralysés par votre hurlement. Les rares survivantes s'enfuient
en tournoyant dans l'obscurité. Vous cessez de crier et, après
avoir repris votre souffle, descendez rapidement l'escalier. (Si
vous avez utilisé la Discipline Magnakaï du Foudroiement
Psychique, ne déduisez aucun point de votre total
d'ENDURANCE.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_236.py", label="236", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
