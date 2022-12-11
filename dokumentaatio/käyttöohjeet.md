## Ohjeet:
- Peliä pelataan kokonaisuudessaan hiirellä. hiiren vasemmalla painikkeella voi ostaa osakkeen/tuotteen kaupasta ja oikealla painikkeella myydä omistamiaan osakkeita. 
- klikattavissa olevat painikkeet kirkastuvat kun hiirellä hoverataan niiden yli, jotta pelaaja paremmin hahmottaa käytettävissään olevat komennot.
- Tavoitteena on pörssikeplottelun avulla sekä kaupasta saatavien pysyvien parannusten voimalla taistella yhä nousevaa inflaatiota vastaan samalla kun noin 30 sekunnin ajastin rajoittaa toiminta aikaa.
- Mitä pidemmälle päivissä pelaaja pääsee, sitä parempi hänen ennätyksensä on.
- päivien välissä (ajastimen loppuessa) pelaajan käteisvaroista vähennetään menot. jos pelaajalla ei ole tarpeeksi käteistä päivän lopussa maksaa hän häviää pelin.
- osakkeiden kurssit vaihtelevat melko villisti päivien välissä sekä kaupan tarjonta vaihtuu.



## Asennus
komennot suoritetaan ot-harjoistustyo kansion sisällä.

1. lisäosa poetry:n alustus komennolla:

```bash
poetry install
```

2. Pelin saa käyntiin komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

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

Testien raportin voi luokea hakemiston _htmlcov_ tiedoston index.html avulla tai komentoriviin tulostuvalla informaatiolla.

pylint virheet saa esiin komennolla:

```bash
poetry run invoke lint
```

