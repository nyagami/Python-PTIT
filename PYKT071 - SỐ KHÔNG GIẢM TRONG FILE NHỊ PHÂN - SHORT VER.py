from io import BytesIO
import struct

#NOTE : this code only suit for ArrayList<Integer> object

def check(x):
    if x < 10: return 0
    l = x%10
    x//=10
    while x:
        e = x%10
        if e > l: return 0
        else:
            x//=10
            l = e
    return 1

class JavaObject:
    def __init__(self, filename) -> None:
        with open(filename, 'rb') as f:
            self.data = BytesIO(f.read())
            f.close()
            self.data.read(4)   #read header

        self.references = []
        self.map = {}
        self.set = set()

        #operators map
        self.opmap = {
            0x70: self.do_null, #null object
            0x71: self.do_reference,    #reference object
            0x72: self.do_classdesc,    #class of object
            0x73: self.do_object,   #the object
            0x77: self.do_blockdata,    #blockdata
            0x78: self.do_null, #end of blockdata
        }
        self.read()

    def _read_struct(self, unpack):
        length = struct.calcsize(unpack)    #length of bytes
        return struct.unpack(unpack, self.data.read(length))    #return (value,) maybe is operator code, length of package, ...

    def read(self):
        (opid, ) = self._read_struct(">B")  #get operator id
        return self.opmap[opid]()

    @classmethod
    def do_null(parent): pass

    def do_reference(self):
        (handle, ) = self._read_struct(">L")
        return self.references[handle - 0x7E0000]    #get the reference object

    def read_string(self, length_fmt="H"):
        (length,) = self._read_struct(f">{length_fmt}") #length of string
        return self.data.read(length).decode()

    def do_classdesc(self):
        name = self.read_string()
        self._read_struct(">qB")    #serial version ID and class flags

        self.references.append(name)
        (length,) = self._read_struct(">H") #length of propertises

        for i in range(length):
            self._read_struct(">B") # typecode
            self.read_string()  # propertise

        self._read_struct(">B") # classAnnotation
        self.read()  # superClassDesc
        return name

    def do_object(self): 
        classdesc = self.read()    #if this object is Integer, it will return the classdesc of the reference
        res = self.read_value()    #value of object (if the object is an array, this would be the size)
        if classdesc == 'java.util.ArrayList': o = []
        else: o = res
        self.references.append(o)
        if o == []:
            self.read()    #read the block data
            for i in range(res): 
                obj = self.read()   #maybe read new object or just a reference object
                if check(obj):
                    self.set.add(obj)
                    if self.map.get(obj): self.map[obj] += 1
                    else: self.map[obj] = 1
        return o

    def do_blockdata(self):
        (length,) = self._read_struct(">B")
        self.data.read(length)

    def read_value(self): 
        (res,) = self._read_struct(">i")
        return res

jobj1 = JavaObject("DATA1.in")
jobj2 = JavaObject("DATA2.in")
s = sorted(jobj1.set.intersection(jobj2.set))
m1, m2 = jobj1.map, jobj2.map
for i in s: print(i, m1[i], m2[i])