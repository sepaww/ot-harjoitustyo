

# Pörssipeli projekti
Itsekeksitty klikkeri/resurssien managerointi peli, jossa kilpaillaan sekä inflaatiota että aikaa vastaan.

## Dokumentaatio:

[releases](https://github.com/sepaww/ot-harjoitustyo/releases)

[käyttöohjeet](dokumentaatio/käyttöohjeet.md)

[tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

[määrittelydokumentti](dokumentaatio/vaatimusmaarittely.md)

[changelog](dokumentaatio/changelog.md)

[arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

[testausdokumentti](dokumentaatio/testaus.md)

## Näin saat pelin toimimaan:

1. Asennetaan riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistetään peli komennolla:

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

Testikattavuusreportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Reportin voi lukea _htmlcov_-hakemistosta tai terminaalista.

### Pylint

pelin koodin pelilogiikan laatua voi tarkastella komennolla

```bash
poetry run invoke lint
```
