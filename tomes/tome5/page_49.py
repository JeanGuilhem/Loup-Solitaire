import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=49, book=5)

fr_text = """
La muraille d'enceinte du Grand Palais est bien trop haute à
escalader et, quand bien même vous auriez une corde assez
longue, le vert éclatant de votre manteau Kaï se détachant sur le
mur de marbre blanchi par le soleil, se verrait à des kilomètres à
la ronde. Vous vous aplatissez dans l'encoignure sombre d'une
porte pour réfléchir au plan que vous devez adopter. A la porte
nord, il y a un va-et-vient incessant de cavaliers et de messagers.
Avant d'entrer, les messagers qui arrivent tendent un rouleau de
parchemin aux deux Gardes en faction. Peu à peu, l'ébauche d'un
plan audacieux se dessine dans votre esprit : si vous réussissez à
neutraliser un de ces messagers avant qu'il n'atteigne la porte du
Palais, vous pourriez revêtir ses habits, puis prendre sa place en
utilisant son parchemin pour entrer. La plupart des cavaliers se
rendent du port au Grand Palais et, bien que ce trajet soit très
emprunté, vous découvrez un lieu idéal pour vous embusquer. A
un certain endroit, une passerelle de bois et de métal enjambe la
grande avenue. Dissimulé sous l'arche, vous attendez le moment
propice pour surprendre votre victime. L'occasion ne se fait pas
attendre : un cavalier, tout de noir vêtu, apparaît au bout de
l'avenue en éperonnant sa monture. Vous vous préparez à bondir
sur lui lorsqu'il passera sous le pont.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï de la Chasse, ajoutez 1 point au chiffre que vous avez tiré. Si vous avez le titre de Savant Kaï, ou un titre supérieur, ajoutez 3 points au chiffre que vous avez tiré.'))
    roll = hazard_roll()
    if roll is not None:
        bonus = 0
        if has_kai("La Chasse"):
            bonus += 1
        if kai_rank() >= 9:
            bonus += 3
        total = roll + bonus
        if bonus:
            st.write(f"*Bonus : +{bonus}, soit un total de {total}.*")
        if total <= 5:
            st.write_stream(stream_text('Si le résultat obtenu est compris entre 0 et 5, rendez-vous au :'))
            st.page_link("tomes/tome5/page_106.py", label="106", icon="📄")
        else:
            st.write_stream(stream_text('Si le résultat obtenu est compris entre 6 et 13, rendez-vous au :'))
            st.page_link("tomes/tome5/page_189.py", label="189", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
