import os, sys 

sys.path.append(os.path.join(os.path.dirname(__file__),".."))

from app import get_drones_details

app = get_drones_details()


if __name__ == "__main__":
    app.run()