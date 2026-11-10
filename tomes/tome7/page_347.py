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

check_inventory(current_page_number=347, book=7)

fr_text = """
Vous portez le sifflet à vos lèvres et soufflez. Aussitôt, la créature
visqueuse se cabre en agitant ses courtes pattes caoutchouteuses
dans tous les sens. Le sifflement hyperaigu du sifflet a détruit son
système nerveux. L'énorme ver se tortille pitoyablement, et sa
tête disparaît dans la brume du plafond. Vous entendez alors un
craquement assourdissant, et un éclair bleu s'enroule, tel un
serpent, autour de sa gorge. La créature se débat sauvagement
pendant plusieurs minutes tandis qu'une odeur de chair brûlée
envahit le couloir. L'horrible danse de la créature cesse
rapidement, et le brouillard se dissipe. Dans l'obscurité, vous
apercevez alors une passerelle et une plate-forme d'observation.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez grimper sur le corps du ver pour vous hisser sur la plate-forme, rendez-vous au :"))
    st.page_link("tomes/tome7/page_294.py", label="294", icon="📄")
    st.write_stream(stream_text("Si vous préférez enjamber le cadavre afin de continuer ensuite votre chemin le long du tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_46.py", label="46", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
