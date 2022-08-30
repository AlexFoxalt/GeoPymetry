from models.triangles import RightTriangle
from tests.utils import remove_input_prefixes

Model = RightTriangle


def test_cathetus():
    case = {
        "cathetus_ab": 11,
        "cathetus_ac": 22,
        "hypotenuse_bc": 0,
        "small_r": 0,
        "big_r": 0,
        "height": 0,
        "median": 0,
        "angle_a": 0,
        "angle_b": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "cathetus_ab": 11,
        "cathetus_ac": 22,
        "hypotenuse_bc": 24.597,
        "small_r": 4.202,
        "big_r": 12.298,
        "height": 9.839,
        "median": 12.298,
        "angle_a": 63.435,
        "angle_b": 26.565,
        "square": 121,
        "perimeter": 57.597,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_ab_and_hypotenuse():
    case = {
        "cathetus_ab": 4,
        "cathetus_ac": 0,
        "hypotenuse_bc": 5,
        "small_r": 0,
        "big_r": 0,
        "height": 0,
        "median": 0,
        "angle_a": 0,
        "angle_b": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "cathetus_ab": 4,
        "cathetus_ac": 3,
        "hypotenuse_bc": 5,
        "small_r": 1,
        "big_r": 2.5,
        "height": 2.4,
        "median": 2.5,
        "angle_a": 36.87,
        "angle_b": 53.13,
        "square": 6,
        "perimeter": 12,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_ac_and_hypotenuse():
    case = {
        "cathetus_ab": 0,
        "cathetus_ac": 3,
        "hypotenuse_bc": 5,
        "small_r": 0,
        "big_r": 0,
        "height": 0,
        "median": 0,
        "angle_a": 0,
        "angle_b": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "cathetus_ab": 4,
        "cathetus_ac": 3,
        "hypotenuse_bc": 5,
        "small_r": 1,
        "big_r": 2.5,
        "height": 2.4,
        "median": 2.5,
        "angle_a": 36.87,
        "angle_b": 53.13,
        "square": 6,
        "perimeter": 12,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_ab_and_angle_b():
    case = {
        "cathetus_ab": 50,
        "cathetus_ac": 0,
        "hypotenuse_bc": 0,
        "small_r": 0,
        "big_r": 0,
        "height": 0,
        "median": 0,
        "angle_a": 0,
        "angle_b": 33,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "cathetus_ab": 50,
        "cathetus_ac": 76.993,
        "hypotenuse_bc": 91.804,
        "small_r": 17.595,
        "big_r": 45.902,
        "height": 41.934,
        "median": 45.902,
        "angle_a": 57,
        "angle_b": 33,
        "square": 1924.831,
        "perimeter": 218.797,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_ac_and_angle_b():
    case = {
        "cathetus_ab": 0,
        "cathetus_ac": 66.66,
        "hypotenuse_bc": 0,
        "small_r": 0,
        "big_r": 0,
        "height": 0,
        "median": 0,
        "angle_a": 0,
        "angle_b": 66.66,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "cathetus_ab": 154.486,
        "cathetus_ac": 66.66,
        "hypotenuse_bc": 168.254,
        "small_r": 26.446,
        "big_r": 84.127,
        "height": 61.205,
        "median": 84.127,
        "angle_a": 23.34,
        "angle_b": 66.66,
        "square": 5149.012,
        "perimeter": 389.4,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_ab_and_angle_a():
    case = {
        "cathetus_ab": 123,
        "cathetus_ac": 0,
        "hypotenuse_bc": 0,
        "small_r": 0,
        "big_r": 0,
        "height": 0,
        "median": 0,
        "angle_a": 80,
        "angle_b": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "cathetus_ab": 123,
        "cathetus_ac": 697.568,
        "hypotenuse_bc": 708.329,
        "small_r": 56.119,
        "big_r": 354.164,
        "height": 121.131,
        "median": 354.164,
        "angle_a": 80,
        "angle_b": 10,
        "square": 42900.411,
        "perimeter": 1528.896,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_ac_and_angle_a():
    case = {
        "cathetus_ab": 0,
        "cathetus_ac": 1.111,
        "hypotenuse_bc": 0,
        "small_r": 0,
        "big_r": 0,
        "height": 0,
        "median": 0,
        "angle_a": 33.33,
        "angle_b": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "cathetus_ab": 1.689,
        "cathetus_ac": 1.111,
        "hypotenuse_bc": 2.022,
        "small_r": 0.389,
        "big_r": 1.011,
        "height": 0.928,
        "median": 1.011,
        "angle_a": 33.33,
        "angle_b": 56.67,
        "square": 0.938,
        "perimeter": 4.822,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_hypotenuse_and_angle_b():
    case = {
        "cathetus_ab": 0,
        "cathetus_ac": 0,
        "hypotenuse_bc": 111,
        "small_r": 0,
        "big_r": 0,
        "height": 0,
        "median": 0,
        "angle_a": 0,
        "angle_b": 50,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "cathetus_ab": 85.031,
        "cathetus_ac": 71.349,
        "hypotenuse_bc": 111,
        "small_r": 22.69,
        "big_r": 55.5,
        "height": 54.657,
        "median": 55.5,
        "angle_a": 40,
        "angle_b": 50,
        "square": 3033.454,
        "perimeter": 267.38,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_hypotenuse_and_angle_a():
    case = {
        "cathetus_ab": 0,
        "cathetus_ac": 0,
        "hypotenuse_bc": 4,
        "small_r": 0,
        "big_r": 0,
        "height": 0,
        "median": 0,
        "angle_a": 5,
        "angle_b": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "cathetus_ab": 3.985,
        "cathetus_ac": 0.349,
        "hypotenuse_bc": 4,
        "small_r": 0.167,
        "big_r": 2,
        "height": 0.347,
        "median": 2,
        "angle_a": 5,
        "angle_b": 85,
        "square": 0.695,
        "perimeter": 8.333,
    }
    assert expect == remove_input_prefixes(Model(**case).process())
