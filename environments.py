"""
Ambiances visuelles selon le lieu où se trouve le Loup Solitaire (forêt, ville, mer, souterrain...).
Tout est en CSS : un ciel en dégradé, une silhouette de paysage en bas de l'écran (SVG en data URI)
et un panneau semi-opaque sous le contenu pour garder le texte lisible. Aucune image à télécharger.

L'ambiance de chaque paragraphe est dans ambiances.json ({tome: {paragraphe: ambiance}}) ;
check_inventory() l'applique à chaque page (cf. apply_page_environment).
"""
import base64
import functools
import json

import streamlit as st

AMBIANCES_FILE = "ambiances.json"


def _svg(body: str, width: int, height: int, aspect: str = "none") -> str:
    """aspect : "none" étire le motif (frises répétées), "xMidYMax slice" garde les proportions d'une scène."""
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" preserveAspectRatio="{aspect}">{body}</svg>'
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


def _pines(color: str, offset: int = 0) -> str:
    """Rangée de sapins de hauteurs variées, sur 400 px de large (motif répété)."""
    trees = []
    for i, (x, h) in enumerate([(10, 150), (55, 210), (95, 170), (140, 240), (185, 160), (230, 220),
                                (270, 180), (315, 250), (360, 190), (395, 150)]):
        x = (x + offset) % 400
        w = h * 0.32
        trees.append(f'<path d="M{x} {300 - h} L{x + w} 300 L{x - w} 300 Z"/>')
    return f'<g fill="{color}">{"".join(trees)}<rect y="290" width="400" height="10"/></g>'


def _mist(color: str, y: int, opacity: float) -> str:
    """Nappe de brume horizontale."""
    return f'<rect y="{y}" width="400" height="40" fill="{color}" opacity="{opacity}"/>'


FOREST = _svg(
    _pines("#2b3c33", 25) + _mist("#3a4a42", 205, .35) + _pines("#1e3324"),
    400, 300,
)


def _crenels(x: int, width: int, top: int, merlon: int = 6) -> str:
    """Créneaux : une suite de merlons sur le haut d'un mur ou d'une tour."""
    teeth = "".join(
        f'<rect x="{x + i}" y="{top - merlon}" width="{merlon}" height="{merlon}"/>'
        for i in range(0, width - merlon + 1, merlon * 2)
    )
    return f'<rect x="{x}" y="{top}" width="{width}" height="{300 - top}"/>{teeth}'


def _tower(x: int, width: int, top: int, roof: int = 0) -> str:
    """Tour crénelée, ou coiffée d'un toit pointu si `roof` > 0."""
    if roof:
        return (f'<rect x="{x}" y="{top}" width="{width}" height="{300 - top}"/>'
                f'<path d="M{x - 3} {top} L{x + width / 2} {top - roof} L{x + width + 3} {top} Z"/>')
    return _crenels(x, width, top, 5)


CITY = _svg(
    '<g fill="#100d13">'
    + _crenels(0, 400, 238)  # rempart
    + _tower(18, 26, 170, roof=38) + _tower(92, 22, 196) + _tower(150, 44, 120)  # donjon
    + _tower(162, 20, 70, roof=34) + _tower(238, 24, 186, roof=30) + _tower(300, 30, 150)
    + _tower(360, 22, 192, roof=28)
    + '<path d="M196 300v-34a12 12 0 0 1 24 0v34z" fill="#060508"/>'  # porte
    + '</g><g fill="#c9772f" opacity=".55">'
    + '<rect x="168" y="140" width="4" height="7"/><rect x="306" y="172" width="4" height="7"/>'
    + '<rect x="27" y="200" width="4" height="7"/>'
    + '</g>',
    400, 300,
)

SEA = _svg(
    '<path d="M0 210q25-15 50 0t50 0 50 0 50 0 50 0 50 0 50 0 50 0V300H0z" fill="#1c3442"/>'
    '<path d="M0 240q25-15 50 0t50 0 50 0 50 0 50 0 50 0 50 0 50 0V300H0z" fill="#12242f"/>'
    '<path d="M0 270q25-12 50 0t50 0 50 0 50 0 50 0 50 0 50 0 50 0V300H0z" fill="#0a161d"/>',
    400, 300,
)

