import paho.mqtt.client as mqtt


def initiate_client() -> object:
    """
    Initiate a new mqtt client that is stored as an object.

    :return: an object

    """
    return mqtt.Client("marlon_pi")


def on_connect(client: object, userdata: None, flags: dict, rc: int):
    """
    Display a helpful message to notify user they successfully connected to the server.

    :param client: an object
    :param userdata: NoneType
    :param flags: a dictionary
    :param rc: an int
    :precondition: client must be a properly formatted object initiate through mqtt
    :post condition: will notify that it successfully connected to the server
    :return: nothing

    """
    print("Successfully connected")
    return


def on_message(client: object, userdata: None, message: str):
    """
    Display a message when the server receives one.

    :param client: an object
    :param userdata: NoneType
    :param message: a string
    :precondition: client must be a properly formatted object initiate through mqtt
    :precondition: message must be a string
    :post condition: print the message that was sent to the server
    :return: nothing

    """
    message_text = str(message.payload.decode("utf-8"))
    print(message_text)
    return


def connect(user: object, topic: str) -> None:
    """
    Connect the user to the public mosquitto server.

    :param user: an object
    :param topic: a string
    :precondition: user has to be a properly formed object that was initiated through the mqtt server
    :precondition: topic must be a string
    :post condition: will connect to the public mqtt server
    :return: nothing

    """
    user.connect("test.mosquitto.org", 1883)
    user.subscribe(topic)
    user.on_connect = on_connect
    return


def open_chatroom():
    """
    Initiate a chat room to view all messages that are sent to the mqtt server.

    :return: nothing

    """
    chatroom_listener = initiate_client()
    connect(chatroom_listener, "Ugh")
    chatroom_listener.on_message = on_message
    chatroom_listener.loop_forever()
    return


def main():
    """Run the module."""
    open_chatroom()
    

if __name__ == '__main__':
    main()
