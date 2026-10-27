import streamlit as st
from inventory import (
    add_gold,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    spend_gold,
)
from utils import stream_text, called_cookies, table_des_hasards

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=238, book=2)

fr_text = """
Face au relais de diligence, une rue étroite mène à une maison de jeu
sur la façade de laquelle est placardé cet avis:
LES ARMES SONT INTERDITES A L'INTÉRIEUR DE CET
ÉTABLISSEMENT
La perspective de pouvoir gagner un peu d'or vous décide à y entrer
sans attendre. Si vous avez des armes, vous devrez les déposer au
vestiaire ; vous aurez le droit de les reprendre en quittant les lieux. En
échange d'une Pièce d'Or, on vous donne un jeton d'argent qui vous
permet d'entrer dans l'établissement. Le hall mène à une vaste salle où
se pratiquent toutes sortes de jeux de hasard. L'un d'eux vous semble
particulièrement intéressant : on l'appelle la « Roue du Carrosse». Au
bout d'une longue table, une jeune femme fort séduisante fait tourner
une sorte de disque noir qui a été divisé en dix tranches égales
numérotées de 0 à 9. Lorsque le disque tourne, elle y laisse tomber une
petite boule d'argent qui finit par s'immobiliser sur l'une des tranches
numérotées. Plusieurs marchands sont assis autour de la table où se
déroule ce jeu et misent de grosses sommes en essayant de deviner sur
quel numéro la boule s'arrêtera. Pour jouer à la « Roue du Carrosse », il
vous faut tout d'abord choisir le numéro sur lequel vous voulez miser ;
ensuite, vous devrez décider combien de Couronnes d'Or vous allez
mettre en jeu. Notez bien ces deux chiffres, puis utilisez la Table de
Hasard pour savoir si vous avez gagné. Si la Table vous donne le
chiffre sur lequel vous avez parié, vous empocherez 8 Pièces d'Or pour
chaque Couronne mise en jeu. Si le chiffre que vous obtenez se situe
immédiatement avant ou immédiatement après celui choisi par vous,
chaque Couronne mise en jeu vous rapportera 5 Pièces d'Or. Vos gains
cependant devront se limiter à 40 Pièces d'Or maximum. Vous pouvez
jouer aussi longtemps que vous voulez, jusqu'à ce que vous ayez perdu
tout votre or ou que vous décidiez d'emporter vos gains (40 Couronnes
maximum).
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # droit d'entrée : 1 Pièce d'Or contre un jeton d'argent (les armes sont rendues à la sortie)
    if is_new_page():
        spend_gold(1)
        st.session_state.hazard_gains = 0
        st.session_state.hazard_log = []
        st.session_state.hazard_stopped = False
    gains = st.session_state.get("hazard_gains", 0)
    log = st.session_state.setdefault("hazard_log", [])

    st.metric(label="Couronnes", value=st.session_state.purse, delta=gains if gains else None)
    for entry in log[-5:]:
        st.write(entry)

    can_play = (
        not st.session_state.get("hazard_stopped", False)
        and st.session_state.purse > 0
        and gains < 40
    )
    if can_play:
        if st.session_state.get("hazard_stake", 1) > st.session_state.purse:
            st.session_state.hazard_stake = st.session_state.purse
        col1, col2 = st.columns(2)
        pick = col1.selectbox("Numéro misé", list(range(10)), key="hazard_pick")
        stake = col2.number_input(
            "Couronnes misées", min_value=1, max_value=st.session_state.purse, step=1, key="hazard_stake"
        )
        play, stop = st.columns(2)
        if play.button("Jouer", key="hazard_play"):
            stake = min(int(stake), st.session_state.purse)
            ball = table_des_hasards() % 10
            if ball == pick:
                win = 8 * stake
            elif ball in ((pick - 1) % 10, (pick + 1) % 10):
                win = 5 * stake
            else:
                win = 0
            if win:
                win = min(win, 40 - gains)  # gains limités à 40 Pièces d'Or
                win = add_gold(win, notify=False)
                st.session_state.hazard_gains = gains + win
                log.append(f"La boule s'arrête sur le {ball} : vous gagnez {win} Couronne(s).")
            else:
                spend_gold(stake)
                st.session_state.hazard_gains = gains - stake
                log.append(f"La boule s'arrête sur le {ball} : vous perdez {stake} Couronne(s).")
            st.rerun()
        if stop.button("Arrêter de jouer", key="hazard_stop"):
            st.session_state.hazard_stopped = True
            st.rerun()
    elif gains >= 40:
        st.info("Vous avez atteint le maximum de 40 Pièces d'Or de gains.")

    if st.session_state.purse == 0:
        st.write_stream(stream_text("Si vous avez perdu tout votre or, rendez-vous au :"))
        st.page_link("tomes/tome2/page_169.py", label="169", icon="📄")
    else:
        st.write_stream(
            stream_text(
                "Si vous décidez de partir avec vos gains ou l'or qui vous reste, quittez la maison de jeu "
                "et rendez-vous au :"
            )
        )
        st.page_link("tomes/tome2/page_186.py", label="186", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
