class Tuner:

    def __init__(self, tune_file):
        self.tune_file = tune_file

    def tuning(self, tune_hex, a, b, element="0x"):
        driver_to_list = tune_hex.split()
        count = 0
        for i in range(a, b+1):
            changer = element + driver_to_list[count]
            self.tune_file[i] = int(changer, base=16)
            count += 1
        return self.tune_file
