import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=40, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Des chariots de mine vides sont alignés sur une voie ferrée, le
long d'un tunnel qui s'ouvre dans le mur ouest de cette galerie.
Au-dessus de l'entrée du tunnel, un escalier de bois mène à un
couloir plus étroit éclairé par la flamme vacillante d'une torche.
Vous restez caché dans l'ombre en observant la galerie pendant
une demi-heure. Vous estimez alors que vous pouvez y pénétrer
sans risque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez suivre la voie ferrée en direction de l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome4/page_55.py", label="55", icon="📄")

    st.write_stream(stream_text("Si vous préférez monter l'escalier pour explorer le passage auquel il mène, rendez-vous au :"))
    st.page_link("tomes/tome4/page_291.py", label="291", icon="📄")

    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï de l'Orientation et si vous avez le rang Kaï d'Aspirant (ou un rang supérieur), rendez-vous au :"))
    if has_kai("L'Orientation") and kai_rank() >= 6:
        st.page_link("tomes/tome4/page_349.py", label="349", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_349.py", label="349", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
