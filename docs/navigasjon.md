# Navigasjonsikoner

Filer i `assets/nav/` – hver i to tilstander, som PNG (96×96, brukes i appen) og SVG (master):

| Ikon | Inaktiv | Aktiv | Brukes til |
|---|---|---|---|
| Utklippstavle med hake | `idag.png` | `idag-aktiv.png` | Fanen «I dag» |
| Kalender | `uka.png` | `uka-aktiv.png` | Fanen «Uka» |
| Hus med hjerte | `familien.png` | `familien-aktiv.png` | Fanen «Familien» |
| Pluss i sirkel | `ny.png` | `ny-aktiv.png` | Ny oppgave (plussknappen / fanen «ny») |
| Stjerne | `barn.png` | `barn-aktiv.png` | Knapper til barnevisning («Idas visning») |

Bildene ligger også i Claude-artefakten på samme sti (`assets/nav/…`), så relative stier virker både lokalt og publisert.

## Regler

- **Bunnmeny:** ikonet vises i **32×32 px** over etiketten. Inaktiv fane: inaktiv variant + etikett i `--krom`. Aktiv fane (`aria-current`): aktiv variant + etikett i `--skiltturkis`, 800. Ingen annen bakgrunnsfarge på fanen.
- **Plussknappen:** bruk `ny-aktiv.png` i 56×56 px som selve knappen (behold `aria-label="Ny oppgave"`, fjern den gamle turkise sirkelen og plusstegnet). Når «Ny oppgave»-skjermen er åpen er knappen skjult som i dag.
- **Barnevisning-knapper:** `barn.png` 24 px foran navnet; `barn-aktiv.png` ved hover/fokus.
- Ikonene er dekor: `alt=""` og `aria-hidden="true"` – teksten på knappen er det tilgjengelige navnet.
- `width`/`height` alltid satt, `decoding="async"`. Ikke `loading="lazy"` i bunnmenyen (den er alltid synlig).
- Bytt bilde ved å sette `src` i `visFane()` når aktiv fane endres – ikke med CSS-bakgrunn.

## Prompt til Claude Code

> Les docs/navigasjon.md. Bytt ut SVG-ikonene i bunnmenyen med bildene i assets/nav/ etter reglene der, gjør plussknappen om til ny-aktiv.png, og bruk stjerneikonet på knappene til barnevisningen. Test i 390 px at fanene bytter mellom inaktiv og aktiv variant, og publiser til artefakten.
