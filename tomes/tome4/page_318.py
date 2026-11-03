import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

fr_unknown_item = "Vous ne possédez pas cet objet."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=318, book=4)

fr_text = """
Oren Vanalund est le quinzième baron de Ruanon. C'est un noble
guerrier de lignée royale, cinquième dans l'ordre de succession
au trône du Sommerlund. Ce Seigneur de la Guerre, vaillant et
orgueilleux d'ordinaire, est à présent prostré sur le sol de pierre
froide de cette salle, l'œil rouge et la voix gémissante. On dirait
un chien peureux. « Il a tout perdu, dit le capitaine Gayal à voix
basse. Barraka a détruit son château, saccagé ses terres et sa ville,
massacré sa famille. Ses fils sont morts et sa fille unique est
retenue prisonnière par Barraka lui-même. J'ai bien peur que ces
terribles épreuves ne lui aient fait perdre la raison. » L'homme
pitoyable affalé devant vous lève alors son visage baigné de
larmes et marmonne d'une faible voix deux étranges vers :
Quand mourra sur l'autel la vierge aux cheveux blonds,
Des gorges de Maaken les morts se lèveront.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un rouleau de parchemin, rendez-vous au :"))
    if has_item("ROULEAU DE PARCHEMIN"):
        st.page_link("tomes/tome4/page_279.py", label="279", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_279.py", label="279", icon="📄", disabled=True)

    st.write_stream(stream_text("Sinon, rendez-vous au :"))
    if has_item("ROULEAU DE PARCHEMIN"):
        st.page_link("tomes/tome4/page_57.py", label="57", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome4/page_57.py", label="57", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
