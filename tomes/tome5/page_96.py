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

check_inventory(current_page_number=96, book=5)

fr_text = """
Toute une variété de sombres immondices et d'écume écœurante
aux teintes verdâtres flottent à la surface de l'eau. Le liquide
boueux vous arrive à la taille, et lorsque vous avancez, la nappe
de détritus se déchire en laissant échapper des gaz nocifs. La
puanteur est tellement épouvantable que vous devez vous couvrir
le nez et la bouche à l'aide de votre manteau Kaï. Soudain, des
clapotements vous avertissent que les hommes de Maouk ne sont
pas loin. Mais tout à coup, votre pied se prend dans quelque
chose qui est enfoui sous la vase et, pendant quelques secondes,
vous êtes totalement pris de panique. Vous tirez sur votre jambe
pour vous dégager, mais vous êtes bel et bien coincé. Dans un
mouvement de terreur aveugle, vous donnez avec votre arme de
violents coups de lame à travers l'eau infecte, jusqu'à ce que votre
pied se trouve enfin libéré. Lorsque vous relevez votre arme, vous
vous attendez à trouver, empalée sur la pointe, quelque horrible
créature des égouts. Mais, au lieu de cela, c'est un crâne humain
que vous découvrez ! Un frisson vous parcourt l'échine et vous
vous empressez de rejeter dans l'eau puante votre macabre
trouvaille. Bientôt, le souterrain se sépare en deux : un autre
tunnel part vers l'ouest tandis que celui que vous longez continue
vers le sud. Les clapotis se rapprochent au fur et à mesure que les
hommes de Maouk gagnent du terrain sur vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez aller vers l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome5/page_135.py", label="135", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer plein sud, rendez-vous au :"))
    st.page_link("tomes/tome5/page_164.py", label="164", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
