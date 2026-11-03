import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=3, book=4)

fr_text = """
Vous montez sur la barricade et vous lancez un ordre : « Tendez
les arcs ! » puis, tandis que le mur de boucliers de l'ennemi
s'avance en une course mortelle, vous ordonnez à vos archers de
tirer. Les boucliers de bois et de peau de vos ennemis ne suffisent
pas à les protéger de cette pluie de flèches qui s'abat sur eux. Ils
s'immobilisent et semblent vaciller, de larges brèches s'ouvrant
dans leurs rangs, tandis que les lanciers s'effondrent par dizaines
sur le sol. Rares sont ceux qui n'ont pas été blessés. Vous sentez
alors que le vent de la bataille a tourné. Les soldats ennemis
battent en retraite, portant leurs blessés à dos d'homme ou sur
leur bouclier retourné. Vous sautez à bas de la barricade et vous
vous précipitez vers la tour de guet où le capitaine Gayal, dans un
combat acharné, est toujours aux prises avec des brigands à
cheval. Vous vous apprêtez à enjamber le corps d'un des bandits,
apparemment mort, lorsque celui-ci se relève à cet instant et
vous porte un coup aux jambes à l'aide d'une masse d'armes.
Cette attaque surprise vous projette à terre et vous fait perdre 1
point d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_62.py", label="62", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
