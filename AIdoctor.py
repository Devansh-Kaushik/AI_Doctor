from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
import socket
import pyttsx3
from serpwow.google_search_results import GoogleSearchResults
import webbrowser
import re
import pygame

serpwow = GoogleSearchResults("Get Your key")
engine = pyttsx3.init()
m = sr.Recognizer()
ph = sr.Recognizer()
root = Tk()
root.geometry('1920x1020')
root.title("AMIGO-Your Personal AI Doctor")
root.iconbitmap('C:/Users/DEVANSH/Desktop/project-files/doc.ico')
c = Canvas(root, bg='black')
img = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Desktop/project-files/Amigo.png'))
img1 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Desktop/project-files/Brain.png'))
img2 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Desktop/project-files/s1.png'))
img3 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Desktop/project-files/phy.png'))
c.pack(ipadx=0, ipady=0, fill=BOTH, expand=TRUE)
# ----------------------------Physocial images------------------------------------------------
i1 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Desktop/project-files/1.jpeg'))
i2 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Desktop/project-files/2.jpeg'))
i3 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Desktop/project-files/3.jpeg'))
i4 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Desktop/project-files/4.jpeg'))
i5 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Desktop/project-files/5.jpeg'))
i6 = ImageTk.PhotoImage(Image.open('C:/Users/DEVANSH/Desktop/project-files/6.jpeg'))



def psychosocial():
    n2 = e1.get()
    b2.place_forget()
    engine.setProperty('rate', 130)
    engine.say(" Hi " + n2 )
    engine.say("Relax Your Mind Through this small session")
    engine.say(" Lets Perfome A White Light Session for you")
    engine.runAndWait()
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/DEVANSH/Desktop/project-files/in-the-light.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    k1 = Label(root,width=760, height=900, bg='black')
    k1.place(x=760, y=0)
    k1.configure(image=i1)
    root.update()
    root.after(500, None)
    engine.setProperty('rate', 90)
    engine.say("Imagin  A stream of vibrant, white light flows infinitely down from Source and in through the top of your head.\
               Feel the light wash over you as a purifying waterfall, cleansing all past worries, fears, and anxieties.\
               The light flows through you as you experience unconditional Love, joy, well-being, and vitality all in the name of the Creator")
    engine.say("The white light shines vibrantly, as vibrant as all the jewels and gems in this world, and reflects all the colors of the rainbow throughout.\
               Feel each colour strike each individual cell of your body with radiating love and nourishment .")
    engine.runAndWait()
    root.after(500, None)

    k1.configure(image=i2)
    root.update()
    engine.setProperty('rate', 87)
    engine.say("YOU ARE HEALING.")
    engine.say(" ")
    engine.runAndWait()
    engine.say("The stream of light flows through your body enrichening and enlivening you.\
               Breathe this light deep through your body and down through your feet through your soles and into the Mother.\
               The healing light resides within you and circulates through you cleansing of any impurities that have misconstrued your perception of Love.\
               Old and stagnant energy is instantly eradicated and replaced with the vibrant energy of Life.")
    root.after(500, None)

    k1.configure(image=i3)
    root.update()
    engine.setProperty('rate', 87)
    engine.say("From your crown chakra, Breathe the white light deeper into your 3rd eye chakra filling it with Love and Light.\
                Reach out and request the white light to grant you clairvoyance to your inner vision and allow your perspective to expand infinitely.\
                From here, breathe the white light down further into your throat chakra. \
               Your place of speaking where Truth is uttered. \
               Breathe out the white light it passes through your throat chakra and releases the Truth into the universe through your voice.")
    engine.say("Next, move the white light down into you heart chakra with your breath.\
               Feel the ultimate expansion at an infinite rate as pure white light pierces and becoyous every aspect of your heart.\
               Your heart now radiates as a brilliant white sphere of Light and Love.")
    engine.runAndWait()
    root.after(500, None)

    k1.configure(image=i4)
    root.update()
    engine.setProperty('rate', 87)
    engine.say("You are Light.")
    engine.say("")
    engine.say("Bring the healing white light down through your crown chakra and into you solar plexus chakra, just below the chest but above the belly.\
               release youself from all limitations and expectations placed upon you externally.\
               Live freely and openly and by your own heart.")
    engine.runAndWait()
    root.after(500, None)

    k1.configure(image=i5)
    root.update()
    engine.setProperty('rate', 87)
    engine.say("Now breathe this pure, white light down from your crown chakra and into you sacral chakra, just below the navel.\
               Breathe deeply into this space.\
               This is the space you were born from. How you entered into this world.")
    engine.say(" ")
    engine.say("Surrender all things that no longer serve you .")
    engine.say(" ")
    engine.runAndWait()
    root.after(500, None)

    k1.configure(image=i6)
    root.update()
    engine.setProperty('rate', 87)
    engine.say("Now,  breathe the pure, healing, white light down into you root chakra.\
               This grounds you within this reality and provides you with a strong foundation in which to operate from.\
               Feel an ancient connection to Mother Earth and all of your fellow humans.")
    engine.say("")
    engine.say("You are pure, white light.")
    engine.runAndWait()
    pygame.mixer.music.stop()
    engine.setProperty('rate', 130)
    engine.say("Hope   Your Mind  are Relaxed")
    engine.runAndWait()
    screen1()



