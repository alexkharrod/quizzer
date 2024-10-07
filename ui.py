from tkinter import *

from data import question_data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280,text="text",fill="black",font=('arial', 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2,pady=30)


        self.score_label = Label(bg=THEME_COLOR, fg="white", text=f"Score: 0")
        self.score_label.grid(row=0, column=1)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(width=100, height=97, image=true_image, highlightthickness=0, command=self.true_button)
        self.true_button.grid(row=2, column=1)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(width=100, height=97, image=false_image, highlightthickness=0,command=self.false_button)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()

        self.window,mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_button(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)

    def false_button(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)



    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')


        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)