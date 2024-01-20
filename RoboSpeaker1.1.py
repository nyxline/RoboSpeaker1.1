import os #importing os module for text-speech functionality

if __name__ == '__main__': #determines if python script is being run as the main program or if it's being imported as a module into another script.
    print("welcome to RoboSpeaker 1.1. Created by Nandini")
    while True: #loop
        x= input("Enter what you want me to speak")
        if x == "q":
            os.system("say 'bye bye'")
            break; 
        command = f"say {x}" #f string is included, say commond is used on macos system to convert text to speech
        os.system(command)  #os.system is function that will help in executing the command
