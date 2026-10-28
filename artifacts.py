"""
Écran d'équipement façon « artefacts » (Crusader Kings 3) : le Loup Solitaire au centre, ses
emplacements autour (tête, corps, mains, fourreau, bourse), les autres Objets Spéciaux en dessous,
et la fiche de l'objet choisi (rareté, effets, histoire, provenance).

La rareté et l'histoire des objets sont ici, la provenance dans st.session_state.provenance.
"""
import base64
import html

import streamlit as st

from variable import ITEMS, MAX_PURSE

RARITIES = {
    "ordinaire": {"label": "Ordinaire", "color": "#9a9a8e"},
    "peu_commun": {"label": "Peu commun", "color": "#5fae6e"},  # pièces d'équipement de qualité
    "unique": {"label": "Unique", "color": "#5b8fd6"},  # objets propres à l'histoire
    "legendaire": {"label": "Légendaire", "color": "#e0b54a"},
}

RARITY = {
    # Peu commun
    "CASQUE": "peu_commun",
    "COTTE DE MAILLES": "peu_commun",
    "BOUCLIER": "peu_commun",
    "GILET DE CUIR MATELASSÉ": "peu_commun",
    # Unique
    "ÉPÉE DU PRINCE": "unique",
    "SCEAU D'HAMMARDAL": "unique",
    "PENDENTIF À L'ÉTOILE DE CRISTAL": "unique",
    "LANCE MAGIQUE": "unique",
    "CLÉ D'OR": "unique",
    "CLÉ D'ARGENT": "unique",
    "PARCHEMIN": "unique",
    "PIERRES PRÉCIEUSES": "unique",
    "BILLET DE DILIGENCE": "unique",
    "LAISSEZ-PASSER BLANC": "unique",
    "LAISSEZ-PASSER ROUGE": "unique",
    "DOCUMENTS": "unique",
    "CASQUE D'ARGENT": "unique",
    "DISQUE DE PIERRE BLEUE": "unique",
    "TRIANGLE DE PIERRE BLEUE": "unique",
    "BRACELET D'OR": "unique",
    "EFFIGIE": "unique",
    "DIAMANT": "unique",
    "SPHÈRE DE FEU": "unique",
    "PIERRE RAYONNANTE": "unique",
    # Légendaire
    "GLAIVE DE SOMMER": "legendaire",
}

LORE = {
    "GLAIVE DE SOMMER": "Forgé avant que les hommes ne peuplent les Fins de Terre par une lignée que l'on "
    "appellerait divine, l'Épée du Soleil abattit Vashna au gouffre de Maaken. Seul un Seigneur Kaï "
    "peut en éveiller la puissance ; c'est la seule arme du nord de Magnamund capable de tuer un "
    "Maître des Ténèbres.",
    "SCEAU D'HAMMARDAL": "Anneau d'or frappé du sceau royal de Durenor, offert au Sommerlund par le roi "
    "Alin en gage de l'alliance des deux royaumes après la défaite de Vashna.",
    "PENDENTIF À L'ÉTOILE DE CRISTAL": "Symbole de la Confrérie de l'Étoile de Cristal, offert par le "
    "jeune magicien Banedon.",
    "LANCE MAGIQUE": "Une lance de métal gravée de runes, aussi légère que du bois. Elle fut retirée de "
    "la poitrine d'un Monstre d'Enfer, qu'elle seule pouvait blesser.",
    "BOUCLIER": "Pris à l'Arsenal du Palais de Holmgard, avant le départ pour Durenor.",
    "COTTE DE MAILLES": "Une cotte de mailles d'acier qui protège le torse.",
    "CASQUE": "Un casque de fer cabossé mais solide.",
}

# Emplacement -> (libellé, icône, placement). Tête et mains sont dans la grille de 3 colonnes ;
# corps, bourse et fourreau sont posés sur la silhouette (classes « ov-… », positions en % de la figure).
SLOTS = {
    "head": ("Tête", "helmet", "grid-column:2;grid-row:1;justify-self:center;width:min(130px, 100%);"),
    "right": ("Main droite", "sword", "grid-column:1;grid-row:2;"),
    "left": ("Main gauche", "shield", "grid-column:3;grid-row:2;"),
    "body": ("Corps", "mail", "ov ov-body"),
    "purse": ("Bourse", "purse", "ov ov-side ov-purse"),
    "scabbard": ("Fourreau", "scabbard", "ov ov-side ov-scabbard"),
}
ON_FIGURE = ("body", "purse", "scabbard")

HIDDEN = {"CARTE GÉOGRAPHIQUE"}  # toujours possédée : ne l'affiche pas, c'est du bruit visuel

