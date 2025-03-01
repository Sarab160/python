#dictionre
car = {
    "color":"red",
    "price":3456,
    "model":"2434"
    }

#read from dictoionre
print(car["color"]) 

colorcar = car["color"]
#{} agr price nhi hogi to empty answer aaya ga error nhi
pric = car.get("price",{})

#enter or replce data
car["price"]= 4567  
#delete data
del car["model"]    
#{} agr price nhi hogi to empty answer aaya ga error nhi
car.pop("price",{})
#last wali item del hogi 
car.popitem()