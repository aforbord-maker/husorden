# Husorden

En familieapp for husarbeid: oppgaver dag for dag, daglige vaner, en fireukers plan med en halvtime om dagen, større ryddeoppgaver innimellom, barnevisning med stjerner og en oversikt over hvem som gjør mest.

Appen er publisert som en Claude-artifact: https://claude.ai/artifact/WqsyM4joBeTF3XHUBwCx1c

## Innhold

| Sti | Hva |
|---|---|
| `husorden.html` | Hele appen i én fil: HTML, CSS og JavaScript uten byggesteg. |
| `data/tasks/*.json` | Oppgavene slik de ligger i appens delte lager (ett dokument per oppgave). |

`husorden.html` er skrevet for Claude-artifacter. Den har ingen `<html>`/`<head>`/`<body>`, fordi de legges på ved publisering. Åpnes fila direkte i en nettleser, fungerer den likevel, men lagrer da bare i nettleserens `localStorage`.

## Nytt design på vei: vaskerom-retningen

Appen skal over på et nytt design: pastell 50-tallsvaskerom med HUSORDEN-skilt, mint og rosa, sjakkruter og glitter. Alt som trengs ligger her:

| Sti | Hva |
|---|---|
| `CLAUDE.md` | Instruksjoner for Claude Code |
| `docs/design.md` | Designspesifikasjonen (fasiten) |
| `docs/oppgaver.md` | Implementeringsplan i 16 steg |
| `design/tokens.css` | Nye farger, fonter og former |
| `design/mockups/` | Mockups fra Claude Design (referanse) |
| `assets/skilt/`, `assets/illustrasjoner/` | Skiltet (SVG), oppgavebilder og merker (PNG) |
| `verktoy/fargejuster.py` | Justerer nye AI-bilder til paletten |

Start Claude Code i repoet og skriv: «Les CLAUDE.md, docs/design.md og docs/oppgaver.md. Start på fase 1 og vis meg resultatet etter hvert steg.»

## Design (nåværende, erstattes)

50-tallsretro med moderne vri. Alle farger og skrifter er tokens i `:root` øverst i `<style>`.

| Token | Verdi | Bruk |
|---|---|---|
| `--bg` | `#FFF7EA` | Bakgrunn (krem) |
| `--surface` | `#FFFFFF` | Kort og lister |
| `--ink` | `#1D2B3A` | Tekst, 2px kanter, harde skygger |
| `--muted` | `#5B6878` | Sekundær tekst |
| `--accent` | `#0D7A72` | Primærknapper, valgt dag, avkryssing |
| `--mint` | `#5FD3C6` | Fremdriftsstolpe |
| `--mint-soft` | `#D3F2EA` | Ferdige oppgaver |
| `--child` | `#FFCF4D` | Barn, barneoppgaver, ledige oppgaver |
| `--adult` | `#F6A6B6` | Voksne |
| `--pink-soft` | `#FDE3E7` | Meldinger |
| `--danger` | `#A8281E` | Sletting |

Skrifter (Google Fonts): Shrikhand til logo og «Hei, …!», Bricolage Grotesque 800 til overskrifter og tall, Figtree til brødtekst.

Kjennetegn: 2px marineblå kanter, harde forskjøvne skygger (`3px 3px 0`), sjakkstripe øverst, runde piller, stjerne for barn og rosa prikk for voksne. Appen har ett lyst tema og ingen mørk variant.

## Datamodell

Tre samlinger i artifactens `db`:

- `members/{id}`: `name`, `child`, `starGoal`, `reward`, `created`
- `tasks/{id}`: `title`, `minutes`, `kind`, `days`, `rot`, `every`, `order`, `date`, `child`, `assignee`, `tips`, `created`
- `done/{YYYY-MM-DD}`: `ids` (oppgave → hvem som fikk æren) og `claims` (oppgave → hvem som tok den den dagen)

`kind` er en av:

- `vane`: daglig vane
- `oppgave`: vanlig oppgave
- `plan`: steg i «Dagens halvtime», sortert på `order`
- `stor`: større ryddeoppgave som gjentas hver `every` uke

`days` er ukedager (1 = mandag). `rot` er planuker (1–4) i en fast fireukers rotasjon regnet fra mandag 1. januar 2024. Tom liste betyr alle.
