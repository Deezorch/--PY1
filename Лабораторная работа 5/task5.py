def get_random_password(n=8) -> str:
    import string
    from random import sample

    all_values = string.ascii_lowercase + string.ascii_uppercase + string.digits

    return "".join(sample(all_values, n))


print(get_random_password())
