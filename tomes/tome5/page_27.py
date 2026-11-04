import streamlit as st
from inventory import (
    buy_button,
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

check_inventory(current_page_number=27, book=5)

fr_text = """
Chacune des trois bouteilles porte une étiquette écrite à la main à
l'encre verte.
Huile de Larnuma (qui vous fera gagner 2 points d'ENDURANCE par dose) : 3 Pièces d'Or.
Potion de Laumspur (qui vous fera gagner 4 points d'ENDURANCE par dose) : 5 Pièces d'Or.
Élixir de Rendalim (qui vous fera gagner 6 points d'ENDURANCE par dose) : 7 Pièces d'Or.
Parmi ces potions vous pouvez acheter celles de votre choix. Le
prix indiqué est celui d'une dose et ces potions devront être
inscrites sur votre Feuille d'Aventure dans la case Sac à Dos.
"""

fr_text_2 = """
L'herboriste vous mène ensuite jusqu'à une porte latérale et elle
vous dit : « Je sais combien vous êtes désespéré, Homme du
Nord, et j'espère de tout mon cœur que vous saurez trouver le
remède qui vous guérira. » Alors que vous vous apprêtez à partir,
elle vous donne un dernier conseil : « Il est possible de soudoyer
les Gardes qui surveillent la porte nord du Grand Palais. » Après
l'avoir remerciée, vous vous engagez dans l'allée qui longe son
magasin et vous vous éloignez.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    buy_button("HUILE DE LARNUMA", 3, key="larnuma_1", label="Acheter une dose d'Huile de Larnuma (3 Pièces d'Or)")
    buy_button("HUILE DE LARNUMA", 3, key="larnuma_2", label="Acheter une deuxième dose d'Huile de Larnuma (3 Pièces d'Or)")
    buy_button("HUILE DE LARNUMA", 3, key="larnuma_3", label="Acheter une troisième dose d'Huile de Larnuma (3 Pièces d'Or)")
    buy_button("POTION DE LAUMSPUR", 5, key="laumspur_1", label="Acheter une dose de Potion de Laumspur (5 Pièces d'Or)")
    buy_button("POTION DE LAUMSPUR", 5, key="laumspur_2", label="Acheter une deuxième dose de Potion de Laumspur (5 Pièces d'Or)")
    buy_button("POTION DE LAUMSPUR", 5, key="laumspur_3", label="Acheter une troisième dose de Potion de Laumspur (5 Pièces d'Or)")
    buy_button("ÉLIXIR DE RENDALIM", 7, key="rendalim_1", label="Acheter une dose d'Élixir de Rendalim (7 Pièces d'Or)")
    buy_button("ÉLIXIR DE RENDALIM", 7, key="rendalim_2", label="Acheter une deuxième dose d'Élixir de Rendalim (7 Pièces d'Or)")
    buy_button("ÉLIXIR DE RENDALIM", 7, key="rendalim_3", label="Acheter une troisième dose d'Élixir de Rendalim (7 Pièces d'Or)")

    st.write(fr_text_2)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_160.py", label="160", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
