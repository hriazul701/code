# Dictionary
product = {
    "brand": "Mango",
    "name": "T-Shirt",
    "price": 1500
}
print(product)

# Updating Dictionary
product["price"] = 2000
product["brand"] = "Banana"
print(product)


#Removing Element

product.pop("brand")
print(product)

#Marging Dictionary
student = {
    "grade": "A",
    "roll no": 13,
    "name": "Riaz"     
}
merged_dic= product|student
print(merged_dic)