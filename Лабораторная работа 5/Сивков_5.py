import random
import string

def get_random_password() -> str:
    end_ = 8
    low_ = list(set(string.ascii_lowercase))
    high_ = list(set(string.ascii_uppercase))
    num_ = list(set(string.digits))
    low_.sort()
    high_.sort()
    num_.sort()

    add_up = low_ + high_ + num_
    result_ = "".join(random.sample(add_up, end_, counts=None))
    return result_

print("Ваш новый пароль:", get_random_password())
