import pytest
import json
import sys

sys.path.append("..")

from gstClass import *


def test_filter_product_with_product_price():

    product = {'phone':60000,
               'laptop':1999,'TV':50000,'Hometheator':10000,'Fridge':50000}     #ALL Products in Inventory
    elegibleProduct=['TV','laptop']             #Filter GST Products
    amount=3000                                 #Enter Amount


    productPurchase = productInShop(product)            #Object Creation of Class Product.

    productPurchase.sellProductSub('phone')         #Subtract Product from inventory
    productPurchase.inventoryAdd('AC',30000)        #Add Product in Inventory
    productPurchase.updateProductPrice("AC",50000)  #update Price of Inventory
    actualPrice = productPurchase.availableProducts()   #Display Products and Price.
    print("Actual Price and Product excluding GST" + " " + str(actualPrice))


    #Act
    valid_product=0
    calculated_price=productPurchase.filterProductsWithAmount(elegibleProduct,amount)
    print("Product Elegible For GST with Price" + " "+ str(calculated_price))

    for key,value in product.items():
        for key_cal,val_cal in calculated_price.items():
            if key==key_cal:
                valid_product=1


    #Assert

    assert type(calculated_price) is dict       #TYpe assert
    assert valid_product == 1                   #Product is valid or not.

test_filter_product_with_product_price()