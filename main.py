import random


def retry(attempts=5, desired_value=None):
    def wrapper(func):
        def wrapper_inner(*args, **kwargs):
            for _ in range(attempts):
                result = func(*args, **kwargs)
                if result == wrapper.desired_value:
                    return result
            print("Не удалось достичь желаемого значения.")
            return None

        wrapper.desired_value = desired_value
        return wrapper_inner

    return wrapper


@retry(attempts=5, desired_value=3)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(attempts=5, desired_value=[1, 2])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


print(get_random_value())
print(get_random_values([1, 2, 3, 4, 5]))