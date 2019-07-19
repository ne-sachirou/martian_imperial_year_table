[![Build Status](https://travis-ci.com/ne-sachirou/martian_imperial_year_table.svg?branch=master)](https://travis-ci.com/ne-sachirou/martian_imperial_year_table)

# 帝國火星暦

https://martian-imperial-year-table.c4se.jp/

## Abbreviation

- grdt : `GregorianDateTime`
- juld : `JulianDay`
- delta_t : `JulianDay.delta_t`
- tert : `TerrestrialTime`
- mrls : Mars Ls (Areocentric Solar Longitude)
- mrsd : `MarsSolDate`
- imsn : `ImperialSolNumber`
- imdt : `ImperialDateTime`

## CONTRIBUTING

Requirements :

- Python 3
- Docker
- gcloud (only for deploy)

See `./tasks.py help`.

Start development.

```sh
./tasks.py build start
./tasks.py sh
```

Dev server : http://localhost:5000/
API spec : http://localhost:5000/apidocs/

When the file changed you may need to build UI files by `./tasks.py build`.

Before deploy & merge you shuld pass `./tasks.py format test`.

Staging is https://martian-imperial-year-table.staging.c4se.jp/ (may be broken).
