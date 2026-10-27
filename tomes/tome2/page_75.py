import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    spend_gold,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=75, book=2)

fr_text = """
Vous pénétrez dans un bureau aux odeurs de moisi. Deux hommes y
sont assis, penchés sur leurs tables qui ploient sous des piles de livres et
de papiers. « Bonsoir, monsieur», dit l'un des hommes. Sa longue
moustache soigneusement cirée tressaute quand il parle. « Monsieur
désire-t-il un laissez-passer de marchand ? » demande-t-il. Avant même
que vous ayez pu répondre, l'homme vous tend une poignée de
formulaires incompréhensibles. « Si Monsieur veut bien se donner la
peine de signer ici, je me ferai un plaisir de donner immédiatement à
Monsieur son laissez-passer. Il en coûtera 10 Couronnes à Monsieur. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous désirez signer ces papiers et faire l'achat d'un laissez-passer blanc (10 "
            "Couronnes), rendez-vous au :"
        )
    )
    if st.button("Payer 10 Couronnes (142)", disabled=st.session_state.purse < 10):
        if spend_gold(10):
            add_to_inventory("LAISSEZ-PASSER BLANC")
            st.switch_page("tomes/tome2/page_142.py")
    if st.session_state.purse < 10:
        st.caption("Vous ne possédez pas la somme requise.")

    st.write_stream(
        stream_text(
            "Si vous n'avez pas assez d'argent ou si ce laissez-passer ne vous intéresse pas, quittez "
            "le bureau et retournez dans le hall en vous rendant au :"
        )
    )
    st.page_link("tomes/tome2/page_318.py", label="318", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
