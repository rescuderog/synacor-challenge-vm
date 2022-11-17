import struct

class VirtualMachine:
    def __init__(self):
        #initialize registers (reg 0 to 7)
        self.reg0, self.reg1, self.reg2, self.reg3, self.reg4, self.reg5, self.reg6, self.reg7 = None
        #initialize memory (15 bit = 32768 - 1)
        memory = [None] * 32767

    def toBinaryData(buf):
        """toBinaryData: transforms information to little endian 16-bit binary data

        Args:
            buf (unsigned short size): the buffer to transform to binary

        Returns:
            unpacked buf: transformed data
        """        
        return struct.unpack("<H", buf)

