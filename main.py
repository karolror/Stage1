import pymongo
from intelhex import IntelHex


ih = IntelHex()
path = "golf.bin"
client = pymongo.MongoClient(
    "mongodb+srv://db_user1:useruser123@cluster0.qqmqr.mongodb.net/sample_training?retryWrites=true&w=majority")


class File:

    def __init__(self, intel):
        self.ih = intel

    def import_file(self):
        while True:
            file_dir = input('Enter the location of the file: ')
            self.ih.loadbin(file_dir)
            return self.ih


class Database:

    def __init__(self, cluster):
        self.cluster = cluster

    def get_model(self):
        db = self.cluster["drivers"]
        collection = db["sizes"]
        desc = collection.find({})
        for i in desc:
            print(" \n")
            for x in i:
                print(x, ":", i[x], "|", end=" ")
        print(" \n")
        while True:
            try:
                car_id = int(input('Enter the vehicle ID: '))
                return car_id
            except ValueError:
                print("Oops! Value must be an integer. Try again...")

    def get_injection(self, id_inj, inj=None):
        db = self.cluster["drivers"]
        collection = db["injection"]
        for i in collection.find({"_id": id_inj}, {"_id": 0, "inj": 1}):
            for x in i:
                inj = i[x]
        if inj:
            return inj
        else:
            return False

    def get_turbo(self, id_trb, trb=None):
        db = self.cluster["drivers"]
        collection = db["injection"]
        for i in collection.find({"_id": id_trb}, {"_id": 0, "turbo": 1}):
            for x in i:
                trb = i[x]
        if trb:
            return trb
        else:
            return False

    def get_rail(self, id_rail, ril=None):
        db = self.cluster["drivers"]
        collection = db["injection"]
        for i in collection.find({"_id": id_rail}, {"_id": 0, "rail": 1}):
            for x in i:
                ril = i[x]
        if ril:
            return ril
        else:
            return False

    def get_injection_pos(self, id_inj_pos):
        inj_pos = []
        db = self.cluster["drivers"]
        collection = db["injection"]
        for i in collection.find({"_id": id_inj_pos}, {"_id": 0, "inj_pos1": 1, "inj_pos2": 1}):
            for x in i:
                inj_pos.append(i[x])
        return inj_pos[0], inj_pos[1]

    def get_turbo_pos(self, id_trb_pos):
        trb_pos = []
        db = self.cluster["drivers"]
        collection = db["injection"]
        for i in collection.find({"_id": id_trb_pos}, {"_id": 0, "turbo_pos1": 1, "turbo_pos2": 1}):
            for x in i:
                trb_pos.append(i[x])
        return trb_pos[0], trb_pos[1]

    def get_rail_pos(self, id_rail_pos):
        rail_pos = []
        db = self.cluster["drivers"]
        collection = db["injection"]
        for i in collection.find({"_id": id_rail_pos}, {"_id": 0, "rail_pos1": 1, "rail_pos2": 1}):
            for x in i:
                rail_pos.append(i[x])
        return rail_pos[0], rail_pos[1]


class Tuner:

    def __init__(self, tune_file):
        self.tune_file = tune_file

    def tuning(self, tune_hex, a, b, element="0x"):
        driver_to_list = tune_hex.split()
        count = 0
        for i in range(a, b):
            changer = element + driver_to_list[count]
            self.tune_file[i] = int(changer, base=16)
            count += 1
        return self.tune_file


if __name__ == "__main__":

    file = File(ih)
    data = Database(client)
    ih = file.import_file()
    tune = Tuner(ih)

    model = data.get_model()
    injection = data.get_rail(model)
    turbo = data.get_turbo(model)
    rail = data.get_rail(model)

    if injection:
        x_inj, y_inj = data.get_injection_pos(model)
        ih = tune.tuning(injection, x_inj, y_inj)
    else:
        pass
    if turbo:
        x_trb, y_trb = data.get_turbo_pos(model)
        ih = tune.tuning(turbo, x_trb, y_trb)
    else:
        pass
    if rail:
        x_ril, y_ril = data.get_rail_pos(model)
        ih = tune.tuning(rail, x_ril, y_ril)
    else:
        pass
    save_it = input("Enter the name of modified file (e.g file.bin): ")
    ih.tofile(save_it, format='bin')
    print("Don't forget to check checksums!")
