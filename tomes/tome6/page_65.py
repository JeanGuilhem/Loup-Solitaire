import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    pickup_button,
    show_illustrations,
    show_map,
    use_arrow,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=65, book=6)

fr_text = """
Avec un cri à vous glacer le sang, le Yamsark s'élance droit sur
vous du haut de l'escalier. Courageusement, vous l'attendez de
pied ferme, prêt à lui décocher un coup mortel. Votre Arc tendu
à rompre laisse partir la flèche qui atteint la créature en
pleine poitrine. Quelques instants après, le corps du Yamsark
s'effondre lourdement au bas des marches et vous faites un bond
pour ne pas être écrasé sous son poids. L'ignoble bête est
secouée de spasmes pendant une ou deux minutes, puis elle
succombe enfin. Remerciant le ciel d'être encore en vie, vous
retournez à la chapelle et vous remplissez votre flacon d'Eau de
Taunor. (Vous en recueillez suffisamment pour gagner 6 points
d'ENDURANCE.) Vous pouvez boire cette eau aux vertus
régénérantes dès maintenant, ou bien la conserver dans votre Sac
à Dos pour l'utiliser plus tard ; dans ce cas, inscrivez-la sur
votre Feuille d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        use_arrow()

    # boire l'Eau de Taunor tout de suite ou la garder dans le Sac à Dos (l'un ou l'autre)
    drunk = st.session_state.get("visibility_t6_65_eau", False)
    if st.button("Boire l'Eau de Taunor (+6 ENDURANCE)", key="t6_65_boire", disabled=drunk):
        st.session_state["visibility_t6_65_eau"] = True
        change_endurance(6)
        st.rerun()
    pickup_button("EAU DE TAUNOR", key="t6_65_eau", label="Garder l'Eau de Taunor dans le Sac à Dos")

    st.write_stream(stream_text("A présent, si vous voulez inspecter la chapelle plus attentivement, rendez-vous au :"))
    st.page_link("tomes/tome6/page_24.py", label="24", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller rejoindre Cyrilus sans plus tarder, rendez-vous au :"))
    st.page_link("tomes/tome6/page_338.py", label="338", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
