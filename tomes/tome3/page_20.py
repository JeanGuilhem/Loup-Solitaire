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

check_inventory(current_page_number=20, book=3)

fr_text = """
Le corps du Monstre d'Enfer bouillonne et se dissout à vos pieds,
un gaz vert et fétide s'échappant de ses vêtements. Tandis que
vous contemplez avec dégoût la décomposition du cadavre, vous
comprenez soudain que l'immonde créature a probablement été
envoyée pour tuer Vonotar ; il ne peut y avoir d'autre raison
plausible à sa présence ici. Les Maîtres des Ténèbres de
Helgedad veulent à tout prix la mort de Vonotar pour lui faire
payer sa défaite dans la bataille du golfe de Holm, et sans doute
ont-ils appris où il se trouvait à présent. Le mage, après avoir
découvert le Monstre de l'Enfer, l'a vraisemblablement enfermé
dans un pentacle en attendant de mettre au point un moyen de le
détruire à tout jamais. Vous tâtez prudemment votre gorge
blessée et vous remerciez les dieux d'avoir en votre possession le
Glaive de Sommer : une fois de plus, ses pouvoirs vous ont sauvé
la vie. Empruntant le couloir principal, vous vous hâtez de vous
éloigner de ces restes fumants.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_254.py", label="254", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
