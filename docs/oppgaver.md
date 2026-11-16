# Implementeringsplan

Gjør stegene i rekkefølge. Ett steg = én commit. Kryss av her når et steg er ferdig og testet i 390 px og desktop.

## Fase 1 – Grunnmur
- [x] **1. Tokens og fonter.** Legg Google Fonts-lenken og innholdet i `design/tokens.css` inn i `<style>` i `husorden.html`. Fjern gamle variabler og fonter (Shrikhand, Bricolage, krem/turkis-retro). Mørk modus: slå den av foreløpig (`color-scheme: light`); den designes senere.
- [x] **2. Grunnstil.** Bakgrunn `--vegg`, brødtekst Figtree, standard 2 px blekkkontur på kort, radius fra tokens, fokusring 3 px `--skiltturkis`.
- [x] **3. Skiltfunksjonen.** Lag `skilt({ tekst, undertekst, pil, bredde })` som bygger inline SVG etter `docs/design.md` §3. Escape tekst. Test med HUSORDEN, HEI, IDA! og et langt navn.

## Fase 2 – Voksenvisning
- [x] **4. Toppfelt.** Tapet-bakgrunn, skiltet (210 px) til venstre, runde uke-knapper til høyre, sjakkbånd under. Behold ukenummer/dato som tekst (f.eks. under skiltet eller i dagskortet).
- [x] **5. Ukestripe og dagskort.** Piller og fremdriftsring etter §5.
- [x] **6. Filterchips.**
- [x] **7. Oppgavelister.** Seksjonstitler, rader, vaskemaskindør-avkrysning (stil `input[type=checkbox]` med `appearance: none` – behold ekte checkbox), ferdig-tilstand, tildelt-merker, tips, slett.
- [x] **8. Øvrige seksjoner.** «Hvem gjør mest?», «Ny oppgave», «Familien», stjernemål-redigering: samme kort, knapper og felt.
- [x] **9. Bunnmeny + ny oppgave-knapp** (knappen hopper til «Ny oppgave»-skjemaet).

## Fase 3 – Barnevisning
- [x] **10. Topp.** Skilt «HEI, NAVN!» med antall igjen som undertekst, stjernekort, sjakkbånd.
- [x] **11. Barnekort med illustrasjoner.** Legg til valgfritt `ikon`-felt på oppgaver + velger i skjemaet, og nøkkelord-gjetting (§6). Store dør-knapper 58 px.
- [x] **12. Ledige oppgaver.** «Ta den»-kort med illustrasjon som barnekortene.
- [x] **13. Feiring.** Neon-boks «Glitrende!» etter avkrysning, «Alt er gjort i dag» og når stjernemålet er nådd (vis belønningen). Ingen illustrasjoner med mennesker.

## Fase 4 – Kvalitet
- [x] **14. Tilgjengelighet.** Sjekk kontrast (bruk parene i `docs/design.md`), tab-rekkefølge, `aria-label` på ikonknapper, `alt` på bilder, skjermleser-tekst for skiltet.
- [x] **15. Ytelse.** Bilder med `loading="lazy"` og faste mål. Vurder å komprimere PNG-ene (f.eks. `pngquant`) til under 100 KB hver.
  - Gjort: `loading="lazy"`, `decoding="async"` og faste mål (84×84) på alle oppgavebilder. Ikke gjort: komprimering. Ingen bildeverktøy (pngquant o.l.) var tilgjengelig lokalt; 14 av 23 PNG-er er over 100 KB (største ca. 140 KB).
- [ ] **16. Gjennomgang.** Sammenlign med mockupene i `design/mockups/` og ta skjermbilder av begge visningene i 390 px til brukeren.
