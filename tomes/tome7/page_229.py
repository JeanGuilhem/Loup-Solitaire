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

check_inventory(current_page_number=229, book=7)

fr_text = """
Le cœur battant à tout rompre, vous courez le plus vite possible
vous mettre à l'abri au pied de la paroi rocheuse de Kazan-Oud.
Vous arrivez tout essoufflé devant le mur de pierres noires et
brillantes et vous découvrez une fissure, suffisamment grande
pour offrir un refuge. Vous vous apprêtez à pénétrer dans la
brèche lorsque vous entendez tout à coup d'étranges sifflements
qui retentissent à l'intérieur dans les ténèbres et vous font
hésiter.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous glisser dans la brèche en dépit de ces bruits inquiétants, rendez-vous au :"))
    st.page_link("tomes/tome7/page_16.py", label="16", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer à avancer le long de la plage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_173.py", label="173", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
