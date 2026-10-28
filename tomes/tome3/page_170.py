import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

fr_unknown_item = "Vous ne possédez pas cet objet."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=170, book=3)

fr_text = """
A l'aide d'un pan de votre cape, vous effacez une partie du
pentagramme, traçant ainsi un chemin suffisamment large pour
que l'homme puisse s'en échapper. Vous êtes alors frappé par sa
maigreur impressionnante et vous constatez qu'il a du mal à se
maintenir debout. « Soyez remercié, Seigneur Kaï, dit-il, si
jamais nous parvenons à nous enfuir d'Ikaya, je m'efforcerai de
payer la dette de reconnaissance que j'ai désormais envers vous ;
il vaut mieux que vous passiez devant, ajoute-t-il, car j'ai quant à
moi trop mal aux yeux pour voir clairement : j'ai été atteint, en
effet, de cécité des neiges et j'en subis encore les séquelles. »
Vous ouvrez donc la marche le long du passage et vous vous
apprêtez à emprunter le couloir principal en direction du nord
lorsque deux mains aux doigts d'acier vous attrapent soudain
par-derrière et se referment autour de votre cou. Un terrible
hurlement trahit alors la véritable identité du marchand : c'est en
fait un Monstre d'Enfer, un redoutable serviteur des Maîtres des
Ténèbres, un mort vivant doué de la faculté de changer
d'apparence à sa guise. Il vous a menti pour que vous le libériez
du pentagramme et, à présent qu'il n'a plus besoin de vous, il
tente de vous tuer. Vous vous efforcez désespérément de
reprendre votre respiration tandis que les doigts squelettiques de
votre agresseur vous brûlent sous leur étreinte en essayant de
vous déchirer la gorge. Vous perdez aussitôt 6 points
d'ENDURANCE. Si vous êtes toujours vivant, vous parvenez
enfin à vous dégager, mais il vous faut à présent affronter la
créature dans un combat à mort. Compte tenu de la brusquerie
de l'attaque, vous n'avez pas le temps d'avaler quelque potion
que ce soit avant d'engager le combat.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-6)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-6)
    st.write_stream(stream_text('Si vous possédez le Glaive de Sommer, rendez-vous au :'))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome3/page_304.py", label="304", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_304.py", label="304", icon="📄", disabled=True)
    st.write_stream(stream_text('Dans le cas contraire, rendez-vous au :'))
    st.page_link("tomes/tome3/page_175.py", label="175", icon="📄", disabled=has_item("GLAIVE DE SOMMER"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
