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

check_inventory(current_page_number=345, book=5)

fr_text = """
Dans le hall en dessous, vous entr'apercevez la silhouette du
Seigneur des Ténèbres Haakon qui brandit son poing clouté dans
votre direction. Un éclair bleu jaillit d'une pierre qu'il tient au
creux de la main et se dirige sur vous dans un fracas
assourdissant. Vous plongez à l'abri derrière le corps du guerrier
Drakkar, mais celui-ci disparaît instantanément, ne laissant de
lui qu'une odeur de chair brûlée et quelques cendres lorsque le
rayon explose à son contact. Vous vous relevez rapidement et
vous courez le long du passage. Un autre éclair jaillit et va
heurter le plafond. Des éclats de marbre, tranchants comme des
lames de rasoir, tombent en sifflant autour de vous et déchirent
votre manteau et votre tunique. Vous descendez quelques
marches sous un passage voûté puis vous longez un balcon qui
surplombe la partie inférieure du Palais. C'est alors que vous entendez les cloches carillonner, puis le martèlement
assourdissant de bottes ferrées : le Zakhan a sonné l'alarme et les
Gardes se précipitent de tous côtés. Au bout du balcon, il y a une
autre arche et un escalier ; tous deux semblent déserts.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous échapper en passant sous l'arche, rendez-vous au :"))
    st.page_link("tomes/tome5/page_381.py", label="381", icon="📄")

    st.write_stream(stream_text('Si vous préférez grimper rapidement les marches, rendez-vous au :'))
    st.page_link("tomes/tome5/page_317.py", label="317", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
