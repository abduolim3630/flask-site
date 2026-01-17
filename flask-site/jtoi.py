def complex_to_string(c):
    # Check if both real and imaginary parts are zero
    if c.real == 0 and c.imag == 0:
        return "0"

    # Format the real part
    real_str = f"{c.real:.2f}".rstrip('0').rstrip('.')
    # Format the imaginary part
    imag_str = f"{c.imag:.2f}".rstrip('0').rstrip('.')

    # Check if either part is zero and format accordingly
    if c.real == 0 and c.imag != 0:
        return f"{imag_str}i"
    elif c.imag == 0 and c.real != 0:
        return f"{real_str}"
    elif c.imag >= 0:
        return f"{real_str} + {imag_str}i"
    else:
        return f"{real_str} - {abs(c.imag):.2f}".rstrip('0').rstrip('.') + "i"
