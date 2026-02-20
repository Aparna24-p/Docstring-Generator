@st.cache_data  # Decorated function
def outer_func(a):
    def inner_func(b):  # Nested function
        return b * 2
    return inner_func(a)

class EmptyClass:  # Class without methods
    pass