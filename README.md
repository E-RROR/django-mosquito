<p align="center">
  <img src="https://www.flaticon.com/svg/static/icons/svg/2297/2297334.svg" height="250" width="250" /> 
</p>
<h1 align="center">Django Mosquito 🦟</h1>
<h4 align="center">Limit visitors to your django app by count</h4>
<p align="center">
  <img src="https://img.shields.io/pypi/v/django-mosquito"/>
  <img src="https://img.shields.io/github/issues/E-RROR/django-mosquito"/>
</p>

# Whats Django Mosquito
Mosquito middleware helps you set limit of visiting you django for each user

# Installation
```
pip install djangomosquito
```

# Import
import it inside middleware in django settings
```
middlewares = [
  ...,
  'djangomosquito.middleware.DjangoMosquito',
  ...,
]
```

# Usage
This middleware do it job you just need to set limit number and
by setting the limit number after reaching this number user get banned from
your website for 1 day

# How
`settings.py`
```
# after 100 requests user get banned
LIMIT_MOSQUITO = 100
```
