from models.quadrangles import Rectangle
from tests.utils import remove_input_prefixes

Model = Rectangle


def test_sides():
    case = {
        "side_ab": 10,
        "side_bc": 20,
        "angle_x": 0,
        "angle_y": 0,
        "diag": 0,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 10,
        "side_bc": 20,
        "angle_x": 126.87,
        "angle_y": 53.13,
        "diag": 22.361,
        "square": 200,
        "perimeter": 60,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_ab_and_square():
    case = {
        "side_ab": 3,
        "side_bc": 0,
        "angle_x": 0,
        "angle_y": 0,
        "diag": 0,
        "square": 60,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 3,
        "side_bc": 20,
        "angle_x": 162.938,
        "angle_y": 17.062,
        "diag": 20.224,
        "square": 60,
        "perimeter": 46,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_bc_and_square():
    case = {
        "side_ab": 0,
        "side_bc": 10.10,
        "angle_x": 0,
        "angle_y": 0,
        "diag": 0,
        "square": 10.10,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 1,
        "side_bc": 10.10,
        "angle_x": 168.691,
        "angle_y": 11.309,
        "diag": 10.149,
        "square": 10.10,
        "perimeter": 22.2,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_diag_and_ab():
    case = {
        "side_ab": 25,
        "side_bc": 0,
        "angle_x": 0,
        "angle_y": 0,
        "diag": 50,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 25,
        "side_bc": 43.301,
        "angle_x": 120,
        "angle_y": 60,
        "diag": 50,
        "square": 1082.532,
        "perimeter": 136.603,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_diag_and_bc():
    case = {
        "side_ab": 0,
        "side_bc": 3,
        "angle_x": 0,
        "angle_y": 0,
        "diag": 32,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 31.859,
        "side_bc": 3,
        "angle_x": 10.759,
        "angle_y": 169.241,
        "diag": 32,
        "square": 95.577,
        "perimeter": 69.718,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_diag_and_perimeter():
    case = {
        "side_ab": 0,
        "side_bc": 0,
        "angle_x": 0,
        "angle_y": 0,
        "diag": 132.544,
        "square": 0,
        "perimeter": 288,
    }
    expect = {
        "side_ab": 12,
        "side_bc": 132,
        "angle_x": 169.611,
        "angle_y": 10.389,
        "diag": 132.544,
        "square": 1584.044,
        "perimeter": 288,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_diag_and_angle_y():
    case = {
        "side_ab": 0,
        "side_bc": 0,
        "angle_x": 0,
        "angle_y": 60,
        "diag": 25,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 12.5,
        "side_bc": 21.651,
        "angle_x": 120,
        "angle_y": 60,
        "diag": 25,
        "square": 270.633,
        "perimeter": 68.301,
    }
    assert expect == remove_input_prefixes(Model(**case).process())


def test_diag_and_angle_x():
    case = {
        "side_ab": 0,
        "side_bc": 0,
        "angle_x": 120,
        "angle_y": 0,
        "diag": 15,
        "square": 0,
        "perimeter": 0,
    }
    expect = {
        "side_ab": 7.5,
        "side_bc": 12.99,
        "angle_x": 120,
        "angle_y": 60,
        "diag": 15,
        "square": 97.428,
        "perimeter": 40.981,
    }
    assert expect == remove_input_prefixes(Model(**case).process())
