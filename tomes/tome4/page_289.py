import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=289, book=4)

fr_text = """
Vous suivez le capitaine Gayal qui descend quatre à quatre le
large escalier de la tour de guet, puis se précipite vers la
barricade. Un grondement sonore, comme un lointain tonnerre,
retentit alentour. La cavalerie ennemie envahit la plaine de tous
côtés et se prépare à l'attaque. Des colonnes de soldats à pied,
revêtus d'armures écarlates, avancent parmi les chevaux en
poussant devant eux une foule de civils terrifiés. « Ce sont des
habitants de Ruanon ! s'écrie le capitaine Gayal, la main en
visière au-dessus des yeux. Ce chien de Barraka s'en sert comme
boucliers ! Autour de vous, les hommes du capitaine Gayal ont
tendu leurs arcs, attendant le signal de tirer. Le capitaine
cependant n'ose pas en donner l'ordre. Soudain, une catapulte
projette dans les airs un énorme rocher noir en direction de la
barricade. Horrifié, vous le voyez prendre feu et se désintégrer en
déversant une pluie d'huile enflammée sur les soldats du
Sommerlund. Ces derniers ne peuvent s'enfuir et nombre d'entre
eux sont gravement brûlés avant qu'on ait pu éteindre les
flammes. Un cri de guerre retentit alors dans les rangs ennemis.
C'est le signal de l'attaque. Les habitants de Ruanon sont écartés
et piétinés par les hordes de Guerriers écarlates qui se portent à
l'assaut de la barricade. La pluie d'huile enflammée a dispersé les
hommes du capitaine Gayal, et la barricade n'est plus que
sommairement défendue. Un instant plus tard, vous entendez le
capitaine crier votre nom. Sa cape et sa tunique sont en feu et il
vous appelle au secours.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez aider le capitaine, rendez-vous au :'))
    st.page_link("tomes/tome4/page_5.py", label="5", icon="📄")
    st.write_stream(stream_text("Si vous préférez rassembler les soldats avant que l'ennemi ait atteint la barricade, rendez-vous au :"))
    st.page_link("tomes/tome4/page_86.py", label="86", icon="📄")
    st.write_stream(stream_text('Enfin, si vous avez atteint le rang Kaï de Guerrier (ce qui signifie que vous maîtrisez huit Disciplines Kaï), rendez-vous au :'))
    if kai_rank() >= 8:
        st.page_link("tomes/tome4/page_255.py", label="255", icon="📄")
    else:
        st.write_stream(stream_text("Vous n'avez pas atteint le rang Kaï de Guerrier."))
        st.page_link("tomes/tome4/page_255.py", label="255", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
