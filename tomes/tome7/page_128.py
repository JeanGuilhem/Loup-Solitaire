import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=128, book=7)

fr_text = """
Tandis que les flammes s'éteignent et que la fumée se disperse
peu à peu, vous voyez que la main reste étendue au pied de son
socle. Mais soudain, elle recommence à bouger et à crisper
nerveusement ses doigts à demi calcinés. Vous contemplez la
scène, bouche bée, n'en croyant pas vos yeux, lorsque la main fait
un prodigieux bond en l'air et se met à planer au-dessus de vous !
Puis elle écarte les doigts et se laisse tomber sur votre tête.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï de l'Art de la Chasse, ajoutez 3 au chiffre que vous avez tiré."))
    roll = hazard_roll(key="main")
    if roll is not None:
        total = roll + (3 if has_magnakai("Art de la Chasse") else 0)
        if has_magnakai("Art de la Chasse"):
            st.write(f"*Art de la Chasse : +3, total {total}.*")
        if total <= 2:
            st.write_stream(stream_text("Si le résultat est compris entre 0 et 2, rendez-vous au :"))
            st.page_link("tomes/tome7/page_77.py", label="77", icon="📄")
        elif total <= 6:
            st.write_stream(stream_text("Si le résultat est compris entre 3 et 6, rendez-vous au :"))
            st.page_link("tomes/tome7/page_198.py", label="198", icon="📄")
        else:
            st.write_stream(stream_text("Si le résultat est supérieur ou égal à 7, rendez-vous au :"))
            st.page_link("tomes/tome7/page_235.py", label="235", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
