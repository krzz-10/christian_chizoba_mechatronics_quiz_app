
# ==========================================
# PROJECT 3: MECHATRONICS QUIZ APP
# Author: Christian Chizoba
# Department: Mechatronics Engineering
# ==========================================

# A list containing all quiz questions and answers
questions = [
    {
        "question": "What does a sensor do in a mechatronic system?",
        "options": [
            "A. Produces electricity",
            "B. Detects physical changes",
            "C. Stores data",
            "D. Controls mechanical movement"
        ],
        "answer": 2
    },
    {
        "question": "Which component converts electrical energy into mechanical motion?",
        "options": [
            "A. Resistor",
            "B. Capacitor",
            "C. Actuator",
            "D. Diode"
        ],
        "answer": 3
    },
    {
        "question": "What is the full meaning of PWM?",
        "options": [
            "A. Pulse Width Modulation",
            "B. Power Wave Management",
            "C. Pulse Wire Measurement",
            "D. Power Width Mechanism"
        ],
        "answer": 1
    },
    {
        "question": "Which device measures temperature?",
        "options": [
            "A. Thermistor",
            "B. Relay",
            "C. Motor",
            "D. Transformer"
        ],
        "answer": 1
    },
    {
        "question": "What is the function of a microcontroller?",
        "options": [
            "A. To generate fuel",
            "B. To control electronic operations",
            "C. To increase friction",
            "D. To produce mechanical pressure"
        ],
        "answer": 2
    },
    {
        "question": "Which unit is used to measure electrical resistance?",
        "options": [
            "A. Volt",
            "B. Ampere",
            "C. Ohm",
            "D. Watt"
        ],
        "answer": 3
    },
    {
        "question": "What does an actuator do?",
        "options": [
            "A. Converts a control signal into physical action",
            "B. Measures resistance only",
            "C. Stores electrical charge",
            "D. Displays information"
        ],
        "answer": 1
    },
    {
        "question": "Which of these is an example of an input device?",
        "options": [
            "A. DC motor",
            "B. LED",
            "C. Temperature sensor",
            "D. Speaker"
        ],
        "answer": 3
    },
    {
        "question": "What is the unit of electrical power?",
        "options": [
            "A. Newton",
            "B. Watt",
            "C. Ohm",
            "D. Joule per second squared"
        ],
        "answer": 2
    },
    {
        "question": "Which system combines mechanical and electronic components?",
        "options": [
            "A. Hydraulic system only",
            "B. Mechanical system only",
            "C. Mechatronic system",
            "D. Chemical system"
        ],
        "answer": 3
    }
]


# Function to collect and validate the user's answer
def get_answer():
    while True:
        try:
            choice = int(input("Enter your answer (1-4): "))

            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice! Enter a number from 1 to 4.")

        except ValueError:
            print("Invalid input! Please enter a number.")


# Function to calculate percentage
def calculate_percentage(score, total):
    return (score / total) * 100


# Function to determine the student's grade
def get_grade(percentage):
    if percentage >= 80:
        return "A - Excellent!"
    elif percentage >= 70:
        return "B - Very Good!"
    elif percentage >= 60:
        return "C - Good!"
    elif percentage >= 50:
        return "D - Fair!"
    else:
        return "F - Keep Practising!"


# Main quiz function
def start_quiz():

    score = 0

    # Stores questions answered incorrectly
    wrong_answers = []

    print("\n================================")
    print("     MECHATRONICS QUIZ APP")
    print("================================")

    name = input("Enter your name: ")

    print("\nWelcome,", name)
    print("Answer the following 10 questions.")
    print("Choose an option from 1 to 4.\n")

    # Loop through every question
    for number, item in enumerate(questions, start=1):

        print("--------------------------------")
        print("Question", number)
        print(item["question"])

        # Display all four options
        for option in item["options"]:
            print(option)

        # Collect the user's answer
        user_answer = get_answer()

        # Check whether the answer is correct
        if user_answer == item["answer"]:

            print("Correct answer!")
            score += 1

        else:
            print("Wrong answer!")

            correct_option = item["options"][item["answer"] - 1]

            print("Correct answer:", correct_option)

            # Save incorrect questions for revision
            wrong_answers.append(item)

    # Calculate final results
    percentage = calculate_percentage(score, len(questions))
    grade = get_grade(percentage)

    print("\n================================")
    print("         QUIZ RESULTS")
    print("================================")

    print("Student Name:", name)
    print("Total Questions:", len(questions))
    print("Correct Answers:", score)
    print("Wrong Answers:", len(questions) - score)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)

    # Extra feature: Review incorrect answers
    print("\n======= REVISION SECTION =======")

    if len(wrong_answers) > 0:

        print("Questions you need to revise:")

        for item in wrong_answers:
            print("\n", item["question"])
            print("Correct answer:",
                  item["options"][item["answer"] - 1])

    else:
        print("Congratulations! You answered every question correctly.")

    print("\nThank you for using the Mechatronics Quiz App!")


# Run the application
start_quiz()
