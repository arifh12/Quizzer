import tkinter as tk
import quiz_builder as quiz


class Quizzer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.FRAME_COLOR = "#f7f3e9"
        self.ROOT_COLOR = "#1aa6b7"
        self.MY_FONT = ('embria', 16)

        self.title("Quizzer")
        self.minsize(800,500)
        self.config(bg=self.ROOT_COLOR)
        
        self.frame = tk.Frame(self, bg=self.FRAME_COLOR)
        self.frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        self.score = 0
        self.score_label = tk.Label(self, text=f"Score: {self.score}", bg=self.ROOT_COLOR, fg="white", font=self.MY_FONT)
        self.score_label.place(relx=0.5, rely=0.05, anchor='center')

        self.q_label = tk.Label(self.frame, bg=self.FRAME_COLOR, font=self.MY_FONT, padx=5)
        self.q_label.bind('<Configure>', lambda e: self.q_label.config(wraplength=self.q_label.winfo_width()))
        self.q_label.pack(expand=True, fill="both")

        self.v = tk.StringVar()
        self.v.set(" ")

        self.radio_options = [] 
        rb = tk.Radiobutton(self.frame, variable=self.v, bg=self.FRAME_COLOR, fg=self.ROOT_COLOR, font=self.MY_FONT)
        rb.bind('<Configure>', lambda e: rb.config(wraplength=rb.winfo_width()-40))
        rb.pack(expand=True, fill="both")
        self.radio_options.append(rb)

        rb2 = tk.Radiobutton(self.frame, variable=self.v, bg=self.FRAME_COLOR, fg=self.ROOT_COLOR, font=self.MY_FONT)
        rb2.bind('<Configure>', lambda e: rb2.config(wraplength=rb2.winfo_width()-40))
        rb2.pack(expand=True, fill="both")
        self.radio_options.append(rb2)

        rb3 = tk.Radiobutton(self.frame, variable=self.v, bg=self.FRAME_COLOR, fg=self.ROOT_COLOR, font=self.MY_FONT)
        rb3.bind('<Configure>', lambda e: rb3.config(wraplength=rb3.winfo_width()-40))
        rb3.pack(expand=True, fill="both")
        self.radio_options.append(rb3)

        rb4 = tk.Radiobutton(self.frame, variable=self.v, bg=self.FRAME_COLOR, fg=self.ROOT_COLOR, font=self.MY_FONT)
        rb4.bind('<Configure>', lambda e: rb4.config(wraplength=rb4.winfo_width()-40))
        rb4.pack(expand=True, fill="both")
        self.radio_options.append(rb4)

        self.button = tk.Button(self.frame, text="Submit", bg=self.ROOT_COLOR, fg=self.FRAME_COLOR, relief=tk.FLAT, font=self.MY_FONT)
        self.button.pack(side="bottom", pady=10)

    def init_quiz(self):
        self.quiz = quiz.generate_questions()
        self.q_label.config(text=self.quiz[-1].question)

        self.answer_choices = self.quiz[-1].answer_choices()
        for choice, option in zip(self.answer_choices, self.radio_options):
            option.config(text=choice, value=choice)

        self.button.config(command=lambda: self.check_answer())

    def check_answer(self):
        if (self.quiz[-1].correct_answer==self.v.get()):
            self.score+=10
            self.score_label.config(fg="SeaGreen1")
        else:
            self.score = max(self.score-10, 0)
            self.score_label.config(fg="light coral")

        self.score_label.config(text=f"Score: {self.score}")
        self.quiz.pop()
        self.next_question()

    def next_question(self):
        if (not self.quiz):
            self.quiz = quiz.generate_questions()

        self.q_label.config(text=self.quiz[-1].question)

        self.answer_choices = self.quiz[-1].answer_choices()
        for choice, option in zip(self.answer_choices, self.radio_options):
            option.config(text=choice, value=choice)
            self.v.set(" ")


app = Quizzer()
app.init_quiz()
app.mainloop()

