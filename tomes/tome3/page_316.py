import streamlit as st
from inventory import (
    add_to_inventory,
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

check_inventory(current_page_number=316, book=3)

fr_text = """
Ce Bracelet dégage une aura de puissance qui vous met mal à
l'aise. Les Barbares des Glaces fabriquent leurs armes à l'aide
d'os et de dents. Il n'y a en effet aucune mine à Kalte et les
métaux y sont considérés comme un bien rare et précieux, tous
les métaux, pas seulement l'or. Or, d'après ce que vous savez,
lorsque les Barbares des Glaces vont échanger leurs fourrures
contre du métal, seul l'acier les intéresse. Ces cruels chasseurs
sont tout à fait insensibles à l'art de la joaillerie. Vous en tirez
donc la conclusion que ce Bracelet était porté par obligation et
non par quelque souci de coquetterie. Vous pouvez prendre ce
Bracelet d'Or et le passer à votre poignet ; inscrivez-le alors sur
votre Feuille d'Aventure dans la case Objets Spéciaux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous décidez de passer ce Bracelet à votre poignet, rendez-vous au :"))
    if has_item("BRACELET D'OR"):
        st.page_link("tomes/tome3/page_236.py", label="236", icon="📄")
    elif st.button("Passer le Bracelet d'Or à votre poignet et vous rendre au 236", key="bracelet"):
        if add_to_inventory("BRACELET D'OR"):
            st.switch_page("tomes/tome3/page_236.py")
    st.write_stream(stream_text("Si vous préférez le laisser là, poursuivez votre chemin le long du couloir en direction du croisement situé plus loin ; rendez-vous pour cela au :"))
    st.page_link("tomes/tome3/page_215.py", label="215", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
