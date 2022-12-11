
# Pörssipeli projekti
Itsekeksitty klikkeri/resurssien managerointi peli, jossa kilpaillaan sekä inflaatiota että aikaa vastaan.

## Ohjeet:
-Peliä pelataan kokonaisuudessaan hiirellä. hiiren vasemmalla painikkeella voi ostaa osakkeen/tuotteen kaupasta ja oikealla painikkeella myydä omistamiaan osakkeita. 
- Tavoitteena on pörssikeplottelun avulla sekä kaupasta saatavien pysyvien parannusten voimalla taistella yhä nousevaa inflaatiota vastaan samalla kun noin 30 sekunnin ajastin rajoittaa toiminta aikaa.
- Mitä pidemmälle päivissä pelaaja pääsee, sitä parempi hänen ennätyksensä on.
- päivien välissä (ajastimen loppuessa) pelaajan käteisvaroista vähennetään menot. jos pelaajalla ei ole tarpeeksi käteistä päivän lopussa maksaa hän häviää pelin.
- osakkeiden kurssit vaihtelevat melko villisti päivien välissä sekä kaupan tarjonta vaihtuu.

##Dokumentaatio:
[releasevko5](https://github.com/sepaww/ot-harjoitustyo/releases/tag/viikko5)

[käyttöohjeet](dokumentaatio/käyttöohjeet.md)

[tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

[määrittelydokumentti](dokumentaatio/vaatimusmaarittely.md)

[changelog](dokumentaatio/changelog.md)

[arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)


##Näin saat pelin toimimaan:

1. Asennetaan riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistään peli komennolla:

```bash
poetry run invoke start
```

## Peliä voi myös käsitellä seuraavilla terminaali komennoilla:


### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportin voi lukea _htmlcov_-hakemistosta tai terminaalista.

### Pylint

pelin koodin pelilogiikan laatua voi tarkastella komennolla

```bash
poetry run invoke lint
```
