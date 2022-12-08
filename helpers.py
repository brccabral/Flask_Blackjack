from functools import wraps
from flask import redirect, session
from random import randint


def game_required(f):
    """
    Decorate routes to require game.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("game_id") is None:
            return redirect("/newgame")
        return f(*args, **kwargs)

    return decorated_function


def new_deck():
    # clubs c, hearts h, diamonds d, spades s
    deck = {
        "ac": 0,
        "2c": 0,
        "3c": 0,
        "4c": 0,
        "5c": 0,
        "6c": 0,
        "7c": 0,
        "8c": 0,
        "9c": 0,
        "jc": 0,
        "qc": 0,
        "kc": 0,
        "ah": 0,
        "2h": 0,
        "3h": 0,
        "4h": 0,
        "5h": 0,
        "6h": 0,
        "7h": 0,
        "8h": 0,
        "9h": 0,
        "jh": 0,
        "qh": 0,
        "kh": 0,
        "ad": 0,
        "2d": 0,
        "3d": 0,
        "4d": 0,
        "5d": 0,
        "6d": 0,
        "7d": 0,
        "8d": 0,
        "9d": 0,
        "jd": 0,
        "qd": 0,
        "kd": 0,
        "as": 0,
        "2s": 0,
        "3s": 0,
        "4s": 0,
        "5s": 0,
        "6s": 0,
        "7s": 0,
        "8s": 0,
        "9s": 0,
        "js": 0,
        "qs": 0,
        "ks": 0,
    }
    return deck


def symbol_literal(symbol):
    if symbol == "2":
        return "two"
    elif symbol == "3":
        return "three"
    elif symbol == "4":
        return "four"
    elif symbol == "5":
        return "five"
    elif symbol == "6":
        return "six"
    elif symbol == "7":
        return "seven"
    elif symbol == "8":
        return "eight"
    elif symbol == "9":
        return "nine"
    return symbol


def new_card(deck, symbols, suits):
    while True:
        symbol = randint(0, len(symbols) - 1)
        suit = randint(0, len(suits) - 1)
        card = "{}{}".format(symbols[symbol], suits[suit])
        if not deck[card]:
            deck[card] = 1
            break

    return card


def get_hand_values(cards):
    symbols = []
    values = []
    for card in cards:
        symbol = card[0]
        symbols.append(symbol)
        if symbol in ["j", "q", "k"]:
            value = 10
        elif symbol == "a":
            value = 11
        else:
            value = int(symbol)
        values.append(value)

    if sum(values) > 21 and "a" in symbols:
        for i, s in enumerate(symbols):
            if s == "a":
                values[i] = 1

    return sum(values)
