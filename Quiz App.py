import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz App")

        self.name_entry = tk.Entry(self.window, width=30)
        self.name_entry.grid(column=0,row=0,pady=10)

        self.click_button = tk.Button(self.window, text="Continue", command=self.hide_entry_and_start_quiz)
        self.click_button.grid(column=0,row=1,pady=10)

        self.quiz_data = [
            {
                "question": "What is the capital of India?",
                "options": ["Mumbai", "Chennai", "Delhi", "Hyderabad"],
                "correct_answer": 3
            },
            {
                "question": "Who wrote the novel 'Pride and Prejudice'?",
                "options": ["Jane Austen", "Emily Bronte", "Charlotte Bronte", "Louisa May Alcott"],
                "correct_answer": 0
            },
            {
                "question": "What is the chemical symbol for the element Gold?",
                "options": ["Ag", "Au", "Cu", "Fe"],
                "correct_answer": 1
            },
        ]
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(self.window, text="")
        self.question_label.grid(row=2,column=0)

        self.options_frame = tk.Frame(self.window)
        self.options_frame.grid(row=3,column=0)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.options_frame, text="", width=30, command=lambda i=i: self.check_answer(i))
            button.grid(column=0,row=i,pady=5)
            self.option_buttons.append(button)

        self.next_question_button = tk.Button(self.window, text="Next Question", width=30, command=self.next_question)
        self.next_question_button.grid(column=0,row=5,pady=10)

    def hide_entry_and_start_quiz(self):
        self.name_entry.grid_forget()
        self.click_button.grid_forget()
        self.start_quiz()

    def start_quiz(self):
        self.load_question()
        self.window.mainloop()

    def load_question(self):
        question_data = self.quiz_data[self.current_question_index]
        self.question_label.config(text=question_data["question"])
        options = question_data["options"]
        for i in range(4):
            self.option_buttons[i].config(text=options[i])

    def check_answer(self, selected_option):
        question_data = self.quiz_data[self.current_question_index]
        correct_answer_index = question_data["correct_answer"]

        for button in self.option_buttons:
            button.config(bg="SystemButtonFace")
        self.option_buttons[selected_option].config(bg="light green")

        if selected_option == correct_answer_index:
            self.score += 1

    def next_question(self):
        for button in self.option_buttons:
            button.config(bg="SystemButtonFace")

        self.current_question_index += 1
        if self.current_question_index == len(self.quiz_data):
            messagebox.showinfo("Quiz Over", f"Quiz finished. Your score: {self.score}/{len(self.quiz_data)} \n Thank You for playing {self.name_entry.get()}.")
            self.window.quit()
        else:
            self.load_question()

quiz_app = QuizApp()
quiz_app.window.mainloop()
