from tkinter import *
import psycopg2
# import webbrowser
# def open_graven_chanel
# window = Tk()
# window.title('My application')
# window.geometry('1080x720')
# window.minsize(480,360)
# window.config(background='green')
# frame = Frame(window, bg='green')
# label_title = Label(frame, text= 'Bienvenue sur l"application', font=('Courrier', 40), bg='green', fg='white')
# label_title.pack(expand=YES)
# label_sutitle = Label(frame, text= 'Hey Salut a tous c samuel', font=('Courrier', 25), bg='green', fg='white')
# label_sutitle.pack(expand=YES)
# yt_button = Button(frame, text='Ouvrir Youtube', font=("Courrier", 25), bg='white', fg='green')
# yt_button.pack(pady=25, fill=X)
# frame.pack(expand=YES)
# window.mainloop()

db_config = {
    "host": "localhost",      
    "database": "quizz_student",    
    "user": "postgres",      
    "password": "Sam159753",   
    "port" : "5432"
}


registration = Tk()
registration.title("Application de Quiz")
registration.geometry('480x320')
registration.minsize(400,300)
# Formulaire d'inscription pour les étudiants
student_registration_frame = Frame(registration)
student_registration_frame.pack(pady=20, padx=100, fill=X)

student_username_label = Label(student_registration_frame, text="Nom d'utilisateur")
student_username_label.pack()
student_username_entry = Entry(student_registration_frame)
student_username_entry.pack(fill=X)

student_password_label = Label(student_registration_frame, text="Mot de passe")
student_password_label.pack()
student_password_entry = Entry(student_registration_frame, show="*")  # Masquer le mot de passe
student_password_entry.pack()

student_first_name_label = Label(student_registration_frame, text="Prenom")
student_first_name_label.pack()
student_first_name_entry = Entry(student_registration_frame)
student_first_name_entry.pack()

student_lastname_label = Label(student_registration_frame, text="Nom")
student_lastname_label.pack()
student_lastname_entry = Entry(student_registration_frame)
student_lastname_entry.pack()

student_email_label = Label(student_registration_frame, text="E-mail")
student_email_label.pack()
student_email_entry = Entry(student_registration_frame)
student_email_entry.pack()

student_register_button = Button(student_registration_frame, text="S'inscrire")
student_register_button.pack(pady=25)



def register_student():
    username = student_username_entry.get()
    password = student_password_entry.get()
    first_name = student_first_name_entry.get()
    last_name = student_lastname_entry.get()
    email = student_email_entry.get()

    # Connexion à la base de données
    conn = psycopg2.connect(**db_config)
    # Création d'un curseur
    cur = conn.cursor()

    # Insertion des données de l'étudiant dans la table "students"
    cur.execute("INSERT INTO students (username, password, first_name, last_name, email) VALUES (%s, %s, %s, %s, %s)",
                (username, password, first_name, last_name, email))

    # Valider la transaction
    conn.commit()

    # Fermer la connexion à la base de données
    conn.close()

student_register_button.config(command=register_student, COMMAND = quit)



registration.mainloop()

