import numpy as np

def calculate_distance(rA, rB):
    """
    This function calculates the distance between two points.

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between two points.

    Examples
    --------
    >>> r1 = np.array([0, 0, 0])
    >>> r2 = np.array([3.0, 0, 0])
    >>> calculate_distance(r1, r2)
    3.0
    """

    dist_vec = (rA - rB)
    distance = np.linalg.norm(dist_vec)
    return distance

def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
