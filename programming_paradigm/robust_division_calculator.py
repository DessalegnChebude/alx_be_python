def safe_divide(numerator, denominator):
    try:
        result = numerator/denominator
        return result
    except ZeroDivisionError as e:
        return e

    except ValueError as e:
        print(e)
