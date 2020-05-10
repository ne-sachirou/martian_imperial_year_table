![test](https://github.com/ne-sachirou/martian_imperial_year_table/workflows/test/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/ne-sachirou/martian_imperial_year_table/badge.svg?branch=master)](https://coveralls.io/github/ne-sachirou/martian_imperial_year_table?branch=master)

# 帝國火星曆

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
