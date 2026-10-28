#!/usr/bin/env python3
import random
import time
import streamlit as st

from variable import AI_INSTRUCTION, GEMINI_API_KEY

def change_visiblity(variable: bool):
    """
    Used when LS check one item to pick up into his bag.
    Change the variable in parameter that'll be used to able/disable checkbox
    """
    return not variable


def set_cookies() -> None:
    """Sauvegarde la partie. Conservé pour compatibilité : end_page() le fait déjà."""
    from save import save_game

    save_game()


def called_cookies() -> bool:
    """
    Recharge la partie depuis le cookie (rechargement du navigateur en cours de partie).
    Renvoie True si l'état est restauré, False s'il faut arrêter le rendu de la page.
    """
    from inventory import init_state
    from save import apply_save, read_save

    data = read_save()
    if data == "pending":
        st.info("Chargement de votre sauvegarde...")
        return False
    if data is None:
        st.error(
            "Aucune sauvegarde trouvée. Si vous étiez en cours de partie, il vous faudra recommencer."
        )
        checkpoint_button()
        st.page_link("tomes/tome1/crafting_hero.py", label="Démarrer mon aventure", icon="⚔️")
        return False

    init_state()
    apply_save(data)
    return True


def ls_death():
    """
    Ths method is called when the LS died.
    """
    from game_stats import record_death
    from save import delete_save

    record_death()
    delete_save()  # sinon un rechargement du navigateur ramènerait la partie à la vie
    st.error(
        "Vous êtes mort ! Votre aventure s'arrête ici, ainsi que la lignée des Kai."
    )
    show_adventure_stats()
    checkpoint_button(book=st.session_state.get("book"))
    st.page_link("tomes/tome1/crafting_hero.py", label="Démarrer mon aventure", icon="⚔️")
    st.stop()


def track_lowest_endurance() -> None:
    """Retient l'ENDURANCE la plus basse du tome en cours (bilan de fin de partie)."""
    lowest = st.session_state.get("lowest_endurance")
    endurance = max(0, st.session_state.get("endurance", 0))
    if lowest is None or endurance < lowest:
        st.session_state.lowest_endurance = endurance


def show_adventure_stats() -> None:
    """Bilan du tome en cours, affiché à la mort du héros et au dernier paragraphe du tome."""
    track_lowest_endurance()
    pages = st.session_state.get("pages_visited", 0)
    here = (st.session_state.get("book"), st.session_state.get("current_page_number"))
    if st.session_state.get("last_recorded_page") != list(here):
        pages += 1  # la page de mort s'arrête avant d'être comptée
    st.subheader(f"Votre aventure dans le tome {st.session_state.get('book', 1)}")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Paragraphes parcourus", pages)
    col2.metric("Combats", st.session_state.get("fights", 0))
    col3.metric("Ennemis vaincus", st.session_state.get("enemies_defeated", 0))
    col4.metric("Endurance la plus basse", st.session_state.lowest_endurance)


def checkpoint_button(book: int = None) -> None:
    """
    « Recommencer le tome N avec mon héros » : repart du point de reprise (le héros au début du
    tome, cf. save.CHECKPOINT_COOKIE), s'il y en a un (et s'il est de ce tome quand book est donné).
    """
    from game_stats import record_start
    from inventory import init_state
    from save import apply_save, page_path, read_checkpoint

    data = read_checkpoint()
    if not isinstance(data, dict) or (book and data.get("book") != book):
        return
    if st.button(f"Recommencer le tome {data['book']} avec mon héros", icon="🔁", type="primary"):
        st.session_state.pop("death_recorded", None)
        init_state()
        apply_save(data)
        st.session_state.game_phase = "playing"
        record_start(continued=True, retry=True)
        st.switch_page(page_path(0, data["book"]))


def table_des_hasards() -> int:
    """
    Chose between 0 et 9 (for the book, here 1 to 10)
    """
    res = random.randint(1, 10)
    return res


def hazard_roll(
    key: str = "hazard", label: str = "Utilisez la Table de Hasard pour obtenir un chiffre."
):
    """
    Bouton de tirage sur la Table de Hasard, une seule fois par visite de la page.
    Renvoie le chiffre tiré, de 0 à 9 comme dans le livre, ou None tant que le joueur n'a pas tiré.
    """
    state_key = f"hazard_{key}"
    if state_key not in st.session_state:
        if not st.button(label, key=f"{state_key}_button"):
            return None
        st.session_state[state_key] = table_des_hasards() % 10
        st.rerun()  # retire le bouton tout de suite
    st.write(f"*Vous avez tiré le {st.session_state[state_key]}.*")
    return st.session_state[state_key]


def stream_text(text: str, time_to_sleep: float = 0.03):
    """
    Affiche le texte mot à mot, une seule fois par visite de la page : lors des reruns
    (clic sur un bouton, sauvegarde...) il est affiché d'un coup.
    """
    streamed = st.session_state.setdefault("streamed_texts", [])
    if text in streamed:
        yield text
        return
    for word in text.split():
        yield word + " "
        time.sleep(time_to_sleep)
    streamed.append(text)


