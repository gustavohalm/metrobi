# Quetion: 7 - Think that you have an unlimited number of carrots, but a limited number of carrot types. Also, you have one bag that can hold a limited weight. Each type of carrot has a weight and a price. Write a function that takes carrotTypes and capacity and return the maximum value the bag can hold.
Example:
carrotTypes = [{kg: 5, price: 100}, {kg: 7, price: 150}, {kg: 3, price: 70}] capacity = 36 //kg
getMaxValue(carrotTypes, capacity)

## How to run the code
```
$ python question_7/carrots.py
```
Entrada:
```
Capability: 36
Number of carrots: 5
kg: 10
price: 100
kg: 4
price: 111
kg: 13
price: 289
kg: 28
price: 10
kg: 102
price: 333
```
Saida:
```
{'kg': 32.0, 'price': 121.0}
```
## How to run the test
```
$ python -m unittest question_7/carrots_test.py
```
