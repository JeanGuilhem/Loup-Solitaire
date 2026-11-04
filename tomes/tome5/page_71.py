import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=71, book=5)

fr_text = """
Après vous être rapidement nettoyé, vous sortez du bain et vous
pénétrez dans une petite pièce où règne une chaleur torride qui
sèche vos vêtements en quelques instants. A côté de cette
antichambre se trouve une autre salle, remplie de monde, où les
conversations vont bon train. Vous êtes à présent dans les Bains
Publics de Barrakeesh. Cet établissement fait la fierté des
citoyens de la ville et l'envie des autres cités du désert où l'eau est
rare et utilisée avec parcimonie. Les habitants de Barrakeesh ont
fait des Bains Publics une sorte de forum où l'on se rassemble
pour discuter avec des amis. D'après ce que vous saisissez des
propos échangés, le Zakhan est le sujet principal des
conversations... et l'on ne dit pas grand bien de lui ! Après vous
être enveloppé dans une grande Serviette, vous vous frayez un
chemin parmi la foule et vous vous dirigez vers la principale
porte de sortie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez garder la Serviette une fois dehors, elle équivaudra à deux objets de votre Sac à Dos en raison de son encombrement."))
    pickup_button("SERVIETTE", key="serviette", label="Garder la Serviette")
    st.write_stream(stream_text("Rendez-vous maintenant au :"))
    st.page_link("tomes/tome5/page_54.py", label="54", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
