import logging

def count_matching(condition, seq : list) -> int:
    """Returns the amount of items in seq that return true from condition"""

    if len(seq) > 0:

        if type(seq[0]) is tuple:

            return sum(1 for item in seq if condition == item[1])

    else:
        logging.Logger.error("List is empty")
        


    