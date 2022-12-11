
# ma 7.11.2022
- pygame käyntiin projektina. Syntaksin ja toimintojen muistelua sekä pelin koodin rakenteen suunnittelua.
- etenemistä aloitusruutu toimintaan sekä pörssi saadan nyt blitattua ruudulle pelinäkymään.
- seuraavaksi ostamistoiminnot sekä raha tulot ja menot ja niihin liittyvä koodi.


# ti 8.11.2022
- kauppa toimintaan ja sinne tulevat asiat, ei vielä ruudulle kuitenkaan.
- määritelty pelaajan rahallinen tilanne sekä siihen liittyvä logiikka.
- rakenteiden suunnittelua.


# ke 9.11.2022
- kauppa ruudulle näkyviin ja näkymän vaihtava logiikka toimintaan.
- koodin osioiden siirtelyä pois samasta main.py tiedostosta erillisiin luokiteltuihin tiedostoihin.
- parannuksia koodin laatuun.
- vähemmän copypastea ja lisätty muutama "tool" funktio, joiden avulla vähemmän copypastea.
- osakemäärät ja niiden logiikka näkyviin.


# to 10.11.2022
  - määrittelydokumentti toimintaan
  

# la 12.11.2022
- pelin perustoiminnallisuus kasassa.
 - pelaaja voi sijoittaa rahansa haluamiinsa osakkeisiin tai myydä omistamansa osakkeet, pelaaja voi ostaa kaupasta pysyviä parannuksia avittamaan päivien edetessä.
 - jos pelaajan rahat ovat riittämättömät, niin tämä häivää pelin ja peli siirtyy aloitus ruutuun.
- korjattu virheitä, kuten toimimattomnia tuotteita kaupassa sekä vääriä muuttuja-arvoja näyttävät osakekurssit.
- seuraavaksi ending screen, highscores, sql, (configuraatio.txt), mahdollisesti itemmaker kauppaa varten, hahmo valinta, luck-modifieri jne...

# 21.11.2022
- Lisätty koodia testaavat testit ja niiden kattaavuus 89%
- paranneltu osakkeiden koodia (vähemmän copypastea)
- ohjelman koodi luokiteltu omiin osiinsa ja niitä vastaaviin foldereihin (vähemmän koodia yhdellä tiedostolla jolloin toivottavasti selkeämpää)
- changelog ja tuntikirjanpito erillisiksi

# 28.11.2022
- Lisätty ending screeniin liittyvät pygame koodit sekä sovelluslogiikkaan liittyvät koodit kuten database_op sekä endinginit.
- lisätty database
- parannettu hakemisto rakennetta src:n sisällä
- lisätty stats luokka, josta voidaan lukea ja lisätä vaivattomasti yleisesti käytettyjä käyttöliittymään liittyviä muuttujia.
- Lisätty config.txt, josta stats lukee tietonsa.
- massiivinen linttaus listan lyhennys sadoista neljään.
- seuraavaksi reroll toiminto kauppaan, hahmovalikko ja osakehistoria

# 5.12.2022
- erotettu pelilogiikkaa käyttöliittymästä (lähinnä inputtien pieniä muutoksia rahatilanteeseen erotettu financeen uusiksi funktioiksi)
- lisätty reroll ominaisuus kauppaan sekä tehty sille skaalautuvuus
- lisätty hahmovalikko, jossa 4 erilaista hahmo vaihtoehtoa, jotka kukin vaikuttavat pelin kulkuun omalla tavallaan.
- seuraavaksi osakehistoria, mahdollisesti item_maker ominaisuus taikka hahmo_maker

# 6.12.2022
- pelin värit nyt täysin muutettavissa pelaajan toiveiden mukaan. (nyt myös teksti)
- parempi testikattavuus
- uudelleen lintattu
- alustavat sekvenssikaaviot

# 8.12.2022
- peliin vihdoin lisätty osakehistorian katselu mahdollisuus.
  - pelaaja voi avata historia näkymän klikkaamalla osakkeen h näppäintä
  - osakkeen 10 päivän historian korkein sekä alhaisin arvo esitetään graafin ylä sekä ala reunoissa
- testien kattavuutta korotettu
- pelissä käytettävien olentojen luokkia siirretty ulos main.pystä stats.py:hyn

# 9.12.2022
- ohjelmaa lintattu.
- hakemistorakenne uudistettu.
- arkkitehtuuri sekä vaatimusmäärittely päivitetty ajantasalle.

# 11.12.2022
- dokumentaatiota paranneltu
- testausdokumenttilisätty
