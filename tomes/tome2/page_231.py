import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    is_new_page,
    pickup_button,
    receive_gold,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=231, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
La porte de derrière ouvre sur une petite place au centre de laquelle se
dresse une haute sépulture. Les pêcheurs ont disparu dans les rues
sombres, sauf un qui est tombé en glissant sur le pavé mouillé et s'est
assommé dans sa chute. Il est étendu dans le caniveau, le visage dans
une flaque d'eau. Vous le retournez du bout du pied et vous le fouillez.
Dans ses poches, vous trouvez 5 Pièces d'Or et 1 Poignard, mais mieux
que tout, vous découvrez, passé à son doigt, le Sceau d'Hammardal;
vous poussez un long soupir de soulagement et vous inscrivez sur votre
Feuille d'Aventure toutes ces trouvailles.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    receive_gold(5)
    if is_new_page() and not has_item("SCEAU D'HAMMARDAL"):
        add_to_inventory("SCEAU D'HAMMARDAL")
    st.write("Vous pouvez prendre le Poignard :")
    pickup_button("POIGNARD", key="poignard", label="Prendre le Poignard")

    st.write_stream(stream_text('Si vous souhaitez à présent retourner dans la taverne, rendez-vous au :'))
    st.page_link("tomes/tome2/page_177.py", label="177", icon="📄")

    st.write_stream(stream_text('Si vous préférez examiner la sépulture, rendez-vous au :'))
    st.page_link("tomes/tome2/page_24.py", label="24", icon="📄")

    st.write_stream(stream_text("S'il vous semble plus judicieux de suivre la rue du Tombeau en direction de l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome2/page_253.py", label="253", icon="📄")

    st.write_stream(stream_text("Vous pouvez également aller vers l'est en empruntant la rue de la Tour de Guet ; rendez-vous pour cela au :"))
    st.page_link("tomes/tome2/page_319.py", label="319", icon="📄")

    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome2/page_182.py", label="182", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_182.py", label="182", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
