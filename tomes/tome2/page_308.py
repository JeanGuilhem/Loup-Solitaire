import streamlit as st
from inventory import (
    add_gold,
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    spend_gold,
)
from utils import called_cookies, stream_text, table_des_hasards

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=308, book=2)

fr_text = """
Un marin du nom de Sprogg s'est assis à côté de vous et vous explique
les règles du jeu de « Hublot». Il vous montre d'abord une paire de dés
en forme de diamant, taillés dans du verre rouge. Chaque dé possède
dix faces numérotées de 0 à 9 ; les joueurs doivent lancer les deux dés
et ajouter les chiffres obtenus. Celui qui tire deux 0 crie « Hublot » ! et
gagne automatiquement. Chaque joueur mise 3 Couronnes à chaque
lancer de dés. Il y a trois joueurs en tout, et chacun dépose ses Pièces
d'Or dans un chapeau avant que les dés soient jetés. Utilisez la Table de
Hasard pour obtenir deux chiffres.
Faites ainsi deux tirages de deux chiffres qui correspondront aux scores
obtenus par chacun des deux autres joueurs, puis notez le résultat de ces
deux tirages consécutifs. Ensuite, la Table de Hasard vous donnera
votre propre score (vous tirerez également deux chiffres pour vous-
même). Si le total que vous obtenez est supérieur à celui de chacun des
deux autres joueurs vous gagnerez 6 Couronnes. Si l'un des deux autres
joueurs, a fait un tirage supérieur au vôtre, vous perdrez 3 Couronnes.
En cas d'égalité entre deux joueurs, la partie est annulée et vous
recommencez le tirage depuis le début. Vous pouvez jouer autant que
vous voudrez, sans dépasser un gain maximum de 40 Couronnes. Vous
avez également le droit de quitter la table de jeu quand bon vous
semblera et vous êtes bien entendu obligé d'abandonner la partie si
vous perdez toutes vos Pièces d'Or.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    net = st.session_state.setdefault("hazard_hublot_net", 0)  # gains nets de la soirée
    stopped = st.session_state.get("hazard_hublot_stop", False)
    can_play = not stopped and st.session_state.purse >= 3 and net < 40

    col1, col2 = st.columns(2)
    if col1.button("Jouer (mise : 3 Couronnes)", key="hublot_play", disabled=not can_play):
        cancelled = 0
        while True:
            throws = [(table_des_hasards() % 10, table_des_hasards() % 10) for _ in range(3)]
            totals = [a + b for a, b in throws]
            if len(set(totals)) == 3:
                break
            cancelled += 1  # égalité entre deux joueurs : la partie est annulée
        hublots = [total == 0 for total in totals]
        names = ["Premier joueur", "Deuxième joueur", "Vous"]
        lines = [f"{name} : {a} + {b} = {a + b}" + (" — « Hublot ! »" if hub else "")
                 for name, (a, b), hub in zip(names, throws, hublots)]
        if cancelled:
            lines.insert(0, f"*{cancelled} partie(s) annulée(s) pour égalité, les dés sont relancés.*")
        if hublots[2] or (not any(hublots[:2]) and totals[2] > max(totals[:2])):
            gain = add_gold(min(6, 40 - net), notify=False)
            st.session_state["hazard_hublot_net"] = net + gain
            lines.append(f"**Vous gagnez {gain} Couronnes !**")
        else:
            spend_gold(3)
            st.session_state["hazard_hublot_net"] = net - 3
            lines.append("**Vous perdez 3 Couronnes.**")
        st.session_state["hazard_hublot_last"] = "  \n".join(lines)
        st.rerun()
    if col2.button("Arrêter de jouer", key="hublot_stop", disabled=stopped):
        st.session_state["hazard_hublot_stop"] = True
        st.rerun()

    if "hazard_hublot_last" in st.session_state:
        st.info(st.session_state["hazard_hublot_last"])
    st.metric(label="Bourse", value=st.session_state.purse, delta=st.session_state["hazard_hublot_net"])

    if not can_play:
        if not stopped and net >= 40:
            st.write("Vous avez atteint le gain maximum de 40 Couronnes.")
        elif not stopped:
            st.write("Il ne vous reste plus assez d'or pour miser : vous devez abandonner la partie.")
        st.write_stream(stream_text("Lorsque vous aurez décidé d'arrêter de jouer, rentrez dormir dans votre cabine en vous rendant au :"))
        st.page_link("tomes/tome2/page_197.py", label="197", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
