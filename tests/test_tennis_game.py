from hamcrest import assert_that, equal_to
from pytest import fixture
from src.tennis_game import TennisGame


@fixture(name="tennis_game")
def fixture_tennis_game() -> TennisGame:
    return TennisGame("player1", "player2")


def test_initial_score(tennis_game: TennisGame):
    score = tennis_game.score()

    assert_that(score, equal_to("Love-All"))


def test_player1_score_one_point(tennis_game: TennisGame):
    setPlayerScore(tennis_game, "player1", 1)

    score = tennis_game.score()

    assert_that(score, equal_to("Fifteen-Love"))


def test_player1_score_two_points(tennis_game: TennisGame):
    setPlayerScore(tennis_game, "player1", 2)

    score = tennis_game.score()

    assert_that(score, equal_to("Thirty-Love"))


def test_player1_score_three_points(tennis_game: TennisGame):
    setPlayerScore(tennis_game, "player1", 3)

    score = tennis_game.score()

    assert_that(score, equal_to("Forty-Love"))


def test_player1_wins_game(tennis_game: TennisGame):
    setPlayerScore(tennis_game, "player1", 4)

    score = tennis_game.score()

    assert_that(score, equal_to("Win for player1"))


def test_player2_score_one_point(tennis_game: TennisGame):
    setPlayerScore(tennis_game, "player2", 1)

    score = tennis_game.score()

    assert_that(score, equal_to("Love-Fifteen"))


def test_player2_score_two_points(tennis_game: TennisGame):
    setPlayerScore(tennis_game, "player2", 2)

    score = tennis_game.score()

    assert_that(score, equal_to("Love-Thirty"))


def test_player2_score_three_points(tennis_game: TennisGame):
    setPlayerScore(tennis_game, "player2", 3)

    score = tennis_game.score()

    assert_that(score, equal_to("Love-Forty"))


def test_player2_wins_game(tennis_game: TennisGame):
    setPlayerScore(tennis_game, "player2", 4)

    score = tennis_game.score()

    assert_that(score, equal_to("Win for player2"))


def test_both_players_score_one_point(tennis_game: TennisGame):
    setPlayerScore(tennis_game, "player1", 1)
    setPlayerScore(tennis_game, "player2", 1)

    score = tennis_game.score()

    assert_that(score, equal_to("Fifteen-All"))


def test_both_players_score_two_points(tennis_game: TennisGame):
    setPlayerScore(tennis_game, "player1", 2)
    setPlayerScore(tennis_game, "player2", 2)

    score = tennis_game.score()

    assert_that(score, equal_to("Thirty-All"))


def test_both_players_score_three_points(tennis_game: TennisGame):
    setPlayerScore(tennis_game, "player1", 3)
    setPlayerScore(tennis_game, "player2", 3)

    score = tennis_game.score()

    assert_that(score, equal_to("Deuce"))


def test_player1_advantage(tennis_game: TennisGame):
    setPlayerScore(tennis_game, "player1", 4)
    setPlayerScore(tennis_game, "player2", 3)

    score = tennis_game.score()

    assert_that(score, equal_to("Advantage player1"))


def test_player2_advantage(tennis_game: TennisGame):
    setPlayerScore(tennis_game, "player1", 3)
    setPlayerScore(tennis_game, "player2", 4)

    score = tennis_game.score()

    assert_that(score, equal_to("Advantage player2"))


def setPlayerScore(tennis_game: TennisGame, player: str, score: int):
    for _ in range(0, score):
        tennis_game.won_point(player)
