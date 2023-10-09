#Imoprting modules
import requests
from tkinter import *
import datetime
import json


# function to get data from API
def Data() :
    parm = {
        "q" :textfield.get(), # output of function to textfield
         "appid" : "YOURKEY" # work with your key
    }

    s = requests.get("http://api.openweathermap.org/data/2.5/weather",params=parm).json() #Requesting data
    dat = []    # Data (you can add what you want)
    sunrise = datetime.datetime.fromtimestamp(s["sys"]["sunrise"])
    sundwon = datetime.datetime.fromtimestamp(s["sys"]["sunset"])
    dict_data = {
        "country name": s["name"],
        "weather": s["weather"][0]["main"],
        "description of weather": s["weather"][0]["description"],
        "sunrise": sunrise.strftime("%H:%M:%S"),
        "sunset": sundwon.strftime("%H:%M:%S"),
    }
    dat.append(dict_data) # append dict of data to a dict
    daaata = json.dumps(dict_data, indent=4) # dump data with json
    resultattext.insert("end-1c", daaata) # insert data to a text label



#Gui
root = Tk()
root.title("geo data by city")

label = Label(root,font=("bold",30),fg="#5225d9",bg ="#1d1c21",text="Add your country")
label.pack()
textfield = Entry(root,font=("bold",20),fg="#3bdb4b",bg ="#1d1c21",)
textfield.pack()
b1 = Button(root,font=("bold",10),fg="#3bdb4b",bg ="#1d1c21",text="click",command=Data)
b1.pack()
resultattext = Text(root,font=("bold",10),fg="#3bdb4b",bg ="#1d1c21")
resultattext.pack()


root.mainloop()
