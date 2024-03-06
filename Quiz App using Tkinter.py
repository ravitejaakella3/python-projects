import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Quiz App")

        self.label=tk.Label(text="Welcome to Quiz game.Please Enter your name and click continue")
        self.label.grid(column=0,row=0)
        
        #create entry box to write the name of a player
        self.name_entry = tk.Entry(self.window, width=30)
        self.name_entry.grid(column=0,row=1,pady=10)

        self.click_button = tk.Button(self.window,text="Continue", command=self.hide_entry_and_start_quiz)
        self.click_button.grid(column=0,row=2,pady=10)

        #create quiz questions
        self.quiz_data = [
            {
                "question": "What is the capital of India?",
                "options": ["Mumbai", "Chennai", "Delhi", "Hyderrabad"],
                "correct_answer": 2
            },
            {
                "question": "Who won the Men's ODI World Cup 2023?",
                "options": ["India", "Australia", "England", "South Africa"],
                "correct_answer": 1
            },
            {
                "question": "The Gateway Of India is located in which city?",
                "options": [ "Mumbai", "Chennai", "Delhi", "Hyderrabad"],
                "correct_answer": 0
            },
            {
                "question": "When was the Chandrayaan-3 launch?",
                "options": [ "12 July 2023", "13 July 2023", "14 July 2023", "15 July 2023"],
                "correct_answer": 2
            },
            {
                "question": "Who won the player of the match award in the World Test championship in 2023?",
                "options": [ "Steve Smith", "Virat Kohli", "Travis Head", "Scott Boland"],
                "correct_answer": 2
            },
        ]
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(self.window, text="")
        self.question_label.grid(row=3,column=0)

        self.options_frame = tk.Frame(self.window)
        self.options_frame.grid(column=0,row=4)
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.options_frame, text="", width=30, command=lambda i=i: self.check_answer(i))
            button.grid(column=0,row=i,pady=5)
            self.option_buttons.append(button)

        self.next_question_button = tk.Button(self.window, text="Next Question", width=30, command=self.next_question)
        self.next_question_button.grid(column=0,row=5,pady=10)

        self.hide_options()
        self.hide_next_question()
        
    #After click continue to hide the entry and continue button and start the quiz 
    def hide_entry_and_start_quiz(self):
        self.label.grid_forget()
        self.name_entry.grid_forget()
        self.click_button.grid_forget()
        self.show_next_question()
        self.show_options()
        self.start_quiz()
    
    #To start the quiz after click continue
    def start_quiz(self):
        self.load_question()
        self.window.mainloop()
        
    
    def hide_options(self):
        for button in self.option_buttons:
            button.grid_forget()

    def show_options(self):
        for button in self.option_buttons:
            button.grid()

    def hide_next_question(self):
        self.next_question_button.grid_forget()

    def show_next_question(self):
        self.next_question_button.grid()

    #to load the question and options
    def load_question(self):
        question_data = self.quiz_data[self.current_question_index]
        self.question_label.config(text=question_data["question"])
        options = question_data["options"]
        for i in range(4):
            self.option_buttons[i].config(text=options[i])
    
    #to check the answer correct or not
    def check_answer(self, selected_option):
        question_data = self.quiz_data[self.current_question_index]
        correct_answer_index = question_data["correct_answer"]
        
        for button in self.option_buttons:
            button.config(bg="SystemButtonFace")
        self.option_buttons[selected_option].config(bg="light green")

        if selected_option == correct_answer_index:
            self.score += 1
        
            
    #to print the user score
    def next_question(self):
         
        for button in self.option_buttons:
            button.config(bg="SystemButtonFace")

        self.current_question_index += 1

        if self.current_question_index == (len(self.quiz_data)-1):
            self.next_question_button = tk.Button(self.window, text="Submit", width=30, command=self.next_question)
            self.next_question_button.grid(column=0,row=5,pady=10)

        if self.current_question_index == len(self.quiz_data):
            messagebox.showinfo("Quiz Over", f"Quiz finished. Your score: {self.score}/{len(self.quiz_data)} \n Thank you for playing {self.name_entry.get()}")
            self.window.quit()
        else:
            self.load_question()

quiz_app = QuizApp()
quiz_app.start_quiz()
