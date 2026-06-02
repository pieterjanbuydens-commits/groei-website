#!/usr/bin/env python3
"""
Statische-site generator voor Scholengemeenschap Groei.

Bouwt 6 HTML-pagina's met een gedeelde header/footer en huisstijl.
Output = gewone statische bestanden (geschikt voor GitHub Pages).

Gebruik:  python3 build.py
Daarna:   open index.html  (of:  python3 -m http.server)
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ navigatie
PAGES = [
    ("index.html", "Home"),
    ("scholen.html", "Onze scholen"),
    ("scholengemeenschap.html", "Scholengemeenschap"),
    ("samenwerking.html", "Samenwerking"),
    ("solliciteren.html", "Solliciteren"),
    ("contact.html", "Contact"),
]

TAILWIND_CONFIG = """
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            primary: '#95C11E', secondary: '#E30413', neutral: '#9D9FA2',
            dark: '#1F2421', surface: '#F4F8E9', 'surface-light': '#E8F1D2'
          },
          borderRadius: { 'xl': '1.5rem', '2xl': '2rem', '3xl': '2.5rem' },
          fontFamily: {
            headline: ['Quicksand', 'sans-serif'],
            body: ['Nunito Sans', 'sans-serif']
          }
        }
      }
    }
"""


def nav(active):
    links = []
    for href, label in PAGES:
        if label == active:
            cls = "text-primary font-bold border-b-4 border-primary pb-1"
        else:
            cls = "text-dark font-medium hover:text-primary transition-colors"
        links.append(f'<a class="{cls}" href="{href}">{label}</a>')
    desktop = "\n".join(links)

    mlinks = "\n".join(
        f'<a class="block px-4 py-3 rounded-xl hover:bg-surface font-medium text-dark" href="{href}">{label}</a>'
        for href, label in PAGES
    )
    return f"""
<nav class="site-nav fixed top-0 w-full z-50 bg-transparent backdrop-blur-md">
  <div class="flex justify-between items-center w-full px-6 md:px-8 py-3 max-w-7xl mx-auto">
    <a href="index.html" class="flex items-center gap-2 shrink-0">
      <img src="assets/img/logo-groei-kleur-web.png" alt="Scholengemeenschap Groei"
           class="h-9 md:h-11 w-auto hover:scale-105 transition-transform duration-300"/>
    </a>
    <div class="hidden lg:flex items-center gap-7">
      {desktop}
    </div>
    <div class="hidden lg:block">
      <a href="solliciteren.html"
         class="bg-primary text-white px-6 py-2.5 rounded-full font-bold hover:scale-105 hover:shadow-lg active:scale-95 transition-all duration-300">
        Solliciteer
      </a>
    </div>
    <button id="menu-toggle" aria-label="Menu" aria-expanded="false"
            class="lg:hidden text-dark p-2">
      <span class="material-symbols-outlined text-3xl">menu</span>
    </button>
  </div>
  <div id="mobile-menu" class="hidden lg:hidden bg-white/95 backdrop-blur-md shadow-lg mx-4 mb-2 rounded-2xl p-2">
    {mlinks}
    <a href="solliciteren.html" class="block text-center mt-2 bg-primary text-white px-4 py-3 rounded-xl font-bold">Solliciteer</a>
  </div>
