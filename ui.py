from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=500, height=700)
        self.window.maxsize(width=500, height=700)
        self.window.config(bg=THEME_COLOR, padx=40, pady=40)

        self.quiz = quiz_brain
        self.scoreboard = Label(text=f"Score: {self.quiz.score}/{self.quiz.question_number}",
                                font=("Arial", 16), bg=THEME_COLOR, fg="#fff")
        self.scoreboard.grid(column=1, row=0)

        self.canvas = Canvas(width=420, height=350)
        self.canvas.config(bg="#fff")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=(40, 70))

        self.question_text = ""

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, command=self.pressed_true, highlightthickness=0)
        self.true_button.grid(column=0, row=3)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, command=self.pressed_false, highlightthickness=0)
        self.false_button.grid(column=1, row=3)

        self.show_next_question()

        self.window.mainloop()

    def make_canvas_white(self):
        self.canvas.config(bg="#fff")
        self.canvas.itemconfig(self.question_text, text="")
        self.question_text = self.canvas.create_text(200, 170, width=300, text=self.quiz.next_question(),
                                                     font=("Arial", 20, "italic"))

    def show_next_question(self):
        self.window.after(1000, self.make_canvas_white)

    def pressed_true(self):
        if self.quiz.check_answer("True"):
            self.canvas.config(bg="#03AC13")
        else:
            self.canvas.config(bg="#ff2400")
        self.show_next_question()
        self.scoreboard.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number - 1}")

    def pressed_false(self):
        if self.quiz.check_answer("False"):
            self.canvas.config(bg="#03AC13")
        else:
            self.canvas.config(bg="#ff2400")
        self.window.after(1000, self.show_next_question)
        self.scoreboard.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number - 1}")
