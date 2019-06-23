# Tietorakenteen kuvaus
Tässä osassa kuvataan tietokantojen CREATE -lauseet, sekä käydään lyhyesti läpi SQL -injektio ja tietokantojen normalisointi tämän applikaation osalta. 

## SQL -Injektio
Applikaation syötteiden käsittely on rakennettu ORM:n varaan, joka samalla estää SQL -injektio hyökkäysten tekemisen.

## Tietokantataulujen normalisointi
Normalisoinnin tarkoituksena on pilkkoa tietokantojen sisältämät tiedot järkeviin kokonaisuuksiin, jotta niiden poisto, ylläpito ja lisäys olisi mahdollisimman helppoa. Helpoiten tähän pääsee (nyt kirjoitan voimakkaan pelkistyksen, mutta menköön) luomalla tietokannoille yhden id -kentän, ja pilkkomalla tietokannat niin pieniin osiin kuin sama tieto toistuu tietokannan sisällä. Tässäkin asiassa DontRepeatYourself (DRY) -ajattelu ohjaa ohjelmointia. 

Tämän applikaation tietokantataulut on normalisoitu, ja jokainen tietokantataulu vastaa sille kuuluvan, eheän tietokokonaisuuden ylläpidosta.

## CREATE TABLE -lauseet
Applikaatiossa on viisi tietokantataulua: rekisteröityneiden käyttäjien tiedot (account), tykkäysten tallentamiseen (liked), kuvien tallentamiseen (picture), hashtagien tallentamiseen (hashtag), ja kuvien sekä hashtagien yhdistämistaulu (hashtags).

Tietokanta tauluissa on lisäksi lisättynä joitain SQL -kyselyjä, joiden avulla kerätään tietoa näkymien näyttämiseen. Näitä on kuvattu tarkemmin [UserStoreissa](UserStories.md).

### Account -tietokantataulu
Account tietokantataulu sisältää seuraavat SQLAlchemyn mukaiset kentät
- id = db.Column(db.Integer, primary_key=True) **Base -olion tietojen kautta**
- date_created = db.Column(db.DateTime, default=db.func.current_timestamp()) **Base -olion tietojen kautta**
- date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()) **Base -olion tietojen kautta**
- username = db.Column(db.String(144), nullable=False)
- password = db.Column(db.String(144), nullable=False) 

`CREATE TABLE account (id INT PRIMRY KEY AUTO_INCREMENT, date_created DATETIME default CURRENT_TIMESTAMP, date_modified DATETIME default CURRENT_TIMESTAMP, username VARCHAR(144) NOT NULL, password VARCHAR(144) NOT NULL)` 

En tiedä onko SQL:ssä valmiina toiminta, jolla date_modified kenttä päivittyisi automaattisesti? Vai onko ainoa tapa päivittää date_modified `UPDATE` kutsun yhteydessä.

### Liked -tietokantataulu
Liked tietokantataulu sisältää seuraavat SQLAlchemyn mukaiset kentät
- db.PrimaryKeyConstraint('account_id', 'picture_id')
- date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
- date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
- account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
- picture_id = db.Column(db.Integer, db.ForeignKey("picture.id"), nullable=False) 

`CREATE TABLE liked (date_created DATETIME default CURRENT_TIMESTAMP, date_modified DATETIME default CURRENT_TIMESTAMP, account_id ID NOT NULL, picture_id ID NOT NULL, PRIMARY KEY (account_id, picture_id), FOREIGN KEY (account_id) REFERENCES account(id), FOREIGN KEY (picture_id) REFERENCES picture(id))` 

### Picture -tietokantataulu
Picture tietokantataulu sisältää seuraavat SQLAlchemyn mukaiset kentät
- id = db.Column(db.Integer, primary_key=True) **Base -olion tietojen kautta**
- date_created = db.Column(db.DateTime, default=db.func.current_timestamp()) **Base -olion tietojen kautta**
- date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()) **Base -olion tietojen kautta**
- date_taken = db.Column(db.DateTime, default=db.func.current_timestamp())
- path = db.Column(db.String(255), nullable=False)
- account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
- hashtags = db.relationship('Hashtag', secondary=hashtag_table, back_populates="pictures")

`CREATE TABLE picture (id INT PRIMRY KEY AUTO_INCREMENT, date_created DATETIME default CURRENT_TIMESTAMP, date_modified DATETIME default CURRENT_TIMESTAMP, date_taken DATETIME default CURRENT_TIMESTAMP, path VARCHAR(255) NOT NULL, account_id ID NOT NULL, FOREIGN KEY (account_id) REFERENCES account(id))` 

Hashtagit käsiteltäisiin puhtaassa SQL -kielisessä tietokannassa kokoomataulussa "hashtags", joka esitellään seuraavaksi. Koska hashtagien kohdalla kyseessä on monesta moneen suhde (yhdellä kuvalla voi olla monta hashtagia, ja yhteen hashtagiin voi liittyä monta kuvaa), tämä suhde on pitänyt eriyttää omaksi kokonaisuudekseen. Toisaalta kenttä account_id on yhdestä moneen suhde. Yhdellä kuvalla voi olla vain yksi omistaja, mutta yhdellä omistajalla voi olla monta kuvaa. Tällöin tämän suhteen kuvaaminen onnistuu lisäämällä kuvalle foreign key kentän, joka osoittaa omistajan id:hen.

### Hashtags -tietokantataulu
Hashtags tietokantataulu sisältää seuraavat SQLAlchemyn mukaiset kentät
- db.Column('hashtag_id', db.Integer, db.ForeignKey('hashtag.id'))
- db.Column('picture_id', db.Integer, db.ForeignKey('picture.id'))
- UniqueConstraint('hashtag_id', 'picture_id', name='uix_1')

`CREATE TABLE hashtags (hashtag_id INT NOT NULL, picture_id INT NOT NULL, FOREIGN KEY (hashtag_id) REFERENCES hashtag(id), FOREIGN KEY (picture_id) REFERENCES picture(id), PRIMARY KEY (hashtag_id, picture_id))` 

Tässä primarykey luodaan yhdistämällä hashtag_id ja picture_id. Tämä on ok valinta sen takia, että yhdellä kuvalla voi olla sama hashtag ainoastaan yhden kerran. 

### Hashtag -tietokantataulu
Hashtag tietokantataulu sisältää seuraavat SQLAlchemyn mukaiset kentät

- id = db.Column(db.Integer, primary_key=True) **Base -olion tietojen kautta**
- date_created = db.Column(db.DateTime, default=db.func.current_timestamp()) **Base -olion tietojen kautta**
- date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()) **Base -olion tietojen kautta**
- hashtag = db.Column(db.String(255), unique=True, nullable=False)
- pictures = db.relationship('Picture', secondary=hashtag_table, back_populates="hashtags")

`CREATE TABLE hashtag (id INT PRIMRY KEY AUTO_INCREMENT, date_created DATETIME default CURRENT_TIMESTAMP, date_modified DATETIME default CURRENT_TIMESTAMP, hashtag VARCHAR(255) NOT NULL)`

Hashtag taulu eroaa hashtags taulusta siinä, että Hashtag taulu sisältää erilliset hashtagit esim. #kuvanen, kun taas hashtags yhdistää hashtagit ja kuvat toisiinsa. Hashtag taulussa ei ole itsessään viittauksia taulun ulkopuolella, vaan liittäminen tapahtuu hashtags taulun kautta.
