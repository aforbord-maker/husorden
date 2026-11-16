# Husorden – designspesifikasjon (vaskerom-retningen)

**Stemning:** et pastell retro-vaskerom fra 50-tallet med moderne vri. Krem vegger med prikketapet, turkise skap, mintgrønne vaskemaskindører, rosa håndklær, sjakkrutegulv og et diner-skilt med pil. Det skal føles **glitrende rent og ryddig**: mye luft, få farger per skjerm, glitter når noe blir ferdig, og neon bare til feiring.

Alle verdier finnes som CSS-variabler i `design/tokens.css`.

---

## 1. Farger

| Token | Hex | Brukes til | Tekst på fargen |
|---|---|---|---|
| `--vegg` | #FBF7F0 | Bakgrunn i hele appen | `--blekk` (16:1) |
| `--kort` | #FFFFFF | Kort, lister, inputfelt | `--blekk` |
| `--blekk` | #1A2227 | All tekst, 2 px konturer, sjakkruter | – |
| `--krom` | #5E6A72 | Dempet tekst: minutter, gjentakelse, hjelpetekst | på vegg/hvit: 5,2–5,5:1 |
| `--skapturkis` | #1FC1B8 | Primærknapp, valgt dag, avkrysset, fremdrift | `--blekk` (7,2:1). **Aldri hvit tekst** (2,2:1) |
| `--skiltturkis` | #0B7A74 | Skiltkant, lenker, seksjonstitler, knappskygge | hvit 5,2:1 / som tekst på vegg 4,9:1 |
| `--maskinmint` | #8EE3C8 | Ringen rundt avkrysning, skiltramme | `--blekk` |
| `--skumaqua` | #D2F4EE | Bakgrunn på ferdige oppgaver | `--blekk` |
| `--handklerosa` | #F7A1B5 | Skiltflate, barnemerker, feiring | `--blekk` (8,2:1). **Aldri hvit tekst** |
| `--lysrosa` | #FFD9E1 | Barnechips, tips-bokser | `--blekk` |
| `--glitter` | #FFE45C | Glitterstjerner, stjernetelling | (dekor) |
| `--kirsebaer` | #B4233F | «Slett», feilmeldinger | på hvit 6,4:1 |
| `--natt` | #141A22 | Bunn for neon | – |
| `--neon-rosa` / `--neon-turkis` / `--neon-gul` | #FF4FA3 / #2FF3E0 / #FFE45C | Neon-glød | bare på `--natt` |

**Regler**
- Skapturkis er den eneste «gjør noe»-fargen. Én primærknapp per skjerm/seksjon.
- Rosa betyr barn og feiring. Voksne har hvite chips.
- Kirsebær bare når noe kan gå tapt.
- Neon: kun på `--natt`, kun til feiring (oppgave ferdig, alt gjort i dag, mål nådd).

## 2. Typografi

Google Fonts-lenke står øverst i `design/tokens.css`.

| Rolle | Font | Eksempel |
|---|---|---|
| Logo / skiltnavn | Anton | HUSORDEN, HEI, IDA! (alltid store bokstaver) |
| Skiltets undertekst | Bebas Neue, 4 px sperring | — VASK • RYDD • GLITRE — |
| Overskrifter, datoer, tall | Righteous | MANDAG 16. NOV, DAGLIGE VANER, 3/7 |
| Brødtekst og UI | Figtree 400–800 | oppgavenavn 16 px/700, meta 13 px |
| Neon-feiring | Neonderthaw | *Glitrende!* (bare på mørk bunn) |

- Seksjonstitler (DAGLIGE VANER, OPPGAVER): Righteous 16 px, store bokstaver, sperring 0.08em, farge `--skiltturkis`.
- Brødtekst minst 16 px. Barnevisningen: oppgavenavn 18 px/800.

## 3. Skiltet (logo og hilsen)

Filer: `assets/skilt/husorden-skilt.svg` (logo) og `assets/skilt/hei-navn-eksempel.svg`. Kilde: `design/mockups/Skilt.dc.html`. Inspirasjon: `design/referanser/skilt-gemini-*.png`.

