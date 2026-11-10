import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    confiscate_equipment,
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

check_inventory(current_page_number=335, book=7)

fr_text = """
Une créature bossue et rachitique, enveloppée dans un habit à
capuchon, s'approche de l'endroit où vous êtes attaché. Elle vous
débarrasse prestement de toutes vos armes et les remet à un nain
affreux qui se tient à côté d'elle. Il regarde le Glaive de Sommer
en connaisseur, puis le brandit au-dessus de sa tête pour le
montrer à son maître. Avant qu'il ne puisse parler, vous entendez
un craquement sonore, et un éclair d'énergie dorée enveloppe la
garde de l'épée. Le nain laisse tomber celle-ci en hurlant de
douleur : la décharge lui a arraché la moitié des doigts. Vous
réprimez difficilement un sourire et vous êtes aussitôt puni de
votre insolence. La créature vous frappe au visage avec son poing
rugueux et couvert de verrues. (Vous perdez 1 point
d'ENDURANCE.) « Emmenez-le au labyrinthe ! ordonne Zahda,
le seigneur aux cheveux blancs. Et gardez-moi l'épée. » Le Glaive
de Sommer s'élève alors dans l'air et flotte sur un coussin de
brouillard bleu en avançant vers le trône doré. Le rire cruel et
sarcastique de Zahda retentit dans la galerie et, tandis que l'on
vous emmène, enchaîné, vers le labyrinthe, vous craignez que
votre quête ne soit vouée à l'échec. Effacez toutes les Armes ou ce
qui peut servir d'arme, ainsi que tous les Objets Spéciaux de
votre Feuille d'Aventure mais notez-les sur une feuille de papier
à part au cas où vous les retrouveriez à un stade ultérieur de
votre aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
        # armes et Objets Spéciaux confisqués, peut-être retrouvés plus tard
        confiscate_equipment(backpack=False, gold=False)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)
    st.warning("Vos Armes et vos Objets Spéciaux vous ont été pris : ils sont mis de côté au cas où vous les retrouveriez.")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_286.py", label="286", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
