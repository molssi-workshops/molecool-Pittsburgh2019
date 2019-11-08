"""
Unit testing for the measure module.
"""

import numpy as np
import pytest

import molecool

def test_calculate_distance():

    r1 = np.array([0, 0, 0])
    r2 = np.array([0.1, 0, 0])

    expected_distance = 0.1

    calculated_distance = molecool.calculate_distance(r1, r2)

    expected_distance == calculated_distance

"""
Write a test for the calculate_angle function

Use the points

r1 = np.array([0, 0, -1])
r2 = np.array([0, 0, 0])
r3 = np.array([1, 0, 0])

Angle should be 90 degrees
"""
def test_calculate_angle():
    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 0, 0])
    r3 = np.array([1, 0, 0])

    expected_angle = 90

    calculated_angle = molecool.calculate_angle(r1, r2, r3, degrees=True)

    assert expected_angle == calculated_angle

@pytest.mark.parametrize("p1, p2, p3, expected_angle",[
        (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0,0,0]), np.array([1, 0, 0]), 45),
        (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60),
        (np.array([np.sqrt(3)/2, (1./2.), 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 30)
])
def test_calculate_angle_many(p1, p2, p3, expected_angle):

    calculated_angle = molecool.calculate_angle(p1, p2, p3, degrees=True)

    assert calculated_angle == pytest.approx(expected_angle)


def test_calculate_distanc_failure():

    r1 = [0, 0, 0]
    r2 = [0.1, 0, 0]

    expected_distance = 0.1

    with pytest.raises(TypeError):
        calculated_distance = molecool.calculate_distance(r1, r2)
