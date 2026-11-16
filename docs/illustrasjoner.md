# Illustrasjoner – status, nøkkelord og prompter

**Regel:** én gjenstand per bilde som viser hva oppgaven handler om. Ingen mennesker, ingen hender, ingen metaforer, ingen tekst. Et barn på 9 skal skjønne oppgaven uten å lese.

Alle bilder ligger i `assets/illustrasjoner/<filnavn>.png` (480×480). Appen velger bilde ut fra nøkkelord i oppgavetittelen (se tabellen). Nøkkelordene sjekkes i rekkefølgen i tabellen; første treff vinner. Store bokstaver ignoreres. Ingen treff → lite glitter-ikon.

## Status

Hvert motiv finnes som `.svg` (vektor, masterfil – store filer, 400–700 KB) og `.png` (480×480, brukes i appen).

| Filnavn | Status | Nøkkelord i oppgavetittel |
|---|---|---|
| `plan` | ❌ Mangler | plan for neste uke, kjøleskapsjekk |
| `skuffer` | ❌ Mangler | skuffer, rotskuff, baderomsskap, kjøkkenskap, skap innvendig |
| `vask` | ✅ | sette på vask, vaske pledd, gardiner, putetrekk |
| `oppvaskmaskin` | ✅ (tallerkener) | oppvaskmaskin, oppvask |
| `dekke-bordet` | ✅ | rydde kjøkkenet etter middag, dekke bordet |
| `brette` | ✅ | brette, tørkestativ, tørre klær, rent tøy |
| `kurv` | ✅ (kurv med tøy) | kveldsrydd, skittentøy, på plass, rydde flater, ryddeoppgave |
| `sokker` | ❌ Mangler | sokker, pare |
| `seng` | ✅ | re opp, sengetøy, madrass |
| `stovsuger` | ✅ | støvsuge, sofa |
| `mopp` | ✅ | vaske gulv, gulvene |
| `bad` | ❌ Mangler | bad, dusj, toalett, sluk, fliser |
| `kjokkenbenk` | ❌ Mangler | benker, benkene, vasken, komfyr, kran |
| `kjoleskap` | ❌ Mangler | kjøleskap, fryser |
| `ovn` | ❌ Mangler | stekeovn, mikrobølgeovn, kjøkkenvifte |
| `klut` | ✅ | tørke, støv, fronter, dører, lister, lamper, karmer, håndtak |
| `sopla` | ✅ | søppel, sortere, søppelbøtte |
| `sko` | ✅ (har en liten musikknote – kan byttes) | sko, jakker, ytterklær, gang |
| `klesskap` | ❌ Mangler | klesskap, garderobe |
| `leker` | ❌ Mangler | leker, spill |
| `papirer` | ❌ Mangler | post, papirer |
| `vindu` | ❌ Mangler | vinduer, vinduskarmer |
| `plante` | ✅ | planter |

Tabellen står i den rekkefølgen nøkkelordene skal sjekkes. Rekkefølgen betyr noe: «Kjøleskapsjekk og plan for neste uke» skal treffe `plan` før `kjoleskap`, og «Rydde baderomsskapene» skal treffe `skuffer` før `bad`. Claude Code bør legge spesialtilfellene øverst i nøkkelordlista.

## Slik lager du et nytt bilde (ChatGPT)

1. Start en ny samtale og legg ved **`assets/illustrasjoner/vask.png`** som stilreferanse.
2. Lim inn **grunnprompten** og bytt ut `[MOTIV]` med motivet fra lista under. Ett bilde per melding.
3. Er bildet bra, ber du om neste motiv i samme samtale: «Same style, new subject: [MOTIV]».
4. Lagre som PNG og kjør: `python3 verktoy/fargejuster.py nedlastet.png assets/illustrasjoner/<filnavn>.png 480` (vektorisering er valgfri: `pip install vtracer`, se `verktoy/vektoriser.py`)
5. Oppdater status i tabellen over.

**Avvis bildet** hvis det har mennesker eller hender, tekst, symboler som lyspærer/raketter/trofeer, åpen ramme, eller en annen stil (f.eks. akvarell).

### Grunnprompt

```
Make a sticker illustration in EXACTLY the same style as the attached image: tilted rounded sign-shaped frame with a mint border, thin cream inner line and a pink background, a mint star and a pink star overlapping the top-left corner, white four-pointed sparkles, short cream "shine" strokes, dark teal outlines, flat pastel colours with small glossy highlights.
Subject: ONLY [MOTIV], shown clearly and centred, filling about 70% of the frame.
No people, no hands, no faces, no text, no symbols or metaphors (no light bulbs, trophies, rockets, hearts).
Colours: pink #F7A1B5, mint #8EE3C8, turquoise #1FC1B8, pale aqua #D2F4EE, cream #FBF7F0, dark teal outlines #1A2227, yellow #FFE45C only for small sparkles.
Square 1024×1024, transparent background, complete frame on all four sides.
```

### Motiver – lim inn i stedet for `[MOTIV]`

**Gjenstår (11):**
1. `sokker` – two matching pairs of striped socks lying side by side
2. `bad` – a sparkling clean toilet next to a small sink with a round mirror above
3. `kjokkenbenk` – a clean kitchen counter with a sink and a shiny tap
4. `kjoleskap` – an open retro fridge with tidy shelves
5. `ovn` – a retro oven with a microwave on top, both doors closed and shiny
6. `klesskap` – an open wardrobe with clothes on hangers and folded sweaters on a shelf
7. `skuffer` – an open drawer with small organiser boxes inside
8. `leker` – a toy box with building blocks, a ball and a soft teddy on top
9. `papirer` – a tidy stack of letters and papers held by a clip
10. `vindu` – a sparkling clean window with tied-back curtains
11. `plan` – a small notice board with a calendar sheet and a pinned shopping list (no readable text)
