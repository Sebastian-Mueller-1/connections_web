from flask import Flask, render_template
from discord_bot import run_discord_bot

app = Flask(__name__)

@app.route('/')
def home():
    # Extracting the streaks by running the function from discord_bot.py
    group_streak, seb_streak, joey_streak, ryan_streak = run_discord_bot()
    
    # Passing the values to the template
    return render_template('index.html',
                           group_streak=group_streak,
                           seb_streak=seb_streak,
                           joey_streak=joey_streak,
                           ryan_streak=ryan_streak)

if __name__ == "__main__":
    app.run(debug=True)
