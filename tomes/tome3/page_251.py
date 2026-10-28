import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=251, book=3)

fr_text = """
Dans l'après-midi, votre voyage en direction du glacier devient
peu à peu de plus en plus pénible. Les vaisseaux sanguins de vos
yeux se mettent à enfler et bientôt vous avez l'impression qu'on
vous pique les globes oculaires à l'aide d'aiguilles chauffées au
rouge ou que vos paupières sont couvertes de sable sur leur face
intérieure. Fenor est le premier à s'apercevoir de ce qui vous
arrive et il fait arrêter les traîneaux. « Cécité des neiges, dit-il en
déchirant un vieux chiffon pour en faire un bandeau. Si vous
continuez ainsi, la douleur vous aura rendu fou avant que le
soleil ne soit couché. » Vous perdez 2 points d'ENDURANCE.
Fenor bande vos yeux irrités et vous installe à l'arrière du
traîneau. Vous êtes à présent allongé à côté du chargement
tandis que l'expédition repart. A la nuit tombée, vous atteignez
enfin le glacier de Viad.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_62.py", label="62", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