Oppbygning (viewBox 0 0 1040 760):
1. Skrå firkant med runde hjørner, punkter `110,175 915,105 895,585 150,600`. Tegnes som fire lag av samme polygon med `stroke-linejoin="round"`: blekk (stroke 88) → maskinmint (78) → hvit (30) → håndklærosa (20).
2. Navn i Anton 200 px, `text-anchor="middle"` på x=512, y=372. Fyll `--skiltmint` #B8F0DD, kontur blekk 7 px (`paint-order="stroke"`). Bak den 9 lag med 3D-skygge forskjøvet ca. 1,1/1,2 px per lag i #E58A9B, bakerste lag med blekkkontur.
   - Lange navn: `font-size = 200 * 9 / antall tegn` når over 9 tegn. `textLength = min(760, tegn * fontstørrelse * 0.47)`, `lengthAdjust="spacingAndGlyphs"`.
3. Undertekst i Bebas Neue 80 px, blekk, y=510.
4. To femtakkede stjerner oppe til venstre over rammen: mint (150,150; r=58) og rosa (250,112; r=54), blekkkontur 7.
5. Hvitt firtakket glitter spredt i flaten.
6. Pil nederst som stikker ut til høyre: mint fyll, blekkkontur, hard blekkskygge (10,12) og hvite «lyspærer» langs midten.

**Implementering:** lag en JS-funksjon `skilt({ tekst, undertekst, pil = true, bredde })` som returnerer inline SVG (samme markup som i SVG-filene, med tekst satt inn og escaped). Brukes:
- Voksenvisning, toppen: `skilt({ tekst: 'HUSORDEN', undertekst: '— VASK • RYDD • GLITRE —', bredde: 210 })`.
- Barnevisning, toppen: `skilt({ tekst: 'HEI, ' + navn.toUpperCase() + '!', undertekst: '— ' + n + ' OPPGAVER IGJEN —', bredde: 290 })`, eller «— ALT ER GJORT —».
- `role="img"` og `aria-label` med hele teksten. `<h1>` i dokumentet kan være visuelt skjult tekst ved siden av SVG-en.

## 4. Mønstre

- **Prikketapet** (`--tapet`): bak toppfeltet på hver skjerm. Rosa og mint prikker 28 px rutenett.
- **Sjakkrutebånd** (`--sjakk`): 16 px høyt bånd rett under toppfeltet. Aldri bak tekst.

## 5. Komponenter

**Primærknapp:** `--skapturkis`, tekst `--blekk` Figtree 800, 2 px blekkkontur, pille-radius, `box-shadow: var(--skygge-knapp)`, min. høyde 52 px. Trykk: `translateY(3px)` og mindre skygge.
**Sekundærknapp:** hvit, samme kontur, skygge `--skygge-knapp-sek`.
**Slett:** tekstknapp i `--kirsebaer`, bekreftelse som i dag.
**Ikonknapper** (uke frem/tilbake, bytt visning): 44 px runde, hvit, 2 px blekkkontur.

**Ukestripe:** 7 piller i rutenett. Ukedag 11 px/800 store bokstaver, dato Righteous 19 px, telling 11 px. Valgt: `--skapturkis` + `--skygge-valgt`. I dag: tykkere kontur.

**Dagskort:** hvitt kort, 2 px kontur, radius 24. Venstre: rund fremdriftsring 76 px (conic-gradient skapturkis på skumaqua, hvit kjerne med «3/7» i Righteous). Høyre: dato i Righteous store bokstaver + «ca. 35 min igjen».

**Filterchips:** pille, 2 px kontur. Valgt = blekk-fyll med hvit tekst. Barn = `--lysrosa` fyll.

**Oppgaveliste:** hvit boks, 2 px kontur, radius 22, rader skilt med 2 px linjer.
- **Avkrysning = vaskemaskindør:** 32 px rund, hvit, 5 px ring i `--maskinmint`, ytre 2 px blekkring. Avkrysset: fyll `--skapturkis` med blekk-hake.
- Ferdig rad: bakgrunn `--skumaqua`, tittel gjennomstreket i `--krom`, gult glitter til høyre.
- Tildelt-merke: pille med 2 px kontur, `--handklerosa` for barn, hvit for voksne.