</nav>
"""


FOOTER = """
<footer class="bg-dark text-white rounded-t-[2rem] mt-16">
  <div class="grid grid-cols-1 md:grid-cols-4 gap-10 px-8 py-14 max-w-7xl mx-auto">
    <div class="space-y-5">
      <img src="assets/img/logo-groei-wit-web.png" alt="Groei" class="h-11 w-auto"/>
      <p class="text-white/70 text-sm leading-relaxed">
        Heirbrugstraat 271<br/>9160 Lokeren<br/>
        <a class="hover:text-primary" href="tel:+3293481300">09 348 13 00</a>
      </p>
    </div>
    <div class="space-y-4">
      <h4 class="font-headline font-bold text-primary text-lg">Snelle links</h4>
      <ul class="space-y-2.5 text-sm">
        <li><a class="text-white/70 hover:text-white transition-colors" href="scholen.html">Onze scholen</a></li>
        <li><a class="text-white/70 hover:text-white transition-colors" href="scholengemeenschap.html">Scholengemeenschap</a></li>
        <li><a class="text-white/70 hover:text-white transition-colors" href="samenwerking.html">Samenwerking</a></li>
        <li><a class="text-white/70 hover:text-white transition-colors" href="solliciteren.html">Solliciteren</a></li>
        <li><a class="text-white/70 hover:text-white transition-colors" href="contact.html">Contact</a></li>
      </ul>
    </div>
    <div class="space-y-4">
      <h4 class="font-headline font-bold text-primary text-lg">Schoolbesturen</h4>
      <ul class="space-y-2.5 text-sm text-white/70">
        <li>vzw Katholiek Basisonderwijs Lokeren en Moerbeke-Waas</li>
        <li>vzw Zorg en onderwijs De Hagewinde</li>
      </ul>
    </div>
    <div class="space-y-4">
      <h4 class="font-headline font-bold text-primary text-lg">Info</h4>
      <ul class="space-y-2.5 text-sm">
        <li><a class="text-white/70 hover:text-white transition-colors" href="contact.html">Privacybeleid</a></li>
        <li><a class="text-white/70 hover:text-white transition-colors" href="contact.html">Contactformulier</a></li>
      </ul>
    </div>
  </div>
  <div class="border-t border-white/10 px-8 py-6 max-w-7xl mx-auto text-center">
    <p class="text-white/40 text-xs">© 2026 Scholengemeenschap Groei — Lokeren &amp; Moerbeke-Waas.</p>
  </div>
</footer>
"""


def shell(title, active, content, description):
    return f"""<!DOCTYPE html>
<html lang="nl" class="scroll-smooth">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<meta name="description" content="{description}"/>
<link rel="icon" type="image/png" href="assets/img/favicon.png"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@500;600;700&family=Nunito+Sans:wght@300;400;600;700;800&family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0&display=swap" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms"></script>
<script>{TAILWIND_CONFIG}</script>
<link rel="stylesheet" href="assets/css/site.css"/>
</head>
<body class="bg-white selection:bg-primary/30 antialiased">
{nav(active)}
<main>
{content}
</main>
{FOOTER}
<script src="assets/js/site.js"></script>
</body>
</html>
"""


# ------------------------------------------------------------------ herbruikbaar
def page_hero(eyebrow, title_html, subtitle):
    """Compacte pagina-kop voor subpagina's."""
    return f"""
<section class="blob-bg pt-36 pb-16">
  <div class="max-w-4xl mx-auto px-6 md:px-8 text-center space-y-5">
    <span class="inline-flex items-center gap-2 px-4 py-2 bg-white rounded-full shadow-sm text-primary font-bold text-sm">
      <span class="material-symbols-outlined text-secondary" style="font-variation-settings:'FILL' 1;">eco</span>
      {eyebrow}
    </span>
    <h1 class="text-4xl md:text-5xl font-headline font-bold text-dark leading-tight">{title_html}</h1>
    <p class="text-lg md:text-xl text-neutral leading-relaxed max-w-2xl mx-auto">{subtitle}</p>
  </div>
</section>
"""


