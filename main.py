from neuralintents.assistants import BasicAssistant

done = False

def bad_message():
    print("Sorry but i cant continiue this conversation")

assistant = BasicAssistant('intents.json', method_mappings={"very_bad": bad_message})

assistant.fit_model(epochs=50)
assistant.save_model()


while not done:
    message = input("Enter a message: ")
    if message == "STOP":
        done = True
    if bad_message:
        print("Sorry but i cant continiue this conversation")
        done = True
    else:
        print(assistant.process_input(message))