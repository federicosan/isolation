"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random
import math

class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    ## finish this function!
    if game.is_loser(player):
            return float("-inf")

    if game.is_winner(player):
            return float("inf")
    my_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(1.5*my_moves - opp_moves)


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(my_moves - 1.5*opp_moves)


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
            return float("-inf")

    if game.is_winner(player):
            return float("inf")

    my_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(my_moves*my_moves-10*opp_moves)


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move





    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        player = game.active_player

        def is_terminal_state(thegame):
            """Implements the terminal state test function by checking if
            the for this it askes if the active player has any legal moves.

            Parameters
            -----------
            game: isolation.Board
                An instance of the Isolation game board class
                representing the current game state.

            Returns
            -------
            true if this board is a terminal state
            false if this board is not a terminal state.
            """
        #    if self.time_left() < self.TIMER_THRESHOLD:
        #        raise SearchTimeout()
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            return len(thegame.get_legal_moves(thegame.active_player)) == 0

        def result(thegame, action):
            """Returns the game state result for an action.

            Parameters
            -----------
            game: isolation.Board
                An instance of the Isolation game board class
                representing the current game state.

            action: a legal move

            Returns
            -------
            A copy of the board where the action has been played.
            """
        #    if self.time_left() < self.TIMER_THRESHOLD:
            #    raise SearchTimeout()
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            return thegame.forecast_move(action)

        def max_value(thegame, thedepth):
            """Implements the max-value function that
            checks all possible moves for the max player on
            a given state.

            Parameters
            -----------
            game: isolation.Board
                An instance of the Isolation game board class
                representing the current game state.

            depth: Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

            Returns
            -------
            The move with the maximum utility for max
            on a given game state.
            """
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

            if thedepth == 0 or is_terminal_state(thegame):
                return self.score(thegame, player)
                #return game.utility(player)
            v = -math.inf
            actions = thegame.get_legal_moves()
            #print(game.to_string())
            #print ("depth: {d} | legal moves:{a}".format(d=depth, a=actions))
            if not actions:
                return (-1, -1)
            for a in actions:
                v = max(v, min_value(result(thegame, a), thedepth-1))
            #print(game.to_string())
            return v

        def min_value(thegame, thedepth):
            """Implements the max-value function that
            checks all possible moves for the max player on
            a given state.

            Parameters
            -----------
            game: isolation.Board
                An instance of the Isolation game board class
                representing the current game state.

            depth: Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

            Returns
            -------
            The move with the maximum utility for max
            on a given game state.
            """
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

            if thedepth == 0 or is_terminal_state(thegame):
                return self.score(thegame, player)
                #return game.utility(player)
            v = math.inf
            actions = thegame.get_legal_moves()
            if not actions:
                return (-1, -1)
            for a in actions:
                v = min(v, max_value(result(thegame, a),thedepth-1))
            #print(game.to_string())
            return v

        argmax = lambda iterable, func: max(iterable, key=func)

        def argmax_f(keys, f):
            if len(keys) == 0:
                return (-1,-1)
            return max(keys, key=f)

        decision = argmax_f(game.get_legal_moves(), lambda a: min_value(result(game, a),depth-1))
        #print(decision)
        #print(game.to_string())
        return decision



class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            depthaux = 0
            found = None
            cutoff = 100
            for  depthaux in range(1, 1000000000000000):
                #print(depthaux)
                if self.time_left() < self.TIMER_THRESHOLD:
                    raise SearchTimeout()
                best_move = self.alphabeta(game, depthaux)
                if depthaux > cutoff:
                    return best_move

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def alphabeta(self, game, depth, alpha=-math.inf, beta=math.inf):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        player = game.active_player

        def is_terminal_state(thegame):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            return len(thegame.get_legal_moves()) == 0

        def result(thegame, theaction):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            return thegame.forecast_move(theaction)

        def max_value(thegame, thedepth, thealpha, thebeta):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            if thedepth == 0 or is_terminal_state(thegame):
                return self.score(thegame, player)
            v = -math.inf
            actions = thegame.get_legal_moves()
            if not actions:
                return (-1, -1)
            for a in actions:
                v = max(v, min_value(result(thegame, a),thedepth-1, thealpha, thebeta))
                if v>= thebeta:
                    return v
                thealpha = max(thealpha, v)
            return v

        def min_value(thegame, thedepth, thealpha, thebeta):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            if thedepth == 0 or is_terminal_state(thegame):
                return self.score(thegame, player)
            v = math.inf
            actions = thegame.get_legal_moves()
            if not actions:
                return (-1, -1)
            for a in actions:
                v = min(v, max_value(result(thegame, a),thedepth-1, thealpha, thebeta))
                if v<= thealpha:
                    return v
                thebeta = min(thebeta, v)
            return v

        #def argmax_f(keys, f):
        #    if len(keys) == 0:
        #        return (-1,-1)
        #    return max(keys, key=f)

        #decision = argmax_f(game.get_legal_moves(), lambda a: max_value(result(game, a),depth, alpha, beta))
        #print(decision)
        #print(game.to_string())
        decision = None
        thealpha = alpha
        thebeta = beta
        for a in game.get_legal_moves():
            v = min_value(result(game, a), depth-1, thealpha, thebeta)
            if v > thealpha:
                thealpha = v
                decision = a
        return decision
