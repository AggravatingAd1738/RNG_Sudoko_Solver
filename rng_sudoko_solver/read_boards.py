"""
Functions for reading sudoko boards.

Boards should be given as a file path. The functions should take the
file path, load the board and return it as a numpy array.

The board should be checked if its valid before its returned.
"""
import pandas


def validate_board(board):
    """ Validates a numpy suduko board. """
    # Check dimensions.
    valid_dimensions = ((9, 9))
    shape = board.shape
    if shape not in valid_dimensions:
        raise ValueError(f"Board shape ({shape}) not a valid shape.")
    
    # Check for valid data type.
    

def load_csv_board(file_path):
    """ Load CSV sudoko boards. """
    board = pd.read_csv(
        file_path,
        header=None,
        index_col=False,
        skipinitialspace=True
    )
    board = board.to_numpy(dtype=np.uint8)
    validate_board(board)
