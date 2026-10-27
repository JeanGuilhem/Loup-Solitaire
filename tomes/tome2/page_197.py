import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=197, book=2)

fr_text = """
Lorsque l'aube paraît, une terrible tempête se lève sur la mer et vous
êtes réveillé par le violent roulis du navire. Le plancher de votre cabine
est inondé et les hurlements du vent laissent à peine percevoir de
temps à autre les cris de l'équipage. Vous vous habillez en hâte, vous
rassemblez vos affaires et vous montez sur le pont. Le capitaine vous
rejoint bientôt ; il vous prend par le bras et vous donne l'ordre de
retourner dans votre cabine. Vous revenez donc sur vos pas, mais
soudain un craquement effroyable retentit ; vous levez la tête : la partie
supérieure du grand mât vient de se rompre dans la tourmente et tombe
droit sur vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Utilisez la Table de Hasard pour obtenir un chiffre. Entre 1 et 4, rendez-vous au 78. "
            "Entre 5 et 9, rendez-vous au 141. Enfin, si vous tirez le 0, rendez-vous au 247."
        )
    )
    number = hazard_roll()
    if number is not None and 1 <= number <= 4:
        st.page_link("tomes/tome2/page_78.py", label="78", icon="📄")
    elif number is not None and 5 <= number <= 9:
        st.page_link("tomes/tome2/page_141.py", label="141", icon="📄")
    elif number is not None and number == 0:
        st.page_link("tomes/tome2/page_247.py", label="247", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
