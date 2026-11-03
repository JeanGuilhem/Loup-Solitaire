import streamlit as st
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

check_inventory(current_page_number=116, book=4)

fr_text = """
« J'espérais bien que le roi enverrait un détachement pour partir
à notre recherche, dit le capitaine Gayal qui a retrouvé à présent
toutes ses forces. Je commençais à être fatigué de cette ville.
Vous vous redressez sur votre paillasse et vous remerciez le
capitaine. En agissant avec courage et au moment opportun, il
vous a sauvé d'une mort certaine. « Ce n'est rien, comparé à vos
exploits, Loup Solitaire, répond-il. Votre vaillance est légendaire
et votre présence ici vaut celle de cent hommes. » Il vous
demande de lui parler de votre mission et vous lui racontez les
événements qui vous ont conduit à le retrouver : votre marche
vers le sud, la perte de vos hommes, la traversée des mines de
Maaken et les brigands. « Oui, les brigands, les hommes d'un
certain Barraka, dit le capitaine Gayal d'une voix qui exprime
tout le mépris qu'il leur porte, à eux et à leur chef. Nous avons eu
tous deux à souffrir des méfaits de Barraka. Il y a un mois, il m'a
tendu une embuscade sur la voie de Ruanon en compagnie de ses
renégats vassagoniens. Nous étions largement surpassés en
nombre et le combat fut acharné, mais finalement nous avons
réussi à leur échapper et à nous réfugier ici à Ruanon. Depuis ce
temps, nous avons été assiégés sans relâche en espérant qu'on
nous enverrait de l'aide. Nous avons suffisamment d'armes pour
leur résister, mais nous commençons à manquer de vivres et
d'eau. » Vous lui demandez ensuite ce qu'il est advenu des
habitants de Ruanon. « La plupart sont devenus des esclaves de
Barraka qui les a emmenés dans les mines pour lui servir de
main d'œuvre, répond-il. En dehors de vous, un seul homme a pu
s'échapper des mines et survivre aux attaques des Chiens de
Guerre et des patrouilles de brigands. Cet homme est le baron
Oren Vanalund. Venez, je vais vous conduire auprès de lui. » Le
capitaine Gayal vous mène à la plus haute salle de la tour de guet
et pousse une porte ornée de ferrures. La vision qui s'offre alors à
vous vous remplit de chagrin et de pitié.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_318.py", label="318", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
