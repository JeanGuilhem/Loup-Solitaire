import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=31, book=2)

fr_text = """
Votre première rencontre avec le Lieutenant Général vous surprend.
Vous vous attendiez sans doute à voir un vieil homme servile,
semblable à ces émissaires des contrées méridionales qui viennent sans
cesse encombrer le palais du roi. Mais l'homme qui se tient devant
vous, vêtu d'une lourde cotte de mailles, n'est ni vieux ni servile. C'est
même un personnage tout à fait exceptionnel comme vous n'allez pas
tarder à le découvrir. Né d'un père sommerlundois et d'une mère
durenoraise, le Lieutenant Général Rhygar est devenu dans cette ville
une figure de légende. Au cours des dix dernières années, il a pris la
tête d'une armée formée par l'Alliance des Nations et sous son
commandement, les Barbares des Glaces venus du pays de Kalte ont
été repoussés et taillés en pièces. Sage en temps de paix, implacable
lorsque la guerre fait rage, c'est là le meilleur compagnon que vous
puissiez souhaiter. Nul ne saurait mieux vous aider dans votre quête du
Glaive de Sommer. Rhygar fait servir un somptueux repas ; jamais
vous n'avez aussi bien mangé depuis que la guerre a commencé. Au
cours du festin, vous repensez à tous les événements qui se sont
déroulés entre votre départ du Sommerlund et votre arrivée à Port Bax.
Vous songez également aux terribles périls qui vous attendent encore.
A la fin du repas, Rhygar fait venir son médecin personnel qui
s'empresse de soigner vos blessures. Les potions qu'il vous fait boire
vous rendent 6 points d'ENDURANCE. Le praticien vous conseille
ensuite de prendre une bonne nuit de repos car, au matin, vous partirez
pour Hammardal en compagnie du Lieutenant Général. Le lendemain
de bonne heure, on vous conduit dans un jardin clôturé, à l'arrière du
consulat. Rhygar et trois de ses meilleurs soldats vous y attendent. Ils
sont déjà montés sur leurs chevaux, prêts à vous accompagner jusqu'à
Hammardal, la capitale de Durenor, distante de 370 kilomètres. Les
rues de Port Bax s'éveillent à peine tandis que vous parcourez la ville à
cheval. En passant la porte de pierre moussue qui marque la limite de la
cité, vous vous sentez confiant dans le succès de votre mission : vous
êtes quasiment sûr désormais de réussir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        before = st.session_state.endurance
        change_endurance(6)
        st.session_state["visibility_potions"] = st.session_state.endurance - before
    st.metric(label="Endurance", value=st.session_state.endurance, delta=st.session_state.get("visibility_potions") or 0)
    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous tirez 0, 1, 2, 3 ou 4, rendez-vous au 176. Si vous tirez 5, 6, 7, 8 ou 9, rendez-vous au 254."))
    number = hazard_roll()
    if number is not None and 0 <= number <= 4:
        st.page_link("tomes/tome2/page_176.py", label="176", icon="📄")
    elif number is not None and 5 <= number <= 9:
        st.page_link("tomes/tome2/page_254.py", label="254", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
