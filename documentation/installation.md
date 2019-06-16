# Asennusohja

## Vaatimukset

Asennettavasta ympäristöstä tulisi löytyä seuraavat toiminnallisuudet

- [Python](https://www.python.org/downloads/)
- [GIT (käsittääkseni Maceissä aika usein valmiina.)](https://git-scm.com/downloads/)
- Heroku käyttäjätunnus

## Lokaaliasennus
- Luo uusi kansio johon haluat kopioida Valokuva galleria -applikaation tiedostot
- Avaa komentorivi, jossa on git asennettuna, ja suunnista yllä luotuun kansioon
- Aja komento `git clone https://github.com/Tseipii89/Valokuvagalleria-tietokantasovellus-koulu.git`
- Komennon jälkeen kansioon kopioituu uusi kansio nimeltä "Valokuvagalleria-tietokantasovellus-koulu". Mene komentoriville sen sisään `cd Valokuvagalleria-tietokantasovellus-koulu/`
- Nyt kaikki tarvittavat tiedostot on asennettu. Seuraavana on virtuaaliympäristön käynnistäminen, joka luo samalla tietokantataulut. Virtuaaliympäristön käynnistäminen vaihtelee hieman käyttöjärjestelmän mukaan. Alla kuvattu molemmat Windows ja Mac/Unix ympäristön käynnistyskomennot. [Lisätietoa ja ongelmatapauksien tarkastelu](https://docs.python.org/3/tutorial/venv.html)
- Aja ensin komento `python3 -m venv tutorial-env` (tai `python -m venv venv` riippuen miten komentorivi tunnistaa pythonin). Aja seuraavaksi jompi kumpi alla olevista käskyistä.
- Windows: `venv\Scripts\activate.bat` (omalla Windows koneellani ainoa komento, joka käynnisti ympäristön oli yllättäen `source venv/Scripts/activate`)
- Mac/Unix: `source venv/bin/activate`
- Aja komento `pip install -r requirements.txt`
- Tämän jälkeen aja komento `python run.py`, joka käynnistää applikaation ja kertoo minkä url:in takaa sovellus löytyy (esim. `http://127.0.0.1:5000/` )

## Pilviasennus Herokuun
- Tässä ohjeessa käytetään kurssin ohjeiden mukaisesti web-palvelimena Gunicornia, joka asennettiin jo aikaisemmassa lokaalissa vaiheessa. Aja kaikki tässä mainitut komennot lokaalissa vaiheessa luodussa virtuaaliympäristössä.
- Jäädytä riippuvuudet Herokuun siirtoa varten. `pip freeze | grep -v pkg-resources > requirements.txt`
- Aja komento `echo "web: gunicorn --preload --workers 1 hello:app" > Procfile`, jolla käynnistää applikaation web prosessina.
- Luodaan sovellukselle paikka Herokussa. Aja komento `heroku create VALITSE-SOVELLUKSEN-NIMI-TÄHÄN`. 
- Ajetaan projektin tiedot Herokuun komennolla `git push heroku`
- Komentorivi antaa takaisin tiedon applikaation Heroku url -osoitteen

### Muuta Herokun käyttämä tietokanta PostgreSQL:ksi
- Aja komento `heroku config:set HEROKU=1`
- Luodaan Herokuun tietokanta `heroku addons:add heroku-postgresql:hobby-dev`
- Heroku käyttää nyt PostgreSQL:ää

