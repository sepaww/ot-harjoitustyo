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
## Pelin kulku

aloitusruutu
![image](https://user-images.githubusercontent.com/117186747/206914114-1ac5207f-353d-43e3-ae8e-009601b16047.png)

hahmovalikko
![image](https://user-images.githubusercontent.com/117186747/206914134-f05f695f-2bfc-4034-8361-5ac3b288da9e.png)

itse pelinäkymä osakkeiden kanssa
![image](https://user-images.githubusercontent.com/117186747/206914166-377aff9e-e071-4d6c-acd4-ce02ed68c0af.png)

kauppanäkymä
![image](https://user-images.githubusercontent.com/117186747/206914229-c08bd3af-6755-424b-b00b-2c89d93cb364.png)

summary
![image](https://user-images.githubusercontent.com/117186747/206914247-1d5b818e-a336-452f-8bd3-7c9bbc3e66b5.png)

gameover ruutu (nimenä xd)
![image](https://user-images.githubusercontent.com/117186747/206914288-4726e8a6-470d-48c2-ad87-7f4d4c340586.png)

play again/quit ruutu
![image](https://user-images.githubusercontent.com/117186747/206914314-e08df8a0-f08a-4b1f-8bd7-c4d1e3089a16.png)