# Icônes au trait, 24×24
ICONS = {
    "helmet": '<path d="M4 15a8 8 0 0 1 16 0v3H4z"/><path d="M12 7v11M8 18v3M16 18v3"/>',
    "mail": '<path d="M7 3 4 6v13h16V6l-3-3-5 3z"/><path d="M8 10h8M8 14h8M8 18h8M12 6v14"/>',
    "sword": '<path d="M19 3 9 13M19 3v4M19 3h-4"/><path d="m6 14 4 4M7 17l-3 3"/>',
    "shield": '<path d="M12 3 5 6v6c0 4 3 7 7 9 4-2 7-5 7-9V6z"/><path d="M12 3v18M5 11h14"/>',
    "scabbard": '<path d="M9 4h6l-1 13-2 4-2-4z"/><path d="M8 4h8"/>',
    "purse": '<path d="M9 6c0-2 6-2 6 0"/><path d="M6 9c0-2 12-2 12 0l1 9c0 2-14 2-14 0z"/><path d="M10 13h4"/>',
    "ring": '<circle cx="12" cy="15" r="5"/><path d="m10 7 2-3 2 3-2 3z"/>',
    "pendant": '<path d="M6 3c0 5 3 8 6 8s6-3 6-8"/><path d="m12 13 2 3-2 4-2-4z"/>',
    "scroll": '<path d="M7 4h11v13a3 3 0 0 1-3 3H6a2 2 0 0 1-2-2v-1h11"/><path d="M9 8h6M9 12h6"/>',
    "map": '<path d="m3 6 6-2 6 2 6-2v14l-6 2-6-2-6 2z"/><path d="M9 4v14M15 6v14"/>',
}


# Noms propres que str.capitalize() écraserait
PROPER_NAMES = ["Hammardal", "Sommer", "Étoile de Cristal", "Prince", "Glok"]


def display_name(item: str) -> str:
    """« SCEAU D'HAMMARDAL » -> « Sceau d'Hammardal »."""
    name = item.capitalize()
    for proper in PROPER_NAMES:
        name = name.replace(proper.lower(), proper)
    return name


def icon_img(icon: str, color: str, css_class: str = "") -> str:
    """Icône en <img> : st.html retire les balises <svg>, pas les images en data URI."""
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" '
        f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[icon]}</svg>'
    )
    data = base64.b64encode(svg.encode()).decode()
    return f'<img class="{css_class}" src="data:image/svg+xml;base64,{data}" alt="">'


def rarity_of(item: str) -> str:
    if item in RARITY:
        return RARITY[item]
    return "ordinaire"


def icon_of(item: str) -> str:
    info = ITEMS.get(item, {})
    if item == "GLAIVE DE SOMMER":
        return "scabbard"
    if info.get("type") == "weapon" or info.get("weapon"):
        return "sword"
    return {
        "CASQUE": "helmet", "COTTE DE MAILLES": "mail", "BOUCLIER": "shield", "SCEAU D'HAMMARDAL": "ring",
        "PENDENTIF À L'ÉTOILE DE CRISTAL": "pendant", "CARTE GÉOGRAPHIQUE": "map",
        "CASQUE D'ARGENT": "helmet", "GILET DE CUIR MATELASSÉ": "mail", "BRACELET D'OR": "ring",
        "TRIANGLE DE PIERRE BLEUE": "pendant",
    }.get(item, "scroll")


def effects_of(item: str) -> list:
    """Effets en jeu, lus dans le catalogue."""
    info = ITEMS.get(item, {})
    effects = []
    if item == "GLAIVE DE SOMMER":
        effects += ["+8 HABILETÉ au combat (+10 avec la Maîtrise de l'Épée)",
                    "Annule la magie ennemie", "Pertes d'ENDURANCE des morts vivants ×2"]
    elif info.get("combat_bonus"):
        effects.append(f"+{info['combat_bonus']} HABILETÉ au combat")
    if info.get("endurance_bonus"):
        effects.append(f"+{info['endurance_bonus']} ENDURANCE maximale")
    if info.get("heal"):
        effects.append(f"Rend {info['heal']} points d'ENDURANCE (une dose)")
    if info.get("combat_hability"):
        effects.append(f"+{info['combat_hability']} HABILETÉ pour un combat (une dose)")
    if (info.get("type") == "weapon" or info.get("weapon")) and item != "GLAIVE DE SOMMER":
        mastery = info.get("mastery")
        if mastery and mastery != item:
            effects.append(f"Compte comme {mastery.lower()} pour la Maîtrise des armes")
    return effects


