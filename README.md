# Website Scholengemeenschap Groei

Statische website voor Scholengemeenschap Groei (12 katholieke basisscholen in
Lokeren en Moerbeke-Waas). Gebouwd in de huisstijl (groen `#95C11E`, rood
`#E30413`, grijs `#9D9FA2`), warm en speels-modern. Klaar voor **GitHub Pages**.

## Pagina's
- `index.html` — homepagina
- `scholen.html` — onze scholen (12 scholen + links)
- `scholengemeenschap.html` — visie, werking, bestuur
- `samenwerking.html` — GOBO + VLOT!
- `solliciteren.html` — sollicitatieprocedures
- `contact.html` — contactgegevens + formulier

## Bouwen
De HTML wordt gegenereerd uit één template door `build.py` (gedeelde header/footer):

```bash
python3 build.py
```

Pas inhoud aan in `build.py` en draai opnieuw. Styling staat in
`assets/css/site.css`, scriptjes in `assets/js/site.js`. Tailwind draait via CDN
(geen buildstap nodig).

## Lokaal bekijken
```bash
python3 -m http.server 8099
# → http://127.0.0.1:8099/
```

## Nog in te vullen (placeholders)
Zoek op `LET OP` in `build.py`:
- URL van het **sollicitatieformulier** (Google Form) — `solliciteren.html`
- URL van het **contactformulier** (Google Form) — `contact.html`
- URL van het **privacybeleid** — `contact.html`

## Assets
- `assets/img/logo-groei-*` — hoofdlogo (kleur / grijs / wit, web-versies)
- `assets/img/hero-illustratie.png` — kiemplant met vliegertje (hero)
- `assets/img/favicon.png` — kiemplant uit het logo
- `assets/img/puzzel*.png` — puzzelvisual (nog niet gebruikt; schoolnamen worden
  nog afgewerkt)

## Deploy op GitHub Pages
1. Repo aanmaken en pushen (branch `main`).
2. Settings → Pages → Source: `Deploy from a branch` → `main` / `(root)`.
3. `.nojekyll` zorgt dat GitHub niets wegfiltert.
