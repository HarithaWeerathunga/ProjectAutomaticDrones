
import json 
import numpy as np
import matplotlib.pyplot as plt

from dbfunctions import addDroneDetails




def importDroneData(json_data):

    serial_array = []
    drone_data_details = []

    json_object = json.loads(json_data)
    report_data = json_object['report']['capture']['drone']
    time_data = json_object['report']['deviceInformation']['deviceStarted']
    


    for dronedata in report_data:
        serial_number = dronedata['serialNumber']
        X_position = dronedata["positionX"]
        Y_position = dronedata["positionY"]
        serial_array.append(serial_number)
        drone_data_details.append([X_position,Y_position])
        # plt.scatter(X_position,Y_position)  

        # addDroneDetails(serialNo=serial_number, xPosition= X_position, yPosition= Y_position, timeRecorded=time_data)


    
    print(serial_array)
    print(drone_data_details)
    # plt.savefig('foo.png')

    return serial_array
   
