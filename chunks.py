import worldspawner


def pos2chunkid(a):
    return (a-a % 10)/10


class chunk:
    def __init__(self, x, y, type='normal'):
        if type == 'normal':
            self.surface_data = worldspawner.spawner_default(x, y)
        elif type == 'flat':
            self.surface_data = worldspawner.spawner_flat()
        self.cover_data = worldspawner.spawner_cover()


class chunk_store:
    def __init__(self):
        self.chunk_data = {}

    def get_chunk(self, x, y):
        if not (x, y) in self.chunk_data:
            self.chunk_data[(x, y)] = chunk(x, y)
        return self.chunk_data[(x, y)]

    def get_block(self, x, y):
        return self.get_chunk(pos2chunkid(x), pos2chunkid(y)).surface_data[y % 10][x % 10]
