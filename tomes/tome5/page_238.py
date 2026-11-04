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

check_inventory(current_page_number=238, book=5)

fr_text = """
Vous fuyez le lieu du combat et vous courez vers le passage
opposé, mais vos ennemis vous donnent la chasse et le bruit de
leurs bottes ferrées résonne à vos oreilles. Vous dévalez l'escalier,
passez sous un porche d'argent et longez un balcon surplombant
le Palais inférieur. Dans le hall, au-dessous de vous, vous
apercevez la silhouette de Haakon brandissant le poing. Un
Drakkar, surgissant de nulle part, se jette sur vous, son épée
levée au-dessus de son heaume en forme de tête de mort.
Soudain, il se produit un craquement assourdissant ; une gerbe
d'étincelles bleues jaillit d'une pierre que le Seigneur des
Ténèbres tient à la main et dirige droit vers vous. Le Drakkar se
précipite sur vous et vous blesse au bras (vous perdez 1 point
d'ENDURANCE), mais il se trouve maintenant sur la trajectoire
du rayon de Haakon. Après un éclair aveuglant, il ne reste plus
de lui qu'un tas de cendres et une âcre odeur de chair roussie. Au
bout du balcon, vous apercevez un autre porche et un escalier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text("Si vous souhaitez vous enfuir par le porche, rendez-vous au :"))
    st.page_link("tomes/tome5/page_381.py", label="381", icon="📄")

    st.write_stream(stream_text("Si vous souhaitez fuir par l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome5/page_317.py", label="317", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
