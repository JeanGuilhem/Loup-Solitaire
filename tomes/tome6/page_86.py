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

check_inventory(current_page_number=86, book=6)

fr_text = """
Vous arrachez la bourse des mains du voleur et vous la replacez
dans la poche du soldat inconscient. De nombreux blessés ont été
témoins de votre geste et, à leurs yeux, vous devenez un
véritable héros. Par ailleurs, grâce à votre maîtrise de la
Discipline Magnakaï de la Science Médicale, vous utilisez vos
talents de guérisseur pour soigner les blessures de ces
malheureux. Et cela ne fait, bien entendu, qu'accroître leur
estime envers vous. Pour vous remercier de vos bienfaits, ils se
déclarent prêts à vous aider, dans la limite de leurs pouvoirs.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez leur demander s'il existe un moyen de pénétrer discrètement dans Tekaro, rendez-vous au :"))
    st.page_link("tomes/tome6/page_109.py", label="109", icon="📄")

    st.write_stream(stream_text("Si vous préférez partir sans leur demander quoi que ce soit, rendez-vous au :"))
    st.page_link("tomes/tome6/page_70.py", label="70", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
