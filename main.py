import spacy
from data import students, tutorials, staff
from art import logo


nlp = spacy.load("en_core_web_sm")


subject_words = ["math", "physics", "chemistry", "biology", "history", "english"]
grades_words = ["grade", "grades", "mark", "marks", "gpa"]
tutorial_words = ["tutorial", "reference", "tutorials", "references", "docs", "videos", "material",
                      "materials", "documents", "document", "video", "lecs", "lec", "lecture",
                      "lectures", "news", "announcements", "website", "link", "links", "guide",
                      "guidance"]
staff_words = ["staff", "doctor", "doctors", "teachers", "tutor", "teacher", "tutors", "contact",
                   "reach", "assist", "assistant", "instructor", "member", "members"]
student = {}

def print_gpa():
    print(f"Your Overall Gpa is {student['gpa']}")

def process_input(user_input):
    doc = nlp(user_input.lower())
    subjects = [token.text for token in doc if token.text in subject_words]
    grades = any(token.text for token in doc if token.text in grades_words)
    tutorials = any(token.text for token in doc if token.text in tutorial_words)
    staff_query = any(token.text for token in doc if token.text in staff_words)
    gpa_check = any(token.text for token in doc if token.text == "gpa")
    if gpa_check and len(subjects) == 0:
        print_gpa()
        return []
    else:
        return [subjects, grades, tutorials, staff_query]


def get_student():
    student_id = int(input("Please enter your Student ID: "))
    if student_id not in students:
        print("Invalid ID, please try again.")
        return get_student()
    else:
        return students[student_id]


def print_subjects(subjects, student):
    if not subjects:
        subjects = subject_words
    for subject in subjects:
        subject_name = subject.title()
        if subject_name in student['grades']:
            subject_info = student['grades'][subject_name]
            print(f"Your grade in {subject_name}: {subject_info['grade']} ({subject_info['mark']} / 100)")
            print(f"GPA for {subject_name}: {subject_info['gpa']}\n")
        else:
            print(f"Sorry, no grades available for {subject_name}.\n")

    if len(subjects) == 6:
        print(f"Your Overall Gpa is {student['gpa']}\n")


def print_tutorials(subjects):
    if not subjects:
        subjects = subject_words
    for subject in subjects:
        subject_name = subject.title()
        if subject_name in tutorials:
            print(f"Tutorials for {subject_name} can be found here: {tutorials[subject_name]}\n")
        else:
            print(f"No tutorials found for {subject_name}.\n")


def print_staff(subjects):
    if not subjects:
        subjects = subject_words
    for subject in subjects:
        subject_name = subject.title()
        if subject_name in staff:
            members = staff[subject_name]
            print(f"Doctor for {subject_name}: {members['Doctor']}")
            print(f"Teaching Assistant for {subject_name}: {members['Assistant']}\n")
        else:
            print(f"No staff information found for {subject_name}.\n")


def handle_multiple_inputs(grades, tutorials, staff_query):
    count = sum([grades, tutorials, staff_query])
    if count > 1:
        print("Please only request one thing at a time (grades, tutorials, or staff).")
        return False
    return True


#Program Starts Here...
print(logo)
print("Hello, I'm your personal college chatbot.")
print("I can help you with the following:\n"
      "1. Knowing Your grades, marks, gpa\n"
      "2. Getting tutorials for subjects\n"
      "3. Connecting you with teaching staff")
def chatbot():
    global student
    student = get_student()
    print(f"Hello {student['name']}, I'm your college assistant chatbot.")

    while True:
        user_input = input("How can I assist you today? ").lower()
        processed_input = process_input(user_input)
        if len(processed_input) == 0:
            cont = input("Do you need help with anything else? (yes/no): ").lower()
            if cont != "yes":
                print("Thank you for using our college chatbot. Have a great day!")
                break
            else:
                continue
        else:
            subjects = processed_input[0]
            check_grades = processed_input[1]
            check_tutorials = processed_input[2]
            check_staff = processed_input[3]


        if not handle_multiple_inputs(check_grades, check_tutorials, check_staff):
            continue

        if check_grades:
            print_subjects(subjects, student)
        elif check_tutorials:
            print_tutorials(subjects)
        elif check_staff:
            print_staff(subjects)
        else:
            print("Sorry, I didn't understand that. Please ask about grades, tutorials, or staff.")


        cont = input("Do you need help with anything else? (yes/no): ").lower()
        if cont != "yes":
            print("Thank you for using our college chatbot. Have a great day!")
            break



chatbot()
