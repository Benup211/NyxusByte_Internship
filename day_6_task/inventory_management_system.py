from abc import ABC,abstractmethod
class abstractInventory(ABC):
    @abstractmethod
    def AddItem(self):
        pass
    def removeItem(self):
        pass
    def updateItem(self):
        pass
    def viewInventory(self):
        pass
    def LowStockReport(self):
        pass
class InventoryItem(abstractInventory):
    _Inventory_list=list()
    def __init__(self):
        print("Inventory Instance Created")
    def AddItem(self):
        name=input("Enter item name:")
        try:
            price=int(input("Enter price of item:"))
            quantity=int(input("Enter quantity of item:"))
            if (price<0 or quantity<0):
                print(f"{'Enter postive number value':-^100}")
                return
            category=input("Enter category of item:")
            match_found=False
            for inv_item in self._Inventory_list:
                if inv_item['name']==name:
                    match_found=True
                    break
            if match_found:
                temp=inv_item
                temp['quantity']+=1
                self._Inventory_list.remove(inv_item)
                self._Inventory_list.append(temp)
            else:
                dict_value={'name':name,'price':price,'quantity':quantity,'category':category}
                self._Inventory_list.append(dict_value)
        except Exception as e:
            print(f"Error:{e}, only enter number for price and quantity")
    def removeItem(self):
        if len(self._Inventory_list)>0:
            name=input("Enter item name to remove from inventory:")
            match_found=False
            for inv_item in self._Inventory_list:
                if inv_item['name']==name:
                    match_found=True
                    break
            if match_found:
                self._Inventory_list.remove(inv_item)
                print(f"Given item:{name} is removed from the Inventory")
            else:
                print(f"Given item:{name} is not found in the Inventory")
        else:
            print(f"{'Inventory List is empty':#^100}")
    def updateItem(self):
        if len(self._Inventory_list)>0:
            name=input("Enter item name to remove from inventory:")
            match_found=False
            for inv_item in self._Inventory_list:
                if inv_item['name']==name:
                    match_found=True
                    break
            if match_found:
                temp=inv_item
                try:
                    while(1):
                        choice=input("Update [price,quantity,or category]:")
                        match choice:
                            case 'price':
                                price=int(input(f"Enter new price for {name}:"))
                                temp['price']=price
                                break
                            case 'quantity':
                                quantity=int(input(f"Enter new quantityfor {name}:"))
                                temp['quantity']=quantity
                                break
                            case 'category':
                                category=int(input(f"Enter new category for {name}:"))
                                temp['category']=category
                                break
                            case default:
                                print("Error command!Try again")
                except Exception as e:
                    print(f"Error:{e}, only enter number for price and quantity")
            else:
                print(f"Given item:{name} is not found in the Inventory")
        else:
            print(f"{'Inventory List is empty':#^100}")
    def viewInventory(self):
        if len(self._Inventory_list)>0:
            sorted_list_inv=sorted(self._Inventory_list,key=lambda inv:inv['name'])
            print(f"{'Inventory item':#^100}")
            for inv_item in sorted_list_inv:
                print(f"Item name:{inv_item['name']}")
                print(f"Item price:{inv_item['price']}")
                print(f"Item quantity:{inv_item['quantity']}")
                print(f"Item category:{inv_item['category']}\n")
            print("#"*100)
        else:
            print(f"{'Inventory Item is Empty':#^100}")
    def LowStockReport(self):
        if len(self._Inventory_list)>0:
            print(f"{'Low Stock Report':#^100}")
            for inv_item in self._Inventory_list:
                if inv_item['quantity']<10:
                    print(f"Item name:{inv_item['name']}")
                    print(f"Current Quantity:{inv_item['quantity']}")
                    print(f"Warning message:item {inv_item['name']} is running low\n")
            print("#"*100)
        else:
            print(f"{'Inventory Item is Empty':#^100}")
class InheritInventoryItem(InventoryItem):
    def __str__(self):
        return ("Inherit from Inventory Item")
NyxusInv=InheritInventoryItem()
print(NyxusInv)
while(1):
    command=input("Enter your command [add,remove,update,view,stock,exit]:")
    match command:
        case 'add':
            NyxusInv.AddItem()
        case 'remove':
            NyxusInv.removeItem()
        case 'update':
            NyxusInv.updateItem()
        case 'view':
            NyxusInv.viewInventory()
        case 'stock':
            NyxusInv.LowStockReport()
        case 'exit':
            choice=input("Are you sure you want to exit[yes/no]:").lower()
            if choice=='yes' or choice=='y':
                del NyxusInv
                break
            else:
                print("Continuing....")
        case default:
            print(f"{'Enter valid choice':#^100}")