**Barnekort:** hvitt, 2 px kontur, radius 24, padding 12. Illustrasjon 84 px til venstre, tittel/meta/«Slik gjør du det» i midten, avkrysningsdør 58 px til høyre (7 px mint ring). Ferdig: `--skumaqua`, grønn hake, «Ferdig · +1 stjerne».

**Stjernekort (barn):** hvitt, glitterstjerne, «Ukas glitter 12 av 20», stolpe 12 px med skapturkis fyll på skumaqua.

**Neon-feiring:** mørk boks (`--natt`), radius 24. «Glitrende!» i Neonderthaw 46 px, farge #FFE3F1 med `--glod-rosa`. Undertekst i Righteous 13 px med `--glod-turkis` (f.eks. «SENGEN ER REDD»). En rosa neonring delvis utenfor hjørnet. Vises etter at en oppgave krysses av (dagens `state.lastDone`) og når alt er gjort. Respekter `prefers-reduced-motion` hvis du animerer.

**Bunnmeny:** hvit, 2 px kontur øverst, tre faner. Aktiv i `--skiltturkis` 800.
**Ny oppgave-knapp:** rund 62 px, skapturkis, blekkkontur, turkis hard skygge, plusstegn.

## 6. Illustrasjoner

Alle i `assets/illustrasjoner/`. Laget med ChatGPT og fargejustert til paletten. Stil: skrå sticker-ramme med mint kant, rosa eller aqua flate, to stjerner (mint + rosa) oppe til venstre, hvitt glitter, mørk kontur.

**Oppgaver** (PNG 480×480 i appen, SVG som master): status, filnavn og nøkkelord står i `docs/illustrasjoner.md`. 12 av 23 motiver er ferdige. Koden skal tåle at et bilde mangler (vis glitter-ikonet).

**Regel for alle illustrasjoner:** én gjenstand som viser hva oppgaven handler om. Ingen mennesker, ingen metaforer (trapper, raketter, puslespill, lyspærer o.l.). Barnet skal skjønne oppgaven uten å lese.

**Planlagt sett** (mangler foreløpig – se `docs/illustrasjoner.md` for prompt og liste): ett motiv per gjenstand, brukt på tvers av oppgaver via nøkkelord.

**Kobling oppgave → bilde:** legg til et valgfritt felt `ikon` på oppgaven (verdi = filnavn uten .png) med velger i «Ny oppgave»-skjemaet. Uten `ikon`: gjett fra tittelen med nøkkelordene i `docs/illustrasjoner.md`. Ingen treff: vis et lite glitter-ikon i stedet.

Bilder: `alt=""` når tittelen står ved siden av (dekor), `loading="lazy"`, `width`/`height` satt.

Nye bilder: kjør `python3 verktoy/fargejuster.py inn.png ut.png 640` for å treffe paletten.

## 7. Skjermer

Mål og markup: se `design/mockups/VaskeromIdag.dc.html` og `VaskeromBarn.dc.html` (390 × 844). Palettside med alle komponenter: `Vaskerom.dc.html`.

**Voksenvisning («I dag»):** tapet-topp med skilt + uke-knapper → sjakkbånd → ukestripe → dagskort → filterchips → «DAGLIGE VANER» → «OPPGAVER» → (eksisterende seksjoner: Hvem gjør mest?, Ny oppgave, Familien) → bunnmeny + ny oppgave-knapp.

**Barnevisning:** tapet-topp med «HEI, NAVN!»-skilt + stjernekort → sjakkbånd → «Mine oppgaver i dag» (barnekort med illustrasjon) → «Ledige oppgaver – ta en!» → neon-feiring nederst når noe er ferdig.

Innholdsbredde maks 760 px, sidemarg 20 px på mobil.

## 8. Ikke gjør

- Ingen hvit tekst på turkis, rosa, mint eller gult.
- Ingen gradienter utenom fremdriftsringen og neon-glød.
- Ingen emoji som ikoner – bruk inline SVG.
- Ingen sjakkruter bak tekst, ingen neon på lys bunn.
- Ikke bland inn bilder i andre stiler (bare dette illustrasjonssettet).
