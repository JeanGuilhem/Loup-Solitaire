import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=224, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Le grand oiseau noir fait battre ses puissantes ailes en poussant
des croassements rauques. Ses yeux noirs et féroces vous fixent
agressivement tandis que vous approchez de son perchoir. Vous
essayez de monter sur la selle en vous accrochant au pommeau
mais, vif comme l'éclair, l'oiseau tente de vous désarçonner d'un
grand coup de patte. Instinctivement, vous vous protégez le
visage tandis qu'à quelques centimètres de votre tête, l'Itikar
fouette l'air de son bec courbe où se reflète la lumière jaune du
soleil.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Communication Animale, rendez-vous au :"))
    if has_kai("Communication Animale"):
        st.page_link("tomes/tome5/page_308.py", label="308", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_308.py", label="308", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous possédez un Médaillon d'Onyx, rendez-vous au :"))
    if has_item("MÉDAILLON D'ONYX"):
        st.page_link("tomes/tome5/page_319.py", label="319", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_319.py", label="319", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne répondez à aucune de ces conditions, utilisez la Table de Hasard pour obtenir un chiffre. Si vous avez atteint le titre d'Aspirant Kaï ou bien un titre plus élevé, ajoutez 2 au chiffre obtenu."))
    if has_kai("Communication Animale") or has_item("MÉDAILLON D'ONYX"):
        st.write("*Vous répondez à l'une de ces conditions : la Table de Hasard ne vous concerne pas.*")
        for n in (287, 240, 370, 257):
            st.page_link(f"tomes/tome5/page_{n}.py", label=str(n), icon="📄", disabled=True)
    else:
        roll = hazard_roll()
        if roll is not None:
            bonus = 2 if kai_rank() >= 6 else 0
            total = roll + bonus
            if bonus:
                st.write(f"*Bonus : +{bonus}, soit un total de {total}.*")
            if total >= 8:
                st.write_stream(stream_text("Si votre total est compris entre 8 et 11, rendez-vous au :"))
                st.page_link("tomes/tome5/page_287.py", label="287", icon="📄")
            elif total >= 4:
                st.write_stream(stream_text("Si votre total est compris entre 4 et 7, rendez-vous au :"))
                st.page_link("tomes/tome5/page_240.py", label="240", icon="📄")
            elif total >= 1:
                st.write_stream(stream_text("Si votre total est compris entre 1 et 3, rendez-vous au :"))
                st.page_link("tomes/tome5/page_370.py", label="370", icon="📄")
            else:
                st.write_stream(stream_text("Si enfin, vous avez tiré un 0, rendez-vous au :"))
                st.page_link("tomes/tome5/page_257.py", label="257", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
