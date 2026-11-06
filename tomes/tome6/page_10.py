import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

# billet de bateau : BILLET POUR LUYEN / BILLET POUR RHEM / BILLET POUR EULA (Objets Spéciaux)
if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=10, book=6)

fr_text = """
Un homme d'apparence joviale, portant de longs cheveux tombant sur
les épaules, est allongé dans un hamac accroché au bout de la
passerelle. Il ouvre un œil à votre approche et, avec la rapidité
de l'éclair, saute sur ses pieds et tire de sa poche un carnet de
tickets en s'écriant avec empressement : « Bienvenue à bord du
Kazomra, le meilleur bateau qui ait jamais navigué sur les eaux de
la Storn ! » Vous consultez le tableau des prix :

- Luyen : 10 Pièces d'Or ;
- Rhem : 15 Pièces d'Or ;
- Eula : 20 Pièces d'Or.

« Nous levons l'ancre à minuit, noble seigneur, reprend-il. Alors
n'attendez pas trop pour faire embarquer vot' cheval. » Après
avoir choisi votre destination, payez votre billet (n'oubliez pas
de rayer les Pièces d'Or dépensées à cet effet) puis rangez-le
soigneusement dans votre poche après l'avoir inscrit dans la case
Objets Spéciaux de votre Feuille d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    tickets = {"BILLET POUR LUYEN": ("Luyen", 10), "BILLET POUR RHEM": ("Rhem", 15), "BILLET POUR EULA": ("Eula", 20)}
    bought = [ticket for ticket in tickets if has_item(ticket)]
    if bought:
        st.success(f"Vous avez votre billet pour {tickets[bought[0]][0]}.")
    else:
        for ticket, (town, price) in tickets.items():
            if st.button(f"Billet pour {town} ({price} Couronnes)", disabled=st.session_state.purse < price):
                spend_gold(price)
                add_to_inventory(ticket)
                st.rerun()

    st.write_stream(stream_text("Après avoir choisi votre destination et payé votre billet, rendez-vous au :"))
    st.page_link("tomes/tome6/page_82.py", label="82", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
