# ShortPrint, the module to help you understand your data in an instant


![GitHub Workflow Status](https://img.shields.io/github/workflow/status/marcoboucas/shortprint/CI)
[![Documentation Status](https://readthedocs.org/projects/shortprint/badge/?version=latest)](https://shortprint.readthedocs.io/en/latest/?badge=latest)
![CodeQL](https://github.com/marcoboucas/shortprint/workflows/CodeQL/badge.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/marcoboucas/shortprint)
[![wakatime](https://wakatime.com/badge/github/marcoboucas/shortprint.svg)](https://wakatime.com/badge/github/marcoboucas/shortprint)

## How to use Shortprint

For more information, you can check our documentation here: [Documentation](https://shortprint.readthedocs.io/en/latest/)


First, you need to install our module
```
pip install shortprint
```

Then, you simply need to do the following in your code:
```python
from shortprint import shortprint

from requests import Request
your_object = Request()

# Print a preview of the result of you function
# Without having hundred lines filled with text

shortprint(your_object)
```
And the result could be the following:
```
===== Shortprinting =====
Shortprinting the variable located at the following location:
File: test.py, at line 10
Variable Name: 'your_object'
=========================
requests.models.Request(
  auth: None
  cookies: None
  data: List[]
  files: List[]
  headers: Dict[]
  hooks: Dict[
    (1) str: List[]
  ]
  json: None
  method: None
  params: Dict[]
  url: None
)
```


## How to contribute

1. Clone the repository
1. Run the `make install-dev` command to install the development dependencies
1. Enjoy !