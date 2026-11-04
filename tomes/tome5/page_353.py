import streamlit as st
from combat import combat
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

check_inventory(current_page_number=353, book=5)

fr_text = """
Alors que vous tuez la dernière créature de la Crypte, Haakon
recule en titubant, comme affaibli par la mort de ses monstres.
Vous brandissez le Glaive de Sommer en espérant que jaillira de
sa lame un éclair d'énergie brûlante qui consumera le malfaisant
Seigneur des Ténèbres et le fera disparaître à tout jamais de la
surface du Magnamund. La lame se met à briller d'une lumière
de feu mais, cependant, aucun éclair ne jaillit de sa pointe ! Vous
comprenez subitement ce qui se passe : vous êtes sous terre, et le
Glaive ne peut donc pas capter l'énergie du soleil qui lui est
indispensable. Haakon éclate alors d'un rire si puissant qu'il fait
trembler le sol. Une flamme bleue surgit de la pierre qu'il tient au
creux de la main, puis un éclair, vif et tranchant comme une lame
effilée, jaillit en sifflant à travers la fumée et la poussière. Une
odeur de décomposition et de mort parvient à vos narines au
moment où le Seigneur des Ténèbres se prépare à attaquer.
A moins que vous ne maîtrisiez la Discipline Kaï du Bouclier
Psychique, vous devrez déduire 2 points de votre total
d'HABILETÉ pour toute la durée du combat.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # Bouclier Psychique : l'attaque psychique de Haakon (-2 HABILETÉ) est gérée par combat()
    outcome = combat([("HAAKON", 28, 45)], psychic_attack=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de ce terrible affrontement, rendez-vous au :"))
        st.page_link("tomes/tome5/page_400.py", label="400", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
