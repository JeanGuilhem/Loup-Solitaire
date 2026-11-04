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

check_inventory(current_page_number=285, book=5)

fr_text = """
Tandis que vous fuyez à toutes jambes, un mugissement de haine
et de rage emplit le hall. « Tuez-le ! » En jetant un bref coup
d'œil par-dessus votre épaule, vous voyez que les Drakkars sont
en train de dégainer leurs noires épées, impatients d'exécuter les
ordres de leur maître. Vous dévalez alors rapidement les
quelques marches qui descendent sous un porche, puis vous
longez un balcon qui surplombe le Palais inférieur. L'Akataz vous
a presque rejoint et vous pouvez sentir son haleine fétide sur vos
jambes. Mais, à l'instant même où il se jette sur vous, vous faites
instinctivement un saut de côté et l'animal va s'écraser la gueule
la première sur un pilier de marbre. Vous bondissez pour lui
donner le coup de grâce et l'Akataz laisse échapper un long râle
de douleur : il n'attaquera plus jamais. C'est alors que vous
apercevez la silhouette inquiétante du Seigneur des Ténèbres
Haakon dans le hall du bas, brandissant son poing clouté. Par
ailleurs, semblant surgir de nulle part, un Drakkar s'avance en
levant son épée au-dessus de son heaume à tête de mort.
Soudain, dans un sifflement assourdissant, un éclair bleu jaillit
d'une petite pierre que le Seigneur des Ténèbres tient à la main.
Son rayon se dirige droit sur vous. Simultanément, le Drakkar
s'élance et parvient à vous blesser au bras (vous perdez 2 points
d'ENDURANCE). Mais il se trouve maintenant sur la trajectoire
du rayon. En un éclair, le Drakkar disparaît, ne laissant de lui
que des cendres et une odeur âcre de chair brûlée. Au bout du
balcon se trouvent une autre arche et un escalier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Si vous souhaitez vous évader par l'arche, rendez-vous au :"))
    st.page_link("tomes/tome5/page_381.py", label="381", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous échapper par l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome5/page_317.py", label="317", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
