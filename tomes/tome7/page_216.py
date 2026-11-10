import streamlit as st
from inventory import (
    check_inventory,
    completed_lore_circles,
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

check_inventory(current_page_number=216, book=7)

fr_text = """
Vous découvrez avec soulagement que la porte n'est ni
verrouillée ni gardée et vous pénétrez dans un couloir éclairé par
des torches. Vous le suivez à travers toute une suite de pièces
vides, à l'abandon depuis des années : c'est l'ancienne et
somptueuse demeure du Seigneur de Kazan-Oud. Du luxe de
cette retraite souterraine, il ne reste plus à présent que des
lambeaux de rideaux à moitié pourris et quelques meubles
moisis. Vous vous apprêtez à pénétrer dans une de ces pièces
lorsque vous entendez des bruits de voix. Vous vous arrêtez
brusquement et vous apercevez trois créatures très maigres,
assises autour d'une table au centre de la pièce. Leurs doigts
verts et décharnés pointés sur un parchemin, elles tiennent une
discussion très animée dans une langue qui vous est totalement
étrangère. Elles portent de longs habits à capuchon en soie
violette et ne semblent pas armées.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous avez complété le Cercle de Solaris, rendez-vous au :"))
    if "Cercle de Solaris" in completed_lore_circles():
        st.page_link("tomes/tome7/page_244.py", label="244", icon="📄")
    else:
        st.write_stream(stream_text("Vous n'avez pas complété le Cercle de Solaris."))
        st.page_link("tomes/tome7/page_244.py", label="244", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous souhaitez lancer une attaque-surprise contre ces créatures, apparemment inoffensives, rendez-vous au :"))
    st.page_link("tomes/tome7/page_295.py", label="295", icon="📄")

    st.write_stream(stream_text("Si vous préférez essayer de traverser la pièce en vous dissimulant, rendez-vous au :"))
    st.page_link("tomes/tome7/page_343.py", label="343", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
