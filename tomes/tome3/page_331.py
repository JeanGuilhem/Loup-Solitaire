import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=331, book=3)

fr_text = """
Le lendemain, la température descend et un froid rigoureux
s'installe. Des vents du nord amènent une grêle de glace qui vous
cingle le visage et vos lèvres gercées se mettent à saigner. Vers
midi, vous êtes pris dans un blizzard qui rend votre progression
difficile et épuisante. Le vent violent vous force à descendre du
traîneau pour le pousser. Vous êtes exténué, vos mains et vos
orteils sont engourdis par le froid et la transpiration provoquée
par vos efforts harassants a gelé sur votre peau, déposant à
l'intérieur de vos moufles et de vos bottes une couche de glace.
Lorsque vous atteignez enfin le glacier, la nuit est presque
tombée, et vous êtes tous si fatigués que vous avez à peine
suffisamment de force pour dresser la tente et prendre un repas.
La situation frise le désastre. Vos orteils, vos doigts et votre nez
ont subi la morsure du gel et, à moins que vous ne maîtrisiez la
Discipline Kaï de la Guérison, vous perdez 4 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if has_kai("La Guérison"):
        st.success("*Votre Discipline Kaï de la Guérison vous protège des effets du gel.*")
    else:
        if is_new_page():
            change_endurance(-4)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)
    roll = hazard_roll()
    if roll is not None and roll <= 4:
        st.write_stream(stream_text("Si vous tirez un chiffre entre 0 et 4, rendez-vous au :"))
        st.page_link("tomes/tome3/page_62.py", label="62", icon="📄")
    elif roll is not None:
        st.write_stream(stream_text("Entre 5 et 9, rendez-vous au :"))
        st.page_link("tomes/tome3/page_288.py", label="288", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
