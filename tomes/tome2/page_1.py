import streamlit as st
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=1, book=2)

fr_text = """
L'homme désigne un navire marchand qui mouille dans le port, près du
quai d'embarquement. C'est une caravelle de belle apparence,
soigneusement entretenue. « Le capitaine en second s'appelle Ronan,
poursuit le conducteur, il vous attend de l'autre côté de la place, à
l'auberge du Joyeux Drille. » Puis l'homme vous salue et disparaît dans
la foule en se faufilant avec son chariot dans les rues étroites de la ville.
Vous traversez la place mais lorsque vous parvenez devant l'auberge,
vous constatez que la porte en est fermée à clé et que les volets des
fenêtres sont clos. Tandis que vous vous demandez ce qu'il convient de
faire, une main vous agrippe le bras et vous pousse dans un coin
obscur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous désirez dégainer votre arme et combattre l'inconnu qui vous a ainsi agressé, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_273.py", label="273", icon="📄")

    st.write_stream(
        stream_text("Si vous préférez essayer d'échapper à son emprise en vous débattant, rendez-vous au :")
    )
    st.page_link("tomes/tome2/page_160.py", label="160", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