# ================================================================== HOME
HOME = """
<!-- Hero -->
<section class="relative pt-32 pb-20 overflow-hidden blob-bg">
  <div class="max-w-7xl mx-auto px-6 md:px-8 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
    <div class="relative z-10 space-y-8">
      <div class="inline-flex items-center gap-2 px-4 py-2 bg-white rounded-full shadow-sm text-primary font-bold text-sm">
        <span class="material-symbols-outlined text-secondary" style="font-variation-settings:'FILL' 1;">send</span>
        <span>Samen onderweg</span>
      </div>
      <h1 class="text-5xl lg:text-7xl font-headline font-bold text-dark leading-[1.05]">
        Samen laten we <span class="text-primary">kinderen groeien</span>
      </h1>
      <p class="text-xl text-neutral max-w-lg leading-relaxed">
        Alles zelf doen is optellen. Samenwerken is vermenigvuldigen. Een warme plek
        waar twaalf scholen hun krachten bundelen.
      </p>
      <div class="flex flex-wrap gap-4">
        <a href="scholen.html" class="px-8 py-4 bg-primary text-white rounded-2xl font-bold shadow-lg shadow-primary/20 hover:-translate-y-0.5 transition-all">
          Ontdek onze scholen
        </a>
        <a href="solliciteren.html" class="px-8 py-4 border-2 border-primary text-primary rounded-2xl font-bold hover:bg-primary/5 transition-all">
          Werk bij Groei
        </a>
      </div>
      <div class="flex flex-wrap gap-3 pt-2">
        <div class="glass-card px-4 py-2 rounded-xl flex items-center gap-2 shadow-sm">
          <span class="material-symbols-outlined text-primary">school</span><span class="font-bold text-dark">12 scholen</span>
        </div>
        <div class="glass-card px-4 py-2 rounded-xl flex items-center gap-2 shadow-sm">
          <span class="material-symbols-outlined text-primary">diversity_1</span><span class="font-bold text-dark">10 gewoon + 2 buitengewoon</span>
        </div>
        <div class="glass-card px-4 py-2 rounded-xl flex items-center gap-2 shadow-sm">
          <span class="material-symbols-outlined text-primary">location_on</span><span class="font-bold text-dark">Lokeren &amp; Moerbeke-Waas</span>
        </div>
      </div>
    </div>
    <div class="relative">
      <div class="absolute -top-12 -right-12 w-64 h-64 bg-primary/10 rounded-full blur-3xl"></div>
      <img src="assets/img/hero-illustratie.png" alt="Een groeiende kiemplant met een rood papieren vliegertje"
           class="relative z-10 w-full max-w-xl mx-auto h-auto rounded-3xl animate-float"/>
    </div>
  </div>
</section>

<!-- Wie zijn wij -->
<section class="py-24 bg-white overflow-hidden">
  <div class="max-w-7xl mx-auto px-6 md:px-8 grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-16 items-center">
    <div class="relative">
      <div class="absolute -top-8 -left-8 w-48 h-48 bg-primary/10 rounded-full blur-3xl"></div>
      <div class="absolute -bottom-10 -right-6 w-40 h-40 bg-secondary/10 rounded-full blur-3xl"></div>
      <img src="assets/img/foto-gemeenschap.jpg"
           alt="Lachende kinderen en leerkrachten samen op de speelplaats"
           class="relative z-10 w-full h-auto rounded-3xl shadow-xl shadow-primary/10 object-cover"/>
      <div class="absolute z-20 -bottom-5 left-6 glass-card px-5 py-3 rounded-2xl shadow-lg flex items-center gap-3">
        <span class="material-symbols-outlined text-primary" style="font-variation-settings:'FILL' 1;">groups</span>
        <span class="font-headline font-bold text-dark text-sm leading-tight">Een warme plek<br/>voor elk kind</span>
      </div>
    </div>
    <div class="space-y-6">
      <span class="inline-flex items-center gap-2 px-4 py-2 bg-surface rounded-full text-primary font-bold text-sm">
        <span class="material-symbols-outlined text-secondary" style="font-variation-settings:'FILL' 1;">favorite</span>
        Wie zijn wij?
      </span>
      <h2 class="text-3xl md:text-4xl font-headline font-bold text-dark leading-tight">
        Een netwerk van scholen met <span class="text-primary">hart voor kinderen</span>
      </h2>
      <p class="text-lg text-neutral leading-relaxed">
        Scholengemeenschap Groei is een samenwerkingsverband van twaalf katholieke basisscholen in
        Lokeren en Moerbeke-Waas: tien scholen gewoon basisonderwijs en twee scholen buitengewoon
        basisonderwijs.
      </p>
      <p class="text-lg text-neutral leading-relaxed">
        Door duidelijke afspraken te maken en expertise te delen, versterken we elkaar, met respect
        voor de eigenheid van elke school. Zo maken we van elke school een warme plek waar kinderen
        en personeelsleden hun talenten kunnen ontplooien.
      </p>
    </div>
  </div>
</section>

<!-- Samen één geheel -->
<section class="py-24 bg-surface/60 overflow-hidden">
  <div class="max-w-7xl mx-auto px-6 md:px-8 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
    <div class="order-2 lg:order-1">
      <div class="bg-white rounded-3xl p-8 shadow-sm puzzle-glow">
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-3">
          __PUZZELSTUKKEN__
        </div>
      </div>
    </div>
    <div class="order-1 lg:order-2 space-y-7">
      <h2 class="text-4xl font-headline font-bold text-dark leading-tight">
        Onze scholen vormen samen <span class="text-primary">één geheel</span>
      </h2>
      <p class="text-lg text-neutral leading-relaxed">
        Elke school is een eigen puzzelstuk. Samen vormen ze een sterk geheel. Door samen te werken,
        vergroten we de kansen van elk kind en vermenigvuldigen we talent, passie en expertise.
      </p>
      <ul class="space-y-4">
        __PUNTEN__
      </ul>
      <a href="scholen.html" class="inline-flex items-center gap-2 px-7 py-4 bg-dark text-white rounded-2xl font-bold hover:bg-dark/90 transition-all">
        Bekijk alle scholen <span class="material-symbols-outlined">arrow_forward</span>
      </a>
    </div>
  </div>
</section>

<!-- Kernwaarden -->
<section class="py-24 bg-white">
  <div class="max-w-7xl mx-auto px-6 md:px-8">
    <div class="text-center mb-16 space-y-4">
      <h2 class="text-4xl font-headline font-bold text-dark">Onze kernwaarden</h2>
      <p class="text-neutral">Waar we elke dag met hart en ziel aan werken.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      __WAARDEN__
    </div>
  </div>
</section>

<!-- Rekrutering -->
<section class="py-16 px-6 md:px-8">
  <div class="max-w-6xl mx-auto rounded-[2.5rem] bg-primary/10 overflow-hidden relative">
    <div class="absolute top-0 right-0 p-8 opacity-20 rotate-12 hidden sm:block">
      <span class="material-symbols-outlined text-9xl text-primary">send</span>
    </div>
    <div class="px-8 md:px-16 py-16 text-center md:text-left max-w-2xl relative z-10">
      <h2 class="text-3xl md:text-5xl font-headline font-bold text-dark mb-6">Wil jij ook deel uitmaken van ons team?</h2>
      <p class="text-lg text-dark/70 mb-10 leading-relaxed">
        Ben je op zoek naar een inspirerende werkomgeving in het onderwijs? Bij Groei zet je je
        talenten in binnen een warme, ondersteunende gemeenschap.
      </p>
      <a href="solliciteren.html" class="inline-block bg-primary text-white px-10 py-4 rounded-2xl font-bold shadow-lg shadow-primary/20 hover:scale-105 transition-all">
        Solliciteer nu
      </a>
    </div>
  </div>
</section>
"""

