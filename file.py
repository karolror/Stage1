class File:

    def __init__(self, intel):
        self.ih = intel

    def import_file(self):
        file_dir = input('Enter the location of the file: ')
        self.ih.loadbin(file_dir)
        return self.ih
