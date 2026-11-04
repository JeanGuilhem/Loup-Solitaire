import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=237, book=5)

fr_text = """
Le Jala est aussi bon qu'il en a l'air, et après votre expédition à
travers les collines poussiéreuses, ce vin est une véritable
bénédiction pour votre gorge irritée et desséchée. Vous gagnez 1
point d'ENDURANCE. « Savez-vous où nous pourrions trouver
un homme appelé Tipasa le Vagabond », demande Banedon en
parvenant à dissimuler son accent des Contrées du Nord grâce à
sa maîtrise parfaite du dialecte Ikareshi. « Désolé, l'ami, mais je
n'ai jamais entendu parler de lui », réplique l'un des hommes.
«Vous devriez demander à la veuve Soushilla, interrompt l'autre.
Elle est au courant de tout ce qui se passe à Ikaresh. » « Où peut-on la trouver ? » leur demandez-vous encore. « A la taverne, bien
sûr ! » répondent-ils en chœur. Traversez la place de l'Aigle, et
vous la trouverez sur le chemin du marché aux Douggas. Vous
remerciez l'Ikareshi et vous quittez l'auberge. En revenant sur
vos pas, vers la place, vous prenez le chemin du marché aux
Douggas et vous partez à la recherche de la veuve Soushilla.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=1)

    st.write_stream(stream_text("Rendez-vous maintenant au :"))
    st.page_link("tomes/tome5/page_376.py", label="376", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
