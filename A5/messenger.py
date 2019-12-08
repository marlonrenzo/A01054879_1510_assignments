import paho.mqtt.client as mqtt


def initiate_client(user_id: str) -> object:
    """
    Initiate a new mqtt client that is stored as an object.
    
    :param user_id: a string
    :precondition: user_id must be a string
    :post condition: will return a new client as an object with the user_id as an attribute
    :return: an object
    
    """
    return mqtt.Client(user_id)


def on_connect(client: object, userdata: None, flags: dict, rc: int) -> None:
    """
    Send a message to the server to notify that the user is connected.
    
    :param client: an object
    :param userdata:
    :param flags: a dictionary
    :param rc: an integer
    :return: nothing
    
    """
    client.publish("Ugh", client._client_id.decode("utf-8") + " entered the room")
    return

def connect(user: object, topic: str) -> None:
    """
    Conect the user to the public mosquitto server.
    
    :param user: an object
    :param topic: a string
    
    :return: nothing
    
    """
    user.connect("test.mosquitto.org", 1883)
    user.subscribe(topic)
    user.on_connect = on_connect
    user.loop_start()
    return


def disconnect(current_user: object, topic: str) -> None:
    """
    Disconnect the user from the public mosquitto server.
    
    :param current_user: an object
    :param topic: a string
    :return: nothing
    
    """
    current_user.publish(topic, current_user._client_id.decode("utf-8") + " left the room\n")
    current_user.disconnect()
    print("Successfully disconnected")
    return


def send_message(current_user: object, username: str, topic: str, message: str) -> None:
    """
    Send a message to the server to publish to the selected.
    
    Include the username in the final message to clarify which user is sending the message.
    
    :param current_object:
    :param username:
    :param topic:
    :param message:
    :return: nothing
    
    """
    final_message = f"{username}: {message}"
    current_user.publish(topic, final_message)
    return


def message_loop(current_user: object, username: str, topic: str) -> None:
    """
    Create a loop to grab user input that will be sent to the server as a message.
    
    If the user decides to quit, disconnect the user from the server and break out of the loop.
    
    :param username:
    :param current_user:
    :param topic:
    :return: nothing
    
    """
    user_input = input("Welcome to the chatroom, " + username + "\nThe topic is " +
                       topic + "\nType 'quit' to disconnect\n")
    while user_input != 'quit':
        send_message(current_user, username, topic, user_input)
        user_input = input()  
    disconnect(current_user, topic)
    return


def messenger():
    """
    Run the messenger by calling the necessary functions in the correct order.
    
    :return: nothing
    
    """
    topic = "Ugh"
    username = input("Enter a username: ")
    client_object = initiate_client(username)
    connect(client_object, topic)
    message_loop(client_object, username, topic)
    

def main():
    """Run the module."""
    messenger()
    

if __name__ == '__main__':
    main()
