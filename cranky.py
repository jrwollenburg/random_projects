import numpy as np

""" CURRENTLY ONLY WORKS ON CLEAN DATA. THERE'S AN EDGE CASE WHERE IF EACH SUCCESSIVE POINT IS WITHIN THE TOLERANCE,
IT WILL BE CONSIDERED A PLATEAU. NEED TO FIX. TOLERANCE IS HARDCODED. NEED TO EITHER DETERMINE A VALID HARDCODED
TOLERANCE OR MAKE IT DYNAMIC. """


def average_of_highest_plateau(data, tol, min_length=4):
    """
    Find the average value of each plateau in a list of data. A plateau is 5 or more consecutive points within a
    tolerance of tol.
    :param data: list of data
    :param tol: tolerance for a plateau
    :param min_length: minimum length of a plateau - default is 5. Using for debugging purposes, don't change.
    """
    # Convert the list to a numpy array for easier manipulation
    data_array = np.array(data)

    # Calculate the slope between consecutive points
    differences = np.diff(data_array)

    # Identify the start and end indices of plateaus
    plateau_indices = np.where(np.abs(differences) < tol)[0]
    plateau_starts = np.split(plateau_indices, np.where(np.diff(plateau_indices) != 1)[0] + 1)
    # Calculate the average value within each plateau
    plateau_averages = [np.mean(data_array[start[0]:start[-1] + 2]) for start in plateau_starts if
                        len(start) >= min_length]

    return max(plateau_averages)


baby_test = [1, 2, 3, 4, 3, 2, 1]
print(average_of_highest_plateau(baby_test, 2))
