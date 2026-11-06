import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    remove_from_inventory,
    set_flag,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

# fait posé : "cheval" (nouveau cheval obtenu par l'échange)

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=132, book=6)

fr_text = """
Vous reconnaissez l'homme au visage lunaire : c'est lui qui
était l'arbitre du tournoi. Il vous demande ce qui ne va pas, et
vous lui expliquez dans quelle fâcheuse situation vous vous
trouvez. « Je suis sûr que nous allons trouver une solution à
votre problème », vous dit-il avec empressement, se réjouissant
sans doute à l'avance du bénéfice qu'il pourra tirer de votre
infortune. L'homme vous propose alors d'échanger son cheval
contre 20 Pièces d'Or ou bien 2 de vos Objets Spéciaux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # l'échange se règle ici (le 212 ne sait pas comment vous avez payé)
    st.write_stream(stream_text("Si vous acceptez ce marché, payez le prix demandé puis rendez-vous au 212 :"))
    if st.button("Donner 20 Pièces d'Or", key="troc_or", disabled=st.session_state.purse < 20):
        if spend_gold(20):
            set_flag("cheval")
            st.switch_page("tomes/tome6/page_212.py")
    specials = list(dict.fromkeys(st.session_state.special))
    if len(specials) >= 2:
        given = st.multiselect("Ou choisissez 2 Objets Spéciaux à donner :", specials, max_selections=2, key="troc_select")
        if st.button("Donner ces 2 Objets Spéciaux", key="troc_objets", disabled=len(given) != 2):
            for item in given:
                remove_from_inventory(item)
            set_flag("cheval")
            st.switch_page("tomes/tome6/page_212.py")
    st.page_link("tomes/tome6/page_212.py", label="212", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous refusez, ou si vous ne pouvez pas vous permettre de payer le prix demandé ni de vous séparer de 2 Objets Spéciaux, rendez-vous au :"))
    st.page_link("tomes/tome6/page_176.py", label="176", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
