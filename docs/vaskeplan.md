# VaskMedMeg-planen – 30 minutter om dagen

Ny funksjon. Data ligger i `data/sjekklister/` (`ukeplan.json` + én fil per rom). Les dem og `docs/design.md` før du starter. Kilde: VaskMedMeg (månedlige sjekklister, ukentlig vaskeplan og artikkelen «Vaskeplanen som tar opptil 30 minutter») – kun til familiens eget bruk.

## Slik skal det virke
1. Hver ukedag (man–fre) viser «I dag» et kort **«Dagens 30 minutter»**: rommene fra `ukeplan.dager` for i dag og fokusområdet fra `ukeplan.ukeIMaaned` for denne uka i måneden (uke 1 = dag 1–7 osv.). Inventar deles over uke 2 og 3 (første halvdel av punktene i uke 2, resten i uke 3). Dag 29–31: vis alle punkter fra denne måneden som ikke er krysset av («Ta igjen»).
2. Kortet viser romillustrasjonen (feltet `ikon`), fokusområdet og fremdrift («4/9»). Trykk åpner en egen skjerm med punktene som rader.
3. Hvert punkt har to valg: **«Vasket»** (vaskemaskindør-avkrysningen) og **«Ser fint ut»** (liten sekundærknapp). Begge teller som ferdig. `husk`-teksten vises under tittelen som «Husk: …».
4. Familiemedlemmer kan ta punkter («Ta den»-mønsteret). Barn ser punktene sine i barnevisningen og får 1 stjerne per punkt.
5. Lørdag og søndag: kortet **«Chillax»** med de fem `ukeplan.startsvaner` som avkrysningsliste, pluss lenken «Kryss av mer fra månedslistene».
6. Når dagens punkter er ferdige: neon-feiringen «Glitrende!» med undertekst «DAGENS 30 MINUTTER ER GJORT».
7. Ny skjerm **«Sjekklister»** (lenke fra «Uka»): alle rom med fremdrift for måneden, så man kan åpne et hvilket som helst rom og krysse av fritt.
8. Under «Familien»: slå rom av/på (ikke alle har garderoberom eller vaskerom) og flytt et rom til en annen ukedag. Lagre valgene.
9. Tak: egen påminnelse i mars og september (`ukeplan.tak`). Ikke del av ukeplanen.

## Filosofien bak (styrer tekst og oppførsel)
Fra VaskMedMeg-artikkelen «Vaskefilosofien: litt og ofte». Funksjonen skal kjennes lett, ikke som en pliktliste.

- **Litt og ofte.** Aldri mer enn ca. 30 minutter per dag i forslaget. Vis anslått tid på kortet («ca. 25 min»). Det skal være lettere å *holde* det rent enn å *gjøre* rent.
- **Ingen etterslep og ingen dårlig samvittighet.** Punkter som ikke ble gjort, hoper seg ikke opp som røde «forfalt»-oppgaver. De dukker bare opp igjen i «Ta igjen» (dag 29–31). Ingen røde tall, ingen «du ligger etter».
- **Godt nok er godt nok.** «Ser fint ut» er like verdt som «Vasket». Bruk vennlig tekst: «Godt nok er godt nok»-tonen, ikke perfeksjon. (Ingen emoji i UI – bruk glitter-ikonet.)
- **Ett lite steg i dag.** Når planen slås på første gang: start med bare startsvanene i én uke, foreslå så å slå på ett rom om gangen («Klar for kjøkkenet?»). Vis en kort velkomst som forklarer dette, med knappen «Ta første lille steg».
- **Startsvanene er grunnmuren.** Hver tar 1–5 minutter. Koble dem til eksisterende daglige vaner i appen der de finnes (f.eks. «Re opp sengen») i stedet for å lage duplikater; vis dem som en egen liten gruppe «Startsvaner» på «I dag» hver dag, ikke bare i helgen.
- **Hele familien.** Husarbeid er ikke én persons jobb – punkter fordeles og tas av alle, og «Hvem gjør mest?» teller også punkter fra planen.

## Data
- Bygg inn JSON-filene i `husorden.html` ved oppstart (ingen nettverkskall – artefakten har ikke tilgang til repoet).
- Ny samling `sjekk`: nøkkel `<rom>-<ÅÅÅÅ-MM>` → `{ <punktId>: { status: 'vasket' | 'fint', av: medlemsId | null, dato } }`.
- Ny samling `planvalg`: rom av/på og valgt ukedag per rom.
- Ikke endre `members`, `tasks`, `done` eller `claims`.
- Fremdrift nullstilles naturlig ved ny måned (ny nøkkel). Forrige måned beholdes.
- Vis «Etter VaskMedMeg» med liten skrift nederst på sjekkliste-skjermen.

## Ferdig når
- Testet med falsk dato for uke 1, 2, 3, 4, dag 30 og en lørdag, i 390 px, i voksen- og barnevisning, uten feil i konsollen.
- Fasen «VaskMedMeg-planen» i `docs/oppgaver.md` er krysset av. Commit på norsk og publiser til artefakten.