def handle_repas(penalty: int = 3, gold_cost: int = 0, hunting: bool = True):
    """
    Le Loup Solitaire doit prendre un Repas : la Chasse l'en dispense (si `hunting`), sinon il mange
    un Repas du Sac à Dos (ou sa Moisson de Laumspur, qui rend aussi 3 points d'ENDURANCE), sinon il
    paie `gold_cost` Couronnes s'il le peut (repas à l'auberge), et à défaut il perd `penalty` points
    d'ENDURANCE.
    """
    from inventory import change_endurance, has_kai, is_new_page, remove_from_inventory, spend_gold

    if not is_new_page():
        return

    if hunting and has_kai("La Chasse"):
        st.success(
            "*Grâce à votre Discipline Kaï de la Chasse, vous trouvez votre nourriture par vous-même.*"
        )
    elif remove_from_inventory("REPAS"):
        st.success("Vous avez mangé. 1 Repas vous a été retiré.")
    elif remove_from_inventory("MOISSON DE LAUMSPUR"):
        st.success("Vous mangez votre Moisson de Laumspur : +3 points d'ENDURANCE.")
        change_endurance(3)
    elif gold_cost and spend_gold(gold_cost):
        st.success(f"Vous payez votre repas {gold_cost} Couronne(s).")
    else:
        st.error(f"Vous n'aviez pas de Repas. Vous perdez {penalty} points d'ENDURANCE.")
        st.metric(label="Endurance", value=max(0, st.session_state.endurance - penalty), delta=-penalty)
        change_endurance(-penalty)


def ai_generate_page(page_text: str, page_number: int):
    """
    Using gemini to generate page content.

    Args:
        page_text (str): A page
    """
    from google import genai
    from google.genai import types

    print(f"Page number: {page_number}")

    prompt = f"Convertis ce contenu brut de la page {page_number} en script Python Streamlit en appliquant toutes les règles. Le contenu est : \n---\n{page_text}\n---"

    with open("template.py", "r") as template_file:
        template_content = template_file.read()

    instructions = AI_INSTRUCTION.replace("#TEMPLATE#", template_content)

    config = types.GenerateContentConfig(
        system_instruction=instructions,
        temperature=0.0,  # Très faible, car nous voulons un formatage précis et non créatif
    )

    try:
        print("Generating response...")
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=config,
        )

        print("Creating page...")
        file_name = f"tomes/tome1/page_{page_number}.py"
        with open(file_name, "w", encoding="utf-8") as f:
            code = response.text.strip().replace("```python", "").replace("```", "")
            f.write(code)

        print(f"✅ Fichier {file_name} généré avec succès.")

    except Exception as e:
        print(f"❌ Erreur lors de la génération de la page {page_number}: {e}")


def extract_chapters_from_pdf(pdf_path: str, max_chapters: int = 350) -> dict:
    """
    Extrait le texte d'un PDF, identifie les chapitres par un numéro seul
    sur une ligne, et les stocke dans un dictionnaire.

    Args:
        pdf_path: Chemin vers le fichier PDF de Loup Solitaire.
        max_chapters: Limite supérieure du numéro de chapitre attendu (ex: 350).

    Returns:
        Un dictionnaire {numéro_de_page: contenu_texte_brut}.
    """
    import fitz
    import re

    CHAPTER_START_PATTERN = re.compile(r"^\s*(\d{1,3})\s*$")

    chapters = {}
    current_page_num = 0
    current_chapter_text = []

    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Erreur lors de l'ouverture du fichier PDF: {e}")
        return {}

    print(f"Nombre de pages dans le PDF: {doc.page_count}")

    for page_num_pdf in range(doc.page_count):
        page = doc.load_page(page_num_pdf)
        text = page.get_text("text")

        lines = text.splitlines()

        for line in lines:
            line_stripped = line.strip()

            match = CHAPTER_START_PATTERN.search(line_stripped)

            # Un chapitre commence par une ligne ne contenant que son numéro. Les paragraphes se
            # suivent dans l'ordre, donc seul le numéro suivant est un vrai marqueur : un autre
            # nombre seul sur sa ligne est une destination coupée par un saut de page
            # (« rendez-vous au » / « 217 »), qu'il faut garder dans le texte.
            previous_line = current_chapter_text[-1] if current_chapter_text else ""
            is_marker = (
                match is not None
                and int(match.group(1)) == current_page_num + 1
                and int(match.group(1)) <= max_chapters
                and not re.search(r"\bau$", previous_line)
            )

            if is_marker:
                if current_page_num != 0:
                    chapters[current_page_num] = "\n".join(current_chapter_text).strip()
                current_page_num = int(match.group(1))
                current_chapter_text = []

            elif current_page_num != 0:
                # Filtre pour éviter les lignes trop courtes (pieds de page, etc.), sauf celles qui
                # portent un numéro de destination (« 217 », « 111. », « au 5. »)
                if re.search(r"\d", line_stripped) or len(line_stripped) > 5:
                    current_chapter_text.append(line_stripped)

    # Sauvegarder le dernier chapitre
    if current_chapter_text and current_page_num != 0:
        chapters[current_page_num] = "\n".join(current_chapter_text).strip()

    # for number, text in chapters.items():
    #     print("="*50)
    #     print(number)
    #     print(text)

    return chapters


if __name__ == "__main__":
    #     page_text = """
    # Vous parvenez bientôt à une petite clairière. En son centre, vous
    # trouvez un banc taillé dans le tronc d'un arbre.
    # Vous avez faim, et il vous faut prendre un Repas, sinon, vous
    # perdrez 3 points d'ENDURANCE. Lorsque vous avez fini de
    # manger, vous pourrez quitter la clairière par le sud en vous
    # rendant au 28. Mais si vous préférez emprunter le sentier plus
    # étroit qui mène vers l'est en s'enfonçant dans la forêt, rendezvous au 201.
    # """
    #     # ai_generate_page(page_number=130, page_text=page_text)
    #     chapters = extract_chapters_from_pdf(pdf_path="./tome1.pdf")

    #     for page_number, page_text in chapters.items():
    #         if int(page_number)<149:
    #             continue
    #         ai_generate_page(page_number=page_number, page_text=page_text)
    #         time.sleep(20)
    pass
