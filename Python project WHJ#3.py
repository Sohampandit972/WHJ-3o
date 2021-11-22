from tkinter import * 
root=Tk()
root.title("Luck freind wheel")
root.geometry("500x500")

enter_name_entry = Entry(root)

enter_name_entry.place(relx = 0.5, rely = 0.2, anchor = CENTER)

label1 = Label(root)

label2 = Label(root)

label3 = Label(root)

list = []
def addfreind():
    freind_name = enter_name_entry.get()
    list.append(freind_name)
    label1["text"] = "your freindlist :  " + str(list)
    
    
    def random_number():
        length = len(list)
        random_no = random.randint(0, length-1)
        random_number_label["text"] =
        list1[random_no]
        label3["text"] = "your lucky freind is: " + str(generated_random_number)
        
        btn = Button(root, text="Add to the freindlist", command = addfreind()
        btn1.place(relx= 0.5,rely = 0.4, anchor = CENTER)
        
        freind_list.place(relx= 0.5, rely= 0.5, anchor = CENTER )
        random_number_label.place(relx= 0.5, rely= 0.6, anchor= 0.7, anchor = CENTER)
        
        root.mainloop()