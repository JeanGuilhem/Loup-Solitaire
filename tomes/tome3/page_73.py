import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=73, book=3)

fr_text = """
Les guides vous regardent comme si vous étiez fou et refusent de
vous accompagner. Tout d'abord, les chiens Kanu sont réticents
lorsque vous approchez de la gorge, mais en les encourageant à
l'aide de quelques bons coups de fouet, vous parvenez à les faire
changer d'avis. Il y a moins de 15 centimètres de glace de chaque
côté des patins de votre traîneau et vous avez besoin de toute
votre concentration pour vous maintenir au centre de ce pont
gelé. Vous êtes parvenu à moins de 5 mètres du bord opposé
quand soudain un terrible craquement retentit. Le traîneau est
alors violemment secoué.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll()
    if roll is not None and roll <= 7:
        st.write_stream(stream_text("Vous avez tiré un chiffre entre 0 et 7, rendez-vous au :"))
        st.page_link("tomes/tome3/page_119.py", label="119", icon="📄")
    elif roll is not None:
        st.write_stream(stream_text("Vous avez tiré le 8 ou le 9, rendez-vous au :"))
        st.page_link("tomes/tome3/page_136.py", label="136", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
