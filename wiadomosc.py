class message:

    def __init__(self):
        self.receiver = "default_receiver"
        self.sender = "default_sender"
        self.content = "default_content"

    def GetReceiver(self, string):
        self.receiver = string

    def GetSender(self, string):
        self.sender = string

    def GetContent(self, string):
        self.content = string

    def Receiver(self):
        return self.receiver

    def Sender(self):
        return self.sender

    def Content(self):
        return self.content