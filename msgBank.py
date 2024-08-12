class MsgBank():
    def __init__(self) -> None:
        self.msg_list = []
    
    def add(self,msg):
        self.msg_list.append(msg)
    
    def get(self):
        return "\r\n".join(self.msg_list)
    
    def delete(self):
        self.msg_list = []
    
