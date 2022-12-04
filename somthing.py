from numerize.numerize import numerize, denumerize

num = 50000

normal_data = numerize(num)
unformatted_data = "100"

denum = denumerize(normal_data)

if denum == num:
    print("Test 1 passed")

if denumerize(unformatted_data) == "err":
    print("Test 2 passed")
