# ShortPrint, the module to help you understand your data in an instant

## How to use Shortprint

First, you need to install our module
```
pip install shortprint
```

Then, you simply need to do the following in your code:
```python
from shortprint import shortprint

from requests import Request()
your_object = Request()

# Print a preview of the result of you function
# Without having hundred lines filled with text

shortprint(your_object)
```
And the result could be the following:
```
List[]
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