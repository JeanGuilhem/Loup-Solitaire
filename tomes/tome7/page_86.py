import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=86, book=7)

fr_text = """
Vous vous glissez furtivement entre deux des énormes cocons qui
pendent le long de la paroi et vous recourez à votre habileté de
Maître Kaï afin de masquer l'odeur et la chaleur de votre corps.
L'ignoble créature vermiforme s'arrête, renifle l'air bruyamment
et fait cliqueter ses mandibules. Vous détournez la tête et vous
plongez les yeux dans l'un des cocons qui vous entourent. Un
frisson glacé vous parcourt l'échine ; vous êtes nez à nez avec un
visage de guerrière à moitié décomposé qui vous fixe de ses yeux
creux à travers l'entrelacs de fils soyeux du cocon ! Ébranlé par le
choc provoqué par cette odieuse vision, vous ne pouvez réprimer
un sursaut. La créature vermiforme décèle aussitôt votre
mouvement et se met à avancer rapidement sur ses courtes
pattes caoutchouteuses. Il ne vous reste plus qu'à prier qu'elle ne
découvre pas votre cachette...
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll(key="cachette")
    if roll is not None:
        st.write_stream(stream_text("Si le chiffre que vous avez obtenu est compris entre 0 et 4, rendez-vous au :"))
        st.page_link("tomes/tome7/page_109.py", label="109", icon="📄", disabled=roll > 4)
        st.write_stream(stream_text("Si ce chiffre est compris entre 5 et 9, rendez-vous au :"))
        st.page_link("tomes/tome7/page_278.py", label="278", icon="📄", disabled=roll < 5)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
