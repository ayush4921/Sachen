import os
from flask import Flask, flash, request, redirect, url_for, render_template
import pandas as pd
from datetime import date

today = date.today()
#list123=["sfg",'sgsrg','aegaeg','agaeg']

#drawer1=["sfg",'sgsrg','aegaeg','agaeg']
#drawer2=["sfg",'sgsrg','aegaeg','agaeg']
#drawer3=["sfg",'sgsrg','aegaeg','agaeg']

Milk = {'RFID': "49 20 B3 B0",
'Item': 'Milk', 
'Expiration_date': 10052020, #the number is month, day, year
'Cabinet_number': 5,
'In Cabinet': False
}
Bread = {'RFID': "24 2E BE 2B",
'Item':'Bread',
'Expiration_date': 10202020, #the number is month, day, year
'Cabinet_number': 3,
'In Cabinet': True
}
Eggs = {'RFID': "78 2E BE 2B",
'Item':'Eggs',
'Expiration_date': 10152020,
'Cabinet_number': 8,
'In Cabinet': False
}
df=pd.DataFrame([Milk,Bread,Eggs])

d1 = today.strftime("%d%m%Y")
print(d1)
reminders=[]
for ind in df.index: 
     if (df['Expiration_date'][ind]-int(d1))>1000000:
       df['About to expire']="True"



lenth=len(reminders)
#len_drawer1=len(drawer1)
#len_drawer2=len(drawer2)
#len_drawer3=len(drawer3)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    #return render_template("index.html",abc=abc,list123=list123,drawer1=drawer1,drawer2=drawer2,drawer3=drawer3,lenth=lenth,len_drawer1=len_drawer1,len_drawer2=len_drawer2,len_drawer3=len_drawer3)
    #return render_template("hello.html",tables=[df.to_html(classes="table table-striped table-class",table_id="table-id",border=0)], titles=df.columns.values)
    return render_template("hello.html",lenth=lenth,df=df,reminders=reminders,tables=[df.to_html(index=False,classes="table table-class",table_id="table-id",border=0)], titles=df.columns.values)


if __name__ == '__main__':
    app.run(debug=True)