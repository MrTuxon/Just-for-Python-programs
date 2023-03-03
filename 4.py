# Program to create a quiz

# Create a list of questions and answers
questions = [
    {
        "вопрос": "Какая столица Индии?",
             "ответ": "Нью-Дели"
    },
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    }
]

# Ask the user the questions
for question in questions:
    user_answer = input(question["question"] + ": ")
    if user_answer == question["answer"]:
        print("Yes! You got it right!")
    else:
        print("Sorry, the answer is " + question["answer"])