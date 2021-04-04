from tkinter import *
import requests
import json

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=35801&distance=5&API_KEY=D1833E5C-90E8-4E9D-857D-2FA5AA632B9E
root=Tk()
root.title("Weather")
root.geometry("600x500")

def ZipLookup():
    # zip.get()
    # zipLabel=Label(root,text=zip.get())
    # zipLabel.grid(row=1,column=0,columnspan=2)

    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "+&distance=5&API_KEY=D1833E5C-90E8-4E9D-857D-2FA5AA632B9E")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "green"
        elif category == "Moderate":
            weather_color = "yellow"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "orange"
        elif category == "Unhealthy":
            weather_color = "red"
        elif category == "Very Unhealthy":
            weather_color = "purple"
        elif category == "Hazardous":
            weather_color = "maroon"

        root.configure(background=weather_color)
        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20),
                        background=weather_color)

        myLabel.grid(row=1,column=0,columnspan=2)
    except Exception as e:
        api = "ERROR......"

# api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=35801&distance=5&API_KEY=D1833E5C-90E8-4E9D-857D-2FA5AA632B9E")
# api=json.loads(api_request.content)
#35801


zip=Entry()
zip.grid(row=0,column=0,stick=W+E+N+S)

zipButton=Button(root,text="ZIPCODE",command=ZipLookup)
zipButton.grid(row=0,column=1,stick=W+E+N+S)

root.mainloop()