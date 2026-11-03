import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, handle_repas, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=78, book=4)

fr_text = """
Lorsque vous vous approchez, ils font glisser leur capuchon de
leur tête, laissant apparaître des visages souriants. Ils semblent
soulagés de pouvoir établir un contact amical dans ces terres
inhospitalières. Ni l'un ni l'autre ne prononcent le moindre mot,
mais tous deux ôtent de leur cou des Amulettes accrochées à des
chaînettes. Ils vous donnent ainsi un moyen de les identifier. En
effet, les petits poissons de bois qu'ils vous montrent sont les
symboles d'un Ordre Saint dont les membres sont appelés « les
Rédempteurs ». Il s'agit d'une communauté de pèlerins
contemplatifs qui consacrent leur vie à la prière et à l'étude de
l'art de la Guérison. L'un des pèlerins vous offre un petit flacon
de terre cuite rempli d'Eau Bénite. Si vous souhaitez conserver ce
flacon, inscrivez-le sur votre Feuille d'Aventure, dans la case
Objets Spéciaux. Vos hommes établissent le campement sous le
dôme de marbre et vous vous préparez tous à une bonne nuit de
sommeil. Vous êtes affamé et il vous faut à présent prendre un
Repas, sinon vous perdrez 3 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("EAU BÉNITE", key="eau_benite", label="Prendre le flacon d'Eau Bénite")

    handle_repas()

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_233.py", label="233", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
