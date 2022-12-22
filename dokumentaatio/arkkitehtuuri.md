# Arkkitehtuurikuvaus

## Rakenne
Peli on jaoteltu useisiin kansioihin niiden tyypin perusteella. Ohjelmaa pyörittää tiedosto main.py, joka on suoraan src kansiossa.
- pakkaus src sisältää pelin tiedostot
- ui sisältää käyttöliittymän koodia
  - inputs sisältää pelaajan hiiren liikkeitä ja inputteja tarkkailevan koodin, joka kutsuu/muokkaa sovelluslogiikan     mukaisesti pelin asioita.
  - screen sisältää koodin, jolla piirretään käyttöliittymään pelin ruutu.
  - tools sisältää muutamia toistoa vähentäviä valmiita funktioita, joiden avulla voidaan piirtää pelin ruutuun asioita.
- services sisältää pelilogiikkaa pyörittävät tiedostot
  - finance sisältää pelin sisäisen raha logiikan
  - day_change_op sisältää päivän vaihtoon liittyvän pelilogiikan
  - ending_screen_op sisältää pelin jälkeisiin tapahtumiin tarvittavan pelilogiikan
- repositories sisältää pysyväistietoa käsittelevät tiedostot
 
 ## Käyttöliittymä
 
 Peli koostuu viidestä eri päänäkymästä:
 - aloitusruutu
 - hahmovalinta
 - peliruutu
    - osake-finanssi näkymä
    - kauppa-finanssi näkymä
    - tiiviste ruutu, jossa pelin sisäisten päivien vaihtuessa kerrotaan pelaajalle tämän nettoarvo, eli onko osakkeista tullut voittoa
 - nimen anto ruutu, jos pelaaja pääsi ennätyslista
 - loppuruutu, näkyy ennätys taulu sekä mahdollisuus pelata uudelleen tai lopettaa (quit)
 
 ## Sovelluslogiikka
 Sovellusta pyörittää tiedosto main.py, josta kutsutaan kuhunkin pelin tilanteeseen liittyvät funktio sekä käyttöliittymän kontrollointi sekä inputit.
 Peli lähtee käyntiin funktiolla start_screen, josta kutsutaan funktio intialize, josta alustetaan suurin osa pelissä tarvittavista rakeinteista, kuten osakkeet, kaupan sisältö, pelaajan taloudellinen tilanne sekä osake historia. Initialize myös huolehtii pelaajan hahmo valinnasta. Kun hahmo on valittu siirtyy sovellus funktioon run, joka pyörittää itse peli looppia. run funktiosta kutsutaan tarvittavat input funktiot sekä draw_screen komennot peli-tilan ylläpitämiseen. run funktiosta voidaan myös päivittää pelaajan raha tilanne sekä kaupa sisältämät tuotteet.
 
Kun ajastin loppuu tai pelaaja painaa end näppäintä, siirrytään day_change_op tiedostoihin, jotka vastaavat pelaajan nettoarvon laskemisesta sekä uuden päivän alustamisesta, eli tulojen lisäämisestä rahaan, menojen poistaminen rahoista sekä menojen korottaminen.

Jos pelaajalla ei ole käteisvarantoja maksaa kuluja tämä häviää pelin ja siirrytään ending_screen_op tiedostoihin, joissa käsitellään pelin jälkeiset toiminnot. Jos pelaaja on päässyt ennätys tauluun, kysytään tämän nimeä ja pelaajan annettua nimensä tulos talletetaan ennätystaulukkoon repositoriesin database_op avulla.
 
valittu hahmo vaikuttaaa pelaajan aloitusrahan määrään, tuloihin sekä menoihin. Myös yksi tärkeä elementti hahmolla on rerollprice, joka määrittelee miten tehokkaasti tämä voi hyödyntää kauppaa. Hahmon vaikeustasoon vaikuttaa myös menojen skaalautuminen, mikä ilmoitetaan hahmovalikossa.
 
monet sovelluksen erityisesti käyttöliittymän käyttämistä muuttujista tulee stats.py tiedostosta, joka lukee tarvitut tiedot config.txt tiedostosta. stats on (ainakin yritetty) turvattu try-except lausekkeilla, jotta peliin ei pääsisi vääriä pelin kaatavia arvoja. config.txt tiedoston kautta pystyy muuttamaan haluttuja pelin arvoja, kuten tekstin väriä tai yleistä väriteemaa tai fontteja.

