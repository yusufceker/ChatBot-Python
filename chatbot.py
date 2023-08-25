from tkinter import *
from tkinter import messagebox
import openai


# Set up your OpenAI API Key
openai.api_key = ""


def send_message():
    user_message = entry.get()
    response = generate_response(user_message)
    display_message(response)

# Function to generate a bot response based on the question of the user
def generate_response(user_message):
    # Send user input to the ChatGPT model
    response = openai.Completion.create(
        engine='text-davinci-003', #it's the last version of OpenAI that we can use for free
        prompt=user_message,
        max_tokens=400, #max word limit
        temperature=0.7,
        n=1,
        stop=None
    )
    return f"Bloop: {response.choices[0].text.strip()}" 

def display_message(response):
    chat_box.config(state=NORMAL)
    chat_box.insert(END, response + '\n')
    chat_box.config(state=DISABLED)
    entry.delete(0,END)

window = Tk()
window.title("Bloop")
chat_box = Text(window, width=50, height=40, state=DISABLED)
chat_box.pack()


scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)


chat_box.config(yscrollcommand=scrollbar.set,background="yellow")
scrollbar.config(command=chat_box.yview)


entry = Entry(window, width=50) 
entry.pack()

send_button = Button(window, text="Send", command=send_message)
send_button.pack()

window.mainloop()
