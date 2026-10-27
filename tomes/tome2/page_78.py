import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=78, book=2)

fr_text = """
Vous faites un bond en arrière, juste à temps pour éviter d'être écrasé
par le mât qui s'abat sur le pont en passant au travers. Vous vous
relevez en chancelant et vous examinez les débris de bois. Le corps
sans vie du capitaine Kelman est coincé sous le mât brisé. Vous
contemplez ce spectacle d'un regard horrifié lorsque soudain la tempête
ouvre une large brèche dans la coque déjà endommagée du Sceptre
Vert. Et tandis que le navire se disloque, vous êtes projeté par-dessus le
bastingage et vous tombez dans les flots déchaînés. A moitié étouffé,
vous parvenez tant bien que mal à remonter à la surface pour prendre
une bouffée d'air, et votre tête heurte alors un panneau d'écoutille. Vous
perdez un point d'ENDURANCE et vous vous hissez sur ce radeau de
fortune. Si vous portez une cotte de mailles, il faut vous en débarrasser,
sinon, vous risquez de périr noyé. Rayez-la de votre Feuille d'Aventure.
Dans la lumière grise de la tourmente, vous contemplez la coque brisée
du navire qui sombre dans la mer. Vous êtes alors pris de vertige, vous
vous sentez mal et vous vous cramponnez de toutes vos forces au
panneau d'écoutille, mais peu à peu votre corps faiblit et vous perdez
conscience. Lorsque, enfin, vous vous réveillez, la tempête s'est
calmée. Il ne reste plus du Sceptre Vert que le panneau d'écoutille sur
lequel vous êtes toujours étendu. A en juger par la position du soleil,
l'après-midi touche à sa fin. Au loin, vous apercevez un petit bateau de
pêche et au-delà, la côte qui s'étend à l'horizon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
        remove_from_inventory("COTTE DE MAILLES")
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(
        stream_text(
            "Si vous voulez essayer de signaler votre présence au bateau de pêche en agitant votre "
            "cape, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_278.py", label="278", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez ne pas vous occuper du bateau et tenter de rejoindre la côte en pagayant "
            "à l'aide de vos seules mains, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_337.py", label="337", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
