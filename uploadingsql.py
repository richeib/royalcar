import json

def uploadingtosql():
    with open('data.json','r')as f:
        data= json.load(f)
        
    products=data['data']["items"]
    # print(products)
    product_data = [(product["brdTitle"],product['title'],product['yop'], product['price'],product['fuelType']) for product in products]
    print(product_data)

uploadingtosql()
    
'''make,model,year,price,fuel type'''