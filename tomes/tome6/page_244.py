import streamlit as st
from inventory import (
    check_inventory,
    clear_flag,
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

check_inventory(current_page_number=244, book=6)

fr_text = """
Votre cheval est tué instantanément par la pluie de flèches qui
s'abat sur lui. Il s'écroule au sol, et vous êtes projeté en avant,
pirouettant dans les airs avant d'atterrir comme une masse sur la
terre pleine de sang. Les archers ont massacré les deux premiers
rangs de cavaliers, mais le reste de la troupe continue à attaquer
et se rue vers la porte en piétinant cadavres et blessés dans un
assaut désespéré. Vous vous trouvez à présent allongé sur le
pont, à quelques mètres des cavaliers.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # Fait effacé : « cheval » (votre cheval est tué)
    if is_new_page():
        clear_flag("cheval")

    st.write_stream(stream_text("Si vous souhaitez enjamber le parapet pour éviter les chevaux lancés au grand galop, rendez-vous au :"))
    st.page_link("tomes/tome6/page_38.py", label="38", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous rouler en boule et demeurer immobile, rendez-vous au :"))
    st.page_link("tomes/tome6/page_218.py", label="218", icon="📄")

    st.write_stream(stream_text("Enfin, si vous préférez courir à toutes jambes vers la porte de Tekaro, rendez-vous au :"))
    st.page_link("tomes/tome6/page_329.py", label="329", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
