class PlayerError:
    INSUFFICIENT_FUNDS = 4001
    ROUND_FINISHED = 4002
    PLAYER_BUSTED = 4003
    INVALID_GAME_STATE = 4004

class GameError:
    GAME_ALREADY_CREATED = 4101
    GAME_FULL = 4102
    NOT_HEAD_OF_GAME = 4103
    NOT_ENOUGH_PLAYERS = 4104
    GAME_NOT_STARTED = 4105
    INVALID_PLAYER_ID = 4106
    INVALID_GAME_ID = 4107
