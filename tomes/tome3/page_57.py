import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=57, book=3)

fr_text = """
Le lendemain, un froid vif règne alentour et un vent violent
venant du nord souffle sans relâche. Le visage fouetté par les
rafales, vos lèvres bientôt se dessèchent, gercent et saignent.
Votre nez commence à couler mais le mucus gèle
instantanément. Le soleil est caché par une neige épaisse qui
tombe en flocons serrés et obscurcit la lumière du jour. Les tas de
neige compacte et les trous dans la glace disparaissent sous la
poudreuse et souvent un traîneau verse ou s'enlise, obligeant
l'expédition à interrompre son avance. Il vous faut sans cesse
scruter le sol pour essayer d'apercevoir les obstacles de glace qui
peuvent se dresser sur votre chemin, et le scintillement de la
neige met vos yeux à rude épreuve ; vers midi, votre vision
devient floue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï de la Guérison, rendez-vous au :'))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome3/page_17.py", label="17", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_17.py", label="17", icon="📄", disabled=True)

    st.write_stream(stream_text('Sinon, rendez-vous au :'))
    st.page_link("tomes/tome3/page_251.py", label="251", icon="📄", disabled=has_kai("La Guérison"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
