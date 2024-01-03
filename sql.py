import sqlite3

# Fonction pour créer la base de données et les tables
def create_database():
    # Connexion à la base de données (si elle n'existe pas, elle sera créée)
    conn = sqlite3.connect('chatbot_database.db')
    cursor = conn.cursor()

    # Création de la table users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id_user INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Création de la table conversation
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversation (
            id_conversation INTEGER PRIMARY KEY AUTOINCREMENT,
            id_user INTEGER,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            FOREIGN KEY (id_user) REFERENCES users(id_user)
        )
    ''')

    # Commit et fermeture de la connexion
    conn.commit()
    conn.close()

# Appeler la fonction pour créer la base de données
create_database()
