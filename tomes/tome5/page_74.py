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

check_inventory(current_page_number=74, book=5)

fr_text = """
Grâce à votre maîtrise de la Discipline Kaï de l'Orientation, vous
savez maintenant que la porte ouest donne sur l'Armurerie du
Palais.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez entrer par cette porte, rendez-vous au :"))
    st.page_link("tomes/tome5/page_44.py", label="44", icon="📄")

    st.write_stream(stream_text("Si vous préférez éviter l'Armurerie et quitter la pièce dans laquelle vous vous trouvez par la porte nord, rendez-vous au :"))
    st.page_link("tomes/tome5/page_167.py", label="167", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