pelin pysyväistalletuksesta huolehtii highscore.db, jonka sisällä säilötään hs taulua, joka sisältää edelliset ennätykset ja pelaajien minimerkit. tiedoston voi tyhjentää huoletta, sillä sitä operoiva database_op.py on koodattu luomaan tiedostoon uusi taulu sen puuttuessa.

 ### Luokkakaavio pelin korkean tason kansioiden suhteista
 ```mermaid
 classDiagram
      src "*" -- ui
       src "*" -- services
        src "*" -- repositories
        src "*" -- tests
         ui "*" -- screen
         ui "*" -- inputs
         ui "*" -- tools
         services "*" -- day_change_op
         services "*" -- ending_screen_op
         services "*" -- finance
         
      class src{
          }
      class tests{
      all tests
          }
      class ui{
          }
      class services{
          }
      class repositories{
      database_op.py
      stats.py
          }
      class day_change_op{
      day_change_operator.py
      day_change.py
          }
      class screen{
      draw_ending.py
      draw_screen.py
      draw_start_screen.py
          }
      class inputs{
      start_inputs.py
      end_inputs.py
      inputs.py
          }
      class tools{
      draw_highlight.py
      draw_normal.py
          }
      class ending_screen_op{
      ending_init.py
      
          }
      class finance{
      effects.py
      finance.py
      items.py
      stock_creator.py
      stock_history.py
          }
     
      
      
```
 ### Luokkakaavio main.py:n suhteista (käyttöliittymän koodia ei ole otettu mukaan)
 ```mermaid
 classDiagram
      Main -- stock_creator
       Main -- finance
        Main -- items
         Main -- data_base_op
         Main -- ending_init
         Main -- stats
         Main -- day_change
         Main -- ending_init
         Main -- Data_base_op
         daychange -- day_change_operator
         daychange -- items
      class Main{
          start_screen()
          run()
          initialize()
      }
      class items{
          Item()
          item_pool
          item_giver()
      }
      stock_creator -- stock_history
      class stock_creator{
          names
          create_stocks()
          create_history_view()
          
      }
      
      class stock_history{
          stock_operator
          create_history
          
      }
      
      class Databaseop{
          clear_table()
          name_change()
          insert_in_table()
          exist()
          get_hs()
          
      }
      
      class finance{
          Finance()
      }
      class stats{
      Stats()
      Owned_stocks()
      Timer()
      Switch()
          
      }
      class finance{
      character_list
      Finance()
      }
      class day_change{
      day_change()
      summary_driver()
      }
      class day_change_operator{
      summary()
      finance_update()
      }
      class ending_init{
      need_new_name()
      }
      
```


## Päätoiminnallisuus
Kuvataan pelin toimintaa neljällä sekvenssi kaaviolla.


### Pelin käynnistystä sekä alustamista kuvaa seuraava sekvenssi kaavio
```mermaid
sequenceDiagram
  actor User
  participant start_inputs
  participant inputs
  participant draw_start_screen
  participant draw_screen
  participant Main
  participant finance
  participant items
  participant stock_creator
  participant stock_history
  User->>Main: Player starts the program
  Main->>Main: starting_screen()
  Main->>start_inputs: start_inputs()
  Main->>draw_start_screen: draw_startscreen()
  User->>start_inputs: Player clicks start
  Main->>Main: initialize()
  Main->>Main: character_select()
  Main->>draw_screen: draw_character_select(character_list)
  Main->>inputs: character_select_input(character_list)
  User->>inputs: Player picks a character
  Main->>stock_creator: create_stocks()
  stock_creator->>stock_history: create_history(stocks)
  Main->>finance:Finance(player_eco)
  Main->>items: item_giver()
  Main->>stats: Owned_stocks()
  Main->>stats: Timer()
  Main->>Main: run([stocks, money, owned, switch, item_list, day_switch, time])
  #Game starts running in mainloop and player ends up losing
  Main->>Main: return from run back to starting_screen
  Main->>Main: ending_screen()
  Main->>Main: starting_screen()
```
### Pelin pelinäkymää kuvaava sekvenssi kaavio

