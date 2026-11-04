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

check_inventory(current_page_number=87, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
De l'autre côté de la petite tour, la corniche passe sous des
fenêtres donnant au nord, à plusieurs mètres du sol. Les pierres
de la paroi ont subi l'érosion des vents déchaînés arrivant de
l'océan ; les creux et les fissures qui en résultent vous offrent de
nombreuses prises qui facilitent votre escalade. A votre grand
soulagement, vous découvrez également que, de ce côté-ci du
Palais, on n'a pas encore posé de barreaux aux fenêtres. Vous
sautez à l'intérieur et vous vous retrouvez dans un couloir qui
remonte vers l'ouest. Tout au bout, un grand escalier mène à un
véritable dédale de galeries bordées de niches. Dans chacune de
ces niches se trouve un buste ou une tapisserie retraçant la gloire
des anciens Zakhans et les victoires vassagoniennes des guerres
d'autrefois.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_105.py", label="105", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_105.py", label="105", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne possédez pas cette discipline, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_158.py", label="158", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_158.py", label="158", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
