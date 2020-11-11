# *args and **kwargs

def main(*args, **kwargs):
    args_type = type(args)
    kwargs_type = type(kwargs)
    type_max_len = max([len(str(args_type)), len(str(kwargs_type))])
    value_max_len = max([len(str(args)), len(str(kwargs))])
    print(f"ARG{' ' * 3}TYPE{' ' * ((type_max_len // 2) + 2)}VALUE")

    if __name__ == '__main__':
        main(1, 2, 3, {"name": "kaige"}, name="kaige", domain="www.kaige.online")
