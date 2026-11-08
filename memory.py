import sqlite3

def connect_memory():
    connection = sqlite3.connect("vanta_memory.db")
    return connection
def create_memory_table():
    connection = connect_memory()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            content TEXT NOT NULL,
             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    connection.close()


def save_memory(category, content):
        connection = connect_memory()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO memories (category, content) VALUES (?, ?)", (category, content))
        connection.commit()
        connection.close()


def load_memories():
    connection = connect_memory()
    cursor = connection.cursor()
    cursor.execute("SELECT category, content, created_at FROM memories ORDER BY id")
    memories = cursor.fetchall()
    connection.close()
    return memories
def delete_memory(memory_id):
    connection = connect_memory()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM memories WHERE id = ?",
        (memory_id,)
    )

    deleted_count = cursor.rowcount
    connection.commit()
    connection.close()

    return deleted_count > 0
def list_memories():
    connection = connect_memory()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, category, content FROM memories ORDER BY id"
    )

    memories = cursor.fetchall()
    connection.close()

    return memories