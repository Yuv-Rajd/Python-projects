import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

class QueueAnimation:
    def __init__(self, master):
        self.master = master
        self.master.geometry("700x700")
        self.master.title("Queue Animation")
        self.queue = []
        self.display = tk.Label(self.master, text="", font=("Arial", 14))
        self.display.pack()
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        self.enqueue_button = tk.Button(self.master, text="Enqueue", command=self.enqueue)
        self.enqueue_button.pack()
        self.dequeue_button = tk.Button(self.master, text="Dequeue", command=self.dequeue)
        self.dequeue_button.pack()
        self.front_button = tk.Button(self.master, text="Front", command=self.front)
        self.front_button.pack()

    def enqueue(self):
        element = tk.simpledialog.askinteger("Input", "Enter a number:")
        if element is not None:
            self.queue.append(element)
            self.display.config(text=self.queue)
            self.draw_queue()

    def dequeue(self):
        if self.queue:
            self.queue.pop(0)
            self.display.config(text=self.queue)
            self.draw_queue()
        else:
            self.display.config(text="Queue is Empty")

    def front(self):
        if self.queue:
            self.display.config(text=f"Front Element: {self.queue[0]}")
        else:
            self.display.config(text="Queue is Empty")

    def draw_queue(self):
        self.canvas.delete("all")
        x, y = 50, 50
        for index, item in enumerate(self.queue):
            self.canvas.create_rectangle(x, y, x+50, y+50, fill="lightgray", outline="black")
            self.canvas.create_text(x+25, y+25, text=item, font=("Arial", 14))
            x += 50

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    queue_animation = QueueAnimation(root)
    queue_animation.run()
