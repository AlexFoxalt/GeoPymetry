class BaseLanguage:
    """
    Class of abstract attrs that should be provided in children.
    """

    # Menu
    TXT_WELCOME: str = ""
    TXT_SELECT_FIGURE: str = ""
    TXT_SELECT_TRIANGLE: str = ""
    TXT_SELECT_QUADRANGLE: str = ""
    TXT_SELECT_CIRCLE: str = ""
    TXT_FILL_THE_FORM: str = ""
    TXT_REFRESH_THE_FORM: str = ""
    TXT_CALCULATED: str = ""
    TXT_CONFIRM_FORM: str = ""

    # Message boxes
    ERR_TITLE: str = ""
    ERR_FIGURE_NOT_EXIST: str = ""
    ON_CLOSE_TITLE: str = ""
    ON_CLOSE_MSG: str = ""

    # Available figures
    TXT_TRIANGLE_TYPES: str = ""
    TXT_QUADRANGLE_TYPES: str = ""
    TXT_CIRCLE_TYPES: str = ""

    # Math
    TXT_CATHETUS: str = ""
    TXT_HYPOTENUSE: str = ""
    TXT_SMALL_R: str = ""
    TXT_BIG_R: str = ""
    TXT_HEIGHT: str = ""
    TXT_MEDIAN: str = ""
    TXT_ANGLE: str = ""
    TXT_SQUARE: str = ""
    TXT_PERIMETER: str = ""
    TXT_SIDE: str = ""
    TXT_DIAGONAL: str = ""
    TXT_DIAMETER: str = ""
    TXT_RADIUS: str = ""
    TXT_CIRCUMFERENCE: str = ""

    # Tips
    TXT_HOME_TIP: str = ""
    TXT_START_TIP: str = ""

    TXT_SELECT_CIRCLE_TIP: str = ""
    TXT_SELECT_CIRCLE_TYPE_TIP: str = ""

    TXT_SELECT_TRIANGLE_TIP: str = ""
    TXT_SELECT_RIGHT_TRIANGLE_TYPE_TIP: str = ""
    TXT_SELECT_EQUILATERAL_TRIANGLE_TYPE_TIP: str = ""
    TXT_SELECT_ARBITRARY_TRIANGLE_TYPE_TIP: str = ""

    TXT_SELECT_QUADRANGLE_TIP: str = ""
    TXT_SELECT_RECTANGLE_TIP: str = ""
    TXT_SELECT_PARALLELOGRAM_TIP: str = ""
    TXT_SELECT_TRAPEZOID_TIP: str = ""
    TXT_SELECT_RHOMBUS_TIP: str = ""

    def __init__(self) -> None:
        parent_attrs = {i for i in BaseLanguage.__dict__.keys() if i[:1] != "_"}
        child_attrs = {i for i in self.__class__.__dict__.keys() if i[:1] != "_"}
        if parent_attrs != child_attrs:
            not_implemented = "\n".join(parent_attrs - child_attrs)
            raise NotImplementedError(
                f"Not all of attributes were provided! Not provided attrs:\n{not_implemented}"
            )
