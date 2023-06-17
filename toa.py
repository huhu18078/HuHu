import customtkinter as ctk
import random
app = ctk.CTk()
app.title('เค้าชอบคุณกี่เปอร์เซนต์')
app.geometry('500x500')

label = ctk.CTkLabel(app,text="เค้าชอบคุณกี่เปอร์เซนต์",font=('Aria',30))
label.pack(pady=(20,0))

entry = ctk.CTkEntry(app, placeholder_text="ใส่ชื่อของคุณ")
entry.pack(pady=(15,0))

answer_text = ctk.StringVar()
answer_label = ctk.CTkLabel(app,textvariable=answer_text, font=('Aria',40))
answer_label.pack(pady=(20,0))

def button_event():
    user_input = entry.get()
    answer = user_input
    answer_text.set("เค้าชอบคุณ"+str(random.randrange(0, 101))+"%")
    print(user_input,answer)

button = ctk.CTkButton(app,text="กดเลย",command=button_event)
button.pack(pady=(20,0))
app.mainloop()


