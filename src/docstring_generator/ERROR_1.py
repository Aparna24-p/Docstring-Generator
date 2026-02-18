# ERROR 1: Missing Module-level docstring (D100)

def calculate_area(radius):
    # ERROR 2: Missing Function docstring (D103)
    # This is just a comment, not a docstring.
    return 3.14 * radius * radius

class ShapeProcessor:
    """A class to process shapes."""
    # ERROR 3: Missing blank line after class docstring (D204)
    def __init__(self, name):
        """Initialize shape."""
        self.name = name

    def get_name(self):
        # ERROR 4: Missing Method docstring (D102)
        return self.name