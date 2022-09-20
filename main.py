class Location:
    def __init__(self):
        self.name = None
        self.x = None
        self.y = None
class Party:
    def __init__(self):
        self.name = None
        self.speed = None
        self.x = None
        self.y = None
class Engine:
    def __init__(self):
        self.locations = dict()
        self.parties = dict()
        self.running = True
    def process(self, line):
        parts = line.split(' ')
        part = parts[0]
        size = len(parts)
        if part == 'create':
            if size < 2:
                print('create [location, party]?')
                return
            part = parts[1]
            if part == 'location':
                if size < 3:
                    print('create location [id]?')
                    return
                _id = parts[2]
                self.locations[_id] = Location()
            elif part == 'party':
                if size < 3:
                    print('create party [id]?')
                    return
                _id = parts[2]
                self.parties[_id] = Party()
            else:
                print('create [location, party]?')
        elif part == 'cycle':
            if size < 2:
                print('cycle [value]?')
                return
            try:
                value = int(parts[1])
            except:
                print('cycle [value]?')
            for i in range(value):
                print('cycle')
        elif part == 'exit':
            self.running = False
        elif part == 'help':
            print('create -- to create')
            print('exit -- to exit')
            print('print -- to print')
            print('set -- to set')
        elif part == 'print':
            if size < 2:
                print('print [location, party]?')
                return
            part = parts[1]
            if part == 'location':
                if size < 3:
                    print('print location [id]?')
                    return
                _id = parts[2]
                if not _id in self.locations.keys():
                    print('invalid id!')
                    return
                location = self.locations[_id]
                print('name = {}'.format(location.name))
                print('x = {}'.format(location.x))
                print('y = {}'.format(location.y))
            elif part == 'party':
                if size < 3:
                    print('print party [id]?')
                    return
                _id = parts[2]
                if not _id in self.parties.keys():
                    print('invalid id!')
                    return
                party = self.parties[_id]
                print('name = {}'.format(party.name))
                print('speed = {}'.format(party.speed))
                print('x = {}'.format(party.x))
                print('y = {}'.format(party.y))
            else:
                print('print [location, party]?')
        elif part == 'set':
            if size < 2:
                print('set [location, party]?')
                return
            part = parts[1]
            if part == 'location':
                if size < 3:
                    print('set location [name, x, y]?')
                    return
                part = parts[2]
                if part == 'name':
                    if size < 5:
                        print('set location name [id] [value]?')
                        return
                    _id = parts[3]
                    if not _id in self.locations.keys():
                        print('invalid id!')
                        return
                    value = parts[4].replace('_', ' ')
                    self.locations[_id].name = value
                elif part == 'x':
                    if size < 5:
                        print('set location x [id] [value]?')
                        return
                    _id = parts[3]
                    if not _id in self.locations.keys():
                        print('invalid id!')
                        return
                    try:
                        value = float(parts[4])
                    except:
                        print('invalid input!')
                    self.locations[_id].x = value
                elif part == 'y':
                    if size < 5:
                        print('set location y [id] [value]?')
                        return
                    _id = parts[3]
                    if not _id in self.locations.keys():
                        print('invalid id!')
                        return
                    try:
                        value = float(parts[4])
                    except:
                        print('invalid input!')
                    self.locations[_id].y = value
                else:
                    print('set province [name, x, y]?')
            elif part == 'party':
                if size < 3:
                    print('set party [name, speed, x, y]?')
                    return
                part = parts[2]
                if part == 'name':
                    if size < 5:
                        print('set party name [id] [value]?')
                        return
                    _id = parts[3]
                    if not _id in self.parties.keys():
                        print('invalid id!')
                        return
                    value = parts[4].replace('_', ' ')
                    self.parties[_id].name = value
                elif part == 'speed':
                    if size < 5:
                        print('set party speed [id] [value]?')
                        return
                    _id = parts[3]
                    if not _id in self.parties.keys():
                        print('invalid id!')
                        return
                    try:
                        value = float(parts[4])
                    except:
                        print('invalid input!')
                    self.parties[_id].speed = value
                elif part == 'x':
                    if size < 5:
                        print('set party x [id] [value]?')
                        return
                    _id = parts[3]
                    if not _id in self.parties.keys():
                        print('invalid id!')
                        return
                    try:
                        value = float(parts[4])
                    except:
                        print('invalid input!')
                    self.parties[_id].x = value
                elif part == 'y':
                    if size < 5:
                        print('set party y [id] [value]?')
                        return
                    _id = parts[3]
                    if not _id in self.parties.keys():
                        print('invalid id!')
                        return
                    try:
                        value = float(parts[4])
                    except:
                        print('invalid input!')
                    self.parties[_id].y = value
                else:
                    print('set party [name, speed, x, y]?')
            else:
                print('set [location, party]?')
        else:
            print('use \'help\'')
    def start(self):
        print('FINAL THING')
        while self.running:
            self.process(input('> '))
    def test(self):
        self.process('create location test')
        self.process('set location name test Test_Location')
        self.process('set location x test 10.0')
        self.process('set location y test 10.0')
        self.process('create party test')
        self.process('set party name test Test_Party')
        self.process('set party speed test 10.0')
        self.process('set party x test 0.0')
        self.process('set party y test 0.0')
        self.process('print location test')
        self.process('print party test')
e = Engine()
e.test()
#e.start()
