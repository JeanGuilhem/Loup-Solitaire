import streamlit as st
from inventory import (
    add_gold,
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text, table_des_hasards

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=284, book=6)

fr_text = """
Un immense mercenaire bedonnant se tient debout sur une estrade en
bois près de la porte. Il enregistre les paris des soldats tandis
que ses jeunes assistants essaient de racoler des clients à
l'intérieur de la taverne. Un garçon au visage sale s'approche de
vous et vous demande combien vous voulez parier. Décidez du nombre
de Pièces d'Or que vous souhaitez parier, et notez la somme dans
la marge de votre Feuille d'Aventure - le pari maximal est de 10
Pièces d'Or. Ensuite, utilisez la Table de Hasard pour obtenir un
chiffre et notez-le aussi dans la marge. Utilisez à nouveau la
Table de Hasard pour obtenir un autre chiffre auquel vous ajoutez
3. Si le premier chiffre que vous avez tiré est supérieur au
second total, vous avez gagné votre pari. Multipliez alors la
somme que vous avez pariée par deux pour savoir combien de Pièces
d'Or vous avez gagnées (les cotes sont de deux contre un). Si le
second chiffre est supérieur au premier, le cavalier a transpercé
tous les fruits, et vous avez perdu votre mise de départ. La
partie se déroule en 3 Assauts, et vous pouvez faire un pari par
Assaut ou quitter la taverne à n'importe quel moment de la partie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # jeu de paris en 3 Assauts (état effacé à chaque nouvelle visite : préfixe hazard_)
    game = st.session_state.setdefault("hazard_t6_284_paris", {"round": 0, "log": []})
    for line in game["log"]:
        st.write(line)
    if game["round"] < 3 and st.session_state.purse > 0:
        bet = st.number_input(
            f"Votre mise pour l'Assaut {game['round'] + 1} (10 Pièces d'Or au plus)",
            min_value=1,
            max_value=min(10, st.session_state.purse),
            value=1,
            step=1,
            key=f"t6_284_mise_{game['round']}",
        )
        if st.button(f"Parier {bet} Pièce(s) d'Or (Assaut {game['round'] + 1})", key=f"t6_284_parier_{game['round']}"):
            first = table_des_hasards() % 10
            second = table_des_hasards() % 10 + 3
            if first > second:
                gained = add_gold(2 * bet)
                result = f"vous gagnez {gained} Pièce(s) d'Or"
            else:
                # égalité : le livre ne dit rien, le pari est perdu (le premier chiffre doit être supérieur)
                spend_gold(bet)
                result = f"le cavalier a transpercé tous les fruits, vous perdez votre mise de {bet} Pièce(s) d'Or"
            game["round"] += 1
            game["log"].append(
                f"*Assaut {game['round']} : premier chiffre {first}, second total {second} : {result}. "
                f"Bourse : {st.session_state.purse}.*"
            )
            st.rerun()

    st.write_stream(stream_text("Si vous voulez partir pendant la partie, rendez-vous au :"))
    st.page_link("tomes/tome6/page_336.py", label="336", icon="📄")

    st.write_stream(stream_text("Si vous avez parié sur les 3 Assauts et que vous n'avez pas perdu toutes vos Pièces d'Or, rendez-vous au :"))
    if game["round"] >= 3 and st.session_state.purse > 0:
        st.page_link("tomes/tome6/page_347.py", label="347", icon="📄")
    else:
        st.page_link("tomes/tome6/page_347.py", label="347", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous avez perdu tout votre Or, rendez-vous au :"))
    if game["round"] > 0 and st.session_state.purse == 0:
        st.page_link("tomes/tome6/page_76.py", label="76", icon="📄")
    else:
        st.page_link("tomes/tome6/page_76.py", label="76", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
