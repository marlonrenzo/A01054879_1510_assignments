import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    """"""
    print("Successfully connected")


def on_message(client, userdata, message):
    """"""
    message_text = str(message.payload.decode("utf-8"))
    print(message_text)
    
    
def open_chatroom():
    chatroom_listener = mqtt.Client("marlon_pi")
    chatroom_listener.connect("test.mosquitto.org", 1883)
    chatroom_listener.subscribe("Ugh")
    chatroom_listener.on_message = on_message
    chatroom_listener.on_connect = on_connect
    chatroom_listener.loop_forever()


def main():
    """"""
    open_chatroom()
    

if __name__ == '__main__':
    main()
