import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=183, book=4)

fr_text = """
Vous vous approchez d'un enchevêtrement de buissons d'épines
qui poussent à proximité de la porte de la crypte. De cette
cachette, vous pouvez observer les Gardes vassagoniens sans être
vu. D'autres soldats à cheval apparaissent alors. Ils viennent du
nord et pénètrent dans les ruines de Maaken. Ils mettent ensuite
pied à terre et s'avancent vers la porte. « Le mot de passe ! »
s'écrie l'un des gardes. « Lohn ! » répondent les soldats. La porte
s'ouvre aussitôt et ils sont autorisés à entrer. Maintenant que
vous connaissez le mot de passe, vous décidez d'essayer d'entrer
dans la crypte de la même manière. Dissimulé par le capuchon de
votre cape, vous vous avancez d'un pas assuré vers les Gardes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï du Camouflage, ajoutez 4 au chiffre que vous aurez tiré.'))
    roll = hazard_roll()
    if roll is not None:
        total = roll + (4 if has_kai("Le Camouflage") else 0)
        if has_kai("Le Camouflage"):
            st.write(f"*Camouflage : +4, soit un total de {total}.*")
        if total <= 6:
            st.write_stream(stream_text('Si vous obtenez un total de 0 à 6, rendez-vous au :'))
            st.page_link("tomes/tome4/page_198.py", label="198", icon="📄")
        else:
            st.write_stream(stream_text('De 7 à 13, rendez-vous au :'))
            st.page_link("tomes/tome4/page_338.py", label="338", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
