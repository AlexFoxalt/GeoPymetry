from models.circles import Circle
from tests.utils import remove_input_prefixes

Model = Circle


def test_circle_radius():
    case = {"radius": 3, "diameter": 0, "square": 0, "perimeter": 0}
    expect = {"radius": 3, "diameter": 6, "square": 28.274, "perimeter": 18.85}
    assert expect == remove_input_prefixes(Model(**case).process())


def test_circle_square():
    case = {"radius": 0, "diameter": 0, "square": 10, "perimeter": 0}
    expect = {"radius": 1.784, "diameter": 3.568, "square": 10, "perimeter": 11.21}
    assert expect == remove_input_prefixes(Model(**case).process())


def test_circle_diameter():
    case = {"radius": 0, "diameter": 77, "square": 0, "perimeter": 0}
    expect = {"radius": 38.5, "diameter": 77, "square": 4656.626, "perimeter": 241.903}
    assert expect == remove_input_prefixes(Model(**case).process())


def test_circle_perimeter():
    case = {"radius": 0, "diameter": 0, "square": 0, "perimeter": 11.999}
    expect = {"radius": 1.91, "diameter": 3.819, "square": 11.457, "perimeter": 11.999}
    assert expect == remove_input_prefixes(Model(**case).process())