PUZZEL_SCHOLEN = ["Bengel", "Boskesschool", "De Palster", "Dol-Fijn", "Duizendvoet",
                  "Groei", "Heiende", "OLVC", "Oudenbos", "SLC", "Veertjesplein", "De Vinderij"]


def home_puzzelstukken():
    out = []
    for i, naam in enumerate(PUZZEL_SCHOLEN):
        mid = (naam == "Groei")
        base = "bg-primary text-white" if mid else (
            "bg-surface-light text-dark" if i % 2 else "bg-primary/15 text-dark")
        out.append(
            f'<div class="aspect-square rounded-2xl {base} flex items-center justify-center '
            f'text-center text-sm font-headline font-bold p-2 hover:scale-105 transition-transform">{naam}</div>'
        )
    return "\n          ".join(out)


def home_punten():
    punten = [
        "Een gedeelde visie op kwaliteitsvol onderwijs",
        "Behoud van de lokale eigenheid en de familiale sfeer",
        "Sterke ondersteuning voor leerlingen én leerkrachten",
    ]
    return "\n        ".join(
        f'<li class="flex items-start gap-4">'
        f'<span class="w-9 h-9 rounded-full bg-primary/20 flex items-center justify-center shrink-0">'
        f'<span class="material-symbols-outlined text-primary text-xl">done</span></span>'
        f'<span class="text-dark font-medium pt-1">{p}</span></li>'
        for p in punten
    )


def home_waarden():
    waarden = [
        ("spa", "Warme, gastvrije scholen",
         "We bouwen aan een familiale plek waar iedereen zich welkom voelt. Verbinding tussen kinderen, ouders en team staat centraal."),
        ("volunteer_activism", "Talenten laten ontplooien",
         "Ieder kind is uniek. We geven ruimte aan creativiteit en nieuwsgierigheid, zodat elke leerling zijn eigen weg vindt."),
        ("hub", "Samen sterker",
         "Door expertise te delen en elkaar te ondersteunen, leggen we een sterke basis. Samenwerking is onze grootste kracht."),
    ]
    cards = []
    for icon, titel, tekst in waarden:
        cards.append(f"""
      <div class="p-8 rounded-3xl border border-surface-light hover:shadow-xl hover:shadow-primary/5 transition-all group">
        <div class="w-16 h-16 rounded-2xl bg-surface mb-6 flex items-center justify-center group-hover:scale-110 transition-transform">
          <span class="material-symbols-outlined text-primary text-4xl" style="font-variation-settings:'FILL' 1;">{icon}</span>
        </div>
        <h3 class="text-xl font-headline font-bold text-dark mb-3">{titel}</h3>
        <p class="text-neutral leading-relaxed">{tekst}</p>
      </div>""")
    return "\n".join(cards)


