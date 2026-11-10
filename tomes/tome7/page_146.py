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

check_inventory(current_page_number=146, book=7)

fr_text = """
La première chose qui vous frappe, c'est que le guerrier ne porte
aucune trace de blessure : son armure est intacte, sans aucun
coup d'épée ni perforation de flèche. Si ce n'était l'odeur
caractéristique de la mort qui l'enveloppe, vous pourriez croire
que l'homme est tout bonnement endormi. Vous retournez le
corps sur le dos pour examiner le visage, et vous recevez un rude
choc en le voyant. L'homme n'a plus d'yeux - seulement deux
trous noirs qui s'enfoncent dans sa tête -, sa langue violacée pend
mollement et, à la commissure de ses lèvres crispées en un
affreux rictus, vous voyez s'écouler un liquide verdâtre et épais.
Réprimant à grand-peine la nausée qui s'empare de vous, vous
vous écartez vivement du cadavre et vous entrez dans le passage secret.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_11.py", label="11", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
