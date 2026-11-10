import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
    use_arrow,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=314, book=7)

fr_text = """
Vous essuyez les larmes qui coulent de vos yeux et vous vous
concentrez afin de trouver une cible au milieu des tourbillons de
fumée. Une ombre à votre gauche trahit la présence d'une
créature qui rampe le long du pont. Vous tendez votre arc et vous
tirez. Un instant plus tard, un hurlement de rage et de douleur
indique que vous avez bien visé. Le cri s'éloigne rapidement
tandis que la créature tombe dans le vide vers une mort certaine.
Soudain, une forme surgit de la fumée et se précipite sur vous.
Vous êtes sauvagement griffé et mordu au visage et au bras, et
vous tirez une arme juste à temps pour vous défendre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        use_arrow()  # la flèche tirée sur la créature
    st.caption(f"Vous avez tiré une flèche : il vous en reste {st.session_state.get('arrows', 0)}.")

    outcome = combat([("DHAX", 20, 28)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Vous fuyez le combat en courant vers l'entrée du tunnel opposé ; rendez-vous au :"))
        st.page_link("tomes/tome7/page_277.py", label="277", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_141.py", label="141", icon="📄")
    elif outcome is None:
        st.caption("Vous pouvez fuir à tout moment vers l'entrée du tunnel opposé (rendez-vous alors au 277).")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
