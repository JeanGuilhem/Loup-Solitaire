import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=128, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Soudain, le tunnel s'élargit et l'égout passe sous une pièce au
plafond élevé en forme de voûte d'où jaillit une cascade qui vient
grossir les eaux graisseuses de l'égout. A l'endroit où la cascade
se déverse dans l'égout flotte une masse de restes de repas et de
vieux morceaux de viande avariée qui dégagent une odeur
nauséabonde. Vous vous apprêtez à pénétrer sous la voûte
lorsque vous sentez que le sol de l'égout se dérobe sous vos pieds.
Vous vous raidissez juste à temps afin d'éviter de sombrer dans
les eaux profondes. Le tunnel continue au-delà de la voûte mais
plusieurs mètres d'eau boueuse et putride vous en séparent
encore. Les clapotements qui vous parviennent au loin vous
rappellent que les Sharnazims vous suivent toujours.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez une Corde, vous pouvez essayer de l'enrouler autour d'une barre en fer qui dépasse de la cascade, puis vous hisser hors de l'eau et vous lancer de l'autre côté de la voûte. Rendez-vous au :"))
    if has_item("CORDE"):
        st.page_link("tomes/tome5/page_29.py", label="29", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_29.py", label="29", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous voulez essayer de rejoindre l'autre partie du tunnel en nageant, rendez-vous au :"))
    st.page_link("tomes/tome5/page_84.py", label="84", icon="📄")

    st.write_stream(stream_text("Si vous souhaitez plutôt faire demi-tour et retourner au croisement, rendez-vous au :"))
    st.page_link("tomes/tome5/page_121.py", label="121", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
