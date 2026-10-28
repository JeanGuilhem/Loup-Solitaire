import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_flag,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=151, book=3)

fr_text = """
La bête hideuse meurt à vos pieds tandis que Dyce vous crie : «
Vite, il faut partir d'ici, les Languabarbs ne chassent jamais seuls
et d'autres ne vont pas tarder à arriver. » Vous ramassez alors
votre Sac à Dos et vous suivez Dyce et Irian le long d'un chemin
escarpé qui grimpe à flanc de montagne. Mais à peine avez-vous
parcouru une cinquantaine de mètres qu'une catastrophe se
produit. Aveuglé par l'obscurité et le vent glacial, Dyce ne
s'aperçoit pas que le chemin aboutit brusquement à un précipice.
Saisi d'horreur, vous entendez vos guides pousser des
hurlements qui s'évanouissent peu à peu, au fur et à mesure de
leur longue chute dans les ténèbres. La mort vous menace de
tous côtés et vous vous accrochez désespérément à la paroi
rocheuse pour essayer de survivre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous vous êtes enduit le corps d'huile de Bakanal, rendez-vous au :"))
    if has_flag("huile de Bakanal"):
        st.page_link("tomes/tome3/page_209.py", label="209", icon="📄")
    else:
        st.write_stream(stream_text("Vous ne vous êtes pas enduit d'huile de Bakanal."))
        st.page_link("tomes/tome3/page_209.py", label="209", icon="📄", disabled=True)
    st.write_stream(stream_text('Dans le cas contraire, rendez-vous au :'))
    st.page_link("tomes/tome3/page_339.py", label="339", icon="📄", disabled=has_flag("huile de Bakanal"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
