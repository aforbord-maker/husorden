// Bygger data/sjekklister/*.json inn i husorden.html (mellom SJEKKLISTER:START og SJEKKLISTER:SLUTT).
// Artefakten har ikke tilgang til repoet, så dataene må ligge i selve fila.
// Bruk: node verktoy/bygg-sjekklister.js   (kjør på nytt hver gang en fil i data/sjekklister/ endres)
const fs = require('fs'), path = require('path');
const rot = path.resolve(__dirname, '..'), mappe = path.join(rot, 'data', 'sjekklister');
const les = navn => JSON.parse(fs.readFileSync(path.join(mappe, navn + '.json'), 'utf8'));

const ukeplan = les('ukeplan');
const rekkefolge = Object.keys(ukeplan.dager).sort().flatMap(d => ukeplan.dager[d]);
const rom = rekkefolge.map(id => {
  const r = les(id);
  return { id: r.id, navn: r.navn, ikon: r.ikon, seksjoner: r.seksjoner.map(s => ({ id: s.id, navn: s.navn, punkter: s.punkter.map(p => p.husk ? { id: p.id, tittel: p.tittel, husk: p.husk } : { id: p.id, tittel: p.tittel }) })) };
});
const data = {
  ukeplan: { dager: ukeplan.dager, ukeIMaaned: ukeplan.ukeIMaaned, startsvaner: ukeplan.startsvaner, bruk: ukeplan.bruk, minutterPerDag: ukeplan.minutterPerDag },
  rom,
  rutiner: les('faste-rutiner').rutiner
};

const fil = path.join(rot, 'husorden.html'), a = '/*SJEKKLISTER:START*/', b = '/*SJEKKLISTER:SLUTT*/';
let t = fs.readFileSync(fil, 'utf8');
const i = t.indexOf(a), j = t.indexOf(b);
if (i < 0 || j < 0) throw new Error('Fant ikke markørene ' + a + ' og ' + b + ' i husorden.html');
t = t.slice(0, i + a.length) + JSON.stringify(data).replace(/</g, '\\u003c') + t.slice(j);
fs.writeFileSync(fil, t);
console.log('Bygget inn ' + rom.length + ' rom, ' + rom.reduce((s, r) => s + r.seksjoner.reduce((n, x) => n + x.punkter.length, 0), 0) + ' punkter og ' + data.rutiner.length + ' rutiner.');
