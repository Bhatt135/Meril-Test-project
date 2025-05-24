from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/candidates', methods=['GET'])
def get_candidates():
    conn = sqlite3.connect("candidates.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, phone FROM candidates")
    rows = cursor.fetchall()
    conn.close()

    candidates = [
        {"id": r[0], "name": r[1], "email": r[2], "phone": r[3]}
        for r in rows
    ]
    return jsonify(candidates)

if __name__ == '__main__':
    app.run(debug=True)
