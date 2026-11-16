# Husorden – instruksjoner for Claude Code

Husorden er familiens app for å fordele husarbeid og barneoppgaver. Denne repoen inneholder dagens app og et ferdig nytt design ("vaskerom-retningen") som skal implementeres i den.

Svar og skriv brukertekst på **norsk bokmål**. All tekst i appen er på norsk.

## Hva som ligger her

| Mappe | Innhold |
|---|---|
| `husorden.html` | Dagens app. Én fil med HTML, CSS og JS, uten byggesteg og uten `<html>`/`<head>`/`<body>` (legges på når den publiseres som Claude-artefakt). Dette er filen du endrer. |
| `data/tasks/*.json` | Familiens oppgaver slik de ligger i appens lager. Bruk titlene til å teste ikon-gjettingen. Ikke endre dem. |
| `docs/design.md` | **Designspesifikasjonen.** Les den helt før du begynner. Den er fasiten. |
| `docs/oppgaver.md` | Implementeringsplanen, steg for steg. Følg rekkefølgen og kryss av. |
| `docs/navigasjon.md` | Navigasjonsikonene (bunnmeny, plussknapp, barnevisning) og hvordan de brukes. |
| `docs/illustrasjoner.md` | Motivliste, nøkkelord for å koble oppgaver til bilder, og prompt for nye bilder. |
| `design/tokens.css` | Alle farger, fonter, radier og skygger som CSS-variabler. Kopier inn i appen. |
| `assets/skilt/` | HUSORDEN-skiltet som SVG (logo) + eksempel med navn. |
| `assets/illustrasjoner/` | Oppgaveillustrasjoner (PNG, 480×480). |
| `design/mockups/*.dc.html` | Mockups fra Claude Design. **Bare referanse** – de bruker en mal-syntaks (`{{...}}`, `<sc-if>`, `<dc-import>`, `<x-dc>`) som ikke kjører i appen. Les dem for mål, avstander og markup, men ikke kopier formatet. |
| `design/referanser/` | Inspirasjonsbilder (skiltet og illustrasjonssettet som designet bygger på). |

## Om dagens app (`husorden.html`)

- Lagring: bruker `window.claude.use('db')` når appen kjører som Claude-artefakt (samlinger `members`, `tasks`, `done`, og `claims`), ellers `localStorage` (`husorden-v1`). **Ikke endre datamodellen eller lagringslogikken** med mindre en oppgave sier det. Designjobben er visuell.
- UI bygges i JS med hjelpefunksjonen `h(tag, props, ...barn)` og `render*()`-funksjoner (`renderWeek`, `renderFilters`, `renderDay`, `renderCompare`, `renderMembers`, `renderGoal`, `renderKidLinks`, `renderKid`).
- Barnevisning: `state.view` = id til et barn → `renderKid()`; ellers voksenvisning.
- Stjerner: `stars(t)` = minutter / 5 (min. 1). Barn har `starGoal` og `reward`.
- Appen har allerede et tidlig retro-utkast (krem/turkis, Shrikhand, Bricolage – beskrevet i README under «Design»). Det skal **erstattes** av vaskerom-designet i `docs/design.md`. Oppdater README-tabellen når tokens er byttet.

## Arbeidsregler

1. Les `docs/design.md` og `docs/oppgaver.md` før du rører koden.
2. Behold én fil (`husorden.html`) og ingen byggesteg, med mindre brukeren ber om noe annet. Ikke legg til `<html>`/`<head>`/`<body>`. Fonter lenkes med `<link>` øverst i fila slik den gjør i dag. Bilder og SVG-er lenkes fra `assets/` med relative stier, eller legges inline der spesifikasjonen sier det. Merk: når appen publiseres som Claude-artefakt, må bildene lastes opp som assets der og stiene byttes – spør brukeren før det.
3. Bruk CSS-variablene fra `design/tokens.css` – ikke hardkod hex-koder i komponentene.
4. Endre utseende, ikke oppførsel. Alle eksisterende funksjoner (ukevisning, filtre, tildeling, tips, stjernemål, «Ta den», «Hvem gjør mest?», familie) skal virke som før.
5. Tilgjengelighet er et krav: tekstkontrast minst 4,5:1 (kontrollerte par står i designspesifikasjonen), trykkflater minst 44 px, ekte `<button>`/`<input>`/`<label>`, `aria-label` på ikonknapper, dekorative SVG-er med `aria-hidden="true"`.
6. Neon brukes **bare** på mørk bunn og bare til feiring. Sjakkruter bare som kantbånd, aldri bak tekst.
7. Test i mobilbredde (390 px) og desktop (maks 760 px innholdsbredde). Sjekk både voksenvisning og barnevisning.
8. Commit i små steg, ett steg fra `docs/oppgaver.md` per commit, med norsk commit-melding.

## Når du er usikker

Spør heller enn å gjette når designspesifikasjonen ikke dekker noe. Foreslå løsning i samme stil (mint/rosa, mørk kontur, hard skygge, stjerner) og la brukeren velge.
