import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=323, book=2)

fr_text = """
Vous longez cette rue sordide qui, bientôt, tourne brusquement vers
l'est pour aboutir dans la rue de la Vigie. Au loin, vous apercevez les
eaux du Fleuve Dorn qui sépare les parties Est et Ouest de Ragadorn.
Vous poursuivez votre chemin sous la pluie battante lorsque trois
hommes d'allure louche surgissent soudain d'une ruelle et vous
emboîtent le pas.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez interrompre votre marche et affronter ces trois individus, rendez-vous au :"))
    st.page_link("tomes/tome2/page_131.py", label="131", icon="📄")
    st.write_stream(stream_text("Si vous préférez continuer à marcher, rendez-vous au :"))
    st.page_link("tomes/tome2/page_298.py", label="298", icon="📄")
    st.write_stream(stream_text("Enfin, si vous estimez plus judicieux de courir en direction du fleuve, rendez-vous au :"))
    st.page_link("tomes/tome2/page_121.py", label="121", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
