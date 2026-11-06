import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=211, book=6)

fr_text = """
Le Capitaine est impressionnant. C'est un homme aux muscles
puissants, et son visage au menton volontaire ne semble marqué
ni par la maladie ni par les combats. Ses cheveux blonds sont
coupés ras, et une courte barbe mange sa figure hâlée. Il vous
invite à sa table et, tout en buvant votre bière, vous écoutez les
hommes de sa compagnie raconter leurs prouesses guerrières. Ils
parlent de victoires, de pillages et de butins, mais jamais de
défaites ! Le Capitaine et ses hommes sont las de faire la guerre
dans le Nord. Le Prince Tanveal d'Hélin est au bord de la ruine.
Il a dû vendre la presque totalité de ses biens pour financer la
guerre contre le Baron Maghao de Karkaste, guerre qu'il ne peut
plus espérer gagner maintenant. Le moral des troupes du Prince
est au plus bas, et ses mercenaires désertent à la première
occasion. Vous apprenez ensuite que le Capitaine recrute des
hommes pour une campagne dans le Sud. La guerre fait rage
entre la Salonie et la Slovie, et il y a beaucoup d'or à gagner pour
ceux qui veulent s'engager au service du Prince salonien Ewewin
qui assiège la cité de Tekaro. « Vous semblez être un guerrier
habile et expérimenté, vous dit le Capitaine en vous fixant de ses
yeux bleu acier. Pourquoi ne rejoindriez-vous pas ma compagnie ? J'ai besoin de combattants solides, et je paie en espèces
sonnantes et trébuchantes, non pas avec des promesses ! Nous
partons à l'aube pour Tekaro. Voulez-vous venir avec nous ? »
Vous déclinez poliment son offre en expliquant que vous êtes
venu à Varetta pour régler une affaire personnelle. « A part la
guerre, quelle affaire peut retenir un guerrier ? rétorque-t-il en se
tournant vers ses hommes qui approuvent hautement. Si jamais
vous changez d'avis, rejoignez-nous à Soren d'où nous
embarquerons dans deux jours. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez une carte de Varetta, rendez-vous au :"))
    if has_item("PLAN DE VARETTA"):
        st.page_link("tomes/tome6/page_17.py", label="17", icon="📄")
    else:
        st.write("*Vous ne possédez pas de carte de Varetta.*")
        st.page_link("tomes/tome6/page_17.py", label="17", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous ne possédez pas cet Objet Spécial, rendez-vous au :"))
    if has_item("PLAN DE VARETTA"):
        st.page_link("tomes/tome6/page_104.py", label="104", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome6/page_104.py", label="104", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
