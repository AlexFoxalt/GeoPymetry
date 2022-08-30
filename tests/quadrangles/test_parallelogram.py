from models.quadrangles import Parallelogram
from tests.utils import remove_input_prefixes

Model = Parallelogram


def test_sides_and_height():
    case = {
        "side_ab": 17,
        "side_bc": 25,
        "height": 15,
        "angle_x": 0,
        "angle_y": 0,
        "angle_a": 0,
        "angle_b": 0,
        "diag_1": 0,
        "diag_2": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 17,
        "side_bc": 25,
        "height": 15,
        "angle_x": 114.132,
        "angle_y": 65.868,
        "angle_a": 61.928,
        "angle_b": 118.072,
        "diag_1": 36.249,
        "diag_2": 22.672,
        "square": 375,
        "perimeter": 84,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_sides_and_angle_a():
    case = {
        "side_ab": 12,
        "side_bc": 13,
        "height": 0,
        "angle_x": 0,
        "angle_y": 0,
        "angle_a": 42,
        "angle_b": 0,
        "diag_1": 0,
        "diag_2": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 12,
        "side_bc": 13,
        "height": 8.03,
        "angle_x": 96.829,
        "angle_y": 83.171,
        "angle_a": 42,
        "angle_b": 138,
        "diag_1": 23.342,
        "diag_2": 9.008,
        "square": 104.384,
        "perimeter": 50,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_sides_and_angle_b():
    case = {
        "side_ab": 51,
        "side_bc": 122,
        "height": 0,
        "angle_x": 0,
        "angle_y": 0,
        "angle_a": 0,
        "angle_b": 68,
        "diag_1": 0,
        "diag_2": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 51,
        "side_bc": 122,
        "height": 47.286,
        "angle_x": 136.792,
        "angle_y": 43.208,
        "angle_a": 112,
        "angle_b": 68,
        "diag_1": 113.24,
        "diag_2": 148.817,
        "square": 5768.938,
        "perimeter": 346,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_diags_and_angle_y():
    case = {
        "side_ab": 0,
        "side_bc": 0,
        "height": 0,
        "angle_x": 0,
        "angle_y": 55,
        "angle_a": 0,
        "angle_b": 0,
        "diag_1": 25,
        "diag_2": 12.5,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 10.281,
        "side_bc": 16.88,
        "height": 7.583,
        "angle_x": 125,
        "angle_y": 55,
        "angle_a": 132.477,
        "angle_b": 47.523,
        "diag_1": 25,
        "diag_2": 12.5,
        "square": 127.993,
        "perimeter": 54.321,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_diags_and_angle_x():
    case = {
        "side_ab": 0,
        "side_bc": 0,
        "height": 0,
        "angle_x": 125,
        "angle_y": 0,
        "angle_a": 0,
        "angle_b": 0,
        "diag_1": 11,
        "diag_2": 22,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 9.047,
        "side_bc": 14.854,
        "height": 6.673,
        "angle_x": 125,
        "angle_y": 55,
        "angle_a": 47.523,
        "angle_b": 132.477,
        "diag_1": 11,
        "diag_2": 22,
        "square": 99.117,
        "perimeter": 47.803,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_diags_and_ab():
    case = {
        "side_ab": 20,
        "side_bc": 0,
        "height": 0,
        "angle_x": 0,
        "angle_y": 0,
        "angle_a": 0,
        "angle_b": 0,
        "diag_1": 40,
        "diag_2": 30,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 20,
        "side_bc": 29.155,
        "height": 19.078,
        "angle_x": 112.024,
        "angle_y": 67.976,
        "angle_a": 107.465,
        "angle_b": 72.535,
        "diag_1": 40,
        "diag_2": 30,
        "square": 556.215,
        "perimeter": 98.31,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_diags_and_bc():
    case = {
        "side_ab": 0,
        "side_bc": 60,
        "height": 0,
        "angle_x": 0,
        "angle_y": 0,
        "angle_a": 0,
        "angle_b": 0,
        "diag_1": 65,
        "diag_2": 64,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 23.675,
        "side_bc": 60,
        "height": 23.669,
        "angle_x": 136.941,
        "angle_y": 43.059,
        "angle_a": 91.301,
        "angle_b": 88.699,
        "diag_1": 65,
        "diag_2": 64,
        "square": 1420.127,
        "perimeter": 167.35,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_height_and_bc():
    case = {
        "side_ab": 0,
        "side_bc": 58,
        "height": 11,
        "angle_x": 0,
        "angle_y": 0,
        "angle_a": 0,
        "angle_b": 0,
        "diag_1": 0,
        "diag_2": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 0,
        "side_bc": 58,
        "height": 11,
        "angle_x": 0,
        "angle_y": 0,
        "angle_a": 0,
        "angle_b": 0,
        "diag_1": 0,
        "diag_2": 0,
        "square": 638,
        "perimeter": 0,
    }
    assert expect == remove_input_prefixes(Model(**case).process())