CAVE = _svg(
    '<path d="M0 0h400v40l-20 50-15-45-25 80-20-70-30 40-15-55-25 95-20-80-25 50-20-60-30 70-15-40'
    '-25 60-20-75-30 45-15-30-25 55-20-65-30 40L0 70z" fill="#1d1a1f"/>',
    400, 300,
)

def _ridge(points: list, fill: str) -> str:
    """
    Crête en ligne brisée, fermée jusqu'en bas du motif. Le dernier point est à la même hauteur que
    le premier : le motif se raccorde sans marche quand il est répété sur la largeur.
    """
    assert points[0][1] == points[-1][1] and points[-1][0] == 400, "le motif ne se raccorderait pas"
    path = " ".join(f"L{x} {y}" for x, y in points[1:])
    return f'<path d="M{points[0][0]} {points[0][1]} {path} V300 H0 Z" fill="{fill}"/>'


def _dunes(y: int, amplitude: int, fill: str, width: int = 400) -> str:
    """
    Ondulation douce (une bosse puis un creux tous les 200 px) : même hauteur et même pente aux
    deux bords du motif, dont la largeur doit être un multiple de 200.
    """
    assert width % 200 == 0, "le motif ne se raccorderait pas"
    rest = " ".join(f"T{x} {y}" for x in range(200, width + 1, 100))
    return f'<path d="M0 {y} Q50 {y - amplitude} 100 {y} {rest} V300 H0 Z" fill="{fill}"/>'




MOUNTAINS = _svg(
    _ridge([(0, 150), (40, 95), (65, 125), (110, 55), (145, 105), (175, 70), (225, 150), (265, 90),
            (310, 140), (345, 100), (400, 150)], "#6e604b")
    + '<path d="M110 55l-14 27 10-6 4 8 6-12 9 4zM265 90l-10 18 8-3 4 6 4-8 8 3zM175 70l-9 16 7-3 3 5 4-7 7 3z" '
    'fill="#e8dcc0" opacity=".7"/>'
    + _ridge([(0, 215), (30, 185), (60, 205), (100, 150), (135, 190), (180, 160), (220, 205), (255, 175),
              (300, 210), (340, 180), (400, 215)], "#463b2f")
    + _ridge([(0, 262), (50, 248), (110, 262), (180, 240), (240, 260), (310, 245), (400, 262)], "#241e18"),
    400, 300,
)

def _spear(x: int, top: int, lean: int) -> str:
    return f'<path d="M{x} 300 L{x + lean} {top}" stroke="#0d0b0c" stroke-width="3"/>'


BATTLEFIELD = _svg(
    '<path d="M0 250q60-20 120 0t140-5 140 5V300H0z" fill="#1a1414"/>'
    + _spear(40, 200, 18) + _spear(70, 215, -14) + _spear(150, 190, 10) + _spear(230, 210, -20)
    + _spear(300, 195, 16) + _spear(355, 220, -8)
    # épées plantées
    + '<g fill="#0d0b0c"><path d="M110 300v-55h-8v-4h20v4h-8v55z"/><path d="M265 300v-48h-7v-4h18v4h-7v48z"/></g>'
    # bannière en lambeaux sur sa hampe
    + '<path d="M190 300V150" stroke="#0d0b0c" stroke-width="3"/>'
    + '<path d="M191 152h42l-8 10 8 10-12 4 6 10h-36z" fill="#3a1414"/>'
    # corbeaux
    + '<g fill="none" stroke="#0d0b0c" stroke-width="2.5" stroke-linecap="round">'
    + '<path d="M80 90q8-8 14 0q6-8 14 0"/><path d="M300 70q6-6 11 0q5-6 11 0"/><path d="M335 105q5-5 9 0q4-5 9 0"/></g>'
    + '<path d="M0 285q100-12 200 0t200 0V300H0z" fill="#0a0808"/>',
    400, 300,
)

