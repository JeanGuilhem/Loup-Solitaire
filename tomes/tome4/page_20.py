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

check_inventory(current_page_number=20, book=4)

fr_text = """
Une flèche siffle au-dessus de votre tête et un cri de douleur
retentit aussitôt. L'arc glisse des mains de l'archer qui s'affaisse
sur les genoux, une flèche enfoncée entre ses deux yeux
stupéfaits. Des halètements et des bruits de pas feutrés vous
indiquent que les Chiens de Guerre se rapprochent. En levant le
regard, vous voyez un homme courir vers vous en provenance de
la barricade. Il porte un bouclier dans une main et un arc dans
l'autre. C'est le capitaine Gayal. Il vous rejoint, le souffle court, et
saisit une flèche dans son carquois. Puis il vise et tire, prenant
une autre flèche dès que la première a été lâchée. Autour de vous,
les Chiens de Guerre trébuchent et s'effondrent sur le sol,
transpercés par les flèches mortelles du capitaine Gayal. Dix
cadavres restent ainsi étendus sur le terrain avant que son
carquois ne soit vide. Le capitaine vous saisit alors par le bras
puis, vous hissant sur son épaule d'un seul geste rapide, il vous
ramène en direction de la barricade. D'autres soldats se
précipitent pour vous aider, mais les brigands se sont rapprochés
et vos compatriotes se trouvent contraints de reculer sous une
pluie de flèches. Les projectiles rouges de l'ennemi sifflent de
tous côtés. Vous atteignez la barricade, l'un des chariots est
repoussé et vous franchissez ainsi la ligne de défense, toujours
porté par le capitaine Gayal proche de l'épuisement. Il titube et
ses soldats se ruent sur lui pour le retenir au moment où il
s'effondre sur le sol.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_341.py", label="341", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
