import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=214, book=2)

fr_text = """
Dès que vous êtes entré, vous vous apercevez qu'il ne s'agit pas du tout
d'une boutique. Vous vous trouvez dans une pièce nue et froide qui ne
comporte pour seul ameublement qu'une grande table placée en son
centre. Aux quatre coins de l'endroit, pendent des paires de menottes
dont l'aspect sinistre vous glace le sang. Vous venez en fait de pénétrer
dans le Quartier Général de la Fraternité du Silence, la célèbre police
secrète de Lachelan. Avec un sentiment d'horreur, le récit d'un autre
Seigneur Kaï vous revient alors en mémoire : il vous avait raconté
comment on l'avait arrêté et accusé d'espionnage puis comment il avait
réussi à s'évader après avoir été torturé pendant trois jours et trois nuits.
Hélas, vous n'aurez pas, quant à vous, la chance de pouvoir vous
échapper, car la porte donnant sur la rue vient de se verrouiller
automatiquement et bientôt les Frères du Silence, qui vous observent
pour l'instant derrière des judas aménagés dans les murs, viendront
s'occuper de vous. Vous serez peut-être fier d'apprendre qu'après avoir
passé une longue semaine dans la prison du chef inquisiteur, vous
n'avez pas révélé le moindre secret de la communauté des Seigneurs
Kaï. C'est un record qui n'est pas près d'être égalé, mais qui vous a
coûté la vie. Une vie qui s'achève donc dans ces geôles sinistres en
interrompant brutalement votre mission.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
