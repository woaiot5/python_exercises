from turtle import Turtle


class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.board = Turtle(visible=False)
        self.board.penup()
        self.board.pencolor("white")

        # Load best score from file
        with open('best_score.txt', 'r') as file_score:
            self.best_score = int(file_score.readline())

        self.show_score(0)

    def show_score(self, add):
        self.board.clear()
        self.score += add
        self._display_score(-290, "Score: {}".format(self.score))
        self.check_best_score()
        self._display_score(285, "Best score: {}".format(self.best_score), align="right")

    def _display_score(self, x, text, align="left"):
        self.board.setpos(x, 273)
        self.board.write(text, align=align, font=('Arial', 20, 'bold'))

    def check_best_score(self):
        if self.score > self.best_score:
            self.best_score = self.score
            with open('best_score.txt', 'w') as file_score:
                file_score.write(str(self.best_score))

    def game_over(self):
        self.board.setpos(0, 0)
        self.board.write("GAME OVER", align="center", font=('Arial', 50, 'bold'))