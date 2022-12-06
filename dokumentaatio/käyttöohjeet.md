## Asennus
komennot suoritetaan ot-harjoistustyo kansion sisällä.

1. lisäosa poetry:n alustus komennolla:

```bash
poetry install
```

2. Pelin saa käyntiin komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Testien raportin voi luokea hakemiston _htmlcov_ tiedoston index.html avulla tai komentoriviin tulostuvalla informaatiolla.
