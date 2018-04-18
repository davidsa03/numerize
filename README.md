[![Build Status](https://travis-ci.org/davidsa03/numerize.svg?branch=master)](https://travis-ci.org/davidsa03/numerize)
![Python 2.7](https://img.shields.io/badge/python-2.7-green.svg)
![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/davidsa03/numerize/blob/master/LICENSE)
# Numerize

Numerize is a Python (2 and 3) library for converting large numbers into readable strings.
Similar to what Twitter and Instagram use for large follower counts.

| Number | Numerized |
|------|:---------:|
| 1  | **1**  |
| 1000  | **1K**  |
| 1500  | **1.5K**  |
| 1000000  | **1M**  |
| 1500000  | **1.5M**  |
| 1000000000  | **1B**  |
| 1500000000  | **1.5B**  |
| 1000000000000  | **1T**  |
| 1500000000000  | **1.5T**  |
| 21324314       | **21.32M**|
| -21324314       | **-21.32M**|

## Installation

```
$ pip install numerize
```

## Usage

numerize(number_to_numerize, decimal_places_to_round[optional])

```
>>> from numerize import numerize
>>> numerize(1234567.12)
'1.23M'
>>> numerize(12134.123, 3)
'12.134K'
```
This will convert large numbers like 1234567.12 into 1.23M

## Requirements
- Python >= 2.7 or >= 3.4

## Contributing
[How to contribute](https://github.com/davidsa03/numerize/blob/master/CONTRIBUTING.md)

## Testing

```
$ python numerize/test.py
```

## License
MIT licensed.
