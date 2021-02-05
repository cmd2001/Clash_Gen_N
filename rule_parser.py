# rule parser

class RuleParser:
    def __init__(self, path):
        self.path = path

    def parse(self):
        fin = open(self.path, 'r')
        lines = fin.read().split('\n')
        fin.close()
        ret = []
        for line in lines:
            if len(line) < 3:  # empty line
                continue
            if line[0: 2] == '- ':
                sp = line[2:].split(',')
                ret.append({'method': sp[0], 'domain': sp[1]})
        return ret
