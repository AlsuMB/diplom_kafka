import datetime

import numpy as np
from numpy.random import randint
import string


# department_id      numeric(4),
# hub_load_dts       date,
# hub_rec_src        varchar(12)
def get_random_values():
    new_list = []
    for i in range(1000):
        department_id = randint(-9999, 9999)
        hub_load_dts = random_date()
        letters = string.ascii_lowercase
        hub_rec_src = ''.join(np.random.choice(list(letters), 12))

        new_list.append([department_id, hub_load_dts, hub_rec_src])
        new_list.append({'department_id': department_id, 'hub_load_dts': hub_load_dts, "hub_rec_src": hub_rec_src})
        return {'department_id': department_id, 'hub_load_dts': hub_load_dts, "hub_rec_src": hub_rec_src}
    return new_list


def random_date():
    start = datetime.datetime(1971, 1, 1)
    end = datetime.datetime(2025, 12, 31)

    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = np.random.randint(int_delta)
    return start + datetime.timedelta(seconds=random_second)

