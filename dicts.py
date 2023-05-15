"""
product = {"name":"Iphone 12", 'stock':24, "price":76459.32 }
product['mem']=512
print(product)
#print(product.get('discont',0))
phons=["Iphone 13", "Samsung A355", "Nokia 3310","Iphone 13"]
product['recommends']=phons
product['recommends'].append('Iphone 9')
print(product)
"""
stock=[{'name': 'Iphone 12', 'stock': 24, 'price': 76459.32,
        'recommends': ['Iphone 13', 'Samsung A355']},
        {'name': 'Samsung Galaxy S33', 'stock': 8, 'price': 43159.32, 'discount': 1000},
        {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 53110.00}]

stock[0]['recommends'].append('Xiaomi Mi11')
stock[2]['price']-=30000
print(stock)

