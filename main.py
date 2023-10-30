from neuralintents.assistants import BasicAssistant

done = False

assistant = BasicAssistant('intents.json')

assistant.fit_model(epochs=50)
assistant.save_model()


while not done:
    message = input("Enter a message: ")
    if message == "STOP":
        done = True
    else:
        print(assistant.process_input(message))