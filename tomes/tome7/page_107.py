import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=107, book=7)

fr_text = """
Votre main s'enfonce dans la première bulle sans rencontrer la
moindre résistance ; c'est un peu comme si vous l'aviez plongée
dans un bac d'eau froide. Pourtant, lorsque vous essayez de vous
dégager, la membrane translucide se referme comme un étau sur
votre poignet. Vous vous débattez furieusement, mais cela ne fait
qu'aggraver la situation ; votre bras tout entier se trouve
maintenant pris au piège. Un instant plus tard, la bulle vous a complètement englouti ! A l'intérieur de cette prison transparente, l'oxygène est rare ; vous cherchez l'air
désespérément, mais bientôt vos yeux se révulsent et vos
poumons semblent sur le point d'exploser. (Vous perdez 6 points d'ENDURANCE.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-6)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-6)

    sword = has_item("ÉPÉE") or has_item("GLAIVE DE SOMMER")
    fire = (has_item("TORCHE") and has_item("BRIQUET À AMADOU")) or has_item("LANTERNE")
    sphere = has_item("SPHÈRE DE FEU")

    st.write_stream(stream_text("Si vous possédez une Épée, vous pouvez essayer de percer la membrane de la bulle ; rendez-vous, dans ce cas, au :"))
    st.page_link("tomes/tome7/page_26.py", label="26", icon="📄", disabled=not sword)

    st.write_stream(stream_text("Si vous possédez une Torche et un Briquet d'Amadou, ou bien une Lanterne, et si vous voulez allumer un feu pour brûler l'enveloppe visqueuse qui vous retient prisonnier, rendez-vous au :"))
    st.page_link("tomes/tome7/page_51.py", label="51", icon="📄", disabled=not fire)

    st.write_stream(stream_text("Si vous possédez une Sphère de Feu de Kalte, rendez-vous au :"))
    st.page_link("tomes/tome7/page_145.py", label="145", icon="📄", disabled=not sphere)

    st.write_stream(stream_text("Si vous n'avez aucun de ces Objets, rendez-vous au :"))
    st.page_link("tomes/tome7/page_292.py", label="292", icon="📄", disabled=sword or fire or sphere)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
