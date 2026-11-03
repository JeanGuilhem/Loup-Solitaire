import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    pickup_button,
    pickup_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=44, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Tandis que les patrouilleurs encerclent les ruines, les étrangers
tentent de s'enfuir en direction de la grand-route. Vos hommes
se lancent alors à leur poursuite et ont tôt fait de les tuer à coups
d'épée. L'un des étrangers fracasse un petit flacon en tombant.
Vous fouillez les cadavres et vous trouvez 12 Pièces d'Or et une
quantité de nourriture représentant 2 Repas. Vous remarquez
ensuite que les deux hommes portent autour du cou des
Amulettes attachées à des chaînettes. Ces Amulettes sont en bois
et représentent un poisson. Si vous souhaitez conserver une ou
plusieurs de ces trouvailles, modifiez en conséquence votre
Feuille d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_gold(12, key="gold")
    pickup_button("REPAS", key="repas_1", label="Prendre 1 Repas")
    pickup_button("REPAS", key="repas_2", label="Prendre 1 Repas")
    pickup_button("AMULETTE DE BOIS", key="amulette_1", label="Prendre une Amulette de bois")
    pickup_button("AMULETTE DE BOIS", key="amulette_2", label="Prendre une Amulette de bois")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Guérison, rendez-vous au :"))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome4/page_149.py", label="149", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_149.py", label="149", icon="📄", disabled=True)

    st.write_stream(stream_text("Sinon, rendez-vous au :"))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome4/page_188.py", label="188", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome4/page_188.py", label="188", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
