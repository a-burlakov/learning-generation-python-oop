import json
import functools


def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapper


@jsonify
def make_user(id, live, options):
    return (1, "2", 3.0, None, False, {"1": True})


print(make_user(4, False, None))
