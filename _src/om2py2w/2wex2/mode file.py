class App:
    def __init__(self, master):

        frame  = Frame(master)
        frame.pack()

        self.text_write = Entry(frame)
        self.text_write.pack()

        self.button = Button(frame, text="quit", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text='hello', fg='black', command=self.say_hi)
        self.hi_there.pack(side=RIGHT)

    def say_hi(self):
        print(self.text_write.get())