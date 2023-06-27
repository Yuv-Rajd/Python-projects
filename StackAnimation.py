import tkinter as tk




class StackAnimation:

    def __init__(self, master):
        self.master = master
        self.master.title("Stack Animation")
        self.master.geometry("1200x600")
        # self.master.minsize(1200,600)

        self.intro='''
        insert element to knoe the working of stack 
        max elements are 10
        data type is not yet assigned
        '''
        self.push_text='''
            def push(self):
                self.stack.append(element)
            '''
        self.pop_text='''
        def push(self):
            if self.stack:
                self.stack.pop()
        '''
        

        self.stack = []


        self.top_frame = tk.Frame(self.master)
        self.top_frame.pack(side="top", fill="x")

        self.top_label = tk.Label(self.top_frame, text="This is a responsive frame", font=("Helvetica", 20))
        self.top_label.pack(pady=10)

        self.label = tk.Label(self.master, text="Stack Operations", font=("Courier", 30))
        self.label.pack(pady=20)


        self.canvas_frame = tk.Frame(self.master, bg="white")
        self.canvas_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.display_frame = tk.Frame(self.master)
        self.display_frame.pack(pady=10)

        self.display_label = tk.Label(self.display_frame, text="Stack:", font=("Arial", 14))
        self.display_label.pack(side="left", padx=10)

        self.display = tk.Label(self.display_frame, text=self.stack, font=("Arial", 14))
        self.display.pack(side="left")


        self.push_frame = tk.Frame(self.master)
        self.push_frame.pack(pady=10)

        self.push_label = tk.Label(self.push_frame, text="Enter Element to Push:", font=("Arial", 14))
        self.push_label.pack(side="left", padx=10)

        self.push_entry = tk.Entry(self.push_frame, font=("Arial", 14), width=10)
        self.push_entry.pack(side="left")

        self.push_button = tk.Button(self.push_frame,bg="#73e600", text="Push", font=("Arial", 14), command=self.push)
        self.push_button.pack(side="left", padx=10)

        self.pop_button = tk.Button(self.push_frame,bg="#ff6666", text="Pop", font=("Arial", 14), command=self.pop)
        self.pop_button.pack(side="right", padx=10)

        self.top_button = tk.Button(self.push_frame,bg="lightblue", text="Top", font=("Arial", 14), command=self.top)
        self.top_button.pack(side="right", padx=50)
        
        self.draw_stack_extras()
        self.draw_description(self.intro)


        def callback(event):
            if event.keysym=='BackSpace':
                self.pop()  
            if event.keysym=='Return':
                self.push() 

        self.push_entry.bind("<1>", lambda event: self.push_entry.focus_set())
        self.push_entry.bind("<Key>", callback)
        
    




    def push(self):
        element = self.push_entry.get()
        if len(self.stack)==10:
            self.push_entry.delete(0,len(element))
            self.push_entry.insert(0,string='')
            self.draw_description("Stack OverFlow")
        else:
            if element:
                self.stack.append(element)
                self.display.config(text=self.stack)
                self.canvas.after(0,self.draw_stack(self.push_text))
            self.push_entry.delete(0,len(element))
            self.push_entry.insert(0,string='')


    def pop(self):
        if self.stack:
            self.stack.pop()
            self.display.config(text=self.stack)
            self.canvas.after(0,self.draw_stack(self.pop_text))
        else:
            self.draw_description("Stack UnderFlow")


    def top(self):
        if self.stack:
            self.display.config(text=f"Top Element: {self.stack[-1]}")
        else:
            self.display.config(text="Stack is Empty (-1)")


    def draw_description(self,text):
        self.canvas.create_rectangle(1100, 595, 1600, 2,fill="#e6f7ff", outline="black")
        self.canvas.create_text(1300, 250, text=text, font=("Arial", 14))
    
    def draw_stack_extras(self):
        self.canvas.create_rectangle(693, 557, 807, 43, fill="white", outline="black")


    def draw_stack(self,fun):
        self.canvas.delete("all")
        self.draw_description(fun)
        
        x, y = 700, 500
        self.draw_stack_extras()

        for index, item in enumerate((self.stack)):
            self.canvas.create_rectangle(x, y, x+100, y+50, fill="lightgreen", outline="black",activefill="red")
            self.canvas.create_text(x+50, y+25, text=item, font=("Arial", 14))
            self.canvas.create_text(x-25, y+25, text=f"({index})", font=("Arial", 14))
            y -= 50
        if y<500:
            self.canvas.create_text(x-75, y+75, text="top ->", font=("Arial", 14))



    def run(self):
        self.master.mainloop()


        



if __name__ == "__main__":
    root = tk.Tk()
    stack_animation = StackAnimation(root)
    stack_animation.run()

