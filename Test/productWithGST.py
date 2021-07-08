import pytest
import json

import sys

sys.path.append("..")

from gstClass import *

def test_GST_Products():

    product = {'phone':60000,
               'laptop':20000}
    actualElectronic_list=[]
    actualElectronicPrice=[]
    calculatedElectronic_list=[]
    calculatedElectronicPrice=[]

    productPurchase = productInShop(product)

    productPurchase.sellProductSub('phone')
    productPurchase.inventoryAdd('AC',30000)
    productPurchase.updateProductPrice("AC",50000)
    actualPrice_dict = productPurchase.availableProducts()

    for keys,value in product.items():
        actualElectronic_list.append(keys)
        actualElectronicPrice.append(value)


    #Act

    calculated_price_dict=productPurchase.productGSTApplicable()
    print("Product with GST Added"+" "+str(calculated_price_dict))

    for keys, value in calculated_price_dict.items():
        calculatedElectronic_list.append(keys)
        calculatedElectronicPrice.append(value)

    #Assert

    assert calculated_price_dict == actualPrice_dict        #Should have equal dictionary
    assert actualElectronic_list == calculatedElectronic_list         #should have same product size
    assert type(calculated_price_dict) is dict              #tyoe should be dictionary
    assert len(calculated_price_dict.items) == len(actualPrice_dict.items)          #len of element is equal.


