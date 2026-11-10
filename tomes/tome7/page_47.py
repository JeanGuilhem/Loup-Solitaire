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

check_inventory(current_page_number=47, book=7)

fr_text = """
Vous n'êtes plus qu'à trois mètres du passage voûté lorsqu'un cri
épouvantable vous fait arrêter net. En jetant un coup d'œil par-dessus votre épaule, vous assistez à une horrible scène ; trois
créatures, pas plus grandes que des hommes, mais à la peau
luisante et bleutée, se jettent sur le guerrier et commencent à le
mettre en pièces. Le craquement des os et le bruit de la chair
déchirée à grands coups de dents et de griffes vous soulèvent le
cœur. L'horreur atteint son comble lorsque vous voyez les
membres de la malheureuse victime disparaître peu à peu dans
la gueule de ses tortionnaires. Après avoir mastiqué les reliefs de
leur proie avec une évidente délectation, les trois monstres
anthropophages vous regardent de leurs petits yeux injectés de
sang. Saisi d'une terreur aveugle, vous partez comme une flèche
et vous vous enfoncez dans les ténèbres du passage voûté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome7/page_277.py", label="277", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
