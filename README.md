# Husorden

En familieapp for husarbeid: oppgaver dag for dag, daglige vaner, en fireukers plan med en halvtime om dagen, større ryddeoppgaver innimellom, barnevisning med stjerner og en oversikt over hvem som gjør mest.

Appen er publisert som en Claude-artifact: https://claude.ai/artifact/WqsyM4joBeTF3XHUBwCx1c

## Innhold

| Sti | Hva |
|---|---|
| `husorden.html` | Hele appen i én fil: HTML, CSS og JavaScript uten byggesteg. |
| `forhandsvis.html`, `verktoy/server.js` | Lokal forhåndsvisning (se under). |
| `data/tasks/*.json` | Oppgavene slik de ligger i appens delte lager (ett dokument per oppgave). |
| `assets/skilt/`, `assets/illustrasjoner/` | Skiltet (SVG) og 23 oppgavebilder (PNG i appen, SVG som master). |
| `CLAUDE.md` | Instruksjoner for Claude Code. |
| `docs/design.md` | Designspesifikasjonen (fasiten). |
| `docs/oppgaver.md` | Implementeringsplanen i 16 steg, med avkrysning. |
| `docs/illustrasjoner.md` | Motivliste, nøkkelord og prompt for nye bilder. |
| `design/tokens.css`, `design/mockups/`, `design/referanser/` | Tokens, mockups fra Claude Design og inspirasjonsbilder. |
| `verktoy/fargejuster.py`, `verktoy/vektoriser.py` | Justerer nye AI-bilder til paletten og lager SVG. |

`husorden.html` er skrevet for Claude-artifacter. Den har ingen `<html>`/`<head>`/`<body>`, fordi de legges på ved publisering.

### Kjøre lokalt

```bash
node verktoy/server.js . 8765
```

Åpne deretter http://localhost:8765. `forhandsvis.html` legger på det samme skallet som artifacten får. Lokalt lagres alt i nettleserens `localStorage`, og lista er tom til du legger inn oppgaver selv.

## Design: vaskerom-retningen

Pastell 50-tallsvaskerom: krem vegg med prikketapet, HUSORDEN-skilt med pil, mint og rosa, sjakkrutebånd og glitter. Neon brukes bare til feiring, på mørk bunn. Fasiten er `docs/design.md`.

Alle farger, skrifter, radier og skygger er CSS-variabler i `:root` øverst i `<style>`, kopiert fra `design/tokens.css`.

| Token | Verdi | Bruk |
|---|---|---|
| `--vegg` | `#FBF7F0` | Bakgrunn |
| `--kort` | `#FFFFFF` | Kort, lister, felt |
| `--blekk` | `#1A2227` | Tekst, 2 px konturer, sjakkruter |
| `--krom` | `#5E6A72` | Dempet tekst |
| `--skapturkis` | `#1FC1B8` | Primærknapp, valgt dag, avkrysset, fremdrift |
| `--skiltturkis` | `#0B7A74` | Lenker, seksjonstitler, knappskygge |
| `--maskinmint` | `#8EE3C8` | Ringen rundt avkrysning, skiltramme |
| `--skumaqua` | `#D2F4EE` | Ferdige oppgaver |
| `--handklerosa` | `#F7A1B5` | Skiltflate, barn |
| `--lysrosa` | `#FFD9E1` | Barnechips, ledige oppgaver, tips |
| `--glitter` | `#FFE45C` | Glitter og stjerner |
| `--kirsebaer` | `#B4233F` | Slett og feil |
| `--natt` og `--neon-*` | – | Neon-feiring |

Skrifter (Google Fonts): Anton til skiltet, Bebas Neue til skiltets undertekst, Righteous til overskrifter og tall, Figtree til brødtekst og Neonderthaw til neon-feiringen.

Kontrast: tekst i `--skiltturkis` på `--skumaqua` og `--krom` på `--lysrosa` er under 4,5:1. På de flatene brukes `--blekk`.

Appen har ett lyst tema. Mørk modus er ikke designet ennå.

### Publisering som artifact

Oppgavebildene lenkes med relative stier (`assets/illustrasjoner/<navn>.png`). Det virker lokalt, men ikke i en Claude-artifact. Før den publiserte appen oppdateres, må bildene lastes opp som assets der og stiene byttes.

## Datamodell

Tre samlinger i artifactens `db`:

- `members/{id}`: `name`, `child`, `starGoal`, `reward`, `created`
- `tasks/{id}`: `title`, `minutes`, `kind`, `days`, `rot`, `every`, `order`, `date`, `child`, `assignee`, `tips`, `ikon`, `created`
- `done/{YYYY-MM-DD}`: `ids` (oppgave → hvem som fikk æren) og `claims` (oppgave → hvem som tok den den dagen)

`kind` er en av:

- `vane`: daglig vane
- `oppgave`: vanlig oppgave
- `plan`: steg i «Dagens halvtime», sortert på `order`
- `stor`: større ryddeoppgave som gjentas hver `every` uke

`ikon` er valgfritt: filnavnet til et oppgavebilde uten `.png`. Uten `ikon` gjetter appen bilde fra tittelen (se `docs/illustrasjoner.md`).

`days` er ukedager (1 = mandag). `rot` er planuker (1–4) i en fast fireukers rotasjon regnet fra mandag 1. januar 2024. Tom liste betyr alle.
