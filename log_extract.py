'''
@Filename	: log_extract.py
@Author		: someone , ID
@Contact	: someone@company.com
@Date		: 2020/02/07
@Description:  .
'''

import sys


class LogExtract:
    dirs = []
    files = []
    cntr = 0
    fp = None

    def __init__(self):
        return

    def usage(self):
        # Show the usage of this scripts
        self.cntr = -1
        return

    def option_parser(self, opts):
        if len(opts[0]):
            # Process List of args
            print(opts)
        else:
            self.usage()
        return

    def search_dir(self, dirs):
        # File operation
        return

    def search_file(self, file):
        ret = 0  # if match ret++
        # File operation, search texts
        # match one output to file
        return ret

    def sumary(self):
        # print sumary message, total
        return self.cntr

    def run(self, *args):
        if self.option_parser(args):
            self.search_dir(self.dirs)
        else:
            self.usage()
        return self.sumary()


if __name__ == '__main__':
    le = LogExtract()
    exit(le.run(sys.argv[1:]))
# exit(LogExtract().run(sys.argv[1:]))
