import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=106, book=6)

fr_text = """
Vous vous extirpez péniblement de sous la lourde masse du
monstre. Vous avez quelques côtes enfoncées et une longue
estafilade à la nuque mais, au moins, vous êtes encore en vie !
Vous remontez lentement l'escalier et vous retournez à la
chapelle pour y remplir votre flacon d'Eau de Taunor. Grâce aux
vertus curatives de cette eau, vous pourrez regagner 6 points
d'ENDURANCE. Vous pouvez la boire dès à présent ou bien la
conserver pour une utilisation future. (Dans ce cas, inscrivez
l'Eau de Taunor et ses propriétés dans la case Sac à Dos de
votre Feuille d'Aventure.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("EAU DE TAUNOR", key="taunor", label="Remplir votre flacon d'Eau de Taunor")
    st.caption("Vous pouvez la boire dès maintenant depuis l'onglet Inventaire (6 points d'ENDURANCE).")

    st.write_stream(stream_text("Maintenant, si vous souhaitez inspecter la chapelle plus attentivement, rendez-vous au :"))
    st.page_link("tomes/tome6/page_24.py", label="24", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller rejoindre Cyrilus sans plus tarder, rendez-vous au :"))
    st.page_link("tomes/tome6/page_338.py", label="338", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