def screen1():
    global b1, b2
    c.pack_forget()

    def mental():
        global repeat
        n1 = e1.get()
        b1.pack_forget()
        lab = Label(root, width=760, height=900, image=img2)
        lab.place(x=-4, y=0)
        '''b1.configure(image=img2);
        b4 = Button(root, text="Once's more", width=15, height=2, bg="light blue", font=("Playfair Display", 20), fg="black"
                    , command=restart)
        b4.place(x=650, y=550)#3b3068'''
        d1 = Text(root, width=42, height=18.4, background="#3b3068", foreground="#f96bc0",
                  font=("Playfair Display", 20))
        d1.place(x=56, y=144)
        IPaddress = socket.gethostbyname(socket.gethostname())
        if IPaddress == "127.0.0.1":
            d1.insert(END, "\n\n\n\n\n\n\n       "
                           "NOT CONNECTED TO INTERNET :)\n         "
                           "Please check your internet connectivity \n      "
                           "Then i am ready to help you[--->  /^!^\ <---]")
            root.update()
            engine.say(n1 + "You are not connect to a netork")
            engine.say(n1 + "I will be ready as you connect to a network")
            engine.runAndWait()
            mental()
        else:
            root.after(2000, None)
            d1.insert(END, "\n\n\n\n\n\n\n       "
                      "   Hi " + n1 + " myself Amigo and i am here to help your\n              "
                                           " Take me as your close friend\n            "
                                           "   To exit say --> (GoodBye) ")
            root.update()
            engine.setProperty('rate', 150)
            engine.say("Hi " + n1 + " Myslef Amigo and i am here to help your")
            engine.say("Take me as your close friend     ")
            engine.runAndWait()
            run = True
            while run:
                d1.delete("1.0", "end")
                d1.insert(END, "\n\n\n\n\n\n\n\n             "
                               "      How can i help you     ")
                root.update()
                engine.say('How can i help you' + n1)
                engine.runAndWait()
                with sr.Microphone() as source:
                    print("AMIGO:")
                    audio = m.listen(source)
                try:
                    print(m.recognize_google(audio))
                    l = m.recognize_google(audio)
                    if l == "goodbye":
                        d1.delete("1.0", "end")
                        d1.insert(END, "\n\n\n\n\n\n\n\n             "
                                       " Goodbye be happy and have a nice day     ")
                        root.update()
                        engine.say('Goodbye')
                        engine.say('Be happy and have a nice day' + n1)
                        engine.runAndWait()
                        screen1()

                    def repeat():
                        params = {
                            "q": l,
                            "gl": "in",
                            "hl": "en",
                            "location": "Delhi,India",
                            "google_domain": "google.co.in",
                            "device": "desktop",
                            "csv_fields": "related_questions.answer,related_questions.source.link"
                        }
                        result = serpwow.get_csv(params)
                        urls = re.findall(
                            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                            result[58:None]
                        )
                        text = str(result[58:None])
                        d1.delete("1.0", "end")
                        d1.insert(END, text)
                        root.update()
                        if urls:
                            RU = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', result[58:None])
                            engine.setProperty('rate', 145)
                            engine.say("Here is your solution to your problem " + n1 + " " + RU)
                            engine.runAndWait()
                        for i in range(len(urls)):
                            webbrowser.open(str(urls[i]))

                    run = False
                    repeat()
                except:
                    print(" ")

    b1 = Button(root, text="Mental health", width=760, height=900, image=img1, command=mental)
    b1.place(x=-4, y=0)
    b2 = Button(root, text="Physocial support", width=760, height=900, image=img3, command=psychosocial)
    b2.place(x=760, y=0)

def main_screen():
    global e1
    c.create_image(700, 460, image=img)
    e1 = Entry(c, width=30, bg="#ffde59", fg="black")
    e1.place(x=1150, y=550)
    b1 = Button(c, text='Lets Begin', width=10, font=("Playfair Display", 30), bg="#ffde59", command=screen1)
    b1.place(x=1130, y=600)


main_screen()
root.mainloop()
