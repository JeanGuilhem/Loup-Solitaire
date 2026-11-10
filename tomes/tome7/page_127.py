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

check_inventory(current_page_number=127, book=7)

fr_text = """
Vous franchissez la dalle de pierre d'un bond, puis vous repartez
en courant le long du tunnel. Un vent chaud et humide, chargé
de vapeurs sulfureuses et de relents de pourriture, vous souffle
sur le visage. Vous continuez à progresser pendant plus d'une
heure, sautant par-dessus les nombreuses failles qui déchirent le
sol inégal et prenant garde à ne pas marcher sur les gros vers
bleu de nuit qui grouillent à votre approche pour se faufiler dans
les fissures du rocher, quand le faisceau de votre lumière vient
troubler les ténèbres de leur monde souterrain. Finalement, le
tunnel débouche sur une pièce de forme ovale. Un escalier orné
de toiles d'araignées monte vers une trappe encastrée dans le
plafond. La lueur familière du bouclier de protection filtre à
travers elle. En bas des marches, vous découvrez les restes d'un
corps en armure. Le cadavre tient encore dans sa main osseuse
une vieille épée rouillée, et un poignard à manche d'os est
enfoncé à la base de son cou.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez monter l'escalier pour aller ouvrir la trappe, rendez-vous au :"))
    st.page_link("tomes/tome7/page_93.py", label="93", icon="📄")

    st.write_stream(stream_text("Si vous préférez examiner le cadavre de plus près, rendez-vous au :"))
    st.page_link("tomes/tome7/page_199.py", label="199", icon="📄")

    st.write_stream(stream_text("Si vous jugez plus sage de quitter la pièce et de poursuivre le long du tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_318.py", label="318", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
