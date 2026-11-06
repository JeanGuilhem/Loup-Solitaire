import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=326, book=6)

fr_text = """
Tandis que vous achevez le dernier des spectres décharnés, vous
vous rendez compte que la bataille s'est étendue au-delà des
murs du cimetière. Des profondeurs d'une crypte ouverte surgit
un groupe de zombies. Ils se précipitent sur les cavaliers qu'ils
désarçonnent sauvagement. Roark ne contrôle plus du tout la
situation, et aucune créature vivante n'est plus à l'abri de la
terreur qu'il a semée. Saisi d'une panique aveugle, il fait demi-
tour, abandonnant ses hommes à leur effroyable destin. Tandis
qu'il disparaît au loin, le tourbillon de ténèbres se dissipe
lentement et les morts vivants vacillent et trébuchent avant de
s'effondrer dans les nuages de poussière colportés par la brise du
soir. Vous accourez au secours du vieux magicien, qui gît
mortellement blessé sous le corps de son cheval mort. Vous lui
soutenez la tête, et Cyrilus, dans un dernier effort, murmure
entre ses lèvres exsangues : « La... rue... des... Chaudronniers... »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Magnakaï de la Science Médicale, rendez-vous au :'))
    if has_magnakai("Science Médicale"):
        st.page_link("tomes/tome6/page_216.py", label="216", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_216.py", label="216", icon="📄", disabled=True)

    st.write_stream(stream_text('Sinon, rendez-vous au :'))
    if has_magnakai("Science Médicale"):
        st.page_link("tomes/tome6/page_46.py", label="46", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome6/page_46.py", label="46", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