ARID = _svg(
    '<path d="M640 300V185h40l14-40h110l14 40h40v115z" fill="#5a4226"/>'  # mesa, une fois par motif
    + _dunes(235, 22, "#6b4f2e", width=1000)
    + _dunes(268, 12, "#4a3620", width=1000)
    # arbre mort
    + '<path d="M220 266v-62m0 22-20-17m20 5 18-22m-18 40 13-9" stroke="#2a1f14" stroke-width="5" '
    'stroke-linecap="round" fill="none"/>',
    1000, 300,
)

def _shard(x: int, height: int, lean: int = 0) -> str:
    """Éclat de glace dressé sur la plaine."""
    return f'<path d="M{x - 5} 262 L{x + lean} {262 - height} L{x + 5} 262 Z"/>'


ICE = _svg(
    _dunes(212, 6, "#6f8a9e")  # collines lointaines, très basses
    + _dunes(232, 4, "#4f697c")  # la plaine
    + '<g stroke="#c9d9e4" stroke-width="1.5" opacity=".35" stroke-linecap="round">'
    '<path d="M20 244h60M140 250h90M270 242h50M340 252h40"/></g>'  # reflets sur la glace
    + '<g fill="#a9c0cf" opacity=".75">' + _shard(95, 26, 3) + _shard(108, 14, -2) + _shard(300, 20, -3)
    + '</g>'
    + _dunes(266, 10, "#2c4356")  # congères
    + _dunes(286, 6, "#1d3041"),
    400, 300,
)

def _house(x: int, width: int, top: int, fill: str) -> str:
    """Maison cubique en grès, toit plat, porte et fenêtres carrées (village du désert)."""
    door = f'<rect x="{x + width / 2 - 5}" y="{300 - 18}" width="10" height="18" fill="#1a120a"/>'
    windows = "".join(
        f'<rect x="{x + wx}" y="{top + 10}" width="7" height="7" fill="#1a120a"/>'
        for wx in range(6, width - 9, 16)
    )
    return (f'<rect x="{x}" y="{top}" width="{width}" height="{300 - top}" fill="{fill}"/>'
            f'<rect x="{x - 2}" y="{top}" width="{width + 4}" height="4" fill="#3a2b18"/>{windows}{door}')


DESERT_CITY = _svg(
    # minaret et coupole au loin
    '<g fill="#4a3621"><rect x="300" y="120" width="14" height="180"/><path d="M296 120h22l-11-22z"/>'
    '<path d="M60 300v-95a40 40 0 0 1 80 0v95z"/></g>'
    + _house(0, 46, 230, "#6b5030") + _house(44, 38, 200, "#5e4529") + _house(84, 60, 222, "#6b5030")
    + _house(98, 30, 182, "#5e4529")  # étage en retrait
    + _house(146, 42, 240, "#76593a") + _house(190, 54, 210, "#6b5030") + _house(246, 36, 236, "#5e4529")
    + _house(284, 62, 218, "#6b5030") + _house(300, 28, 190, "#76593a") + _house(348, 52, 232, "#5e4529"),
    400, 300,
)


def _brick_arch(x: int) -> str:
    """Voûte de briques d'un égout : un arc de 200 px de large."""
    return (f'<path d="M{x} 0h200v120a100 100 0 0 0-200 0z" fill="#141a14"/>'
            f'<path d="M{x + 8} 120a92 92 0 0 1 184 0" stroke="#2c3326" stroke-width="10" fill="none" '
            f'stroke-dasharray="14 4"/>')


