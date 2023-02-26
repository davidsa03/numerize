def numerize(n, decimal=2):
    sufixes = ["", "K", "M", "B", "T", "Qa", "Qu", "S", "Oc", "No",
               "D", "Ud", "Dd", "Td", "Qt", "Qi", "Se", "Od", "Nd", "V",
               "Uv", "Dv", "Tv", "Qv", "Qx", "Sx", "Ox", "Nx", "Tn", "Qa",
               "Qu", "S", "Oc", "No", "D", "Ud", "Dd", "Td", "Qt", "Qi",
               "Se", "Od", "Nd", "V", "Uv", "Dv", "Tv", "Qv", "Qx", "Sx",
               "Ox", "Nx", "Tn", "x", "xx", "xxx", "X", "XX", "XXX", "END"]

    sci_expr = [10 ** (3 * i) for i in range(len(sufixes))]

    abs_n = abs(n)
    for i, expr in enumerate(sci_expr[::-1]):
        if abs_n >= expr:
            num = abs_n / expr
            sufix = sufixes[len(sci_expr) - 1 - i]
            formatted_num = '{:.{}f}'.format(num, decimal).rstrip('0').rstrip('.')
            return formatted_num + sufix if n > 0 else '-' + formatted_num + sufix

    # If n is smaller than the smallest sci_expr, return n as a string with the specified number of decimal places
    formatted_num = '{:.{}f}'.format(abs_n, decimal).rstrip('0').rstrip('.')
    return formatted_num if n > 0 else '-' + formatted_num
