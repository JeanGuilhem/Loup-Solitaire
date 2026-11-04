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

check_inventory(current_page_number=235, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Des rangées de stalactites, semblables aux défenses de quelque
monstre fantastique, pendent du plafond de la grotte. Des
profondeurs insondables vous parviennent les bruits inquiétants
des remous d'un geyser. Vous commencez à explorer les lieux et,
finalement, vous parvenez à un endroit où un pont naturel en
pierre enjambe un cours d'eau. Des fumées s'élèvent lentement
des eaux rougies par le minerai de cuivre. Soudain, vous
apercevez la silhouette décharnée et pitoyable d'un homme blotti
sous le pont. Il est enveloppé dans une couverture déchirée qui
cache son visage et il tient dans ses mains maigres une canne à
pêche rudimentaire. Il a déjà attrapé quelques crabes des laves
qui gisent au bord de l'eau, les pinces secouées par les dernières
convulsions de leur lente agonie. Alors que vous vous approchez
de lui, il redresse lentement la tête pour vous examiner : c'est un
homme, mais la vue de son visage vous glace d'effroi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Guérison, rendez-vous au :"))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome5/page_344.py", label="344", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_344.py", label="344", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline, rendez-vous au :"))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome5/page_208.py", label="208", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_208.py", label="208", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
