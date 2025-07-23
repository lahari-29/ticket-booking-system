from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# ---------- 1. Initialize the DB ----------
def init_db():
    conn = sqlite3.connect('booking.db')
    c = conn.cursor()
    # You can keep "event" as the column name instead of "movie"
    c.execute('''CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event TEXT,
                    seats INTEGER
                )''')
    conn.commit()
    conn.close()

init_db()

# ---------- 2. Welcome Page ----------
@app.route('/')
def welcome():
    return render_template('welcome.html')

# ---------- 3. Events Page ----------
@app.route('/events')
def events():
    events = [
        {"name": "Tech Conference", "image": "https://via.placeholder.com/300x200?text=Tech+Conference"},
        {"name": "Dance Show", "image": "https://via.placeholder.com/300x200?text=Dance+Show"},
        {"name": "Food Fest", "image": "https://via.placeholder.com/300x200?text=Food+Fest"}
    ]
    return render_template('events.html', events=events)

# ---------- 4. Booking Form Page ----------
@app.route('/book/<event_name>', methods=["GET", "POST"])
def book(event_name):
    if request.method == "POST":
        seats = int(request.form["seats"])
        conn = sqlite3.connect('booking.db')
        c = conn.cursor()
        c.execute("INSERT INTO bookings (event, seats) VALUES (?, ?)", (event_name, seats))
        conn.commit()
        conn.close()
        return redirect(url_for('show_bookings'))

    return render_template('bookings.html', event=event_name)

# ---------- 5. Show All Bookings ----------
@app.route('/show')
def show_bookings():
    conn = sqlite3.connect('booking.db')
    c = conn.cursor()
    c.execute("SELECT event, SUM(seats) FROM bookings GROUP BY event")
    data = c.fetchall()
    conn.close()
    return render_template('show.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
