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

check_inventory(current_page_number=102, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vos hommes tirent leurs épées et s'approchent des étrangers. Les
deux personnages encapuchonnés lèvent immédiatement les
mains et sortent du dôme de marbre. L'un d'eux laisse tomber un
petit flacon de terre cuite rempli d'un liquide clair ; le flacon se
brise sur le sol de pierre. En fouillant les deux hommes, vous
trouvez 12 Couronnes d'Or et des vivres équivalents à 2 Repas.
Inscrivez-les sur votre Feuille d'Aventure si vous souhaitez les
conserver. Les deux étrangers portent autour du cou des
Amulettes de bois représentant un petit poisson.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_gold(12, key="gold")
    pickup_button("REPAS", key="repas_1", label="Prendre 1 Repas")
    pickup_button("REPAS", key="repas_2", label="Prendre 1 Repas")

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï de la Guérison, rendez-vous au :'))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome4/page_19.py", label="19", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_19.py", label="19", icon="📄", disabled=True)

    st.write_stream(stream_text('Sinon, rendez-vous au :'))
    st.page_link("tomes/tome4/page_339.py", label="339", icon="📄", disabled=has_kai("La Guérison"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
