from time import sleep
from typing import Tuple
from src.pieces.Bishop import Bishop
from src.pieces.Knight import Knight
from src.pieces.Rook import Rook
from src.pieces.Queen import Queen
from src.Controller import Controller
from src.Position import Position
from src.util import cls, parse_move


class PlayerInterface:
    def __init__(self) -> None:
        self._controller = Controller()
        self._is_checkmate = False
        self._move_log = []

    def start(self) -> None:
        cls()
        print(self._controller.get_display(), '\n')
        while not self._is_checkmate:
            move = input(f"{str(self._controller._turn.name).title()} plays: ")
            position, target = parse_move(move)

            self._move(position, target)

            promotion_position = self._controller.is_promotion()
            if promotion_position != None:
                self._promote(promotion_position)

            self._is_checkmate = self._controller.is_checkmate()
            self._move_log += move
        
        self._checkmate()

    def _move(self, position, target) -> bool:
        try:
            self._controller.move(position, target)
            cls()
            print(self._controller.get_display(), '\n')
            return True
        except Exception as e:
            print(e, '\n')
            return False

    def _checkmate(self) -> None:
        cls()
        print(self._controller.get_display(), '\n')
        print("Checkmate!")
        sleep(5)

    def _promote(self, position: Position) -> None:
        cls()
        print(self._controller.get_display(), '\n')
        print("Promotion time!")
        while True:
            desired_piece = input("What should this pawn be promoted to?\n").lower()
            match desired_piece:
                case 'queen':
                    self._controller.promote(position, Queen)
                    break
                case 'bishop':
                    self._controller.promote(position, Bishop)
                    break
                case 'knight':
                    self._controller.promote(position, Knight)
                    break
                case 'rook':
                    self._controller.promote(position, Rook)
                    break
                case _:
                    print("Hmm, pretty sure that's not a piece. Let's do this again.")
        cls()
        print(self._controller.get_display(), '\n')
        print("There you go.\n")