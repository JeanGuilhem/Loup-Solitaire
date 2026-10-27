import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=77, book=2)

fr_text = """
Au cours de votre entraînement au monastère Kaï, vos maîtres vous ont
enseigné de nombreux langues et dialectes en usage dans les régions
septentrionales de Magnamund. L'un de ces dialectes est le squall. Or,
il se trouve précisément que les créatures rassemblées dans cette
clairière sont des Squalls. A grands cris, ils vous expliquent que
l'homme blessé n'a en réalité rien d'humain. C'est un Monstre d'Enfer,
affirment-ils, un de ces êtres maléfiques qui ont le pouvoir de changer
de forme à leur guise et qui comptent parmi les plus fidèles serviteurs
des Maîtres des Ténèbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous pensez que les Squalls disent vrai, jetez un coup d'œil au contenu du sac de "
            "l'homme blessé en vous rendant au :"
        )
    )
    st.page_link("tomes/tome2/page_320.py", label="320", icon="📄")

    st.write_stream(
        stream_text(
            "Si en revanche vous soupçonnez les Squalls de vous mentir pour vous dissuader d'intervenir"
            " dans leurs jeux répugnants, attaquez-les avec votre arme en vous rendant au :"
        )
    )
    st.page_link("tomes/tome2/page_28.py", label="28", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
