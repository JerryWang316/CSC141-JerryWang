def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)

messages_list = ["Hello!", "How are you?", "Python is fun!"]
sent_messages = []

send_messages(messages_list[:], sent_messages)

print(f"Original list: {messages_list}")
print(f"Sent messages: {sent_messages}")