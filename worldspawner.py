import random

import blocks


def spawner_default(x, y):
    return [[random.randint(1, len(blocks.block_res)-1)for i in range(10)]for j in range(10)]


def spawner_flat():
    return [[1 for i in range(10)]for j in range(10)]


def spawner_cover(data):
    return [[(random.randint(1, 2) if (data[j][i] == 1 and random.randint(0, 10) == 0) else 0) for i in range(10)]for j in range(10)]
