from tkinter import *
import quiz_brain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: quiz_brain.QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_text = Label(text=f"Score:{0}/0", font=("Ariel", 20, "bold"), fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)

        self.question_widget = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_widget.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.question_widget.create_text(150, 125, text="Word", font=("Ariel", 10, "italic"),
                                                              fill=THEME_COLOR, width=280)

        nok_image = PhotoImage(file="images/false.png")
        self.nok_button = Button(image=nok_image, highlightthickness=0, borderwidth=0, command=self.nok)
        self.nok_button.grid(row=2, column=0)

        ok_image = PhotoImage(file="images/true.png")
        self.ok_button = Button(image=ok_image, highlightthickness=0, borderwidth=0, command=self.ok)
        self.ok_button.grid(row=2, column=1)
        self.get()
        self.window.mainloop()

    def get(self):
        self.question_widget.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score:{self.quiz.score} / {self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.question_widget.itemconfig(self.question_text, text=q_text)
        else:
            self.ok_button.config(state=DISABLED)
            self.nok_button.config(state=DISABLED)

    def ok(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def nok(self):
        is_right = self.quiz.check_answer("False")

        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_widget.config(bg="green")
        else:
            self.question_widget.config(bg="red")
        self.window.after(1000, self.get)
