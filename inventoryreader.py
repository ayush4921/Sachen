# import serial library to communicate with serial port
import serial

class inventoryItem:
    def __init__(self, name, id, expiration_date, cabinet_number, inside_cabinet):
        self.id = id
        self.name = name
        self.expiration_date = expiration_date
        self.cabinet_number = cabinet_number
        self.inside_cabinet = inside_cabinet
# Milk = inventoryItem('49 20 B3 B0', 'Milk', 10052020, 4, False)
# Bread = inventoryItem('24 2E BE 2B', 'Bread', 10202020, 8, True)

# dictionary of all items in inventory
inventory = {
  '4920B3B0': inventoryItem('Milk', '49 20 b3 b0', 10202020, 4, False),
  '242EBE2B': inventoryItem('Bread', '24 2e be 2b', 10232020, 4, True)
}

# set up serial and baud rate
arduino = serial.Serial('/dev/cu.usbmodem14101', 9600)
# What cabinet am I coming from? The identity of my specific RFID reader
# how can I split the string so that i get only the rfid?
try:
    while True:
        ItemCodeprecursor = arduino.readline()[:-2]
        ItemCode = ItemCodeprecursor.decode('ascii')
        if ItemCode:
            # print out just the Cabinet Number (index 20)
            # What item is coming into the cabinet? The RFID chip number
            # print out just the item number (indices 31-41)
            cabinet, uid = ItemCode.split(',')
        try:
            my_item = inventory[uid]
            my_item.inside_cabinet = not my_item.inside_cabinet
            my_item.cabinet_number = cabinet
            print(my_item.inside_cabinet)
            print(my_item.cabinet_number)
        except KeyError:
            print("not in database")
            # add new entry
            inventory[uid] = inventoryItem('Unknown', uid, 12319999, cabinet, True)
            # properties of all of the items in my database
except KeyboardInterrupt:
    print("goodbye")






# if cabinet == "7":
    #set cabinet_number to cabinet number that is read on on Serial

# if uid == "4920B3B0":

# elif uid == "242EBE2B":
# if serial moniter reads 49 20 B3 B0
    #set inside_cabinet to the opposite boolean value
    #set cabinet_number to cabinet number that is read on on Serial


#Milk = {"ID": "49 20 B3 B0",
#"Item": 'Milk',
#"Expiration_date": 10052020, #the number is month, day, year
#"Cabinet_number": 5,
#"Inside_Cabinet": False
#}
#Bread = {"ID": "24 2E BE 2B",
#"Item": 'Bread',
#"Expiration_date": 10202020, #the number is month, day, year
#"Cabinet_number": 3,
#"Inside_Cabinet": True
#}
#Eggs = {
#"Item": 'Eggs',
#"Expiration_date": 10152020,
#"Cabinet_number": 8,
#"Inside_Cabinet": False
#}
# the list of inventory items
#myInventoryItems = [Milk, Bread, Eggs]
# change the dictionary depending on which item is getting swiped in
#If
