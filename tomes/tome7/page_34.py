import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_magnakai,
    magnakai_rank,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=34, book=7)

fr_text = """
En réponse à la solution que vous venez d'énoncer, la porte ovale
émet un léger déclic et s'ouvre lentement. Vous la franchissez et
vous descendez un pan incliné qui vous conduit jusqu'à un long
couloir. Aussi loin que le regard porte, vous constatez que les
parois sont entièrement tapissées d'une espèce d'énormes
cocons.
Derrière vous, la porte se referme avec un claquement sec.
Curieusement, le cliquetis continue encore après, porté par
l'écho, mais en devenant de plus en plus fort. Soudain, vous
voyez se mouvoir une ombre au fond de l'obscur tunnel : un
gigantesque ver aux yeux noirs est en train de ramper vers vous !
Il possède de puissantes mandibules, et une écume violette
dégouline de sa gueule en bouillonnant. De toute évidence, le
monstre a senti votre odeur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    animal = has_magnakai("Contrôle Animal") and magnakai_rank() >= 4  # rang de Maître primat
    whistle = has_item("SIFFLET D'ARGENT")
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Invisibilité, rendez-vous au :"))
    if has_magnakai("Invisibilité"):
        st.page_link("tomes/tome7/page_86.py", label="86", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_86.py", label="86", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Magnakaï du Contrôle Animal et que vous avez atteint le rang de Maître Primat, rendez-vous au :'))
    if animal:
        st.page_link("tomes/tome7/page_130.py", label="130", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_130.py", label="130", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous possédez un Sifflet d'Argent, rendez-vous au :"))
    st.page_link("tomes/tome7/page_347.py", label="347", icon="📄", disabled=not whistle)

    st.write_stream(stream_text("Si vous ne maîtrisez aucune des disciplines citées et si vous n'avez pas sur vous de Sifflet d'Argent, rendez-vous au :"))
    st.page_link("tomes/tome7/page_233.py", label="233", icon="📄", disabled=has_magnakai("Invisibilité") or animal or whistle)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
