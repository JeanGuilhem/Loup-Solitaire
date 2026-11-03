import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    choose_item_to_lose,
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

check_inventory(current_page_number=272, book=4)

fr_text = """
Vous heurtez un gros rocher qui émerge de la rivière. Fort
heureusement, ce sont vos pieds (et non votre tête) qui ont
encaissé le choc. Vous êtes submergé cependant par l'eau
bouillonnante qui vous remplit le nez et les oreilles. Les rapides
vous emportent, vous êtes roulé en tous sens, les yeux vous
piquent et la douleur que le choc a provoquée dans vos jambes se
répand dans tout votre corps. L'arête pointue d'un rocher déchire
la manche de votre tunique et vous meurtrit le bras. Votre arme
vous échappe des mains. Vous êtes ensuite projeté dans une
sorte de torrent aux berges en forme de V et vous plongez cul
par-dessus tête dans les profondeurs d'une vaste étendue d'eau.
Tandis que vous vous enfoncez dans les flots sombres et agités de
remous, vous perdez rapidement connaissance, sombrant dans
un engourdissement aveugle et silencieux. Lorsque vous ouvrez à
nouveau les yeux, le soleil est en train de se coucher. Vous êtes
échoué sur une berge de la rivière près d'un sentier forestier au
tracé sinueux. Les contours de la chaîne de Maaken se dessinent
à l'est et vous en concluez que vous avez dû être emporté par le
courant sur plusieurs kilomètres. Vous venez de survivre à une
terrible épreuve qui aurait eu raison sans nul doute d'un mortel
ordinaire. Vous avez perdu 5 points d'ENDURANCE en raison
des blessures infligées à vos jambes et à votre tête. Vous avez
également perdu une arme. En revanche, tous vos Objets
Spéciaux, les objets contenus dans votre Sac à Dos et vos Pièces
d'Or, sont intacts.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-5)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-5)
    if choose_item_to_lose(list(st.session_state.weapons), key="arme_perdue", label="Choisissez l'arme qui vous échappe :"):
        st.write_stream(stream_text("Apportez les modifications nécessaires à votre Feuille d'Aventure, puis rendez-vous au :"))
        st.page_link("tomes/tome4/page_79.py", label="79", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
