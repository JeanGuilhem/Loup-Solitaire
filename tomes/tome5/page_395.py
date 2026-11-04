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

check_inventory(current_page_number=395, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Vous apercevez, aussi loin que porte le regard, une longue galerie
creusée dans le grès qui descend droit devant vous. Des torches
fixées au mur éclairent en crépitant des pictogrammes gravés
dans la pierre jaune. A intervalles réguliers, vous remarquez des
dalles aux rebords rugueux scellées dans le sol. En vous baissant
pour examiner l'une de ces dalles de plus près, vous comprenez
avec effroi ce qui a dû se passer : lors de la construction du
Tombeau, de nombreux pièges mortels avaient été creusés pour
empêcher que les lieux ne soient profanés. Les Seigneurs des
Ténèbres connaissaient leur existence et lorsqu'ils firent
désensabler la galerie, au lieu d'avertir les Giaks de la présence
de ces chausses-trappes, ils se servirent d'eux afin qu'ils les
repèrent au prix de leur vie. Une fois le piège découvert, on
recouvrait les corps des malheureux esclaves avec du sable puis,
le trou ainsi comblé, on posait une dalle. Vous êtes rempli
d'indignation en pensant à la barbarie de ces opérations. Vous
suivez la galerie pendant un bon kilomètre avant d'arriver à une
grande porte en pierre. Les montants de la porte sont finement
ouvragés, mais la porte elle-même est faite d'un seul bloc. Par un
trou creusé dans le plafond passe un faible rayon de lumière qui
forme au sol une petite flaque claire. Juste à côté, vous
remarquez un trou, identique à celui du plafond. Par ailleurs,
dans le mur près de la porte, vous apercevez une empreinte
creuse triangulaire, pas plus grande qu'une Pièce d'Or.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un Prisme, rendez-vous au :"))
    if has_item("PRISME"):
        st.page_link("tomes/tome5/page_233.py", label="233", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_233.py", label="233", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous possédez un Triangle de Pierre Bleue, rendez-vous au :"))
    if has_item("TRIANGLE DE PIERRE BLEUE"):
        st.page_link("tomes/tome5/page_245.py", label="245", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_245.py", label="245", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous ne possédez aucun de ces objets, rendez-vous au :"))
    if has_item("PRISME") or has_item("TRIANGLE DE PIERRE BLEUE"):
        st.page_link("tomes/tome5/page_298.py", label="298", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_298.py", label="298", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
