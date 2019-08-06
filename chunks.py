import worldspawner


def pos2chunkid(a):
    return (a-a % 10)/10


class chunk:
    def __init__(self, x, y, type='normal'):
        if type == 'normal':
            self.land_data = worldspawner.spawner_default(x, y)
        elif type == 'flat':
            self.land_data = worldspawner.spawner_flat()
        self.cover_data = worldspawner.spawner_cover(self.land_data)


class chunk_store:
    def __init__(self, mode='normal'):
        self.chunk_data = {}
        self.mode = mode

    def get_chunk(self, x, y):
        if not (x, y) in self.chunk_data:
            self.chunk_data[(x, y)] = chunk(x, y, self.mode)
        return self.chunk_data[(x, y)]

    def get_block(self, x, y):
        return self.get_chunk(pos2chunkid(x), pos2chunkid(y)).land_data[y % 10][x % 10]

    def set_block(self, x, y, id):
        self.get_chunk(pos2chunkid(x), pos2chunkid(
            y)).land_data[y % 10][x % 10] = id

    def get_cover(self, x, y):
        return self.get_chunk(pos2chunkid(x), pos2chunkid(y)).cover_data[y % 10][x % 10]

    def set_cover(self, x, y, id):
        self.get_chunk(pos2chunkid(x), pos2chunkid(y)
                       ).cover_data[y % 10][x % 10] = id