SEWER = _svg(
    _brick_arch(0) + _brick_arch(200)
    + '<g fill="#141a14"><rect x="0" y="120" width="14" height="180"/><rect x="186" y="120" width="28" height="180"/>'
    '<rect x="386" y="120" width="14" height="180"/></g>'
    # gouttes d'eau croupie
    + '<g fill="#5d6b3c" opacity=".7"><path d="M60 140q3 8 0 10q-3-2 0-10z"/><path d="M290 150q3 8 0 10q-3-2 0-10z"/></g>'
    # quai de pierre et canal d'eau verdâtre
    + '<rect y="236" width="400" height="10" fill="#22281f"/>'
    + '<path d="M0 252q25-6 50 0t50 0 50 0 50 0 50 0 50 0 50 0 50 0V300H0z" fill="#2f3a22"/>'
    + '<path d="M0 270q25-5 50 0t50 0 50 0 50 0 50 0 50 0 50 0 50 0V300H0z" fill="#1f2817"/>'
    + '<g stroke="#6f7f45" stroke-width="1.5" opacity=".35"><path d="M30 262h40M170 278h50M300 266h35"/></g>',
    400, 300,
)

PRISON_BARS = _svg(
    # un barreau et sa traverse, répétés sur toute la largeur
    '<rect x="34" y="0" width="12" height="300" fill="#1b1b1d"/>'
    '<rect x="37" y="0" width="3" height="300" fill="#4a4a4e"/>'
    '<rect x="0" y="54" width="80" height="10" fill="#1b1b1d"/><rect x="0" y="56" width="80" height="2" fill="#4a4a4e"/>'
    '<rect x="0" y="236" width="80" height="10" fill="#1b1b1d"/><rect x="0" y="238" width="80" height="2" fill="#4a4a4e"/>',
    80, 300,
)


def _cloud(x: int, y: int, scale: float, fill: str) -> str:
    """Nuage : grappe de cercles sur une base en ellipse aplatie."""
    puffs = "".join(
        f'<circle cx="{x + dx * scale}" cy="{y - dy * scale}" r="{r * scale}"/>'
        for dx, dy, r in [(-30, 2, 16), (-8, 14, 22), (18, 22, 27), (46, 12, 21), (66, 2, 15)]
    )
    return f'<g fill="{fill}">{puffs}<ellipse cx="{x + 18 * scale}" cy="{y + 4 * scale}" rx="{58 * scale}" ry="{12 * scale}"/></g>'


SKY = _svg(
    _cloud(60, 150, 1.1, "#5b5f78") + _cloud(260, 135, 1.3, "#5b5f78") + _cloud(440, 160, 1.0, "#5b5f78")
    + _dunes(205, 18, "#474b63", width=600)
    + _cloud(150, 220, 1.4, "#34374b") + _cloud(390, 232, 1.2, "#34374b") + _cloud(515, 224, .9, "#34374b")
    + _dunes(262, 14, "#262838", width=600),
    600, 300,
)


GOLD = "#c9a65a"


def _glyphs(x: int, y: int) -> str:
    """Une ligne de hiéroglyphes gravés (ankh, œil, oiseau, roseau, vagues) sur une colonne de 56 px."""
    g = (f'<ellipse cx="{x + 6}" cy="{y + 4}" rx="3" ry="4"/><path d="M{x + 6} {y + 8}v10M{x + 1} {y + 11}h10"/>'
         f'<path d="M{x + 17} {y + 9}q7-6 14 0q-7 6-14 0z"/><path d="M{x + 23} {y + 14}l-2 5"/>'
         f'<path d="M{x + 36} {y + 18}q2-12 9-12q5 0 4 5l4 1-4 2q-2 4-8 4z"/>'
         f'<path d="M{x + 3} {y + 30}v-8m4 8v-8m4 8v-8"/>'
         f'<path d="M{x + 18} {y + 27}l3-3 3 3 3-3 3 3 3-3 3 3"/><circle cx="{x + 45}" cy="{y + 26}" r="4"/>')
    return f'<g stroke="{GOLD}" stroke-width="1.6" fill="none" opacity=".55">{g}</g>'


