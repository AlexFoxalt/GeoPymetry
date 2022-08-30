from models.quadrangles import Trapezoid
from tests.utils import remove_input_prefixes

Model = Trapezoid


def test_all_sides():
    case = {
        "side_ab": 3,
        "side_bc": 2,
        "side_cd": 4,
        "side_da": 4,
        "angle_a": 0,
        "angle_b": 0,
        "angle_c": 0,
        "angle_d": 0,
        "diag_1": 0,
        "diag_2": 0,
        "height": 0,
        "median": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 3,
        "side_bc": 2,
        "side_cd": 4,
        "side_da": 4,
        "angle_a": 75.522,
        "angle_b": 104.478,
        "angle_c": 133.433,
        "angle_d": 46.567,
        "diag_1": 5.568,
        "diag_2": 3.162,
        "height": 2.905,
        "median": 3,
        "square": 8.714,
        "perimeter": 13,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_bases_and_height():
    case = {
        "side_ab": 0,
        "side_bc": 15,
        "side_cd": 0,
        "side_da": 30,
        "angle_a": 0,
        "angle_b": 0,
        "angle_c": 0,
        "angle_d": 0,
        "diag_1": 0,
        "diag_2": 0,
        "height": 10,
        "median": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 12.5,
        "side_bc": 15,
        "side_cd": 12.5,
        "side_da": 30,
        "angle_a": 53.13,
        "angle_b": 126.87,
        "angle_c": 126.87,
        "angle_d": 53.13,
        "diag_1": 24.622,
        "diag_2": 24.622,
        "height": 10,
        "median": 22.5,
        "square": 225,
        "perimeter": 70,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_median_and_height():
    case = {
        "side_ab": 0,
        "side_bc": 0,
        "side_cd": 0,
        "side_da": 0,
        "angle_a": 0,
        "angle_b": 0,
        "angle_c": 0,
        "angle_d": 0,
        "diag_1": 0,
        "diag_2": 0,
        "height": 45,
        "median": 45,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 0,
        "side_bc": 0,
        "side_cd": 0,
        "side_da": 0,
        "angle_a": 0,
        "angle_b": 0,
        "angle_c": 0,
        "angle_d": 0,
        "diag_1": 63.64,
        "diag_2": 63.64,
        "height": 45,
        "median": 45,
        "square": 2025,
        "perimeter": 0,
    }
    assert expect == remove_input_prefixes(Model(**case).process())
