from flask import Flask , render_template
import requests
import xml.etree.ElementTree as ET
import xmltodict
import json 
from functions import importDroneData

from apscheduler.schedulers.background import BackgroundScheduler
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

headings = ("Drone Name")

data = (
    ("drone1", "type1","date1"),
    ("drone2", "type2","date2"),
    ("drone3", "type3","date3"),
)



@app.route("/drones")
def hello_drones():
    return "<p>BirdNest Challenge </p>"

@app.route("/")
def get_drones_details():
    url = "https://assignments.reaktor.com/birdnest/drones"
    drone_data = requests.get(url)
    xpars = xmltodict.parse(drone_data.text)
    json_data = json.dumps(xpars)
    serial_number_array = importDroneData(json_data)
    
    return render_template("drones.html", headings=headings, data=serial_number_array)
    


if __name__ == "__main__":
    app.run(debug=True)




