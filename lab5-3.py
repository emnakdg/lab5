def mean_with_args(*args):
    if not args:
        return 0.0
    total = sum(args)
    return round(total / len(args), 2)

def mean_with_kwargs(**kwargs):
    if not kwargs:
        return 0.0
    total = sum(kwargs.values())
    return round(total / len(kwargs), 2)


numbers = [1, 2, 3, 4, 5]
kwargs = {'num1': 10, 'num2': 20, 'num3': 30}

mean_args = mean_with_args(*numbers)
print("Mean with *args:", mean_args)


mean_kwargs = mean_with_kwargs(**kwargs)
print("Mean with **kwargs:", mean_kwargs)