#Testausdokumentti

Pelin koodin testaamiseen on hyödynnetty unittest moduulia. Testit kattavat pelilogiikan kannalta olennaiset tiedostot. Käyttöliittymän koodia ei ole sisällytetty testikattavuuteen.

## Yksikkötestaus ja integraatio testaus.

Sovelluslogiikan yksikkötesteistä huolehtivat tiedostoa vastaavasti nimetyt tests kansion testitiedostot.
Sovelluksen pelilogiikka, joka sijaitsee kansiossa services on melko kattavasti testattu.
testikattavuuden ulkopuolelle on jätetty kansion ui tiedostot, kuten inputit sekä grafiikasta vastaava koodi. Myöskin main.py on jätetty ulkopuolelle, sillä sen ainoa tehtävä on kutsua muita tiedostoja. Samalla logiikalla daychange.py on jätetty testaamatta, sillä sekin vain kutsuu muita (day_change_operator) pelilogiikkaa hoitavia funktioita. Se on kuitenkin sisällytetty kattavuuteen säännönmukaisuuden takia.

repositories kansiossa olevista tiedostoista stats.py ja sen sisältämät pelissä käytettävät oliot on testattu. database_op.py:lle ei ole tehty omia yksikkötestejä. koodi pätkä ei kuitenkaan ota mitään arvoja vastaan, joten sen toiminta pysyy staattisena vaikka pelin kehitystä jatkettaisiin.

Osassa testeistä testataan myös luokkien vuorovaikutusta. Tällaisia ovat esimerkiksi stockcreator_test.py:n testit, joissa testataan sekä osakkeiden luonnin, historianluonnin, sekä osakkeen kurssingraafin matemaattisloogisen toiminnan yhteistyö. Myös day_change_operator_test yhdistelee komponentteja finance.py:stä sekä stats.py:stä ja testaa niiden yhteisvaikutuksia.

### Testikattavuus

![image](https://user-images.githubusercontent.com/117186747/206911653-a2264b73-eb45-4af9-b4a3-5348567da227.png)


## Konfigurointi
Sovellus on testattu toimivaksi ainakin Linux sekä windows ympäristössä.
Sovelluksen väriteema sekä fonttiteemat ovat tehty helposti vaihdettaviksi config.txt tiedoston avulla.
Ne on myös turvattu try-except komennoilla, jottei peliin pääse vääriä arvoja, jotka aiheuttaisivat kaatumisen.

## Toiminnallisuudet

peli on toteutettu määrittelydokumentin vaatimusten perustein. Väärien arvojen antaminen sovellukselle sen juostessa on mahdotonta syystä, että käyttöliittymänä toimii vai hiiri. config.txt on ainakin yritetty turvata vääriä arvoja vastaan.

# Laatuongelmat pelin koodissa:
- Pelin tiedostojen tulee sisältää config.txt sekä highscore.db nykyisillä paikoillaan, sillä muuten peli ei aukea. Ominaisuuden olisi voinut toteuttaa niin, että nämä tiedostoto voisivat sijaita missä vain.
-  Jokainen stats.py:tä hyödyntävä tiedosto lukee sen uudelleen (stats luetaan noin 7 kertaaa pelin aikana). Ominaisuuden olisi saattanut voida toteuttaa järkevämminkin.
-  
