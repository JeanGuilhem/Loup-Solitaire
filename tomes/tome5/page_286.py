import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=286, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Alors que la nuit tombe, vous entamez votre mission désespérée.
Les Giaks ne posent pratiquement pas de problème que vous ne
puissiez résoudre grâce à vos qualités de Guerrier, car ils sont
épuisés. Seuls les Drakkars montrent quelques signes de
vigilance mais, là encore, ils sont moins d'une douzaine à
patrouiller dans tout le cratère. Ce n'est donc pas avant d'avoir
atteint l'entrée principale du Tombeau que vous rencontrerez de
réelles difficultés. Non loin de vous, un Drakkar monte la garde ;
ses yeux cruels brillent derrière son masque à tête de mort en fer
mais, de temps à autre, il relâche son attention pour aller
prendre un peu d'eau dans une cruche.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez la Discipline Kaï de la Maîtrise Psychique de la Matière, rendez-vous au :"))
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("tomes/tome5/page_214.py", label="214", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_214.py", label="214", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline, rendez-vous au :"))
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("tomes/tome5/page_239.py", label="239", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_239.py", label="239", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
