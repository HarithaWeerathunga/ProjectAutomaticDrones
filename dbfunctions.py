import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["BirdNestDroneData"]
mycol = mydb["dronedetails"]

def addDroneDetails(serialNo, xPosition, yPosition, timeRecorded):

    mydict = { "serialNo": serialNo, "xPosition": xPosition, "yPosition" : yPosition, "time" : timeRecorded}

    mycol.insert_one(mydict)
    print("Record added successfully")
