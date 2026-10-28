import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_flag,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=129, book=3)

fr_text = """
Les poils rêches qui couvrent la langue du Languabarb sont
imprégnés d'un puissant venin grâce auquel la créature paralyse
ses victimes avant de les dévorer. En moins de cinq secondes, le
poison fait son effet, et vous perdez connaissance avant même
que votre tête n'ait heurté la neige. Lorsque vous reprenez
conscience, vous sentez un poids vous peser lourdement sur la
poitrine. C'est le cadavre d'Irian. Et tandis que vous essayez tant
bien que mal de vous relever, une vision désolante s'offre à vous
dans la brume du petit matin. Tous vos guides, en effet, sont
morts et ce qui reste de votre équipement est dispersé alentour.
Les cadavres des deux Languabarbs sont étendus dans la neige
tachée de sang : tous deux ont été tués à coups d'épée. Engourdi
par le froid et le choc que vous venez de recevoir, vous cherchez
pendant une heure votre Sac à Dos, parcourant d'un pas
chancelant l'étendue glacée, lorsque vous vous apercevez enfin
qu'il est toujours accroché à vos épaules. Bien que vous soyez
toujours dans un état second, vous parvenez malgré tout à
découvrir un chemin escarpé qui vous permet de poursuivre
votre route. Un vent glacial souffle sur ces montagnes hostiles et
si vous ne vous êtes pas enduit le corps d'huile de Bakanal, vous
perdez 3 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if has_flag("huile de Bakanal"):
        st.success("*L'huile de Bakanal dont vous êtes enduit vous protège du vent glacial.*")
    else:
        if is_new_page():
            change_endurance(-3)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_155.py", label="155", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
