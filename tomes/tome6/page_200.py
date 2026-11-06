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

check_inventory(current_page_number=200, book=6)

fr_text = """
La vieille porte en pierre s'ouvre lentement en grinçant sur ses
gonds. Vous attendez que toute la poussière soit retombée et
vous pénétrez dans la crypte de la cathédrale de Tekaro. L'air y
est froid et humide, et vous sentez tout à coup votre cœur qui bat
à tout rompre dans votre poitrine. La Pierre de la Sagesse se
trouve ici, vous pouvez la sentir ! Les pâles rayons cendrés de la
Lune qui filtrent à travers la crypte éclairent un alignement de
tombes en granit qui gisent là comme des géants endormis sous
la terre. Vous essayez de les ouvrir une par une à l'aide de votre
Clé en Argent jusqu'à ce que vous trouviez celle qui renferme la
légendaire Pierre de la Sagesse. Vous trouvez enfin la bonne
serrure et vous y introduisez votre Clé mais, alors que vous
touchez au but, vous êtes brusquement interrompu par une
créature qui vient de pénétrer dans la crypte par la porte des
égouts.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_334.py", label="334", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
