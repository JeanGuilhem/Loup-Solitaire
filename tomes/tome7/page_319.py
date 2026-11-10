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

check_inventory(current_page_number=319, book=7)

fr_text = """
Vous vous glissez sur le côté du tunnel et, plaqué contre le mur,
attendez le meilleur moment pour frapper. Quatre guerriers, l'air
menaçant, s'avancent dans le vestibule en file indienne. Tout
d'abord, vous les prenez pour des Drakkarims, car leurs armures
noires et leurs casques en forme de tête de mort sont identiques à
ceux que portent ces guerriers malfaisants qui servent les
Seigneurs des Ténèbres d'Helgedad. Mais en lançant votre
attaque, vous apercevez les traits de leurs visages et vous
comprenez qu'il ne s'agit pas d'êtres humains. Ils ont de larges
épaules tombantes, des bras anormalement longs et tiennent
dans leurs mains poilues pourvues de griffes jaunes des haches et
des lances forgées de façon très rudimentaire. Ils s'approchent
rapidement en remuant leurs longues queues touffues comme
celles des lions. Votre premier coup transperce la cuirasse du
dernier guerrier qui hurle comme un démon avant de s'effondrer
comme une masse à vos pieds. Les autres se retournent aussitôt
pour vous faire face et brandissent leurs armes pour parer votre
attaque. Le chef relève sa visière, et vous apercevez un groin
ressemblant à celui d'un sanglier, encadré par deux défenses. Il
pousse un grognement terrifiant et vous attaque avec sa lance.
Les autres se mettent également à crier et attaquent à leur tour.
Vous devez les combattre tous les trois comme un seul ennemi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("RAKHOS DE ZAHDA", 28, 35)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_56.py", label="56", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
