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
        car_id = input('Enter the vehicle ID: ')
        return int(car_id)

    def get_injection(self, id_inj):
        inj = None
        db = self.cluster["drivers"]
        collection = db["injection"]
        for i in collection.find({"_id": id_inj}, {"_id": 0, "name": 0, "inj": 1}):
            for x in i:
                inj = i[x]
        if inj:
            return inj
        else:
            return False

    def get_turbo(self):
        pass

    def get_rail(self):
        pass

    def get_injection_pos(self):
        pass

    def get_turbo_pos(self):
        pass

    def get_rail_pos(self):
        pass
