from tkinter import *
import psycopg2


# Création d'une nouvelle fenêtre pour la création de quiz
root = Tk()
root.title("Application de Quiz")
root.geometry('480x320')
root.minsize(400,300)

create_quiz_window = Toplevel(root)
create_quiz_window.title("Création de Quiz")

# Champs de saisie pour la création de quiz
quiz_name_label = Label(create_quiz_window, text="Nom du Quiz")
quiz_name_label.pack()
quiz_name_entry = Entry(create_quiz_window)
quiz_name_entry.pack()

quiz_category_label = Label(create_quiz_window, text="Catégorie")
quiz_category_label.pack()
quiz_category_entry = Entry(create_quiz_window)
quiz_category_entry.pack()

quiz_difficulty_label = Label(create_quiz_window, text="Difficulté")
quiz_difficulty_label.pack()
quiz_difficulty_entry = Entry(create_quiz_window)
quiz_difficulty_entry.pack()
# Interface pour ajouter des questions
question_frame = Frame(create_quiz_window)
question_frame.pack()

question_label = Label(question_frame, text="Question")
question_label.pack()
question_text = Text(question_frame, height=5, width=40)
question_text.pack()

answer_label = Label(question_frame, text="Réponse")
answer_label.pack()
answer_text = Text(question_frame, height=5, width=40)
answer_text.pack()

def add_question():
    # Récupérez les données de la question et de la réponse
    question = question_text.get("1.0", "end-1c")
    answer = answer_text.get("1.0", "end-1c")

    # Ajoutez la question et la réponse à une liste ou à une structure de données appropriée
    # Vous pouvez également les afficher pour que l'enseignant les voit

    # Effacez les champs de saisie
    question_text.delete("1.0", "end")
    answer_text.delete("1.0", "end")

add_question_button = Button(question_frame, text="Ajouter Question", command=add_question)
add_question_button.pack()

def save_quiz():
    # Récupérez le nom, la catégorie, la difficulté et les questions du quiz
    quiz_name = quiz_name_entry.get()
    quiz_category = quiz_category_entry.get()
    quiz_difficulty = quiz_difficulty_entry.get()
    questions = []  # Liste des questions du quiz

    # Ajoutez le quiz à la base de données (table "quizzes")
    # Assurez-vous de récupérer l'ID de l'enseignant actuellement connecté

    # Ajoutez les questions à la base de données (table "questions")
    # Associez chaque question au quiz en utilisant l'ID du quiz

    # Effacez les champs de saisie et la liste des questions
    quiz_name_entry.delete(0, "end")
    quiz_category_entry.delete(0, "end")
    quiz_difficulty_entry.delete(0, "end")
    question_text.delete("1.0", "end")
    answer_text.delete("1.0", "end")
    questions.clear()

save_quiz_button = Button(create_quiz_window, text="Enregistrer Quiz", command=save_quiz)
save_quiz_button.pack()

root.mainloop()