#import pytest
import json

import sys

sys.path.append("..")
from gstClass import *

def test_Excepted_GST_products():

    #Arrange
    product = {'phone':60000,
               'laptop':20000}

    actualElectronic=[]
    actualElectronicPrice=[]
    calculatedElectronic=[]
    calculatedElectronicPrice=[]
    productPurchase = productInShop(product)

    productPurchase.sellProductSub('phone')
    productPurchase.inventoryAdd('AC',30000)
    productPurchase.updateProductPrice("AC",50000)
    actualPrice_dict = productPurchase.availableProducts()

    for keys,value in product.items():
        actualElectronic.append(keys)
        actualElectronicPrice.append(value)


    #Act

    calculated_price_dict=productPurchase.productGstExcempted()
    print("Product with GST Excempted"+" "+str(calculated_price_dict))

    for keys,value in calculated_price_dict.items():
        calculatedElectronic.append(keys)
        calculatedElectronicPrice.append(value)

    #Assert

    assert calculated_price_dict == actualPrice_dict            #same Dictionary size
    assert actualElectronic == calculatedElectronic     #same keys number
    assert actualElectronicPrice==calculatedElectronicPrice  #Same price should be there
    assert type(calculated_price_dict) is dict   #should be a dictionary

test_Excepted_GST_products()