def equipment_slots(hero: dict) -> tuple:
    """Répartit l'équipement du héros : {emplacement: objet ou None} et les Objets Spéciaux restants."""
    special = list(hero["special"])
    slots = {name: None for name in SLOTS}

    def take(slot, item):
        if item in special:
            special.remove(item)
            slots[slot] = item

    for item in HIDDEN:
        if item in special:
            special.remove(item)
    take("head", "CASQUE D'ARGENT")
    if slots["head"] is None:
        take("head", "CASQUE")
    take("body", "COTTE DE MAILLES")
    if slots["body"] is None:
        take("body", "GILET DE CUIR MATELASSÉ")
    take("scabbard", "GLAIVE DE SOMMER")
    if slots["scabbard"] is None:
        take("scabbard", "LANCE MAGIQUE")  # sans le Glaive de Sommer, la Lance Magique prend sa place
    hands = list(hero["weapons"]) + [item for item in special if ITEMS.get(item, {}).get("weapon")]
    for slot in ("right", "left"):
        if hands:
            item = hands.pop(0)
            slots[slot] = item
            if item in special:
                special.remove(item)
    if slots["left"] is None and "BOUCLIER" in special:
        take("left", "BOUCLIER")
    return slots, special


def _slot_html(slot: str, item, hero: dict) -> str:
    label, default_icon, placement = SLOTS[slot]
    css_class, style = (placement, "") if slot in ON_FIGURE else ("", placement)
    if slot == "purse":
        return _frame(label, "purse", f"{hero['purse']}/{MAX_PURSE}", "ordinaire", True, style, css_class)
    if item is None:
        return _frame(label, default_icon, "Vide", None, False, style, css_class)
    return _frame(label, icon_of(item), display_name(item), rarity_of(item), True, style, css_class)


def _frame(label: str, icon: str, text: str, rarity, filled: bool, style: str = "", extra_class: str = "") -> str:
    color = RARITIES[rarity]["color"] if rarity else "#6b6355"
    classes = " ".join(
        part for part in ("slot", "filled" if filled else "empty", rarity, extra_class) if part
    )
    return (
        f'<div class="{classes}" style="--rarity:{color};{style}">'
        f'{icon_img(icon, color, "slot-icon")}'
        f'<div class="slot-label">{html.escape(label)}</div>'
        f'<div class="slot-item">{html.escape(text)}</div></div>'
    )


# Silhouette centrée dans une figure plus large (160 × 230) : la bourse et le fourreau se posent
# de part et d'autre de la ceinture (y = 112).
SILHOUETTE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 230">
  <path d="M56 50 38 200c22 9 62 9 84 0L104 50z" fill="#4a2620" fill-opacity=".6"/>
  <g fill="#2b251d" stroke="#8c7444" stroke-width="1.2">
    <circle cx="80" cy="28" r="17"/>
    <path d="M58 52h44l10 62-10 4-6-40v60l6 70H90l-10-62-10 62H58l6-70V78l-6 40-10-4z"/>
  </g>
  <path d="M63 112h34" stroke="#8c7444" stroke-width="3"/>
