import os

import streamlit as st
from environments import apply_environment
from inventory import display_inventory, init_state
from save import save_checkpoint, save_game
from utils import called_cookies
from variable import BOOKS

BOOK = 4

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

init_state()
st.session_state.game_phase = "playing"
st.session_state.book = BOOK
st.session_state.current_page_number = 0
st.session_state.last_page_number = 0
apply_environment("ville")  # citadelle de Holmgard, où le roi vous convoque

st.title(f"📜 Tome {BOOK} — {BOOKS[BOOK]['title']}")

fr_text = """
La province de Ruanon est une lointaine région minière située au
sud de votre patrie, le royaume du Sommerlund. Nichés entre les
pics sinistres des monts Durncrag et de la chaîne de Maaken, les
habitants de cette contrée ont longtemps prospéré grâce à
l'exploitation de leurs mines aux riches filons, vivant paisibles du
fruit de leur rude labeur sous la protection de leur seigneur, le
Baron Vanalund.
L'or et les pierres précieuses qui sont extraits des mines de
Ruanon constituent une importante source de revenus pour
votre pays. Chaque mois, des soldats du Sommerlund escortent
un convoi de chariots qui quitte la province pour se rendre dans
la capitale et y apporter son chargement de richesses. Ce
transport mensuel est devenu une routine dont jamais, jusqu'à
présent, la régularité n'avait été interrompue. Le mois dernier,
cependant, tout contact a été soudain perdu avec Ruanon. Une
troupe d'une centaine de cavaliers de la garde royale fut aussitôt
envoyée dans la région pour essayer de retrouver le convoi
disparu. L'officier commandant ce détachement, le capitaine
Gayal, avait reçu l'ordre de faire son rapport directement au roi
dès qu'il aurait découvert le convoi. Hélas, ni lui, ni ses hommes
ne sont revenus : eux aussi ont disparu sans laisser la moindre trace.
Le roi vous a alors convoqué, vous, le Loup Solitaire, dernier des
Seigneurs Kaï, à la citadelle de Holmgard. Là, vous avez reçu
pour mission de retrouver le capitaine Gayal et ses hommes, et
de découvrir ce qui était arrivé au convoi volatilisé. Il vous faudra
également éclaircir le mystère qui plane désormais sur la
province de Ruanon. Le roi a réuni un détachement de
patrouilleurs frontaliers, une unité d'éclaireurs d'élite composée
de cavaliers aguerris spécialisés dans les techniques de survie en
milieu hostile. Le monarque a ordonné à ces cinquante hommes de vous accompagner en espérant que, sous votre
commandement, ils pourront réussir là où ont échoué des forces
plus nombreuses et sans doute trop visibles.
Tandis que vos hommes et vous-même vous rendez à l'Armurerie
Royale pour y recevoir votre équipement, vous apercevez un
corbeau sur le rebord d'une haute fenêtre. Il s'envole presque
aussitôt, mais un frisson vous parcourt l'échine : à Holmgard, en
effet, le corbeau est un oiseau de mauvais augure...
"""

tab1, tab2 = st.tabs(["Page", "Inventaire"])

with tab1:
    st.subheader("Le capitaine Gayal a disparu...")
    st.write(fr_text)
    st.page_link("tomes/tome4/page_1.py", label="1", icon="📄")

with tab2:
    display_inventory()

if st.session_state.pop("checkpoint_pending", False):
    save_checkpoint()  # le héros pourra retenter ce tome depuis ici s'il meurt
save_game()
