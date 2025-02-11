import unittest
import subprocess
import os

class TestPlay(unittest.TestCase):
    def setUp(self) -> None:
        cmd = ["python", "main.py"]
        self.process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')

    def test_board_display_starts_right_and_its_white_pieces_turn(self):

        expected_starting_board = (
            "  a b c d e f g h\n" +
            "8 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n" +
            "7 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n" + 
            "6 ■ □ ■ □ ■ □ ■ □\n" + 
            "5 □ ■ □ ■ □ ■ □ ■\n" + 
            "4 ■ □ ■ □ ■ □ ■ □\n" +
            "3 □ ■ □ ■ □ ■ □ ■\n" + 
            "2 ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎\n" + 
            "1 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n"
        )
        expected_turn_message = "White plays: "

        out, _ = self.process.communicate()

        self.assertIn(expected_starting_board, out)
        self.assertIn(expected_turn_message, out)

    def test_board_display_does_not_change_and_new_message_appears___after_invalid_move(self):
        
        expected_board_after_invalid_pawn_move = (
            "  a b c d e f g h\n" +
            "8 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n" +
            "7 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n" + 
            "6 ■ □ ■ □ ■ □ ■ □\n" + 
            "5 □ ■ □ ■ □ ■ □ ■\n" + 
            "4 ■ □ ■ □ ■ □ ■ □\n" +
            "3 □ ■ □ ■ □ ■ □ ■\n" + 
            "2 ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎\n" + 
            "1 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n"
        )
        expected_turn_message = f"White plays: "
        expected_new_message_after_invalid_pawn_move = "The pawn does not move like that"

        invalid_pawn_move = "a2a2"
        self.process.stdin.write(invalid_pawn_move + os.linesep)
        self.process.stdin.flush()

        out, _ = self.process.communicate()

        self.assertIn(expected_board_after_invalid_pawn_move, out)
        self.assertIn(expected_turn_message, out)
        self.assertIn(expected_new_message_after_invalid_pawn_move, out)

    def test_board_display_is_updated_and_turns_are_switched_after___valid_move(self):

        expected_board_after_valid_pawn_move = (
            "  a b c d e f g h\n" +
            "8 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n" +
            "7 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n" + 
            "6 ■ □ ■ □ ■ □ ■ □\n" + 
            "5 □ ■ □ ■ □ ■ □ ■\n" + 
            "4 ■ □ ■ □ ■ □ ■ □\n" +
            "3 ♟︎ ■ □ ■ □ ■ □ ■\n" + 
            "2 ■ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎\n" + 
            "1 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n"
        )
        expected_turn_message_after_valid_pawn_move = "Black plays: "

        valid_pawn_move = "a2a3"
        self.process.stdin.write(valid_pawn_move + os.linesep)
        self.process.stdin.flush()

        out, _ = self.process.communicate()

        self.assertIn(expected_board_after_valid_pawn_move, out)
        self.assertIn(expected_turn_message_after_valid_pawn_move, out)

    def test_board_display_does_not_change_and_new_message_appears___after_white_trying_to_move_blacks_piece(self):

        expected_board_after_trying_to_move_others_piece = (
            "  a b c d e f g h\n" +
            "8 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n" +
            "7 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n" + 
            "6 ■ □ ■ □ ■ □ ■ □\n" + 
            "5 □ ■ □ ■ □ ■ □ ■\n" + 
            "4 ■ □ ■ □ ■ □ ■ □\n" +
            "3 □ ■ □ ■ □ ■ □ ■\n" + 
            "2 ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎\n" + 
            "1 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n"
        )
        expected_turn_message_after_trying_to_move_others_piece = f"White plays: "
        expected_new_message_after_trying_to_move_others_piece = "It's not black's turn yet"

        others_pawn_move = "a7a6"
        self.process.stdin.write(others_pawn_move + os.linesep)
        self.process.stdin.flush()

        out, _ = self.process.communicate()

        self.assertIn(expected_board_after_trying_to_move_others_piece, out)
        self.assertIn(expected_turn_message_after_trying_to_move_others_piece, out)
        self.assertIn(expected_new_message_after_trying_to_move_others_piece, out)

    def test_foolsmate(self):
        foolsmate = ["f2f3", "e7e6", "g2g4", "d8h4"]

        for move in foolsmate:
            self.process.stdin.write(move + os.linesep)
            self.process.stdin.flush()

        out, err = self.process.communicate()

        self.assertTrue("Checkmate!" in out)
    
    def test_basic_capture(self):
        basic_capture = ["b2b4", "a7a5", "b4a5"]

        for move in basic_capture:
            self.process.stdin.write(move + os.linesep)
            self.process.stdin.flush()

        out, _ = self.process.communicate()

        self.assertTrue("Black plays:" in out)

    def test_blocks_invalid_move(self):
        invalid_move = "b2b5"

        self.process.stdin.write(invalid_move + os.linesep)
        self.process.stdin.flush()

        out, _ = self.process.communicate()

        self.assertTrue("The pawn does not move like that" in out)
    
    def test_enforces_check(self):
        king_exposure = ["e2e4", "g7g5", "d1h5", "f7f6"]

        for move in king_exposure:
            self.process.stdin.write(move + os.linesep)
            self.process.stdin.flush()

        out, _ = self.process.communicate()

        self.assertTrue("You're in check" in out)