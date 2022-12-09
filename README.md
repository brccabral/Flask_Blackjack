# Blackjack
#### Video Demo: https://youtu.be/REZ0wiZlz9g
#### Description:
Blackjack is a card game. There is one dealer and it can have many players, but for this project we will have only one player.

The objective is to sum the values of the card each player has and the player that is closer to 21 points wins.

The game starts with player receiving two cards facing upwards and the dealer gets one card upwards and one downwards, so the player don't know it when playing. While the player has less than 21 points (s)he can request for more cards by pressing "Hit", the dealer will give (s)he a new card to sum up the points. If the player goes over 21 point it is a "Bust" and the player loses. If the player doesn't want to receive any more cards, (s)he can say "Stand" and the points will be only from the cards (s)he currently have. When the players "Stand", the dealer has to take as many cards until the dealer has more points than the player or is busted.

So, the player wins by getting 21 points or when dealer is busted. The player loses when (s)he is busted or if the dealer gets more points than the player but still less than 21.

When there is a Win or a Lose, player can click on "New Game"

This project doesn't consider possibility of a tied game. In real game the dealer can stop at 21 and share the bet with other players with 21 points.

This project doesn't have bets.

In the background it is been considered a deck with 52 cards, which are 4 suits (diamonds, hearts, clubs, spades) and 13 symbols (A, 2 to 10, J, Q and K). In real game the suits and symbols are the same, but it can have more than 52 cards (by using more decks).

J, Q and K have value 10. A is first counted as 11, unless the player passes 21 points, which in this case A is reverted to 1 and the points are counted again and the player is not busted at this time. The player can continue to "Hit", subsequent A cards are still counted as 1, until the player is finally busted.

This is a Flask project, a framework in Python to provide dinamic web pages. All the game logic is in Python code.

In this project the cards are drawn using "random" functions and it doesn't repeat while in same round.

This project uses Javascript to send user command of "Hit" or "Stand".

The cards image is from GNOME cards game Aisleriot https://gitlab.gnome.org/GNOME/aisleriot . One image with all the cards is used, and through CSS the correct card is positioned in the page.
