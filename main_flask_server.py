import os
from flask import Flask, flash, request, redirect, url_for, render_template
import pandas as pd
from datetime import date
import random

today = date.today()
#list123=["sfg",'sgsrg','aegaeg','agaeg']

#drawer1=["sfg",'sgsrg','aegaeg','agaeg']
#drawer2=["sfg",'sgsrg','aegaeg','agaeg']
#drawer3=["sfg",'sgsrg','aegaeg','agaeg']

class inventoryItem:
    def __init__(self, name, id, expiration_date, cabinet_number, inside_cabinet):
        self.id = id
        self.name = name
        self.expiration_date = expiration_date
        self.cabinet_number = cabinet_number
        self.inside_cabinet = inside_cabinet

#Milk = inventoryItem('Milk', '49 20 B3 B0', 10052020, 5, False)
#Bread = inventoryItem('Bread', '24 2E BE 2B', 10202020, 3, True)
#Eggs = inventoryItem('Eggs', '78 2E BE 2B', 10152020, 8, False)
hex_digits = '0 1 2 3 4 5 6 7 8 9 A B C D E F'.split()
perishables = 'batteries Crew_restraints Waste_containers Ziploc_bags ACPA IMAX BLower_screen_assemblies Wipes Cushions Photosensitive_Hardware Purge_Bags CSVS_Targets Printer_Cartridges Decals Film_rolls Actex_Water_filters:'.split()

data = {}
for i in range(0, 100):
    id = ''
    id_spaces = ''
    for j in range (0, 4):
        digs = hex_digits[random.randint(0, 15)] + hex_digits[random.randint(0, 15)]
        id += digs
        id_spaces += digs
        if j != 4:
            id_spaces += ' '
    data[id] = inventoryItem(perishables[random.randint(0, 9)], id_spaces, date.fromordinal(random.randint(737690, 738055)), random.randint(1, 10), bool(random.getrandbits(1)))

data_sorted = sorted(data, key = lambda rfid: data[rfid].expiration_date)

item_list = []
for key in data_sorted:
    item_obj = data[key]
    item_list.append(
        {
            'RFID': item_obj.id,
            'Item': item_obj.name,
            'Expiration Date': item_obj.expiration_date,
            'Cabinet Number': item_obj.cabinet_number,
            'In Cabinet?': item_obj.inside_cabinet
        }
    )
df=pd.DataFrame(item_list)

reminders = []
abclist=[]

for ind in df.index:
    
    print((df['Expiration Date'][ind] - today).days)
    expiry=int((df['Expiration Date'][ind] - today).days)
    if expiry < 7:
        df.at[ind,'About to Expire/Finish?'] = "Yes"
    elif expiry < 0:
        df.at[ind,'About to Expire/Finish?'] = "Already Expired"
    elif expiry>=7:
        df.at[ind,'About to Expire/Finish?'] = "No"

    if df['About to Expire/Finish?'][ind]=="Yes":
        abclist.append(df['Item'][ind])
    elif df['About to Expire/Finish?'][ind]=="Already Expired":
        abclist.append(df['Item'][ind])
    
abc=pd.DataFrame(abclist)
print(abc)

lenth=len(reminders)
#len_drawer1=len(drawer1)
#len_drawer2=len(drawer2)
#len_drawer3=len(drawer3)

app = Flask(__name__)
index=[]



@app.route('/', methods=['GET', 'POST'])
def hello_world():
    
    if request.method == 'POST':
    
        RFID2=str(request.form['Name'])
        item=str(request.form['item'])
        expiration=str(request.form['expiration'])
        cabinet=str(request.form['cabinet'])
        RFID2list = RFID2.split()        

    
        for i in df.index:
            rfidindata=df.at[i,'RFID']
            rfidlist=rfidindata.split()
            print(df.at[i,'RFID'])
            if rfidlist==RFID2list :
                df.at[i,'Item']= item
                df.at[i,'Expiration Date']= expiration
                df.at[i,'Cabinet Number']= cabinet

                print(i)
                print(df['Item'])
                break
            else: 
                print('Not found')
                print(df['RFID'][i])
                print(df['Item'][i])
                print(RFID2)
                

    return render_template("hello.html",lenth=lenth,abc=abc,df=df,reminders=reminders,tables=[df.to_html(index=False,classes="table table-class",table_id="table-id",border=0)], titles=df.columns.values)
   
      

    
    #return render_template("index.html",abc=abc,list123=list123,drawer1=drawer1,drawer2=drawer2,drawer3=drawer3,lenth=lenth,len_drawer1=len_drawer1,len_drawer2=len_drawer2,len_drawer3=len_drawer3)
    #return render_template("hello.html",tables=[df.to_html(classes="table table-striped table-class",table_id="table-id",border=0)], titles=df.columns.values)


    
        

   


if __name__ == '__main__':
    app.run(debug=True)