def build_home():
    c = HOME.replace("__PUZZELSTUKKEN__", home_puzzelstukken())
    c = c.replace("__PUNTEN__", home_punten())
    c = c.replace("__WAARDEN__", home_waarden())
    return shell(
        "Scholengemeenschap Groei | Samen laten we kinderen groeien",
        "Home", c,
        "Scholengemeenschap Groei: twaalf katholieke basisscholen in Lokeren en Moerbeke-Waas die samen kinderen laten groeien.")


# ================================================================== ONZE SCHOLEN
SCHOLEN_GEWOON = [
    ("Bengel", "https://sites.google.com/ictlokeren.be/bengel", ""),
    ("Boskesschool", "https://sites.google.com/ictlokeren.be/de-boskesschool", "Campussen Slagveldstraat &amp; Oude Heerweg"),
    ("De Palster", "https://sites.google.com/ictlokeren.be/depalster", ""),
    ("Dol-Fijn", "https://sites.google.com/ictlokeren.be/gvbsdolfijn", "Campussen Eksaardedorp &amp; Rechtstraat"),
    ("Duizendvoet", "https://sites.google.com/ictlokeren.be/duizendvoet", ""),
    ("Heiende", "https://sites.google.com/ictlokeren.be/heiende", ""),
    ("Onze-Lieve-Vrouwcollege", "https://www.olvc-lokeren.net", ""),
    ("Oudenbos", "https://sites.google.com/ictlokeren.be/basisschool-oudenbos", ""),
    ("Sint-Lodewijkscollege", "https://sites.google.com/ictlokeren.be/gvbsdoorslaar", "Doorslaar"),
    ("Veertjesplein", "https://sites.google.com/ictlokeren.be/veertjesplein", ""),
]
SCHOLEN_BUITENGEWOON = [
    ("De Vinderij 1", "https://www.devinderij.be", "Buitengewoon onderwijs — type 3 en 9"),
    ("De Vinderij 2", "https://www.devinderij.be", "Buitengewoon onderwijs — type basisaanbod, 1 en 2"),
]


def school_card(naam, url, extra):
    sub = f'<p class="text-sm text-neutral mt-1">{extra}</p>' if extra else ""
    return f"""
    <a href="{url}" target="_blank" rel="noopener"
       class="group block p-6 rounded-3xl bg-white border border-surface-light hover:border-primary/40 hover:shadow-xl hover:shadow-primary/5 hover:-translate-y-1 transition-all">
      <div class="flex items-start justify-between gap-3">
        <div class="w-12 h-12 rounded-2xl bg-surface flex items-center justify-center shrink-0">
          <span class="material-symbols-outlined text-primary" style="font-variation-settings:'FILL' 1;">school</span>
        </div>
        <span class="material-symbols-outlined text-neutral group-hover:text-primary group-hover:translate-x-1 transition-all">north_east</span>
      </div>
      <h3 class="text-xl font-headline font-bold text-dark mt-4">{naam}</h3>
      {sub}
    </a>"""


def build_scholen():
    gewoon = "\n".join(school_card(*s) for s in SCHOLEN_GEWOON)
    buiten = "\n".join(school_card(*s) for s in SCHOLEN_BUITENGEWOON)
    content = page_hero(
        "Onze scholen",
        'Twaalf scholen, <span class="text-primary">één gemeenschap</span>',
        "Tien scholen gewoon basisonderwijs en twee scholen buitengewoon basisonderwijs, "
        "elk met een eigen verhaal en sfeer. Klik door naar de school van jouw keuze.")
    content += f"""
<section class="py-16 bg-white">
  <div class="max-w-7xl mx-auto px-6 md:px-8 space-y-16">
    <div>
      <h2 class="text-2xl md:text-3xl font-headline font-bold text-dark mb-2">Gewoon basisonderwijs</h2>
      <p class="text-neutral mb-8">Tien scholen voor kleuter- en lager onderwijs.</p>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {gewoon}
      </div>
    </div>
    <div>
      <h2 class="text-2xl md:text-3xl font-headline font-bold text-dark mb-2">Buitengewoon basisonderwijs</h2>
      <p class="text-neutral mb-8">Onderwijs op maat voor kinderen met specifieke onderwijsbehoeften.</p>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {buiten}
      </div>
    </div>
  </div>
</section>
"""
    return shell("Onze scholen | Scholengemeenschap Groei", "Onze scholen", content,
                 "De twaalf basisscholen van Scholengemeenschap Groei in Lokeren en Moerbeke-Waas.")