def _hieroglyph_column(x: int) -> str:
    """Colonne couverte de hiéroglyphes, chapiteau en lotus et socle."""
    rows = "".join(_glyphs(x + 8, y) for y in range(150, 500, 42))
    return (f'<rect x="{x}" y="120" width="72" height="420" fill="#4c381d"/>'
            f'<path d="M{x - 14} 120l12-34h96l12 34z" fill="#5a4222"/>'
            f'<rect x="{x - 6}" y="78" width="84" height="10" fill="#6a4e28"/>'
            f'<rect x="{x - 8}" y="536" width="88" height="14" fill="#3a2a16"/>'
            f'<rect x="{x}" y="140" width="72" height="3" fill="{GOLD}" opacity=".6"/>'
            f'<rect x="{x}" y="512" width="72" height="3" fill="{GOLD}" opacity=".6"/>{rows}')


def _brazier(x: int) -> str:
    return (f'<path d="M{x - 18} 470h36l-8 20h-20z" fill="#2a1f12"/><rect x="{x - 3}" y="490" width="6" height="60" fill="#2a1f12"/>'
            f'<path d="M{x - 14} 470q4-26 14-40q10 14 14 40z" fill="#c9772f" opacity=".75"/>'
            f'<path d="M{x - 7} 470q2-14 7-22q5 8 7 22z" fill="#f0c060" opacity=".8"/>')


SARCOPHAGUS = (
    '<rect x="300" y="500" width="200" height="50" fill="#2e2213"/><rect x="290" y="494" width="220" height="10" fill="#4a3820"/>'
    # cuve
    '<path d="M330 494V380q0-18 18-22h104q18 4 18 22v114z" fill="#3a2a16"/>'
    # couvercle en forme de momie : tête coiffée du némès, visage, bras croisés
    '<path d="M352 300q48-30 96 0v44q12 6 12 30v104h-120V374q0-24 12-30z" fill="#6a4e28"/>'
    f'<path d="M352 300q48-30 96 0l-10 46h-76z" fill="#2a3a5a"/>'
    f'<g stroke="{GOLD}" stroke-width="3" opacity=".8"><path d="M360 306l8 36M376 296l4 46M400 292v52M424 296l-4 46M440 306l-8 36"/></g>'
    f'<ellipse cx="400" cy="322" rx="18" ry="22" fill="{GOLD}"/>'
    '<rect x="395" y="344" width="10" height="16" fill="#2a3a5a"/>'
    f'<path d="M362 392l76 34M438 392l-76 34" stroke="{GOLD}" stroke-width="7" stroke-linecap="round"/>'
    f'<g fill="none" stroke="{GOLD}" stroke-width="2" opacity=".7"><path d="M348 448h104M348 462h104"/>'
    '<path d="M360 474h80"/></g>'
)

TOMB = _svg(
    '<rect width="800" height="600" fill="#1f160c"/>'
    # frise de hiéroglyphes en haut et dalles du sol
    + '<rect width="800" height="60" fill="#2a1f12"/><rect y="60" width="800" height="6" fill="#8a6a30"/>'
    + "".join(_glyphs(x, 16) for x in range(10, 800, 64))
    + '<rect y="550" width="800" height="50" fill="#140e07"/>'
    + '<g stroke="#3a2a16" stroke-width="2"><path d="M0 550h800M100 550v50M220 550v50M340 550v50M460 550v50M580 550v50M700 550v50"/></g>'
    # lueur des braseros sur le tombeau
    + '<ellipse cx="400" cy="430" rx="260" ry="140" fill="#6a4a22" opacity=".35"/>'
    + _hieroglyph_column(30) + _hieroglyph_column(150) + _hieroglyph_column(578) + _hieroglyph_column(698)
    + _brazier(268) + _brazier(532) + SARCOPHAGUS,
    800, 600, aspect="xMidYMax slice",
)

