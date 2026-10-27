import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=211, book=2)

fr_text = """
« Le consulat du Sommerlund ? » demande-t-il d'un air surpris,
visiblement déconcerté par votre soudaine apparition. Puis, se reprenant
: « Oh mais bien sûr ! s'exclame-t-il, c'est sur la place Alin, près du
port. Prenez à droite en sortant et encore à droite au bout de l'avenue.
Vous arriverez alors à la porte Rouge. Il vous faudra un laissez-passer
rouge pour entrer, car le consulat se trouve à l'intérieur du quartier
maritime et la circulation y est réglementée. » Vous demandez à
l'homme ce qu'il convient de faire pour obtenir un laissez-passer rouge.
« On voit que vous êtes étranger, répond-il, tout le monde sait à Port
Bax qu'il faut demander cela au capitaine de la tour du guet. La tour se
trouve au bout de la rue, vous ne pouvez pas la manquer, vous
tomberez dessus dès que vous aurez tourné le coin. » Vous remerciez le
vieil homme et vous quittez l'hôtel de ville.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_191.py", label="191", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
