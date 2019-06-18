# Rajoitukset ja kehitysideat

Alle on mainittu listana työssä olevat rajoitukset ja kehitysideat

- *Kävijänä näen eniten tykätyn kuvan ensin.* Tämä oli yksi alunperin suunnitelluista user storeista, mutta jätin sen pois lopulta sen takia, että priorisoin muut kurssiin kuuluvat tehtävät tämän toiminnallisuuden rakentamisen edelle (kuten esimerkiksi tämän "rajoitukset ja kehitysideat" dokumentin kirjoittamisen)
- *Kävijänä voin muokata näkymän niin, että vähiten tykätty kuva tulee näkyviin ensin.* Sama selitys kuin yläpuolella.
- *Kävijänä voin suodattaa kuvat päivämäärien mukaan.* Tämä on kolmas ja viimeinen alunperin suunnitelluista toiminnallisuuksista, jonka jätin pois. Syy oli se, että päivämäärien mukaan filtteröinnissä tiettyä päivämäärää olennaisempaa on ehkäpä pystyä filtteröimään jokin jakso (esim. 15.6. - 19.6.). Muuten päivämäärän mukaan filtteröinnin olisi voinut tehdä helposti samalla tavalla kuin henkilön nimen perusteella filtteröinnin. Sama perustelu kuin ylhäällä, eli priorisoin tehtäviä, joista koin saavani enemmän hyötyä.
- Käyttäjät eivät voi muokata tietojaan tai poistaa tiliään. Tämä toiminnallisuus olisi periaatteessa sama kuin kuvien tietojen muokkaus ja kuvien poisto.
-  Hashtagien osalta ei tarkisteta alkavatko kaikki # -merkillä. Tutkin asiaa noin 3 tuntia, ja lopulta kokeilin luoda oman uniikin hashtag -fieldin (vähän kuin StringField on omansa). Huomasin kuitenkin hyvin äkkiä olevani paljon syvemmissä vesissä kuin olisin odottanut, ja lopulta päätin, ettei tuon kentän validoinnin selvittäminen ole siihen tarvittavan ajan arvoista.
- Kuvat voisi tallettaa BLOB -tietoina (tai jotenkin muuten suoraan tiedostona). Nyt tuntuu vähän hölmöltä tallentaa kuva url -tietona. Oikeasti mikään galleria applikaatio ei taida toimia niin, että antaa mahdollisuuden ainoastaan url:in lisäämiseen kuvien kohdalla.
- Applikaatio lähettää kirjautumis-/rekisteröitymistiedot normaalina POST -kutsuna. Telegram -ryhmän mukaan pääsisin tästä hyvästä vankilaan oikeassa elämässä.
- Applikaation html tiedostoja voisi muokata niin, että applikaatio näyttäisi miellyttävämmältä. Nyt käyttöjärjestelmä on helppokäyttöinen, mutta karu.
