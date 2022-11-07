# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus pyörittää leikkimielistä sijoituspeliä, jossa pelaajan tavoitteena on selvitä alati nousevasta vuokrasta
sijoittamalla järkevästi annettuihin osakkeisin. Pelaajalle jaetaan osakkeista tarvittavat tiedot,
kuten hinta, nousu- tai laskusuhdanne ja osakehistoria, joiden avulla tämä voi tehdä optimaalisia investointeja. Pelin kulku seuraa
roguelite tyyliä riskin ja palkkion periaattein. Pelaajan on oltava valmis ottamaan riskejä, mutta liiallinen riski tuo konkurssin

## Pelaaja
Pelaaja tullee toimimaan anonyyminä henkilönä (jollei hahmovalikoimaa lisätä peliin)\
Jos hahmovalikoima lisätään, voi jokaisella hahmolla olla eriävä 
tulo sekä meno määrä tai jokin sijoitusta auttava ns. perkki.

## Käyttöliittymäluonnos
Peli koostuu 6 eri näkymästä:
- Aloitusruutu, jossa pelaaja voi käynnistää pelin.
- Pelinäkymä, jossa pelaaja näkee: osakkeet ja niihin liittyvät tiedot, rahamääränsa ja menomääränsä.
- Osakehistoria, jossa pelaaja voi tarkastella osakkeen kurssihistoriaa.
- Kauppa, josta pelaaja voi ostaa pelin kulkua muokkaavia asioita.
- Tulosruutu, josta pelaaja näkee miten viime sijoitus sessio meni.
- Gameover-ruutu, johon siirrytään pelaajan hävitessä pelin.

##Perusversion tarjoama toiminnallisuus


### Aloitusruutu
- Käyttäjä voi painaa hiirellä nappia aloittaakseen pelin

### Pelinaloituksen_jälkeen

- Pelaaja siirtyy pelinäkymään
 - Pelinäkymä koostuu sijoitus/ostos vaiheesta, jonka jälkeen päivä vaihtuu ja pelissä siirrytään tulosruutuun,
 josta pelaaja voitarkastella sijoitusten tuloksia
 - Pelinäkymässä pelaaja voi myös tarkastella osakkeiden historiaa
 - Jos pelaajan rahat eivät riitä menoihin siirrytään gameover näkymään, josta pelaaja voi tarkastella ennätyslistaa
 
 ## Jatkokehitysideoita
 
 Jos aika sallii perusversioon lisätään pelinkulkua monipuolistavilla ominaisuuksilla:
 - Hahmovalikoima, joka toisi peliin lisää uudelleen pelaus arvoa
 - Lisää tuotteita kauppaan
 - Osakkeen ominaisuudet, esim. osake voi kuulua luokkaa tech, jolloin sillä on suurempi todennäköisyys tehdä
 tappiota, mutta jos se tekee voittoa se todella raketoi arvossaan.
 - Visuaalisia lisäyksiä esim. pelaajan avatar, jonka ilme riippuu ajankohtaisesta rahatilanteesta.
