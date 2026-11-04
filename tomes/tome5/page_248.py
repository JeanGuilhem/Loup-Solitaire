import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=248, book=5)

fr_text = """
Un petit marchand est en train de haranguer la foule derrière
une charrette située près du porche voûté. Ses petits yeux de
fouine brillent sous un turban ridicule, beaucoup trop grand
pour lui. A peine êtes-vous arrivé près de son étalage qu'il se jette
sur vous et essaie désespérément, par un flot de paroles plus ou
moins convaincantes, de vous vendre une marchandise qui a l'air
de bien piètre qualité. Il semble surpris lorsque vous
l'interrompez par votre question. « Tipasa ? reprend-il. Oui, je
sais où il se trouve. » Puis, il vous tend un paletot criard taillé
dans une toile grossière, à rayures roses et orange. « Voilà qui
fera un beau cadeau pour votre cher ami, dit-il, les yeux fixés en
permanence sur la bourse accrochée à votre ceinture. Et cela
pour la modique somme de 5 Pièces d'Or, Seigneur ! » Vous
comprenez que vous allez devoir acheter ce vêtement ridicule
avant que le marchand se décide à vous dire où demeure Tipasa.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez acheter le paletot, payez les 5 Pièces d'Or, puis rendez-vous au 328."))
    if st.button("Payer 5 Couronnes", disabled=st.session_state.purse < 5):
        spend_gold(5)
        add_to_inventory("PALETOT")
        st.switch_page("tomes/tome5/page_328.py")

    st.write_stream(stream_text("Si vous ne voulez pas acheter le paletot ou si vous n'en avez pas les moyens, rendez-vous au :"))
    st.page_link("tomes/tome5/page_274.py", label="274", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
