from models.triangles import ArbitraryTriangle
from tests.utils import remove_input_prefixes

Model = ArbitraryTriangle


def test_all_sides():
    case = {
        "side_ab": 2,
        "side_ac": 3,
        "side_bc": 4,
        "square": 0,
        "small_r": 0,
        "big_r": 0,
        "height": 0,
        "perimeter": 0,
        "median": 0,
        "angle_a": 0,
        "angle_b": 0,
        "angle_c": 0,
    }
    expect = {
        "side_ab": 2,
        "side_ac": 3,
        "side_bc": 4,
        "square": 2.905,
        "small_r": 0.645,
        "big_r": 2.066,
        "height": 1.936,
        "perimeter": 9,
        "median": 2.784,
        "angle_a": 104.478,
        "angle_b": 46.567,
        "angle_c": 28.955,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_two_angles_and_ac():
    case = {
        "side_ab": 0,
        "side_ac": 6,
        "side_bc": 0,
        "square": 0,
        "small_r": 0,
        "big_r": 0,
        "height": 0,
        "perimeter": 0,
        "median": 0,
        "angle_a": 45,
        "angle_b": 55,
        "angle_c": 0,
    }
    expect = {
        "side_ab": 7.213,
        "side_ac": 6,
        "side_bc": 5.179,
        "square": 15.302,
        "small_r": 1.664,
        "big_r": 3.662,
        "height": 5.101,
        "perimeter": 18.393,
        "median": 5.516,
        "angle_a": 45,
        "angle_b": 55,
        "angle_c": 80,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_two_angles_and_ab():
    case = {
        "side_ab": 4,
        "side_ac": 0,
        "side_bc": 0,
        "square": 0,
        "small_r": 0,
        "big_r": 0,
        "height": 0,
        "perimeter": 0,
        "median": 0,
        "angle_a": 100,
        "angle_b": 30,
        "angle_c": 0,
    }
    expect = {
        "side_ab": 4,
        "side_ac": 2.611,
        "side_bc": 5.142,
        "square": 5.142,
        "small_r": 0.875,
        "big_r": 2.611,
        "height": 3.939,
        "perimeter": 11.753,
        "median": 4.418,
        "angle_a": 100,
        "angle_b": 30,
        "angle_c": 50,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_two_sides_and_angle():
    case = {
        "side_ab": 11,
        "side_ac": 20,
        "side_bc": 0,
        "square": 0,
        "small_r": 0,
        "big_r": 0,
        "height": 0,
        "perimeter": 0,
        "median": 0,
        "angle_a": 33,
        "angle_b": 0,
        "angle_c": 0,
    }
    expect = {
        "side_ab": 11,
        "side_ac": 20,
        "side_bc": 12.328,
        "square": 59.91,
        "small_r": 2.765,
        "big_r": 11.318,
        "height": 5.991,
        "perimeter": 43.328,
        "median": 6.041,
        "angle_a": 33,
        "angle_b": 117.925,
        "angle_c": 29.075,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_base_and_height():
    case = {
        "side_ab": 0,
        "side_ac": 11.11,
        "side_bc": 0,
        "square": 0,
        "small_r": 0,
        "big_r": 0,
        "height": 66.66,
        "perimeter": 0,
        "median": 0,
        "angle_a": 0,
        "angle_b": 0,
        "angle_c": 0,
    }
    expect = {
        "side_ab": 0,
        "side_ac": 11.11,
        "side_bc": 0,
        "square": 370.296,
        "small_r": 0,
        "big_r": 0,
        "height": 66.66,
        "perimeter": 0,
        "median": 0,
        "angle_a": 0,
        "angle_b": 0,
        "angle_c": 0,
    }
    assert expect == remove_input_prefixes(Model(**case).process())
