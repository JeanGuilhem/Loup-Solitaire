import streamlit as st
from combat import table_coups
from inventory import (
    bow_bonus,
    check_inventory,
    display_inventory,
    end_page,
    has_flag,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text, table_des_hasards

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=26, book=6)

fr_text = """
Le score que vous avez atteint vous qualifie pour la finale, car
un autre archer a totalisé plus de 8 points. Il s'appelle Altan,
c'est un homme grand, au visage rude, qui est garde forestier dans
les régions montagneuses du Nord. Son arc est en bois de Toa
orange et il le manie avec une adresse remarquable. La compétition
s'annonce donc difficile. L'épreuve finale du tournoi se déroule
selon les règles habituelles de combat, la seule différence étant
que vous commencez chacun avec 50 points de Tir. (Ceux-ci
remplacent en l'occurrence les points d'ENDURANCE, mais votre
total d'ENDURANCE actuel restera inchangé tout au long de
l'épreuve.) Déduisez les points perdus par vous-même et votre
concurrent. Le premier des deux qui perdra ses 50 points de Tir
aura perdu le tournoi. (Ne rayez aucune flèche sur votre Feuille
d'Aventure, puisqu'il s'agit d'une compétition sportive.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # Finale du tournoi : un combat aux « points de Tir » (50 chacun), sans toucher à l'ENDURANCE ni
    # aux flèches. combat() ne sait pas faire : l'épreuve est menée ici avec la Table des coups.
    # Faits testés : « arc Jakan » (298 : -2, se brise sur un 0) et « arc de Kalte » (214 : -4)
    state = st.session_state.setdefault("combat_tir_26", {"me": 50, "altan": 50, "log": [], "broken": False})
    jakan = has_flag("arc Jakan")
    malus = -2 if jakan else -4 if has_flag("arc de Kalte") else 0
    if malus:
        st.write(f"*Arc emprunté : {malus} HABILETÉ.*")
    hability = st.session_state.hability + malus + bow_bonus()
    st.write(f"*Votre HABILETÉ de tir : {hability}"
             + (" (dont +3 de Science des Armes à l'Arc)" if bow_bonus() else "") + ". ALTAN : HABILETÉ 30.*")
    col1, col2 = st.columns(2)
    col1.metric("Vos points de Tir", state["me"])
    col2.metric("Points de Tir d'Altan", state["altan"])
    for line in state["log"]:
        st.write(line)

    def shoot() -> None:
        """Un tir de chacun : la Table des coups, avec les points de Tir à la place de l'ENDURANCE."""
        roll = table_des_hasards() % 10
        if jakan and roll == 0:
            state["broken"] = True
            state["log"].append("*Vous avez tiré le 0 : votre Jakan se brise !*")
            return
        altan_loss, my_loss = table_coups(hability - 30, roll)
        altan_loss = state["altan"] if altan_loss is None else altan_loss
        my_loss = state["me"] if my_loss is None else my_loss
        state["altan"] = max(0, state["altan"] - altan_loss)
        state["me"] = max(0, state["me"] - my_loss)
        state["log"].append(f"*Tir n° {len(state['log']) + 1} : vous avez tiré le {roll}. "
                            f"Altan perd {altan_loss} points de Tir, vous en perdez {my_loss}.*")

    def over() -> bool:
        return state["broken"] or state["me"] <= 0 or state["altan"] <= 0

    if not over():
        col1, col2 = st.columns(2)
        if col1.button("🏹 Tirer (Table de Hasard)", key="tir_26"):
            shoot()
            st.rerun()
        if col2.button("⏩ Tirer jusqu'au bout", key="tir_26_auto"):
            while not over():
                shoot()
            st.rerun()

    if state["broken"]:
        st.write_stream(stream_text("Votre arc s'est brisé : rendez-vous au :"))
        st.page_link("tomes/tome6/page_335.py", label="335", icon="📄")
    elif state["me"] <= 0:
        st.write_stream(stream_text("Vous êtes le premier à perdre vos 50 points de Tir, rendez-vous au :"))
        st.page_link("tomes/tome6/page_183.py", label="183", icon="📄")
    elif state["altan"] <= 0:
        st.write_stream(stream_text("Vous remportez le tournoi, rendez-vous au :"))
        st.page_link("tomes/tome6/page_252.py", label="252", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
