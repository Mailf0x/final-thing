class Engine:
    def __init__(self):
        self.running = True
    def process(self, line):
        parts = line.split(' ')
        part = parts[0]
        if part == 'exit':
            self.running = False
        elif part == 'help':
            print('exit -- to exit')
        else:
            print('use \'help\'')
    def start(self):
        print('FINAL THING')
        while self.running:
            self.process(input('> '))
e = Engine()
e.start()
