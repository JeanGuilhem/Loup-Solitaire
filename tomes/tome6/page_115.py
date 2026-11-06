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

check_inventory(current_page_number=115, book=6)

fr_text = """
Pris au dépourvu, le garde fait un saut de côté au moment où
vous lancez votre cheval sur lui. Le portail du corps de garde
s'ouvre sur une grande place pavée, mais la seule issue en est
bloquée par la roulotte et le chariot de marchandises qui vous
ont précédé. Une douzaine de gardes portant l'uniforme noir et
vert du guet urbain sont en train d'en inspecter la cargaison.
Dès qu'ils vous voient surgir de l'ombre du porche, ils se
mettent à crier à l'unisson : « Arrêtez le fraudeur, arrêtez le
fraudeur ! »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez serrer la bride à votre cheval et vous préparer à affronter les soldats de la ville, rendez-vous au :"))
    st.page_link("tomes/tome6/page_248.py", label="248", icon="📄")

    st.write_stream(stream_text("Si vous voulez essayer de sauter par-dessus les chariots pour fuir ensuite dans l'ombre de la rue tortueuse qui s'enfonce au cœur de la cité, rendez-vous au :"))
    st.page_link("tomes/tome6/page_72.py", label="72", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
