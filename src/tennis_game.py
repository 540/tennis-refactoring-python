class TennisGame:
    def __init__(self, player1_name: str, player2_name: str):
        self.__player1_name: str = player1_name
        self.__player2_name: str = player2_name
        self.__player1_points: int = 0
        self.__player2_points: int = 0

    def won_point(self, player_name: str):
        if player_name == self.__player1_name:
            self.__player1_points += 1
        elif player_name == self.__player2_name:
            self.__player2_points += 1
        else:
            raise ValueError("User not found")

    def score(self) -> str:
        if self.__is_tie():
            tie_scores: list[str] = ["Love-All", "Fifteen-All", "Thirty-All"]
            return (
                "Deuce"
                if self.__player1_points > 2
                else tie_scores[self.__player1_points]
            )

        if self.__any_player_has_advantage():
            return (
                "Advantage player1"
                if self.__player1_points_are_greater_than_player2_points()
                else "Advantage player2"
            )

        if self.__any_player_wins():
            return (
                "Win for player1"
                if self.__player1_points_are_greater_than_player2_points()
                else "Win for player2"
            )

        scores: list[str] = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{scores[self.__player1_points]}-{scores[self.__player2_points]}"

    def __player1_points_are_greater_than_player2_points(self) -> bool:
        return self.__player1_points > self.__player2_points

    def __is_tie(self) -> bool:
        return self.__player1_points == self.__player2_points

    def __any_player_has_advantage(self) -> bool:
        return (
            self.__any_player_has_at_least_four_points()
            and abs(self.__player1_points - self.__player2_points) == 1
        )

    def __any_player_wins(self) -> bool:
        return (
            self.__any_player_has_at_least_four_points()
            and abs(self.__player1_points - self.__player2_points) > 1
        )

    def __any_player_has_at_least_four_points(self) -> bool:
        return self.__player1_points >= 4 or self.__player2_points >= 4
