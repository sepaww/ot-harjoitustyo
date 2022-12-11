#Testausdokumentti

Pelin koodin testaamiseen on hyödynnetty unittest moduulia. Testit kattavat pelilogiikan kannalta olennaiset tiedostot. Käyttöliittymän koodia ei ole sisällytetty testikattavuuteen.

## Yksikkötestaus ja integraatio testaus.

Sovelluslogiikan yksikkötesteistä huolehtivat tiedostoa vastaavasti nimetyt tests kansion testitiedostot.
Sovelluksen pelilogiikka, joka sijaitsee kansiossa services on melko kattavasti testattu.
testikattavuuden ulkopuolelle on jätetty kansion ui tiedostot, kuten inputit sekä grafiikasta vastaava koodi. Myöskin main.py on jätetty ulkopuolelle, sillä sen ainoa tehtävä on kutsua muita tiedostoja.

## Konfigurointi
Sovellus on testattu toimivaksi ainakin Linux sekä windows ympäristössä.
Sovelluksen väriteema sekä fonttiteemat ovat tehty helposti vaihdettaviksi config.txt tiedoston avulla.
Ne on myös turvattu try-except komennoilla, jottei peliin pääse vääriä arvoja, jotka aiheuttaisivat kaatumisen.
