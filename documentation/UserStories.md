### User Storyt

**HUOM! UserStorien kohdalla puhutaan usein näkymistä. Näillä tarkoitetaan html -tiedostoja.** 

- ~~Sivun kävijänä näen listan kaikista kuvista~~ **Toiminnallisuus lisätty 28.5.**
SQLALchemy toteuttaa tämän kysely toteutettu käskyllä `pictures = Picture.query.all()` mitä vastaa `SELECT * FROM picture`

- ~~Sivun kävijänä näen listan kaikista kuvien ottamisajankohdasta~~ **Toiminnallisuus lisätty 28.5.**
Sovelluksessa tämä kysely on toteutettu yllä olevan kyselyn palauttaman oliolistalta valitsemalla `{{ picture.date_taken }}`. Saman kyselyn voisi periaatteessa toteuttaa SQL:llä tyyliin `SELECT date_taken FROM picture WHERE id = "tähän haluttavan kuvan id"`.  
- ~~Sivun kävijänä näen määrän kuvien tykkäyksistä~~ **Toiminnallisuus lisätty 2.6.**
Tämä on toteutettu antamalla näkymälle tieto `likes = Like.query.all()`, josta näkymä sitten tarkistaa kyseisen kuvan kohdalla tykkäysten määrän. SQL kysely voisi olla samankaltainen kuin yllä  `SELECT COUNT(*) FROM like WHERE picture_id = "tähän haluttavan kuvan id"`.
- ~~Sivun kävijänä näen listan kaikista kuva hashtageistä~~ **Toiminnallisuus lisätty 6.6.**
Tämä on toteutettu käyttäen hyväksi ORM:n tehokkuutta. Näkymän puolella filtteröidään vain kuvaan liittyvät hashtagit komennolla `{% for h in picture.hashtags %} <h2><a href="{{ url_for('pictures_hashtags', hashtag = h.id)}}">{{ h.hashtag }}</a></h2>{% endfor %}`. Tietokanta puolella hashtagit ja kuvat on liitetty toisiinsa välitaulun avulla, koska kyseessä on monesta moneen suhde. SQL:llä kyseisen kyselyn voisi toteuttaa esimerkiksi: `SELECT hashtag.hashtag FROM hashtag LEFT JOIN hashtag ON hashtag.id = hashtag_id LEFT JOIN picture ON picture.id = picture_id WHERE picture.id = "halutun kuvan id"`. 
- ~~Uutena käyttäjänä en voi luoda tiliä samalla käyttäjänimellä, joka on jo kannassa~~ **Toiminnallisuus lisätty 31.5.**
Toiminnallisuus on toteutettu ensin ajamalla koodi `user = User.query.filter_by(username=form.username.data).first()` ja mikäli käyttäjää ei löydy, niin sitten luomalla uusi käyttäjä. Tässä tullaan takaisin jo aiemmin tuttuun `SELECT * FROM account WHERE username = "luotavan käyttäjän käyttäjänimi"` sillä erolla, että nyt tarkastetaan saadaanko takaisin tyhjä rivi.
- ~~Käyttäjänä voin kirjautua sisään applikaatioon~~ **Toiminnallisuus lisätty 28.5.**
Tässä Flaskin LoginManager hoitaa sisäänkirjautumisen komennolla `login_user(user)`, ja ainoa tarkastus, jonka olen lisännyt sisäänkirjautumiseen on `user = User.query.filter_by(username=form.username.data).first()`, joka on käytännössä sama tapaus kuin yllä. 
- ~~Käyttäjänä voin kirjautua ulos applikaatiosta~~ **Toiminnallisuus lisätty 28.5.**
Tämän LoginManager hoitaa täysin itse.
- ~~Sisäänkirjautuneena käyttäjänä voin lisätä kuvan~~ **Toiminnallisuus lisätty 30.5.**
LoginManager tarkistaa onko käyttäjäkirjautunut sisään. Tämän jälkeen lomakkeella lähetetyt tiedot kerätään ja niiden perusteella luodaan Picture -olio, joka lisätään tietokantaan. SQL:llä tehtynä tuo toiminto olisi jotain tyyliin `INSERT INTO picture (path, date_taken, account_id) VALUES ("polun arvo", "milloin otettu", "kenen kuva")`. Jätin pois hashtagien lisäämisen, koska tuo toiminto vaatisi erikseen ensin kyseisen hashtagin id:n hakemisen hashtag taulusta (ja mikäli sitä ei löytyisi, pitäisi kyseinen hashtag luoda). Tämän jälkeen kuvan id ja hashtagin id pitäisi lisätä hashtags -tauluun (ja tietysti tarkastaa, etteivät ne ole siellä jo, sillä applikaatiossa on määritelty `UniqueConstraint('hashtag_id', 'picture_id', name='uix_1')`). Hashtagien lisäämisessä on, kuten edellä annetusta selostuksesta huomaa, niin monta eri kohtaa, etten rupea avaamaan niitä tähän erikseen.
- ~~Sisäänkirjautuneena käyttäjänä voin poistaa oman aikaisemmin lisäämäni kuvan~~ **Toiminnallisuus lisätty 30.5.**
Kuva -olio haetaan ensin komennolla `pic = Picture.query.get_or_404(picture_id)`, jonka jälkeen (mikäli kyseessä tosiaan on kirjautuneen käyttäjän kuva `if current_user.id == pic.account_id:`) kuva poistetaan. Tämän pystyisi toteuttamaan yhdellä SQL -käskyllä seuraavasti `DELETE FROM picture WHERE id = "anna kuvan id" AND account_id = "kirjautuneen käyttäjän id";`  
- ~~Sisäänkirjautuneena käyttäjänä voin lisätä kuvalle kuvan ottamispäivämäärän~~ **Toiminnallisuus lisätty 30.5.**
Tämä käsiteltiin jo aiemmin kuvan lisäyksen yhteydessä. 
- ~~Sisäänkirjautuneena kuvanomistajana voin lisätä kuvalle hashtagin~~ **Toiminnallisuus lisätty 6.6.**
Tämä käsiteltiin jo aiemmin kuvan lisäyksen yhteydessä (eli liian monta käskyä kirjoitettavaksi. Kiitos ORM:lle!).
- ~~Sisäänkirjautuneena kuvanomistajana en voi lisätä kuvalle samaa hashtagia useampaa kertaa~~ **Toiminnallisuus lisätty 6.6.**
Hashtageillä on uniikkitunniste, joka hyödyntää hashtagin id:n ja kuvan id:n `UniqueConstraint('hashtag_id', 'picture_id', name='uix_1')`. Monta saraketta sisältävän uniikintunnisteen lisääminen on, ainakin MySQL / SQL Server / Oracle / MS Access järjestelmissä, mahdollista toteuttaa käskyllä `CONSTRAINT uix_1 UNIQUE (hashtag_id,picture_id)`
- ~~Sisäänkirjautuneena käyttäjänä en voi lisätä muiden kuville hashtagejä~~ **Toiminnallisuus lisätty 6.6.**
Tämä on toteutettu kahden eri varmenteen avulla. Ensinnäkin käyttöliittymän puolella ainoastaan käyttäjän omille kuville näkyy "Päivitä kuvan tietoja" -nappi. Lisäksi backendin puolella tehdään tarkastus `if current_user.id == picture.account_id:`. Kyseisen kuvan lisääjän id:n saa käskyllä `SELECT account_id FROM picture WHERE id = "päivitettävän kuvan id"`
- ~~Sisäänkirjautuneena käyttäjänä en voi poistaa muiden kuvia käyttäjien kuvia~~ **Toiminnallisuus lisätty 28.5.**
Tässä samat tarkastukset kuin yllä. 
- ~~Sisäänkirjautuneena käyttäjänä voin muokata lisäämäni kuvan ottamispäivämäärää~~ **Toiminnallisuus lisätty 9.6.**
Huomiona tähän kohtaa: kuvan ottamispäivämäärällä tarkoitetaan päivämäärä kenttää, joka lisätään kuvan luomisvaiheessa. Tähän toiminnallisuuteen liittyy kaksi eri vaihetta. Ensin haetaan muokattavan kuvan kaikki tiedot (joista yksi on kuvan ottamispäivämäärä). Nämä näytetään kuvan luoneelle käyttäjälle (käyttäjät eivät pääse muokkaamaan toistensa kuvia). Lopulta käyttäjän kuvaan liittyvät tiedot lähetetään takaisin käsiteltäväksi. Kaikki lomakkeella annetut tiedot päivitetään kuvaan riippumatta siitä, että muokattiinko kyseistä tietoa vai ei (eli suomeksi: käsky `form.path.data = picture.path` ajetaan joka kerta, kun kuvaa päivitetään, vaikka tuo form.path.data sisältäisi täysin saman tiedon, kun kuvalle on jo annettu). SQL:ssä päivitys tapahtuisi komennolla `UPDATE picture SET date_taken = "lomakkeella annettu päivämäärä", path = "lomakkeella annettu url" WHERE id = "päivitettävän kuvan id"`<br/><br/> 
**Hashtagien** osalta applikaatio toimii hieman eri tavalla. Koko kuvan hashtagit poistetaan ensin, ja tämän jälkeen kuvalle lisätään hashtagit sen mukaisesti, miten ne on annettu päivityslomakkeella. Mikäli samaa hashtagia ei ole aiemmin olemassa, se luodaan. Muuten kuvaan liitetään olemassa oleva hashtag. Päädyin tähän ratkaisuun sen takia, että se oli helpompi toteuttaa kuin vertailemalla hashtagejä ennen päivitystä ja sen jälkeen. Lisäksi se ei ole kovin raskas toiminnallisuus, ellei käyttäjä syötä useita hashtagejä (en tiedä missä raja menee, mutta uskoisin, että käyttäjän pitäisi syöttää satoja, ellei tuhansia hashtagejä). Hashtagien SQL -käskyistä olen jo todennut, että niiden määrittäminen on sen verran monimutkaista, etten sitä tähän tee.
- ~~Sisäänkirjautuneena käyttäjänä voin muokata lisäämäni kuvan hashtagejä~~ **Toiminnallisuus lisätty 9.6.**
Tämä kuvattu yllä kuvan ottamispäivämäärän muokkauksen yhtedessä.
- ~~Sisäänkirjautuneena käyttäjänä voin tykätä kuvista~~ **Toiminnallisuus lisätty 2.6.** Tämä toiminnallisuus on rakennettu siten, että html -näkymälle lähetetään lista kaikista tykkäyksistä (SQl: `SELECT account_id FROM liked`), jonka jälkeen html -näkymä tarkastaa onko sisäänkirjautunut käyttäjä 
- ~~Sisäänkirjautuneena käyttäjänä voin tykätä kuvasta vain kerran~~ **Toiminnallisuus lisätty 2.6.**
- ~~Sisäänkirjautuneena käyttäjänä voin poistaa tykkäykseni~~ **Toiminnallisuus lisätty 2.6.**
- ~~Kävijänä voin suodattaa kuvat hashtagien mukaan~~ **Toiminnallisuus lisätty 16.6.**
- ~~Kävijänä voin suodattaa kuvat käyttäjän mukaan~~ **Toiminnallisuus lisätty 16.6.**

