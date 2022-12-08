from random import randint
from flask import Flask, session, render_template, redirect, request
from flask_session import Session
from helpers import game_required, new_deck, new_card, symbol_literal, get_hand_values

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["symbol_literal"] = symbol_literal

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

symbols = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "j", "q", "k"]
suits = ["c", "h", "d", "s"]


@app.route("/", methods=["GET", "POST"])
@game_required
def index():
    if request.method == "POST":
        command = request.form.get("command")
        if command == "hit":
            session["player"].append(new_card(session["deck"], symbols, suits))
        elif command == "stand":
            session["turn"] = "dealer"

    if not session["player"]:
        session["player"].append(new_card(session["deck"], symbols, suits))
        session["player"].append(new_card(session["deck"], symbols, suits))
    if not session["dealer"]:
        session["dealer"].append(new_card(session["deck"], symbols, suits))
        session["dealer"].append(new_card(session["deck"], symbols, suits))

    player_value = get_hand_values(session["player"])
    if player_value == 21:
        session["turn"] = "win"
    elif player_value > 21:
        session["turn"] = "lose"

    dealer_value = get_hand_values(session["dealer"])
    if session["turn"] == "dealer":
        while dealer_value <= player_value and dealer_value < 21:
            session["dealer"].append(new_card(session["deck"], symbols, suits))
            dealer_value = get_hand_values(session["dealer"])
        if dealer_value == 21:
            session["turn"] = "lose"
        elif dealer_value > 21:
            session["turn"] = "win"
        elif dealer_value > player_value:
            session["turn"] = "lose"

    print(session["turn"], player_value, dealer_value)

    return render_template(
        "index.html",
        player=session["player"],
        dealer=session["dealer"],
        turn=session["turn"],
    )


@app.route("/newgame")
def newgame():
    """New game - clear session"""

    # Forget any user_id
    session.clear()

    session["game_id"] = randint(0, 1000)
    session["deck"] = new_deck()
    session["player"] = []
    session["dealer"] = []
    session["turn"] = "player"

    # Redirect user to login form
    return redirect("/")
