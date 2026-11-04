import streamlit as st
from inventory import (
    add_to_inventory,
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=130, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous arrachez le Masque d'Herbes du visage du guerrier mort
(inscrivez-le sur votre Feuille d'Aventure dans la case Objets
Spéciaux) et vous placez ce petit masque à l'odeur agréable sur
votre bouche. Les herbes filtrent l'air vicié, facilitant ainsi votre
respiration. Vous gagnez 1 point d'ENDURANCE. Laissant le
cadavre derrière vous, vous continuez votre progression lorsque
vous entendez soudain d'autres Sharnazims patauger derrière
vous dans le tunnel. Il vous est impossible de les distancer et
vous devez vous cacher rapidement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("MASQUE D'HERBES")
        change_endurance(1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=1)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au :"))
    if has_kai("Le Camouflage"):
        st.page_link("tomes/tome5/page_151.py", label="151", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_151.py", label="151", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne possédez pas cette Discipline, rendez-vous au :"))
    if has_kai("Le Camouflage"):
        st.page_link("tomes/tome5/page_15.py", label="15", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_15.py", label="15", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
