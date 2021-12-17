from common.text_manipulations import TextParser

class StateMachine:
    def __init__(self, data, binary=False):
        if binary:
            self.data = data
        else:
            self.data = ''.join(bin(int(c, 16))[2:].zfill(4) for c in data)
        self.state = self.ini_state
        self.c = 0
        self.result = 0
        self.ver = self.id = None
        self.vsum = 0

    def run(self):
        while self.state != self.end_state:
            self.state()
        return self.result

    def end_state(self):
        pass

    def ini_state(self):
        self.ver = int(self.data[self.c:self.c+3],2)
        self.id = int(self.data[self.c+3:self.c+6],2)
        self.c += 6
        self.vsum += self.ver

        if self.id == 4:
            self.state = self.literal_state
        else:
            self.state = self.operation_state

    def literal_state(self):
        num = []
        while True:
            num.append(self.data[self.c+1:self.c+5])
            if self.data[self.c] == '0':
                self.c += 5
                break
            self.c += 5
        self.result = int(''.join(num),2)
        self.state = self.end_state

    def operation_state(self):
        t = self.data[self.c]
        self.c += 1

        chunks = []

        if t == '0':
            end = self.c + 15 + int(self.data[self.c:self.c+15], 2)
            self.c += 15
            while self.c < end:
                new = self.new_state_machine(self.data[self.c:], binary=True)
                new.run()
                chunks.append(new.result)
                self.vsum += new.vsum
                self.c += new.c
        else:
            n_packets = int(self.data[self.c:self.c+11], 2)
            self.c += 11
            for _ in range(n_packets):
                new = self.new_state_machine(self.data[self.c:], binary=True)
                new.run()
                chunks.append(new.result)
                self.vsum += new.vsum
                self.c += new.c

        if self.id == 0:
            self.result = sum(chunks)
        elif self.id == 1:
            res = 1
            for p in chunks:
                res *= p
            self.result = res
        elif self.id == 2:
            self.result = min(chunks)
        elif self.id == 3:
            self.result = max(chunks)
        elif self.id == 5:
            self.result = 1 if chunks[0] > chunks[1] else 0
        elif self.id == 6:
            self.result = 1 if chunks[0] < chunks[1] else 0
        elif self.id == 7:
            self.result = 1 if chunks[0] == chunks[1] else 0
        else:
            raise ValueError

        self.state = self.end_state

    @classmethod
    def new_state_machine(cls, data, binary=False):
        return cls(data, binary=binary)

def run():

    source = TextParser("day16.txt").load_file_as_raw_string()
    sm = StateMachine(source)
    sm.run()

    # Part 1
    print(f"Part 1 result: {sm.vsum}")

    #Part 2
    print(f"Part 2 result: {sm.result}")

if __name__ == "__main__":

    run()