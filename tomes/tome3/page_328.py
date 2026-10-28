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
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=328, book=3)

fr_unknown_item = "Vous ne possédez pas cet objet."
fr_has_sommerswerd = "Vous possédez le Glaive de Sommer."

fr_text = """
En dépit de sa frêle constitution, l'homme monte à la Corde avec
une rapidité et une agilité surprenantes. Vous le hissez à travers
l'ouverture et vous récupérez votre Corde. « L'escalier, dit-il en
montrant l'obscurité, c'est par là que nous pourrons nous enfuir,
mais il vaut mieux que vous passiez devant. J'ai en effet trop mal
aux yeux pour y voir clairement : les séquelles de la cécité des
neiges. » Vous rangez votre Corde dans votre Sac à Dos et vous
avancez le long du passage. Vous vous apprêtez à descendre les
marches lorsque des mains squelettiques vous saisissent par-
derrière et se referment autour de votre cou. Un cri terrifiant
trahit alors la véritable identité du prétendu « marchand ». C'est
en fait un Monstre d'Enfer, un redoutable serviteur des Maîtres
des Ténèbres, une créature qui a la faculté de changer
d'apparence à sa guise. Le Monstre a réussi à vous convaincre de
le libérer et il a maintenant l'intention de vous tuer. Vous tentez
désespérément de reprendre votre souffle tandis que les
phalanges décharnées de la créature vous déchirent et vous
brûlent la gorge. Vous perdez aussitôt 6 points d'ENDURANCE.
Si vous êtes toujours vivant, vous parvenez enfin à vous libérer
de l'étreinte d'acier mais il vous faut à présent engager avec le
Monstre un combat à mort. La surprise de l'attaque et la blessure
que votre agresseur vous a infligée au cou vous interdisent
d'avaler quelque Potion que ce soit avant de l'affronter.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-6)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-6)
    st.write_stream(stream_text("Si vous possédez le Glaive de Sommer, rendez-vous au :"))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome3/page_99.py", label="99", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_99.py", label="99", icon="📄", disabled=True)
    st.write_stream(stream_text("Sinon, rendez-vous au :"))
    if not has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome3/page_175.py", label="175", icon="📄")
    else:
        st.write_stream(stream_text(fr_has_sommerswerd))
        st.page_link("tomes/tome3/page_175.py", label="175", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
