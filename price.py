
def discounted(price, discount, max_discount = 20):
    price, discount, max_discount=abs(price), abs(discount), abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Максимальная скидка не должна привышать 100% от стоимости товара')
    if discount >= max_discount:
        price_whit_discount = price
    else:
        price_whit_discount = price - price * discount/100
    return price_whit_discount

#product={'name':'Samsung Galaxy S21', 'price':50000, 'discount':5}
#product['with_discount'] = discounted(product['price'], product['discount'])
#print(product)
print(discounted(100, 50, max_discount=60))



