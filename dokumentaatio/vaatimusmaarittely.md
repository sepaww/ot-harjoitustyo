# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus pyörittää leikkimielistä sijoituspeliä, jossa pelaajan tavoitteena on selvitä alati nousevasta inflaatiosta sijoittamalla järkevästi annettuihin osakkeisiin sekä keksityn kaupan antimiin. Pelaajalle jaetaan osakkeista tarvittavat tiedot,
kuten hinta, nousu- tai laskusuhdanne ja osakehistoria, joiden avulla tämä voi tehdä optimaalisia investointeja. Pelin kulku seuraa roguelike tyyliä riskin ja palkkion periaattein. Pelaajan on oltava valmis ottamaan riskejä, mutta liiallinen riski tuo konkurssin.

## Pelaaja
Pelaaja saa valita yhden neljästä hahmosta, joilla on merkittävästi pelin kulkuun vaikuttavia ominaisuuksia. Eli eri hahmojen lähtökohdat ovat eri esim. toinen aloittaa suurilla rahamäärillä ja suurilla menoilla kun taas toinen pienillä.

## Käyttöliittymäluonnos
Peli koostuu 6 eri näkymästä:
- Aloitusruutu, jossa pelaaja voi käynnistää pelin. "tehty"
- Hahmovalikko, jossa pelaaja voi valita haluamansa hahmon peliin. "tehty"
- Pelinäkymä, jossa pelaaja näkee: osakkeet ja niihin liittyvät tiedot, rahamääränsa ja menomääränsä. "tehty"
- Osakehistoria, jossa pelaaja voi tarkastella osakkeen kurssihistoriaa. "tehty"
- Kauppa, josta pelaaja voi ostaa pelin kulkua muokkaavia asioita. "tehty"
- Tulosruutu, josta pelaaja näkee miten viime sijoitus sessio meni. "tehty"
- Gameover-ruutu, johon siirrytään pelaajan hävitessä pelin. "tehty"

##Perusversion tarjoama toiminnallisuus
- aloitusruutu, jossa start näppäin

- peliruutu, jossa pelaaja voi ostaa osakkeita tai tuotteita marketista. peliruutu siirtyy summary ruutuun ajan loppuessa tai pelaajan erikseen end-näppäintä painaessa. peliruudusta pelaaja myös näkee rahansa. sovelluslogiikkaan kuuluu kurssien teko sekä päivitys toiminnot, kauppaan tuotteiden lisäys, sekä rahallisten toimintojen toteutus pelaajan rahasaldoon oston tapahtuessa. peliruudussa tulee pelaajan voida myös tarkastella osakkeiden kursseja. "tehty"
- summary ruutu, jossa pelaaja voi tarkastella netto arvoaan, eli omistamiensa osakkeiden yhteisarvoa sekä käteisen summaa. pelaaja voi myös tarkastella uusia nousseita kulujaan. sovelluslogiikkaan kuuluu päivän vaihtoon liittyvät ominaisuudet, kuten pelaajan rahasaldon päivittäminen, pelin häviämisen ehtojen täyttymisen tarkastelu, nettoarvon laskeminen sekä tarvittavien ominaisuuksien alustaminen/päivittäminen tulevaa päivää varten. "tehty"
- loppu ruutu, jossa pelaaja voi tarkastella ennätys taulukkoa sekä listoille päästessään kirjoittaa neli-merkkisen nimensä, joka tallennetaan databaseen highscore. Sovelluslogiikkaan kuuluu databasen ylläpito, nimen kirjoittamista hallitseva ohjelma sekä viimeinen näkymä, jossa pelaaja voi joko pelata uudelleen tai lopettaa pelaamisen, mikä sammuttaa ohjelman "tehty"

### Aloitusruutu
- Käyttäjä voi painaa hiirellä nappia aloittaakseen pelin, jonka jälkeen peli siirtyy hahmovalikkoon, mistä pelaaja voi valita haluamansa hahmon neljästä vaihtoehdosta. "tehty"
- Hahmo vaikuttaa pelin sisäiseen Finance luokkaan, joka vastaaanottaa pelin taloudellisen lähtötilanteen sekä kustannusten skaalautumiseen liittyvät tiedot valitun hahmon tiedoista. "tehty"


### Pelinaloituksen_jälkeen

- Pelaaja siirtyy pelinäkymään
 - Pelinäkymä koostuu sijoitus/ostos vaiheesta, jonka jälkeen päivä vaihtuu ja pelissä siirrytään tulosruutuun,
 josta pelaaja voi tarkastella sijoitusten tuloksia eli omaa nettoarvoaan. "tehty"
 - Pelinäkymässä pelaaja voi myös tarkastella osakkeiden historiaa "tehty"
 - Jos pelaajan rahat eivät riitä menoihin siirrytään gameover näkymään, josta pelaaja voi tarkastella ennätyslistaa ja antaa oman nimimerkkinsä päästessään ennätys taululle. Ennätystaulu on toteutettu databasena. "tehty"
 
 ## Jatkokehitysideoita
 
 Jos aika sallii perusversioon lisätään pelinkulkua monipuolistavilla ominaisuuksilla:
 - Lisää tuotteita kauppaan
 - Osakkeen ominaisuudet, esim. osake voi kuulua luokkaa tech, jolloin sillä on suurempi todennäköisyys tehdä
 tappiota, mutta jos se tekee voittoa se todella raketoi arvossaan.
 - Visuaalisia lisäyksiä esim. pelaajan avatar, jonka ilme riippuu ajankohtaisesta rahatilanteesta.
