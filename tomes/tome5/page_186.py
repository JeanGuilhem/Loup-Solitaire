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

check_inventory(current_page_number=186, book=5)

fr_text = """
Vous utilisez votre Discipline Kaï pour dissimuler votre accent du
Sommerlund et vous criez au Garde : « Vite ! à l'aide, l'Homme
du Nord est en train de s'échapper ! » Aussitôt, le Garde se met
en mouvement et monte l'escalier quatre à quatre vers la porte.
Vous attendez qu'il arrive à la dernière marche avant d'attaquer.
Un coup au genou l'envoie rouler au pied des marches. Vous
descendez dans la pièce, prêt à frapper de nouveau au cas où le
Garde reprendrait connaissance. Précaution inutile car le Garde
est, cette fois-ci, bel et bien mort. Dans sa chute, il s'est brisé la
nuque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous désirez fouiller son cadavre, rendez-vous au :'))
    st.page_link("tomes/tome5/page_52.py", label="52", icon="📄")

    st.write_stream(stream_text("Si vous préférez laisser le corps et inspecter l'Armurerie, rendez-vous au :"))
    st.page_link("tomes/tome5/page_140.py", label="140", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
