class message:

    def __init__(self):
        self.receiver = "default_receiver"
        self.sender = "default_sender"
        self.content = "default_content"
        self.packet = "default_packet"

    def DividePacket(self):
        if (self.packet == "default_packet"):
            return False
        else:
            self.content = self.packet
            return True

    def GetPacket(self, string):
        if(string == ""):
            return False
        self.packet = string
        self.DividePacket()

    def Receiver(self):
        return self.receiver

    def Sender(self):
        return self.sender

    def Content(self):
        return self.content