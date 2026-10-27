import streamlit as st
from inventory import (
    buy_button,
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

check_inventory(current_page_number=181, book=2)

fr_text = """
Cette rue est encore plus sale et nauséabonde que celle que vous venez
de quitter. Bientôt, cependant, la vitrine en désordre d'une boutique
attire votre attention; vous y découvrez en effet plusieurs objets qui
pourraient vous être fort utiles ; chacun de ces objets porte une étiquette
qui indique son prix.
"""

fr_text_2 = """
Lorsque vous avez terminé vos emplettes, vous poursuivez votre
chemin le long de la rue du Sage en direction du pont de Ragadorn. Ce
pont est le seul point de passage entre les parties Est et Ouest de la ville ;
 il est toujours bondé et il vous faut jouer des coudes pour parvenir à le
traverser parmi la foule qui s'y presse. Rendu de l'autre côté, vous vous
retrouvez dans une avenue jonchée d'ordures : c'est le boulevard du
Commerce, section Est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.markdown(
        "| Objet | Prix |\n|---|---|\n"
        "| Épée | 4 Couronnes |\n| Poignard | 2 Couronnes |\n| Sabre | 3 Couronnes |\n"
        "| Marteau de guerre | 6 Couronnes |\n| Lance | 5 Couronnes |\n| Masse d'Armes | 4 Couronnes |\n"
        "| Couverture de fourrure | 3 Couronnes |\n| Sac à Dos | 1 Couronne |"
    )
    st.write_stream(stream_text("Vous pouvez entrer dans cette boutique et acheter ce qui vous plaira."))
    buy_button("ÉPÉE", 4, key="epee")
    buy_button("POIGNARD", 2, key="poignard")
    buy_button("SABRE", 3, key="sabre")
    buy_button("MARTEAU DE GUERRE", 6, key="marteau")
    buy_button("LANCE", 5, key="lance")
    buy_button("MASSE D'ARMES", 4, key="masse")
    buy_button("COUVERTURE DE FOURRURE", 3, key="couverture")
    buy_button("SAC À DOS", 1, key="sac")

    st.write(fr_text_2)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_186.py", label="186", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