# ================================================================== SCHOLENGEMEENSCHAP
def info_card(titel, regels):
    items = "".join(f'<li class="text-neutral leading-relaxed">{r}</li>' for r in regels)
    return f"""
    <div class="p-8 rounded-3xl bg-white border border-surface-light">
      <h3 class="text-xl font-headline font-bold text-dark mb-4">{titel}</h3>
      <ul class="space-y-2 list-disc list-inside marker:text-primary">{items}</ul>
    </div>"""


def build_scholengemeenschap():
    content = page_hero(
        "Scholengemeenschap",
        'Samen werken aan <span class="text-primary">goed onderwijs</span>',
        "Scholengemeenschap Groei bundelt diensten en overleg in een centraal secretariaat, "
        "zodat onze scholen zich kunnen toeleggen op wat echt telt: de kinderen.")
    overleg = ", ".join([
        "directies", "administratief personeel", "zorgcoördinatoren",
        "leerkrachten bewegingsopvoeding", "ICT", "GOBO", "CPBW", "LOC/OCSG"])
    content += f"""
<section class="py-16 bg-white">
  <div class="max-w-5xl mx-auto px-6 md:px-8 space-y-12">

    <div class="prose-lg space-y-5">
      <h2 class="text-2xl md:text-3xl font-headline font-bold text-dark">Onze visie</h2>
      <p class="text-lg text-neutral leading-relaxed">
        We streven naar een gastvrije school waar kinderen graag komen. Een plek met respect voor
        ieders overtuiging, waar leren en samenleven hand in hand gaan en waar elk kind en elk
        personeelslid zijn talenten kan ontplooien.
      </p>
    </div>

    <div>
      <h2 class="text-2xl md:text-3xl font-headline font-bold text-dark mb-6">Onze werking</h2>
      <p class="text-lg text-neutral leading-relaxed mb-6">
        De scholengemeenschap bundelt diensten in een centraal secretariaat. Daarnaast komen
        verschillende overleggroepen regelmatig samen rond {overleg}.
      </p>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        {info_card("Gewoon basisonderwijs", ["Bengel", "Boskesschool", "De Palster", "Dol-Fijn", "Duizendvoet", "Heiende", "Onze-Lieve-Vrouwcollege", "Oudenbos", "Sint-Lodewijkscollege (Doorslaar)", "Veertjesplein"])}
        {info_card("Buitengewoon basisonderwijs", ["De Vinderij 1 — type 3 en 9", "De Vinderij 2 — type basisaanbod, 1 en 2"])}
      </div>
    </div>

    <div>
      <h2 class="text-2xl md:text-3xl font-headline font-bold text-dark mb-6">Bestuur</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        {info_card("vzw Katholiek Basisonderwijs Lokeren en Moerbeke-Waas", ["Heirbrugstraat 271, 9160 Lokeren", "Bestuurt de scholen gewoon basisonderwijs binnen de scholengemeenschap."])}
        {info_card("vzw Zorg en onderwijs De Hagewinde", ["Poststraat 6, 9160 Lokeren", "Bestuurt het buitengewoon basisonderwijs (De Vinderij)."])}
      </div>
      <p class="text-neutral mt-6">
        De dagelijkse coördinatie van de scholengemeenschap is in handen van de coördinerend directeur,
        ondersteund door het centraal secretariaat.
      </p>
    </div>

  </div>
</section>
"""
    return shell("Scholengemeenschap | Groei", "Scholengemeenschap", content,
                 "Visie, werking en bestuur van Scholengemeenschap Groei.")


