
# ma 7.11.2022
- pygame käyntiin projektina. Syntaksin ja toimintojen muistelua sekä pelin koodin rakenteen suunnittelua.
- etenemistä aloitusruutu toimintaan sekä pörssi saadan nyt blitattua ruudulle pelinäkymään.
- seuraavaksi ostamistoiminnot sekä raha tulot ja menot ja niihin liittyvä koodi.
- noin 7h

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
