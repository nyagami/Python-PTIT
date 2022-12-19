from io import BytesIO
from sys import stdout
import enum
import struct
import timeit

class TypeCode(enum.IntEnum):
    """
    Type definition chars (typecode)
    """
    # Primitive types
    TYPE_BYTE = ord("B")  # 0x42
    TYPE_CHAR = ord("C")  # 0x43
    TYPE_DOUBLE = ord("D")  # 0x44
    TYPE_FLOAT = ord("F")  # 0x46
    TYPE_INTEGER = ord("I")  # 0x49
    TYPE_LONG = ord("J")  # 0x4A
    TYPE_SHORT = ord("S")  # 0x53
    TYPE_BOOLEAN = ord("Z")  # 0x5A
    # Object types
    TYPE_OBJECT = ord("L")  # 0x4C
    TYPE_ARRAY = ord("[")  # 0x5B


NUMPY_TYPE_MAP = {
    TypeCode.TYPE_BYTE: "B",
    TypeCode.TYPE_CHAR: "b",
    TypeCode.TYPE_DOUBLE: ">d",
    TypeCode.TYPE_FLOAT: ">f",
    TypeCode.TYPE_INTEGER: ">i",
    TypeCode.TYPE_LONG: ">l",
    TypeCode.TYPE_SHORT: ">h",
    TypeCode.TYPE_BOOLEAN: ">B",
}

class TerminalCode(enum.IntEnum):
    """
    Stream type Codes
    """
    TC_NULL = 0x70
    TC_REFERENCE = 0x71
    TC_CLASSDESC = 0x72
    TC_OBJECT = 0x73
    TC_STRING = 0x74
    TC_ARRAY = 0x75
    TC_CLASS = 0x76
    TC_BLOCKDATA = 0x77
    TC_ENDBLOCKDATA = 0x78
    TC_RESET = 0x79
    TC_BLOCKDATALONG = 0x7A
    TC_EXCEPTION = 0x7B
    TC_LONGSTRING = 0x7C
    TC_PROXYCLASSDESC = 0x7D
    TC_ENUM = 0x7E

class JavaObject:
    def __init__(self, filename) -> None:
        with open(filename, 'rb') as f:
            content = f.read()
            self.data = BytesIO(content)
            self.data.read(4)
            f.close()

        self.references = []

        self.opmap = {
            TerminalCode.TC_NULL: self.do_null,
            TerminalCode.TC_CLASSDESC: self.do_classdesc,
            TerminalCode.TC_OBJECT: self.do_object,
            TerminalCode.TC_BLOCKDATA: self.do_blockdata,
            TerminalCode.TC_REFERENCE: self.do_reference,
            TerminalCode.TC_ENDBLOCKDATA: self.do_null,
        }

    def read(self, ident=0):
        (opid, ) = self._read_struct(">B")
        handler = self.opmap[opid]
        return opid, handler(ident=ident)

    def _read_struct(self, unpack):
        length = struct.calcsize(unpack)
        ba = self.data.read(length)
        return struct.unpack(unpack, ba)
    
    @classmethod
    def do_null(parent=None, ident=0): return None

    def do_reference(self, ident):
        (handle,) = self._read_struct(">L")
        ref = self.references[handle - 0x7E0000]
        return ref

    def read_string(self, length_fmt="H"):
        (length,) = self._read_struct(">{0}".format(length_fmt))
        ba = self.data.read(length)
        return ba.decode()

    def do_classdesc(self, ident):
        name = self.read_string()
        self._read_struct(">qB")
        self.references.append(name)
        (length,) = self._read_struct(">H")

        for i in range(length):
            (typecode,) = self._read_struct(">B")
            prop = self.read_string()
        self._read_struct(">B")
        self.read(ident+1)
        return name

    def do_object(self, ident): 
        opcode, classdesc = self.read(ident + 1)
        if classdesc == 'java.util.ArrayList': o = []
        else: o = None
        res = self.read_value(ident)
        if o == None: o = res
        self.references.append(o)
        if o == []:
            while opcode != TerminalCode.TC_ENDBLOCKDATA:
                opcode, obj = self.read(ident + 1)
                if opcode != TerminalCode.TC_BLOCKDATA and isinstance(o, list):
                    o.append(obj)
        return o

    def do_blockdata(self, ident):
        (length,) = self._read_struct(">B")
        ba = self.data.read(length)
        # Ensure we have an str
        return str(ba)

    def read_value(self, ident): 
        (res,) = self._read_struct(">i")
        return res


def check(x):
    if x < 10: return False
    s = str(x)
    for i in range(len(s) - 1):
        if s[i] > s[i+1]: return False
    return True

jobj1 = JavaObject("DATA1.in")
_, a1 = jobj1.read()
a1.pop()
jobj2 = JavaObject("DATA2.in")
_, a2 = jobj2.read()
a2.pop()
m1, m2, s1, s2 = dict(), dict(), set(), set()
for i in a1:
    if check(i):
        if m1.get(i): m1[i]+=1
        else: m1[i] = 1
        s1.add(i)
for i in a2:
    if check(i):
        if m2.get(i): m2[i]+=1
        else: m2[i] = 1
        s2.add(i)
s = sorted(s1.intersection(s2))
for i in s:
    stdout.write(f'{i} {m1[i]} {m2[i]}\n')



