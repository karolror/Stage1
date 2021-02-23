import os
import pymongo
from intelhex import IntelHex


ih = IntelHex()
path = "golf.bin"
client = pymongo.MongoClient(
    "mongodb+srv://db_user1:useruser123@cluster0.qqmqr.mongodb.net/sample_training?retryWrites=true&w=majority")


class File:

    def __init__(self, file_dir, intel):
        self.file_dir = file_dir
        self.ih = intel

    def import_file(self):
        self.ih.loadbin(self.file_dir)
        return self.ih

    def check_file(self, correct_size):
        file_stats = os.stat(self.file_dir)
        print(f'File Size in Bytes is {file_stats.st_size}')
        if correct_size == file_stats.st_size:
            print("File size is correct for that model.")
            return True
        else:
            print("File size is incorrect for that model. Please check your file")
            return False


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

    def get_rail(self, id_rail):
        pass

    def get_injection_pos(self, id_inj_pos):
        inj_pos = []
        db = self.cluster["drivers"]
        collection = db["injection"]
        for i in collection.find({"_id": id_inj_pos}, {"_id": 0, "inj_pos1": 1, "inj_pos2": 1}):
            for x in i:
                inj_pos.append(i[x])
        return inj_pos[0], inj_pos[1]

    def get_turbo_pos(self, trb_info):
        pass

    def get_rail_pos(self, rail_info):
        pass


if __name__ == "__main__":

    data = Database(client)
    model = data.get_model()
    turbo = data.get_turbo(model)
    if turbo:
        print(turbo)
    else:
        pass
