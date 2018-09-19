

import struct

class binary_file():
    def __init__(self):
        self.data = None

    def load_data(self, filepath):
        with open(filepath, 'rb') as f:
            '''
            text = f.read()
            print(type(text))
            
            a = hex(struct.unpack('i', text[0:4])[0])
            print(a)
            '''
            self.data = f.read()

    def show_data(self):
        #print(self.data)
        a = hex(struct.unpack('i', self.data[0:4])[0])
        print(a)

if __name__=="__main__":

    b = binary_file()

    b.load_data("C:\\Users\\mylin\\Desktop\\testpy\\binary_file_viewer\\data.bin")

    b.show_data()