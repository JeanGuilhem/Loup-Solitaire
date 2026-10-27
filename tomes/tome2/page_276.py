import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies, table_des_hasards
from combat import table_coups, KILL

ENEMY = ("MARIN PATIBULAIRE", 18, 25)


def arm_wrestling():
    """Bras de fer mené comme un combat, mais sur un total d'ENDURANCE à part : perdre ne tue pas
    (le Loup Solitaire récupère ses points). Gagner fait perdre les points perdus pendant la partie."""
    st.session_state.page_has_fight = True
    game = st.session_state.setdefault(
        "hazard_bras_de_fer", {"ls": st.session_state.endurance, "enemy": ENEMY[2], "log": [], "result": None}
    )
    hability = st.session_state.hability  # pas d'arme ni de Discipline pour un bras de fer
    st.write(
        f"**{ENEMY[0]}** — HABILETÉ {ENEMY[1]}, ENDURANCE {game['enemy']}/{ENEMY[2]}  \n"
        f"**Loup Solitaire** — HABILETÉ {hability}, ENDURANCE {game['ls']}"
    )
    for line in game["log"]:
        st.caption(line)
    if game["result"] is None:
        if st.button("💪 Assaut suivant", key="bras_de_fer_round", type="primary"):
            dice = table_des_hasards() % 10
            enemy_loss, ls_loss = table_coups(hability - ENEMY[1], dice)
            enemy_loss = game["enemy"] if enemy_loss is KILL else min(enemy_loss, game["enemy"])
            ls_loss = game["ls"] if ls_loss is KILL else min(ls_loss, game["ls"])
            game["enemy"] -= enemy_loss
            game["ls"] -= ls_loss
            game["log"].append(
                f"Assaut {len(game['log']) + 1} : tirage {dice}, le marin perd {enemy_loss}, vous perdez {ls_loss}."
            )
            if game["ls"] <= 0:
                game["result"] = "lost"
            elif game["enemy"] <= 0:
                game["result"] = "won"
                change_endurance(game["ls"] - st.session_state.endurance)
            st.rerun()
        return None
    if game["result"] == "lost":
        st.warning("Vous avez perdu la partie. Vous récupérez vos points d'ENDURANCE.")
    else:
        st.success("Vous avez remporté la partie !")
    return game["result"]

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
check_inventory(current_page_number=276, book=2)

fr_text = """
Un MARIN à la mine patibulaire défie quiconque veut l'entendre
d'engager avec lui une partie de bras de fer. Il a une telle confiance
dans sa force qu'il se déclare prêt à payer 5 Pièces d'Or à celui qui
réussira à le vaincre. Lorsque vous vous approchez de sa table, une
servante vous glisse quelques mots à l'oreille. « Méfiez-vous, étranger,
dit-elle, cet homme est dangereux, il casse le bras de tous ceux qui
perdent contre lui et il tue ceux qui parviennent à le battre. » Et tandis
que vous vous asseyez à la table, face au marin, les autres clients de la
taverne prennent les paris sur l'issue de la partie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï de la Puissance Psychique, rendez-vous au :'))
    if has_kai("La Puissance Psychique"):
        st.page_link("tomes/tome2/page_14.py", label="14", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_14.py", label="14", icon="📄", disabled=True)
        st.write_stream(stream_text(
            "Dans le cas contraire, menez cette partie de bras de fer comme s'il s'agissait d'un combat. "
            "Le premier dont le total d'ENDURANCE sera descendu à zéro aura perdu. Si vous perdez, vous "
            "récupérerez bien entendu tous les points d'ENDURANCE que vous aviez au début de la partie ; "
            "rendez-vous alors au 192. Si vous remportez la victoire, rendez-vous au 305."
        ))
        result = arm_wrestling()
        if result == "lost":
            st.page_link("tomes/tome2/page_192.py", label="192", icon="📄")
        elif result == "won":
            st.page_link("tomes/tome2/page_305.py", label="305", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
