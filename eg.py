def is_float(num_str):
    try:
        float(num_str)
        return True
    except ValueError:
        return False

is_float("hello")