# ================================================================== SAMENWERKING
def build_samenwerking():
    content = page_hero(
        "Samenwerking",
        'Bruggen bouwen, <span class="text-primary">samen sterker</span>',
        "Binnen en buiten de scholengemeenschap werken we samen, met het buitengewoon onderwijs "
        "en met de secundaire scholen van VLOT!.")
    content += """
<section class="py-16 bg-white">
  <div class="max-w-5xl mx-auto px-6 md:px-8 space-y-12">

    <div class="p-8 md:p-10 rounded-3xl bg-surface/70">
      <div class="flex items-center gap-3 mb-4">
        <span class="w-12 h-12 rounded-2xl bg-primary/15 flex items-center justify-center">
          <span class="material-symbols-outlined text-primary" style="font-variation-settings:'FILL' 1;">handshake</span>
        </span>
        <h2 class="text-2xl md:text-3xl font-headline font-bold text-dark">GOBO &mdash; gewoon én buitengewoon onderwijs</h2>
      </div>
      <p class="text-lg text-neutral leading-relaxed">
        Sinds september 2014, toen De Vinderij deel werd van de scholengemeenschap, bouwen we met
        GOBO een brug tussen het gewoon en het buitengewoon onderwijs. Een team van collega's helpt
        bij het vinden van oplossingen voor leerlingen met zorgvragen in het gewoon onderwijs.
        Omgekeerd kunnen ook specialisten uit het buitengewoon onderwijs bij dit team terecht voor advies.
      </p>
    </div>

    <div class="p-8 md:p-10 rounded-3xl border border-surface-light">
      <div class="flex items-center gap-3 mb-4">
        <span class="w-12 h-12 rounded-2xl bg-primary/15 flex items-center justify-center">
          <span class="material-symbols-outlined text-primary" style="font-variation-settings:'FILL' 1;">school</span>
        </span>
        <h2 class="text-2xl md:text-3xl font-headline font-bold text-dark">Samenwerking met VLOT!</h2>
      </div>
      <p class="text-lg text-neutral leading-relaxed mb-6">
        Onze basisscholen werken nauw samen met de secundaire scholen van VLOT!. Zo verloopt de
        overstap van het zesde leerjaar naar het secundair zo vlot mogelijk.
      </p>
      <ul class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        __VLOT__
      </ul>
    </div>

  </div>
</section>
"""
    vlot = [
        "Wederzijdse werkbezoeken tussen scholen",
        "Afstemming tussen het zesde leerjaar en het eerste secundair (o.a. wiskunde, Frans en Nederlands)",
        "Uitwisseling van expertise rond leerlingenbegeleiding",
        "Infomomenten voor leerlingen over de studiekeuze",
    ]
    vlot_html = "\n        ".join(
        f'<li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary shrink-0">check_circle</span>'
        f'<span class="text-dark">{v}</span></li>' for v in vlot)
    content = content.replace("__VLOT__", vlot_html)
    return shell("Samenwerking | Scholengemeenschap Groei", "Samenwerking", content,
                 "Samenwerking binnen Groei: GOBO (gewoon en buitengewoon onderwijs) en de samenwerking met VLOT!.")


# ================================================================== SOLLICITEREN
def build_solliciteren():
    content = page_hero(
        "Solliciteren",
        'Kom <span class="text-primary">groeien</span> bij ons team',
        "Zin om je talenten in te zetten in een warme onderwijsgemeenschap? "
        "We horen graag van je.")
    content += """
<section class="py-16 bg-white">
  <div class="max-w-5xl mx-auto px-6 md:px-8">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">

      <div class="p-8 rounded-3xl bg-surface/70 flex flex-col">
        <span class="w-14 h-14 rounded-2xl bg-white flex items-center justify-center mb-5">
          <span class="material-symbols-outlined text-primary text-3xl" style="font-variation-settings:'FILL' 1;">edit_document</span>
        </span>
        <h2 class="text-2xl font-headline font-bold text-dark mb-3">Gewoon basisonderwijs</h2>
        <p class="text-neutral leading-relaxed mb-6 grow">
          Solliciteer je voor een functie in het gewoon basisonderwijs? Vul het sollicitatieformulier in.
          Je gegevens komen in een lijst die onze directies raadplegen wanneer ze nieuwe medewerkers zoeken.
        </p>
        <!-- LET OP: vervang href door de URL van het Google-sollicitatieformulier -->
        <a href="#" class="inline-flex items-center justify-center gap-2 bg-primary text-white px-7 py-4 rounded-2xl font-bold shadow-lg shadow-primary/20 hover:scale-[1.02] transition-all">
          Naar het sollicitatieformulier <span class="material-symbols-outlined">arrow_forward</span>
        </a>
      </div>

      <div class="p-8 rounded-3xl border border-surface-light flex flex-col">
        <span class="w-14 h-14 rounded-2xl bg-surface flex items-center justify-center mb-5">
          <span class="material-symbols-outlined text-primary text-3xl" style="font-variation-settings:'FILL' 1;">alternate_email</span>
        </span>
        <h2 class="text-2xl font-headline font-bold text-dark mb-3">Buitengewoon basisonderwijs</h2>
        <p class="text-neutral leading-relaxed mb-6 grow">
          Voor een functie in het buitengewoon basisonderwijs (De Vinderij) stuur je een e-mail met je
          gegevens en motivatie.
        </p>
        <a href="mailto:info@devinderij.be" class="inline-flex items-center justify-center gap-2 border-2 border-primary text-primary px-7 py-4 rounded-2xl font-bold hover:bg-primary/5 transition-all">
          info@devinderij.be
        </a>
      </div>

    </div>
  </div>
</section>
"""
    return shell("Solliciteren | Scholengemeenschap Groei", "Solliciteren", content,
                 "Solliciteer bij Scholengemeenschap Groei in het gewoon of buitengewoon basisonderwijs.")


