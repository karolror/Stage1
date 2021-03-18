import pymongo
from intelhex import IntelHex
from database import Database
from file import File
from tuner import Tuner

ih = IntelHex()
client = pymongo.MongoClient(
    "mongodb+srv://db_user1:useruser123@cluster0.qqmqr.mongodb.net/sample_training?retryWrites=true&w=majority")


if __name__ == "__main__":

    file = File(ih)
    data = Database(client)
    ih = file.import_file()
    tune = Tuner(ih)
    print("Collecting data from database... ")
    model = data.get_model()
    injection = data.get_injection(model)
    turbo = data.get_turbo(model)
    rail = data.get_rail(model)

    if injection:
        x_inj, y_inj = data.get_injection_pos(model)
        print("Inj tuning...")
        ih = tune.tuning(injection, x_inj, y_inj)
    else:
        pass
    if turbo:
        x_trb, y_trb = data.get_turbo_pos(model)
        print("Turbo tuning...")
        ih = tune.tuning(turbo, x_trb, y_trb)
    else:
        pass
    if rail:
        x_ril, y_ril = data.get_rail_pos(model)
        print("Rail tuning...")
        ih = tune.tuning(rail, x_ril, y_ril)
    else:
        pass
    save_it = input("Enter the name of modified file (e.g file.bin): ")
    ih.tofile(save_it, format='bin')
    print("Mod saved. Don't forget to check checksums!")
