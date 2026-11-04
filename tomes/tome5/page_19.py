import streamlit as st
from inventory import (
    check_inventory,
    choose_item_to_lose,
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

check_inventory(current_page_number=19, book=5)

fr_text = """
Vous rabattez le capuchon de votre manteau Kaï afin que votre
visage reste dans l'ombre tandis que vous vous approchez des
Gardes. Ceux-ci vous observent avec méfiance, mais vous
maîtrisez parfaitement leur langue et vous réussissez à endormir
leurs soupçons. Vous prétendez être un commerçant dont les
biens ont été confisqués, et vous demandez à être entendu pour
défendre votre cause à la Cour de Justice de Barrakeesh. A ces
mots, les Gardes se mettent à ricaner entre eux, puis ils vous
réclament deux objets de votre Sac à Dos avant de vous accorder
la permission d'entrer au Grand Palais. Ils échangent ensuite un
clin d'œil complice, car ils savent pertinemment qu'on ne restitue
jamais les marchandises confisquées et que vous serez jeté en
prison pour votre impertinence, comme tous ceux qui ont essayé,
avant vous, de réclamer justice.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous acceptez de donner aux Gardes ce qu'ils exigent, rayez sur votre Feuille d'Aventure deux objets de votre Sac à Dos (excepté les Repas). Vous pouvez maintenant franchir la porte et entrer dans les jardins du Palais. Rendez-vous au :"))
    offerable = [item for item in st.session_state.backpack if item != "REPAS"]
    if st.session_state.get("visibility_bribe"):
        if choose_item_to_lose(offerable, key="bribe_1", label="Premier objet donné aux Gardes :"):
            offerable = [item for item in st.session_state.backpack if item != "REPAS"]
            if choose_item_to_lose(offerable, key="bribe_2", label="Second objet donné aux Gardes :"):
                st.page_link("tomes/tome5/page_137.py", label="137", icon="📄")
    else:
        if st.button("Donner deux objets aux Gardes", disabled=len(offerable) < 2):
            st.session_state.visibility_bribe = True
            st.rerun()
        if len(offerable) < 2:
            st.write_stream(stream_text("Vous n'avez pas deux objets à donner (hors Repas)."))
        st.page_link("tomes/tome5/page_137.py", label="137", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous ne voulez pas - ou si vous ne pouvez pas - donner aux Gardes deux objets de votre Sac à Dos, vous devez quitter les lieux et essayer de trouver un autre moyen de pénétrer dans le Palais. Rendez-vous au :'))
    st.page_link("tomes/tome5/page_49.py", label="49", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
