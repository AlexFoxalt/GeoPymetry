from models.quadrangles import Rhombus
from tests.utils import remove_input_prefixes

Model = Rhombus


def test_side_ang_height():
    case = {
        "side": 17,
        "height": 15,
        "angle_a": 0,
        "angle_b": 0,
        "diag_1": 0,
        "diag_2": 0,
        "small_r": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side": 17,
        "height": 15,
        "angle_a": 61.928,
        "angle_b": 118.072,
        "diag_1": 29.155,
        "diag_2": 17.493,
        "small_r": 7.5,
        "square": 255,
        "perimeter": 68,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_square_ang_angle_a():
    case = {
        "side": 0,
        "height": 0,
        "angle_a": 30,
        "angle_b": 0,
        "diag_1": 0,
        "diag_2": 0,
        "small_r": 0,
        "square": 56,
        "perimeter": 0,
    }
    expect = {
        "side": 10.583,
        "height": 5.292,
        "angle_a": 30,
        "angle_b": 150,
        "diag_1": 20.445,
        "diag_2": 5.478,
        "small_r": 2.646,
        "square": 56,
        "perimeter": 42.332,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_square_ang_angle_b():
    case = {
        "side": 0,
        "height": 0,
        "angle_a": 0,
        "angle_b": 110,
        "diag_1": 0,
        "diag_2": 0,
        "small_r": 0,
        "square": 15,
        "perimeter": 0,
    }
    expect = {
        "side": 3.995,
        "height": 3.754,
        "angle_a": 70,
        "angle_b": 110,
        "diag_1": 6.546,
        "diag_2": 4.583,
        "small_r": 1.877,
        "square": 15,
        "perimeter": 15.981,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_square_ang_diag_1():
    case = {
        "side": 0,
        "height": 0,
        "angle_a": 0,
        "angle_b": 0,
        "diag_1": 11,
        "diag_2": 0,
        "small_r": 0,
        "square": 45,
        "perimeter": 0,
    }
    expect = {
        "side": 6.855,
        "height": 6.565,
        "angle_a": 73.284,
        "angle_b": 106.716,
        "diag_1": 11,
        "diag_2": 8.182,
        "small_r": 3.282,
        "square": 45,
        "perimeter": 27.418,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_square_ang_diag_2():
    case = {
        "side": 0,
        "height": 0,
        "angle_a": 0,
        "angle_b": 0,
        "diag_1": 0,
        "diag_2": 33,
        "small_r": 0,
        "square": 99,
        "perimeter": 0,
    }
    expect = {
        "side": 16.771,
        "height": 5.903,
        "angle_a": 20.61,
        "angle_b": 159.39,
        "diag_1": 6,
        "diag_2": 33,
        "small_r": 2.952,
        "square": 99,
        "perimeter": 67.082,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_side_ang_angle_a():
    case = {
        "side": 23,
        "height": 0,
        "angle_a": 11,
        "angle_b": 0,
        "diag_1": 0,
        "diag_2": 0,
        "small_r": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side": 23,
        "height": 4.389,
        "angle_a": 11,
        "angle_b": 169,
        "diag_1": 45.788,
        "diag_2": 4.409,
        "small_r": 2.194,
        "square": 100.938,
        "perimeter": 92,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_side_ang_angle_b():
    case = {
        "side": 34,
        "height": 0,
        "angle_a": 0,
        "angle_b": 34,
        "diag_1": 0,
        "diag_2": 0,
        "small_r": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side": 34,
        "height": 19.013,
        "angle_a": 146,
        "angle_b": 34,
        "diag_1": 19.881,
        "diag_2": 65.029,
        "small_r": 9.506,
        "square": 646.427,
        "perimeter": 136,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_diags():
    case = {
        "side": 0,
        "height": 0,
        "angle_a": 0,
        "angle_b": 0,
        "diag_1": 7,
        "diag_2": 9,
        "small_r": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side": 5.701,
        "height": 5.525,
        "angle_a": 75.75,
        "angle_b": 104.25,
        "diag_1": 7,
        "diag_2": 9,
        "small_r": 2.763,
        "square": 31.5,
        "perimeter": 22.804,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_square_and_side():
    case = {
        "side": 10,
        "height": 0,
        "angle_a": 0,
        "angle_b": 0,
        "diag_1": 0,
        "diag_2": 0,
        "small_r": 0,
        "square": 50,
        "perimeter": 0,
    }
    expect = {
        "side": 10,
        "height": 5,
        "angle_a": 30,
        "angle_b": 150,
        "diag_1": 19.319,
        "diag_2": 5.176,
        "small_r": 2.5,
        "square": 50,
        "perimeter": 40,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_diag_1_and_side():
    case = {
        "side": 75,
        "height": 0,
        "angle_a": 0,
        "angle_b": 0,
        "diag_1": 50,
        "diag_2": 0,
        "small_r": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side": 75,
        "height": 47.14,
        "angle_a": 141.058,
        "angle_b": 38.942,
        "diag_1": 50,
        "diag_2": 141.421,
        "small_r": 23.57,
        "square": 3535.534,
        "perimeter": 300,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_diag_2_and_side():
    case = {
        "side": 25,
        "height": 0,
        "angle_a": 0,
        "angle_b": 0,
        "diag_1": 0,
        "diag_2": 32,
        "small_r": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side": 25,
        "height": 24.588,
        "angle_a": 79.584,
        "angle_b": 100.416,
        "diag_1": 38.419,
        "diag_2": 32,
        "small_r": 12.294,
        "square": 614.7,
        "perimeter": 100,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_small_r_and_side():
    case = {
        "side": 25,
        "height": 0,
        "angle_a": 0,
        "angle_b": 0,
        "diag_1": 0,
        "diag_2": 0,
        "small_r": 12.294,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side": 25,
        "height": 24.588,
        "angle_a": 79.584,
        "angle_b": 100.416,
        "diag_1": 38.419,
        "diag_2": 32,
        "small_r": 12.294,
        "square": 614.7,
        "perimeter": 100,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_small_r_and_angle_a():
    case = {
        "side": 0,
        "height": 0,
        "angle_a": 66,
        "angle_b": 0,
        "diag_1": 0,
        "diag_2": 0,
        "small_r": 15,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side": 32.839,
        "height": 30,
        "angle_a": 66,
        "angle_b": 114,
        "diag_1": 55.082,
        "diag_2": 35.771,
        "small_r": 15,
        "square": 985.173,
        "perimeter": 131.356,
    }
    assert expect == remove_input_prefixes(Model(**case).process())
