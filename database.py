class Database:

    def __init__(self, cluster):
        self.cluster = cluster

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
