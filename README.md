<h1 align="center">Product Description Generator 📦</h1>

## A template-based product description generator. Template is created using **ChatGPT**

<br>

# How to use

## How to generate result

```python
name = "Black Essentials T-Shirt"
price = 28.95
brand = "DR3AMIN"
color = "Black"
size = "Small"
material = "Cotton"
design = "Graphic"
condition = "New"
rating = 4.5
discount = 10
```
```python
from descr import Descr

module = Descr()

result = module.gen_description(name, price, brand,
                                color, size, material,
                                design, condition, rating,
                                discount)
print(result)
>>> """Introducing the Black Essentials T-Shirt from DR3AMIN, available in Black and made of Cotton. This product is available in size Small and features a Graphic design. It is in New condition and has received a rating of 4.5 stars. Priced at only $28.95, it's a steal for such a high-quality product.
And now with 10% off, it's only $26.055!
It's the perfect gift for anyone who loves fashion."""
```