# ================================================================== CONTACT
def build_contact():
    content = page_hero(
        "Contact",
        'Neem <span class="text-primary">contact</span> op',
        "Een vraag of een boodschap? Gebruik het contactformulier of bereik het centraal secretariaat.")
    content += """
<section class="py-16 bg-white">
  <div class="max-w-5xl mx-auto px-6 md:px-8 grid grid-cols-1 md:grid-cols-2 gap-8">

    <div class="space-y-6">
      <div class="p-6 rounded-3xl border border-surface-light flex items-start gap-4">
        <span class="w-12 h-12 rounded-2xl bg-surface flex items-center justify-center shrink-0">
          <span class="material-symbols-outlined text-primary" style="font-variation-settings:'FILL' 1;">location_on</span>
        </span>
        <div>
          <h3 class="font-headline font-bold text-dark">Centraal secretariaat</h3>
          <p class="text-neutral leading-relaxed">Heirbrugstraat 271<br/>9160 Lokeren</p>
        </div>
      </div>
      <div class="p-6 rounded-3xl border border-surface-light flex items-start gap-4">
        <span class="w-12 h-12 rounded-2xl bg-surface flex items-center justify-center shrink-0">
          <span class="material-symbols-outlined text-primary" style="font-variation-settings:'FILL' 1;">call</span>
        </span>
        <div>
          <h3 class="font-headline font-bold text-dark">Telefoon</h3>
          <p class="text-neutral"><a class="hover:text-primary" href="tel:+3293481300">09 348 13 00</a></p>
        </div>
      </div>
      <div class="p-6 rounded-3xl bg-surface/70 flex items-start gap-4">
        <span class="w-12 h-12 rounded-2xl bg-white flex items-center justify-center shrink-0">
          <span class="material-symbols-outlined text-primary" style="font-variation-settings:'FILL' 1;">shield</span>
        </span>
        <div>
          <h3 class="font-headline font-bold text-dark">Privacy</h3>
          <!-- LET OP: vervang href door de URL van het privacybeleid-document -->
          <p class="text-neutral">Lees ons <a class="text-primary font-semibold hover:underline" href="#">privacybeleid</a>.</p>
        </div>
      </div>
    </div>

    <div class="p-8 rounded-3xl bg-primary/10 flex flex-col justify-center text-center">
      <span class="material-symbols-outlined text-primary text-5xl mb-4" style="font-variation-settings:'FILL' 1;">mail</span>
      <h2 class="text-2xl font-headline font-bold text-dark mb-3">Contactformulier</h2>
      <p class="text-dark/70 leading-relaxed mb-7">
        Heb je een vraag of een opmerking? Laat het ons weten via het contactformulier.
        We nemen zo snel mogelijk contact met je op.
      </p>
      <!-- LET OP: vervang href door de URL van het Google-contactformulier -->
      <a href="#" class="inline-flex items-center justify-center gap-2 bg-primary text-white px-8 py-4 rounded-2xl font-bold shadow-lg shadow-primary/20 hover:scale-[1.02] transition-all">
        Open het contactformulier <span class="material-symbols-outlined">arrow_forward</span>
      </a>
    </div>

  </div>
</section>
"""
    return shell("Contact | Scholengemeenschap Groei", "Contact", content,
                 "Contacteer Scholengemeenschap Groei — Heirbrugstraat 271, 9160 Lokeren, 09 348 13 00.")


# ------------------------------------------------------------------ main
def main():
    builders = {
        "index.html": build_home,
        "scholen.html": build_scholen,
        "scholengemeenschap.html": build_scholengemeenschap,
        "samenwerking.html": build_samenwerking,
        "solliciteren.html": build_solliciteren,
        "contact.html": build_contact,
    }
    for fname, fn in builders.items():
        with open(os.path.join(HERE, fname), "w", encoding="utf-8") as f:
            f.write(fn())
        print("geschreven:", fname)


if __name__ == "__main__":
    main()
