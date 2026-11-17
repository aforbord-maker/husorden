# Illustrasjoner – status, nøkkelord og prompter

**Regel:** én gjenstand per bilde som viser hva oppgaven handler om. Ingen mennesker, ingen hender, ingen metaforer, ingen tekst. Et barn på 9 skal skjønne oppgaven uten å lese.

Alle bilder ligger i `assets/illustrasjoner/<filnavn>.png` (480×480). Appen velger bilde ut fra nøkkelord i oppgavetittelen (se tabellen). Nøkkelordene sjekkes i rekkefølgen i tabellen; første treff vinner. Store bokstaver ignoreres. Ingen treff → lite glitter-ikon.

## Status

Hvert motiv finnes som `.svg` (vektor, masterfil – store filer, 400–700 KB) og `.png` (480×480, brukes i appen).

| Filnavn | Status | Nøkkelord i oppgavetittel |
|---|---|---|
| `plan` | ✅ | plan for neste uke, kjøleskapsjekk |
| `chillax` | ✅ | chillax, helg, kaffe |
| `hverdagsflaske` | ✅ | hverdagsflaske |
| `matboks` | ✅ | matboks, drikkeflaske, flaske |
| `skolesekk` | ✅ | skolesekk, sekken |
| `bag` | ✅ | bager, gymbag, treningsbag, bagen |
| `dusjglass` | ✅ | dusjglass, skrap dusj, glassdør |
| `sengetoy` | ✅ | skift(e) sengetøy, dyne, madrassbeskytter |
| `lampe` | ✅ | lampe, belysning, lysarmatur |
| `sofa` | ✅ | sofa, lenestol |
| `skuffer` | ✅ | skuffer, rotskuff, baderomsskap, kjøkkenskap, skap innvendig |
| `vask` | ✅ | sette på vask, vaske pledd, gardiner, putetrekk |
| `oppvaskmaskin` | ✅ (tallerkener) | oppvaskmaskin, oppvask |
| `dekke-bordet` | ✅ | rydde kjøkkenet etter middag, dekke bordet |
| `brette` | ✅ | brette, tørkestativ, tørre klær, rent tøy |
| `kurv` | ✅ (kurv med tøy) | kveldsrydd, skittentøy, på plass, rydde flater, ryddeoppgave |
| `sokker` | ✅ | sokker, pare |
| `seng` | ✅ | re opp, sengetøy, madrass |
| `stovsuger` | ✅ | støvsuge, sofa |
| `mopp` | ✅ | vaske gulv, gulvene |
| `bad` | ✅ | bad, dusj, toalett, sluk, fliser |
| `kjokkenbenk` | ✅ | benker, benkene, vasken, komfyr, kran |
| `kjoleskap` | ✅ | kjøleskap, fryser |
| `ovn` | ✅ | stekeovn, mikrobølgeovn, kjøkkenvifte |
| `klut` | ✅ | tørke, støv, fronter, dører, lister, lamper, karmer, håndtak |
| `sopla` | ✅ | søppel, sortere, søppelbøtte |
| `sko` | ✅ (har en liten musikknote – kan byttes) | sko, jakker, ytterklær, gang |
| `klesskap` | ✅ | klesskap, garderobe |
| `leker` | ✅ | leker, spill |
| `papirer` | ✅ | post, papirer |
| `vindu` | ✅ | vinduer, vinduskarmer |
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

**Alle 32 motiver er ferdige.** Nye motiver lages med grunnprompten over; be gjerne om flere på ett ark i et rutenett uten tekst, og klipp dem ut.
