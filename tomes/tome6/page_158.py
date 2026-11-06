import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=158, book=6)

fr_text = """
Le passage mène à une grande cave voûtée, aussi froide et
silencieuse qu'un tombeau. Gwynian dit quelques mots à ses
frères qui se dirigent ensuite en toute hâte vers un portail assez
éloigné. Tandis qu'ils disparaissent dans les ténèbres, Gwynian
revient vers vous, l'air soucieux mais calme : « La Pierre de la
Sagesse de Varetta est cachée dans la crypte de la cathédrale de
Tekaro. Cette Clé sert à ouvrir la tombe où elle est dissimulée. »
Il vous tend une Clé en Argent et poursuit : « Mes frères vous
procureront un cheval rapide pour le voyage. Lorsque la pendule
de l'Observatoire sonnera minuit, sortez par le portail et suivez le
passage souterrain jusqu'au bout, il vous mènera de l'autre côté
des remparts de la ville. Votre cheval vous attendra à la sortie du
souterrain. N'hésitez pas à prendre ici tout ce dont vous pourriez
avoir besoin pour votre expédition. Et maintenant, que les dieux
vous protègent, Loup Solitaire ! » Après avoir vivement remercié
Gwynian, vous le regardez disparaître à son tour par le portail.
La cave est remplie de provisions et vous découvrez parmi tout le
matériel, des objets qui pourraient se révéler utiles lors de votre
voyage pour Tekaro :
Un Bâton
Des Vivres équivalant à 3 Repas
Une Masse Un Sifflet en Cuivre Une Corde Un Sabre
En plus de la Clé en Argent que Gwynian vient de vous remettre
(inscrivez-la dans la case Objets Spéciaux de votre Feuille
d'Aventure, puis gardez-la précieusement dans votre poche),
vous pouvez rassembler tous les Objets et Provisions que vous
souhaitez emporter avant de vous installer, en attendant que les
douze coups de minuit sonnent au clocher.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("CLÉ EN ARGENT")
    st.success("Vous recevez la Clé en Argent (Objet Spécial).")

    pickup_button("BÂTON", key="baton", label="Prendre le Bâton")
    pickup_button("REPAS", key="vivres_1", label="Prendre 1 Repas")
    pickup_button("REPAS", key="vivres_2", label="Prendre 1 Repas")
    pickup_button("REPAS", key="vivres_3", label="Prendre 1 Repas")
    pickup_button("MASSE D'ARMES", key="masse", label="Prendre la Masse")
    pickup_button("SIFFLET DE CUIVRE", key="sifflet", label="Prendre le Sifflet en Cuivre")
    pickup_button("CORDE", key="corde", label="Prendre la Corde")
    pickup_button("SABRE", key="sabre", label="Prendre le Sabre")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_175.py", label="175", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
