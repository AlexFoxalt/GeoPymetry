from models.triangles import EquilateralTriangle
from tests.utils import remove_input_prefixes

Model = EquilateralTriangle


def test_side():
    case = {
        "side": 55,
        "small_r": 0,
        "big_r": 0,
        "height": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side": 55,
        "small_r": 15.877,
        "big_r": 31.754,
        "height": 47.631,
        "square": 1309.863,
        "perimeter": 165,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_square():
    case = {
        "side": 0,
        "small_r": 0,
        "big_r": 0,
        "height": 0,
        "square": 111,
        "perimeter": 0,
    }
    expect = {
        "side": 16.011,
        "small_r": 4.622,
        "big_r": 9.244,
        "height": 13.866,
        "square": 111,
        "perimeter": 48.032,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_height():
    case = {
        "side": 0,
        "small_r": 0,
        "big_r": 0,
        "height": 1.01,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side": 1.166,
        "small_r": 0.337,
        "big_r": 0.673,
        "height": 1.01,
        "square": 0.589,
        "perimeter": 3.499,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_small_r():
    case = {
        "side": 0,
        "small_r": 66,
        "big_r": 0,
        "height": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side": 228.631,
        "small_r": 66,
        "big_r": 132,
        "height": 198,
        "square": 22634.44,
        "perimeter": 685.892,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_big_r():
    case = {
        "side": 0,
        "small_r": 0,
        "big_r": 0.99,
        "height": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side": 1.715,
        "small_r": 0.495,
        "big_r": 0.99,
        "height": 1.485,
        "square": 1.273,
        "perimeter": 5.144,
    }
    assert expect == remove_input_prefixes(Model(**case).process())
