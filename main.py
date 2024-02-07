import tkinter as tk
import random
import time

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"

class CardGame:
    def __init__(self, root):
        # Constructor for the CardGame class
        self.root = root
        self.root.title("Card Game")
        self.root.configure(bg="#2E8B57")

        # Labels and Canvas for GUI
        self.label = tk.Label(self.root, text="Card Game", font=("Helvetica", 20), bg="#2E8B57", fg="white")
        self.label.pack()

        self.canvas = tk.Canvas(self.root, width=800, height=400, bg="#006400", highlightthickness=0)
        self.canvas.pack()

        # Result and Score Labels
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16), bg="#2E8B57", fg="white")
        self.result_label.pack()

        self.score_label = tk.Label(self.root, text="Scores: Player 1 - 0 | Player 2 - 0", font=("Helvetica", 14), bg="#2E8B57", fg="white")
        self.score_label.pack()

        # Scores for players
        self.player1_score = 0
        self.player2_score = 0

        # Deck of cards
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                       '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
        self.deck = [Card(value, suit) for suit in self.suits for value in self.values]

    def shuffle_animation(self):
        # Animation for shuffling the deck
        self.canvas.delete("all")
        shuffle_text = self.canvas.create_text(400, 200, text="Shuffling Deck...", fill="white", font=("Helvetica", 18))

        for _ in range(20):
            random.shuffle(self.deck)
            self.canvas.update()
            time.sleep(0.1)

        self.canvas.delete(shuffle_text)
#mark
    def draw_cards(self):
        # Method to draw cards and determine the winner
        self.shuffle_animation()

        self.canvas.delete("all")
        player1_card = random.choice(self.deck)
        player2_card = random.choice(self.deck)

        for i in range(10):
            self.canvas.delete("card_animation")
            random_x = random.randint(100, 300)
            random_y = random.randint(100, 200)

            card1 = self.canvas.create_text(random_x, random_y, text=f"{player1_card.value} of {player1_card.suit}",
                                            fill="white", font=("Helvetica", 14), tags="card_animation")
            card2 = self.canvas.create_text(random_x + 400, random_y, text=f"{player2_card.value} of {player2_card.suit}",
                                            fill="white", font=("Helvetica", 14), tags="card_animation")

            self.canvas.update()
            time.sleep(0.1)

        self.canvas.delete("card_animation")
        self.canvas.create_text(200, 200, text=f"{player1_card.value} of {player1_card.suit}",
                                fill="white", font=("Helvetica", 14))
        self.canvas.create_text(600, 200, text=f"{player2_card.value} of {player2_card.suit}",
                                fill="white", font=("Helvetica", 14))

        if self.values[player1_card.value] > self.values[player2_card.value]:
            self.result_label.config(text="Player 1 wins!", fg="yellow")
            self.player1_score += 1
        elif self.values[player1_card.value] < self.values[player2_card.value]:
            self.result_label.config(text="Player 2 wins!", fg="yellow")
            self.player2_score += 1
        else:
            self.result_label.config(text="It's a tie!", fg="yellow")

        self.score_label.config(text=f"Scores: Player 1 - {self.player1_score} | Player 2 - {self.player2_score}")

def main():
    root = tk.Tk()
    card_game = CardGame(root)

    draw_button = tk.Button(root, text="Draw Cards", font=("Helvetica", 16), command=card_game.draw_cards, bg="#8B4513", fg="white")
    draw_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