ENVIRONMENTS = {
    "foret": {
        "label": "Forêt",
        "sky": "linear-gradient(180deg, #121a16 0%, #1f2b24 50%, #2d3b32 80%, #1a241e 100%)",
        "band": FOREST, "band_position": "bottom", "band_height": "34vh",
        "accent": "#2f4a33", "accent_dark": "#8fae8a", "panel": "#faf8ee", "panel_dark": "#1f241d",
    },
    "ville": {
        "label": "Ville",
        "sky": "linear-gradient(180deg, #2e2630 0%, #43353b 40%, #6a4234 75%, #8a4c2e 100%)",
        "band": CITY, "band_position": "bottom", "band_height": "36vh",
        "accent": "#6b3524", "accent_dark": "#c98a62", "panel": "#fcf7f0", "panel_dark": "#262022",
    },
    "mer": {
        "label": "Mer",
        "sky": "linear-gradient(180deg, #11161b 0%, #1f2a32 50%, #34434d 85%, #2a3842 100%)",
        "band": SEA, "band_position": "bottom", "band_height": "32vh",
        "accent": "#1c3a4a", "accent_dark": "#86a9bb", "panel": "#f7fafb", "panel_dark": "#1a2228",
    },
    "souterrain": {
        "label": "Souterrain",
        "sky": "radial-gradient(ellipse at 50% 40%, #6d6371 0%, #3e3742 55%, #1d1a1f 100%)",
        "band": CAVE, "band_position": "top", "band_height": "30vh",
        "accent": "#6b4f8a", "accent_dark": "#c3a7e3", "panel": "#f6f2ec", "panel_dark": "#211e24",
    },
    "montagne": {
        "label": "Montagne",
        "sky": "linear-gradient(180deg, #2e2a24 0%, #4f4535 45%, #8a7350 80%, #a68a5a 100%)",
        "band": MOUNTAINS, "band_position": "bottom", "band_height": "42vh", "tile": "900px",
        "accent": "#5a4a30", "accent_dark": "#d6c08f", "panel": "#f4f5f6", "panel_dark": "#1b1f24",
    },
    "bataille": {
        "label": "Champ de bataille",
        "sky": "linear-gradient(180deg, #120d0d 0%, #2a1714 45%, #5a2416 80%, #3a1a12 100%)",
        "band": BATTLEFIELD, "band_position": "bottom", "band_height": "36vh",
        "accent": "#6b1f17", "accent_dark": "#c9705c", "panel": "#f7f1ee", "panel_dark": "#221717",
    },
    "aride": {
        "label": "Terres arides",
        "sky": "linear-gradient(180deg, #5c4527 0%, #77593a 50%, #94703f 85%, #7a5a34 100%)",
        "band": ARID, "band_position": "bottom", "band_height": "34vh", "tile": "1000px",
        "accent": "#6b4a26", "accent_dark": "#c9a072", "panel": "#f8f3ea", "panel_dark": "#221c16",
    },
    "glace": {
        "label": "Glace",
        "sky": "linear-gradient(180deg, #2b4052 0%, #3a556b 50%, #557389 85%, #44607a 100%)",
        "band": ICE, "band_position": "bottom", "band_height": "34vh", "tile": "800px",
        "accent": "#2c4a5c", "accent_dark": "#a9c7d8", "panel": "#f3f7f9", "panel_dark": "#171e24",
    },
    "ville_desert": {
        "label": "Ville du désert",
        "sky": "linear-gradient(180deg, #3a2a1c 0%, #5e4026 45%, #8a5c30 80%, #a06a34 100%)",
        "band": DESERT_CITY, "band_position": "bottom", "band_height": "36vh",
        "accent": "#7a4a1f", "accent_dark": "#d9a86c", "panel": "#fbf5ea", "panel_dark": "#241b13",
    },
    "egouts": {
        "label": "Égouts",
        "sky": "radial-gradient(ellipse at 50% 45%, #3c4630 0%, #262d1e 55%, #11150e 100%)",
        "band": SEWER, "band_position": "bottom", "band_height": "100vh",
        "accent": "#4a5a2a", "accent_dark": "#a8b97a", "panel": "#f4f5ee", "panel_dark": "#1a1f16",
    },
    "prison": {
        "label": "Prison du palais",
        "sky": "linear-gradient(180deg, #8a7a52 0%, #6c6550 14%, #4a4a4c 40%, #333335 75%, #262628 100%)",
        "band": PRISON_BARS, "band_position": "bottom", "band_height": "100vh", "tile": "120px",
        "accent": "#4a4a4e", "accent_dark": "#c8c2a8", "panel": "#f5f4f0", "panel_dark": "#1f1f21",
    },
    "ciel": {
        "label": "Dans les nuages",
        "sky": "linear-gradient(180deg, #1c1f33 0%, #353a5a 40%, #6b5c6e 75%, #a0705a 100%)",
        "band": SKY, "band_position": "bottom", "band_height": "40vh", "tile": "900px",
        "accent": "#3c4270", "accent_dark": "#b3b9e0", "panel": "#f5f6fa", "panel_dark": "#1b1d2a",
    },
    "tombeau": {
        "label": "Tombeau",
        "sky": "radial-gradient(ellipse at 50% 40%, #6a4a22 0%, #3c2a14 50%, #1a1209 100%)",
        "band": TOMB, "band_position": "bottom", "band_height": "100vh", "tile": "100%",
        "accent": "#8a6a30", "accent_dark": "#e0c07a", "panel": "#fbf6ea", "panel_dark": "#231a10",
    },
}


