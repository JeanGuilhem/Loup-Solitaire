import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=247, book=3)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Le vieil homme relève lentement la tête. Il a les yeux fatigués et
meurtris, et sa longue barbe grise est tachée de sang caillé. Avec
difficulté, il se remet sur pied et scrute l'obscurité au-dessus de
lui. « Qui se cache là-haut ? Est-ce toi, Vonotar ? Montre-toi,
misérable ver de terre ou alors, va-t-en. Je n'ai pas peur de toi et
sache que tu m'inspires le plus profond dégoût. Jamais tu ne
parviendras à me briser, traître infâme ! » crie-t-il en
brandissant un poing décharné. Son accent vous est familier :
c'est en effet le même que le vôtre. Cet homme est l'un de vos
compatriotes, un citoyen du Sommerlund originaire du port de
Toran.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous disposez d'une Corde, vous pouvez la dérouler et la jeter au vieil homme afin de le "
            "tirer de sa prison, rendez-vous pour cela au :"
        )
    )
    if has_item("CORDE"):
        st.page_link("tomes/tome3/page_118.py", label="118", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_118.py", label="118", icon="📄", disabled=True)
    st.write_stream(
        stream_text(
            "Si vous n'avez pas de Corde, ou si vous ne souhaitez pas porter secours au prisonnier, vous "
            "pouvez poursuivre votre chemin le long du passage en vous rendant au :"
        )
    )
    st.page_link("tomes/tome3/page_30.py", label="30", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
