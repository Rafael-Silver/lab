import sqlite3
from pathlib import Path

caminho=str(Path(__file__).absolute())
caminho_completo=str(caminho[:-8])

banco_c=(caminho_completo+'cadastro.db')


def connect():
    conn = sqlite3.connect(banco_c)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS alunos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        endereco TEXT,
                        email TEXT,
                        campus TEXT,
                        periodo TEXT,
                        av1 TEXT,
                        av2 TEXT,
                        av3 TEXT,
                        avd TEXT,
                        avds TEXT)""")
    conn.commit()
    conn.close()

def insert(nome, endereco, email, campus, periodo, av1, av2, av3, avd, avds):
    conn = sqlite3.connect(banco_c)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO alunos VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    (nome, endereco, email, campus, periodo, av1, av2, av3, avd, avds))
    conn.commit()
    conn.close()

def update(id, nome, endereco, email, campus, periodo, av1, av2, av3, avd, avds):
    conn = sqlite3.connect(banco_c)
    cursor = conn.cursor()
    cursor.execute('UPDATE alunos SET nome=?, endereco=?, email=?, campus=?, periodo=?, av1=?, av2=?, av3=?, avd=?, avds=? WHERE id=?',
                   (nome, endereco, email, campus, periodo, av1, av2, av3, avd, avds, id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect(banco_c)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM alunos WHERE id = ?' ,(id,))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect(banco_c)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alunos')
    linhas = cursor.fetchall()
    conn.close()
    return linhas

connect()