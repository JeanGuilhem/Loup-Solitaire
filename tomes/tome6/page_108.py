import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=108, book=6)

fr_text = """
Tout en feignant de relâcher votre attention, vous vous tenez
prêt à parer une attaque impromptue. Après une longue pause, le
chef de la secte vous tourne le dos et s'adresse à ses disciples
d'une voix forte et emphatique : « Soyez témoins de la puissance
de Vashna, mes frères ! Son esprit est vivant, car même un
étranger ignare et indigne peut en constater la présence. » Un
chant lugubre à la louange du maître s'élève alors de la
procession. Pendant que les sinistres incantations atteignent
leur paroxysme, vous vous engagez furtivement dans une allée
avoisinante et vous éperonnez votre cheval pour fuir au plus
vite cette bande de dangereux fanatiques.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_332.py", label="332", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
