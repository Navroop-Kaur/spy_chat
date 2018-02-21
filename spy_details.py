from datetime import datetime
class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

spy = Spy("Navroop",'Ms.',22,2.4)

friend_one = Spy('Raja', 'Mr.', 27, 4.9)
friend_two = Spy('Mata Hari', 'Ms.', 21, 4.39)
friend_three = Spy('No', 'Dr.', 37, 4.95)

friends = [friend_one, friend_two, friend_three]


class ChatMessage:
    def __init__(self, sender,message_sent_to,message, sent_by_me):
        self.name_of_sender = sender
        self.message_sent_to = message_sent_to

    def __init__(self,message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


cm = ChatMessage("message","sent_by_me")
chat_one = ChatMessage("message","sent_by_me")
chat_two = ChatMessage("message","sent_by_me")
chat_three = ChatMessage("message","sent_by_me")
chats =[chat_one,chat_two,chat_three]