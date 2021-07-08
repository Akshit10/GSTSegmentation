# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#GST Segregation :A shop keeper sells products. Some products are eligible for GST and some are not.
#Filter all products eligible for GST & total price (including GST) is more than 2000


class Shopkeeper():                             #Shopkeeper Class
    def __init__(self,product):
        self.product=product                      #constructor Initialiser

    def sellProductSub(self,soldProd):          #Sold Product or Subtract Product
        self.product.pop(soldProd)

    def inventoryAdd(self,item,price):          #Add Product
        self.product[item] = price

    def updateProductPrice(self,item,price):    #Update Product Price
        if item not in self.product:
            print("Element Not Found")
        else:
            self.product[item]=price

    def availableProducts(self):            #Available Products
        return self.product


class productInShop(Shopkeeper):            #Inventory class with Shopkeeper as inherit

    def productPrice(self,prodPrice):       #Product Price with given Product.
        self.prodPrice=prodPrice

    def productGSTApplicable(self):           #All GST Elegible Priducts
        for keys,value in self.product.items():
            updatedGstPrice=value/18
            updatedGstPrice=updatedGstPrice+value
            self.product[keys]=int(updatedGstPrice)
        return(self.product)

    def productGstExcempted(self):              #Al GST Excempted Products
        return self.product

    def particualarProductElegibleforGST(self,elegibleProduct):     #Particular products Elegible for GST
        if elegibleProduct not in self.product:
            print("Product Not Available")
        else:
            for keys,value in self.product.items():
                if keys == elegibleProduct:
                    updatedGstPrice = value / 18
                    updatedGstPrice=updatedGstPrice+value
            self.product[keys]=int(updatedGstPrice)
        return(self.product)

    def particularProductNotElegibleForGSt(self,elegibleProduct):       #Particular Products Excempted from GST
        if elegibleProduct not in self.product:
            print("Product Not Available")
        else:
            for keys,value in self.product.items():
                if keys != elegibleProduct:
                    updatedGstPrice = value / 18
                    updatedGstPrice=updatedGstPrice+value
                    self.product[keys]=int(updatedGstPrice)
        return(self.product)

    def filterProductsWithAmount(self,product,amount):           #Filter Product with Price and Product.
        filteredList={}
        for index in product:
            for key,values in self.product.items():
                if values>amount and key == index:
                    updatedGstPrice = values / 18
                    updatedGstPrice = updatedGstPrice + values
                    filteredList[key] = int(updatedGstPrice)
        return filteredList












