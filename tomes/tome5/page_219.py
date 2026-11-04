import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=219, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
N'écoutant que votre instinct, vous plongez au sol puis vous
effectuez un roulé-boulé. La flamme bleue passe en sifflant au-dessus de votre tête et va exploser contre le mur en faisant un
trou de plusieurs dizaines de centimètres de profondeur dans les
pierres dures de la paroi. Vous vous relevez rapidement, puis
vous courez vous cacher derrière une énorme colonne quand,
tout à coup, retentit le rire sinistre d'Haakon, le Seigneur des
Ténèbres. Peu à peu, le ricanement s'amplifie, et vous ressentez
une violente douleur à la tête, comme si vous aviez le crâne pris
dans un étau.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Bouclier Psychique, rendez-vous au :"))
    if has_kai("Bouclier psychique"):
        st.page_link("tomes/tome5/page_253.py", label="253", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_253.py", label="253", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne possédez pas cette Discipline, rendez-vous au :"))
    if has_kai("Bouclier psychique"):
        st.page_link("tomes/tome5/page_369.py", label="369", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_369.py", label="369", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
