class User:
    def __init__(self, name: str):
        self.name = name
        self.chat_room = ChatRoom()

    def say(self, message: str):
        self.chat_room.display_message(self, message)

    def __str__(self) -> str:
        return self.name


class ChatRoom:
    def display_message(self, user: User, message: str):
        print(f"[{user} says]: {message}")


if __name__ == '__main__':
    molly = User('Molly')
    mark = User('Mark')
    ethan = User('Ethan')

    molly.say("Hi Team! Meeting at 3 PM today.")
    mark.say("Roger that!")
    ethan.say("Alright.")
