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

check_inventory(current_page_number=182, book=6)

fr_text = """
Courbé en deux, vous fuyez rapidement en zigzaguant à travers
les broussailles. Tout à coup, vous entendez un craquement
sonore : une puissante décharge vient de frapper une branche
au-dessus de votre tête. Vous avez échappé de justesse à l'éclair
et vous apercevez des branches enflammées à vos pieds. Vous
faites un saut de côté pour éviter une autre décharge qui
transperce un arbre devant vous. Le trou est si gros que vous
pourriez y passer la tête ! Finalement, vous retrouvez votre
cheval et partez au galop sur la grand-route, sain et sauf. Vous
venez d'être témoin d'un rituel secret des Druides de Cenet et
vous avez survécu à cette rencontre, ce dont peu de gens peuvent
s'enorgueillir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_102.py", label="102", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