Tapahtumat pyörivät main.py tiedoston funktion run loopin sisällä nopeudella 10 tick/second.
Pelin peliloopin aikana ei juurikaan tapahdu muita pelilogiikan kannalta oleellisia asioita kuin rahatilanteen ylläpito ja omistettujen osakkeiden määrät sekä ostettujen asioiden aiheuttamien muutosten asettaminen voimaan. Suurin osa komennoista koostuu pelaajan syötteen lukemisesta sekä käyttöliittymän päivittämisestä niiden perusteella. kaikki kommunikointi käyttäjän ja ohjelman välillä tapahtuu hiirellä helpon käyttäjäkokemuksen luomiseksi.

  ```mermaid
sequenceDiagram
  actor User
  participant inputs
  participant Main
  participant effects
  participant items
  participant draw_screen
  participant (tools)
  Main->>Main: game_loop(shop_switch, whole_finance, day_switch, owned, stocks, item_list)
  Main->>draw_screen: draw_info(whole_finance, time_difference, timer, screen)
  Main->>inputs: inputter_stock(owned, stocks, whole_finance, shop_switch, day_switch)
  Main->>draw_screen: draw_stocks(stocks, screen)
  Main->>draw_screen: draw_owned(owned, screen)
  draw_screen->>(tools): certain unique pygame commands are used to draw needed elements on screen
  User->>inputs: Player leftclicks on a stock
  inputs->>finance: Finance.change_amount(stockprice)
  User->>inputs: Player rightclicks on a stock
  inputs->>finance: Finance.change_amount_up(stockprice)
  User->>inputs: Player leftclicks on market-> shopswitch.take=True
  Main->>draw_screen: blank() (cleans the screen to evade drawn objects overlapping
  Main->>inputs: inputter_market(shop_switch, item_list, whole_finance, day_switch)
  Main->>draw_screen: draw_shop(item_list, screen)
  User->>inputs: Player leftclicks on an item
  inputs->>effects: apply_effect(effects, finance_info)
  User->>inputs: Player clicks reroll
  inputs->>finance: Finance.change_amount(Finance.reroll_price)
  inputs->>finance: Finance.reroll_doubler()
  Main->>items: item_giver()
  User->>inputs: User clicks on end to end the current day -> day_switch.take=True
  Main->>draw_screen: whole_blank(screen)
```
seuraavaksi tapahtuu pelin sisäisen päivän vaihto ja siihen liittyvät toimenpiteet. Jos pelaajan käteisvarat eivät kuitenkaan riitä menoihin, peli siirtyy päivänvaihdon sijaan lopetusruutuun.

### Pelin päivän vaihto
Päivän vaihdon operaatioista huolehtii kansion day_change_op sisällä olevan tiedostot. daychange.py on ikäänkuin ajaja day_change_operator.py:lle. jälkimmäisessä taas on päivän vaihtoo liittyvät pelilogiikan kannalta tärkeät asiat, kuten nettoarvon laskeminen sekä rahatilanteen päivittäminen ja kulujen lisäys.


  ```mermaid
sequenceDiagram
  actor User
  participant inputs
  participant Main
  participant day_change
  participant day_change_operator
  participant Finance
  participant items
  participant stock_history
  participant draw_screen
  Main->>day_change: day_change(stocks, whole_finance, owned, timer)
  day_change->>items: item_giver()
  day_change->>stock_history: stock_update(stocks)
  stock_history->>stock_history: stock_operator(stock)
  day_change->>day_change_operator: finance_update(finance, timer)
  day_change->>day_change_operator: summary(stocks, finance, owned)
  day_change->>Main: return summary, item_list and stocks
  Main->>day_change: summary_driver(screen, summary, whole_finance, summary_loop)
  day_change->>draw_screen: draw_summary(screen, summary, finance)
  day_change->>inputs: summary_input(summary_loop)
  User->>inputs: Player clicks on "okey" button and a new day begins and timer resets
  Main->>draw_screen: whole_blank() clears whole screen
```

### lopetus ruutu ja ennätyslista
Seuraavat tapahtumat alkavat pelaajan hävitessä pelin. operaatioihin kuuluu ennätystaulun päivittäminen, pelaajan nimen ottaminen ja mahdollisuus antaa pelaajan pelata peliä uudestaan tai lopettaa pelaaminen.
  ```mermaid
sequenceDiagram
  actor User
  participant end_inputs
  participant main
  participant Finance
  participant items
  participant stock_history
  participant draw_ending
  participant data_base_op
  participant ending_init
  main->>main: ending_screen(days)
  main->>database_op: data_base=Data_base_op()
  data_base_op->>data_base_op: self.exist()
  data_base_op->>data_base_op: self.get_hs()
  main->>ending_init: need_new_name(days. data_base) (in this case player made it to highscoretable and name is needed)
  main->>draw_ending: draw_name_need(data_base. screen)
  main->>end_inputs: nameinputs(database. needname. cursorposition)
  User->>end_inputs: player types their name and pressses enter ending loop
  end_inputs->>data_base_op: Data_base.name_change()
  data_base_op->>data_base_op: Data_base.clear_table()
  data_base_op->>data_base_op: Data_base.insert_in_table()
  main->>draw_ending: draw_hs(database. screen) draw highscorelist
  main->>end_inputs: next_inputs()
  User->>end_inputs: player presses play again
  main->>main: back to starting screen loop
```

