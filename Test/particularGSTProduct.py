#import pytest
import json
from gstClass import *


import sys

sys.path.append("..")

def test_GSTOnGivenProducts():

    product = {'phone':60000,
               'laptop':20000}    #All Products


    elegibleProduct='AC'            #Products which eligible for GST
    priceActualElecrtonic=0         #Price of Actual Electronic which is Elible for GST
    actualElectronicList=[]                 #List of Actual Products in inventory
    calculatedElectronicList=[]           #List of Product After Applying operation
    priceCalculatedElectronic=0


    productPurchase = productInShop(product)             #inventory class object

    productPurchase.sellProductSub('phone')
    productPurchase.inventoryAdd('AC',30000)
    productPurchase.updateProductPrice("AC",50000)
    actualPrice = productPurchase.availableProducts()
    print("Actual Product List"+" "+str(actualPrice))

    for keys,value in product.items():
        actualElectronicList.append(keys)

    #Act

    calculated_price=productPurchase.particualarProductElegibleforGST(elegibleProduct)
    print("Product which all are GST elegibble other than Product" + ' ' + elegibleProduct + ' ' + str(calculated_price))

    for keys,value in calculated_price.items():
        calculatedElectronicList.append(keys)

    #Assert

    assert type(calculated_price) is dict  # Check data type
    assert actualElectronicList == calculatedElectronicList  # Check Products list is equal or not


test_GSTOnGivenProducts()