def _theme_type():
    """« light » / « dark » d'après Streamlit, ou None s'il ne le sait pas encore."""
    try:
        return st.context.theme.type
    except AttributeError:
        return None


def _panel_css(panel: str, accent: str) -> str:
    """Panneau de lecture presque opaque, aux couleurs du thème (clair ou sombre) de Streamlit."""
    return (
        f'[data-testid="stMainBlockContainer"] {{ background: {panel}f2; border-top-color: {accent}; }}\n'
        f'[data-testid="stMainBlockContainer"] h1, [data-testid="stMainBlockContainer"] h2 {{ color: {accent}; }}'
    )


def apply_environment(name: str) -> None:
    """Applique l'ambiance `name` à toute la page (fond, silhouette, panneau de lecture)."""
    env = ENVIRONMENTS.get(name)
    if env is None:
        return
    light = _panel_css(env["panel"], env["accent"])
    dark = _panel_css(env["panel_dark"], env["accent_dark"])
    theme = _theme_type()
    if theme == "dark":
        panel = dark
    elif theme == "light":
        panel = light
    else:  # thème inconnu : Streamlit suit alors le réglage du système
        panel = light + f"\n@media (prefers-color-scheme: dark) {{ {dark} }}"
    st.html(
        f"""<style>
[data-testid="stApp"] {{ background: {env["sky"]}; background-attachment: fixed; }}
[data-testid="stHeader"] {{ background: transparent; }}
[data-testid="stApp"]::before {{
  content: ""; position: fixed; left: 0; right: 0; {env["band_position"]}: 0; height: {env["band_height"]};
  background: url("{env["band"]}") repeat-x {env["band_position"]} / {env.get("tile", "400px")} 100%;
  pointer-events: none; z-index: 0;
}}
[data-testid="stMainBlockContainer"] {{
  position: relative; z-index: 1; border-radius: 14px; border-top: 4px solid;
  margin-top: 4.5rem; margin-bottom: 3rem; padding-top: 2rem; padding-bottom: 2.5rem;
  box-shadow: 0 6px 30px rgba(0, 0, 0, .25);
}}
{panel}
@media (max-width: 640px) {{
  [data-testid="stApp"]::before {{ height: 18vh; opacity: .8; }}
  [data-testid="stMainBlockContainer"] {{ margin-top: 3.5rem; border-radius: 10px; }}
}}
</style>"""
    )


@functools.lru_cache(maxsize=None)
def _ambiances() -> dict:
    try:
        with open(AMBIANCES_FILE, encoding="utf-8") as ambiances_file:
            return json.load(ambiances_file)
    except (OSError, ValueError):
        return {}


def environment_of(book: int, page: int):
    """Ambiance d'un paragraphe (None si la table ne la donne pas)."""
    return _ambiances().get(str(book), {}).get(str(page))


def apply_page_environment(book: int, page: int) -> None:
    apply_environment(environment_of(book, page))