</svg>"""
SILHOUETTE = (
    '<img class="hero" alt="" src="data:image/svg+xml;base64,'
    + base64.b64encode(SILHOUETTE_SVG.encode()).decode() + '">'
)

CSS = """
<style>
.ck-panel { background: radial-gradient(ellipse at 50% 35%, #3a3226 0%, #1c1813 75%);
  border: 2px solid #8c7444; border-radius: 10px; padding: 18px 14px 14px;
  box-shadow: inset 0 0 0 1px #2a241b, inset 0 0 40px #0008; color: #e9dfc8;
  font-family: Georgia, 'Times New Roman', serif; }
.ck-title { text-align: center; letter-spacing: .12em; text-transform: uppercase; font-size: .8rem;
  color: #c9a85c; margin-bottom: 12px; }
.ck-grid { display: grid; grid-template-columns: 1fr minmax(190px, 1.7fr) 1fr; gap: 10px; align-items: center; }
.ck-figure { grid-column: 2; grid-row: 2; position: relative; width: 100%; max-width: 250px;
  justify-self: center; aspect-ratio: 160 / 230; }
.hero { position: absolute; inset: 0; width: 100%; height: 100%; }
.slot.ov { position: absolute; min-height: 0; padding: 4px 3px; gap: 1px; }
.slot.ov .slot-icon { width: 22px; height: 22px; }
.slot.ov .slot-label { font-size: .52rem; letter-spacing: .05em; }
.slot.ov .slot-item { font-size: .66rem; }
.ov-body { left: 31%; width: 38%; top: 23%; height: 24%; background: #201b15e6; }
.ov-side { top: 44%; width: 27%; height: 30%; background: #201b15e6; }
.ov-purse { left: 1%; }
.ov-scabbard { right: 1%; }
.slot { position: relative; border: 2px solid var(--rarity); border-radius: 8px; padding: 8px 6px 6px;
  background: linear-gradient(180deg, #2c261d, #201b15); text-align: center; min-height: 86px;
  display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; }
.slot.empty { border-style: dashed; opacity: .55; }
.slot-icon { width: 30px; height: 30px; }
.slot-label { font-size: .62rem; letter-spacing: .08em; text-transform: uppercase; color: #a8987a; }
.slot-item { font-size: .78rem; line-height: 1.15; color: #f1e7cf; }
.slot.legendaire { box-shadow: 0 0 14px #e0b54a88, inset 0 0 12px #e0b54a33; }
.slot.unique { box-shadow: 0 0 8px #5b8fd655; }
.slot.peu_commun { box-shadow: 0 0 6px #5fae6e44; }
.ck-trinkets-title { margin: 14px 0 8px; text-align: center; font-size: .7rem; letter-spacing: .12em;
  text-transform: uppercase; color: #c9a85c; border-top: 1px solid #5a4a2e; padding-top: 10px; }
.ck-trinkets { display: grid; grid-template-columns: repeat(auto-fill, minmax(92px, 1fr)); gap: 8px; }
.ck-trinkets .slot { min-height: 72px; }
.ck-card { margin-top: 4px; border: 2px solid var(--rarity); border-radius: 10px; padding: 14px 16px;
  background: linear-gradient(180deg, #2c261d, #1c1813); color: #e9dfc8;
  font-family: Georgia, 'Times New Roman', serif; }
.ck-card.legendaire { box-shadow: 0 0 18px #e0b54a66; }
.ck-card-head { display: flex; gap: 12px; align-items: center; }
.ck-card-icon { width: 44px; height: 44px; flex: none; }
.ck-card-name { font-size: 1.15rem; color: #f6ecd2; }
.ck-card-rarity { font-size: .72rem; letter-spacing: .1em; text-transform: uppercase; color: var(--rarity); }
.ck-card h4 { margin: 12px 0 4px; font-size: .7rem; letter-spacing: .12em; text-transform: uppercase;
  color: #c9a85c; font-weight: normal; }
.ck-card ul { margin: 0; padding-left: 18px; }
.ck-card p { margin: 0; line-height: 1.45; }
.ck-card .muted { color: #a8987a; font-style: italic; }
</style>
"""


def render_equipment(hero: dict, provenance: dict) -> None:
    """Affiche l'écran d'équipement et la fiche de l'objet choisi."""
    slots, trinkets = equipment_slots(hero)
    on_figure = "".join(_slot_html(slot, slots[slot], hero) for slot in ON_FIGURE)
    cells = [f'<div class="ck-figure">{SILHOUETTE}{on_figure}</div>']
    cells += [_slot_html(slot, slots[slot], hero) for slot in SLOTS if slot not in ON_FIGURE]
    trinket_html = "".join(
        _frame("Objet Spécial", icon_of(item), display_name(item), rarity_of(item), filled=True)
        for item in trinkets
    )
    st.html(
        CSS
        + '<div class="ck-panel"><div class="ck-title">Équipement du Loup Solitaire</div>'
        + '<div class="ck-grid">' + "".join(cells) + "</div>"
        + (f'<div class="ck-trinkets-title">Objets Spéciaux</div><div class="ck-trinkets">{trinket_html}</div>'
           if trinkets else "")
        + "</div>"
    )

    owned = [item for item in slots.values() if item] + trinkets
    choice = st.pills("Examiner un objet", owned, format_func=display_name, key="artifact_choice")
    if choice:
        render_card(choice, provenance.get(choice))


def render_card(item: str, origin) -> None:
    rarity = rarity_of(item)
    color = RARITIES[rarity]["color"]
    info = ITEMS.get(item, {})
    effects = effects_of(item)
    lore = LORE.get(item) or info.get("description", "")
    if rarity == "ordinaire":
        origin_html = ""  # une arme commune n'a pas d'histoire à raconter
    elif origin:
        origin_html = f"<h4>Provenance</h4><p>{html.escape(origin)}</p>"
    else:
        origin_html = '<h4>Provenance</h4><p class="muted">Provenance inconnue.</p>'

    st.html(
        CSS
        + f'<div class="ck-card {rarity}" style="--rarity:{color}">'
        + f'<div class="ck-card-head">{icon_img(icon_of(item), color, "ck-card-icon")}'
        + f'<div><div class="ck-card-name">{html.escape(display_name(item))}</div>'
        + f'<div class="ck-card-rarity">{RARITIES[rarity]["label"]}</div></div></div>'
        + ("<h4>Effets</h4><ul>" + "".join(f"<li>{html.escape(e)}</li>" for e in effects) + "</ul>" if effects else "")
        + (f"<h4>Histoire</h4><p>{html.escape(lore)}</p>" if lore and lore != "Arme." else "")
        + origin_html
        + "</div>"
    )
