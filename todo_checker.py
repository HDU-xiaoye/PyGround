'''
@Filename	: todo_checker.py
@Author		: someone , ID
@Contact	: someone@company.com
@Date		: 2020/02/06
@Description: Search all files inside directory and show lines which contains keyword "FIXME" or "TODO" .
'''

import sys


class TodoChecker:

	dirs = []
	files = []
	ecode = -1

	def __init__(self):
		return

	def usage(self):
		# Show the usage of this scripts
		ecode = -1
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
		return ret

	def sumary(self):
		# print sumary message
		# if self.ecode == 0 means ok, print 'Check OK.'
		# if self.ecode != 0 means a number of TO-DO things found, print 'Check Failed.' with error code.
		return self.ecode

	def run(self, *args):
		if self.option_parser(args):
			self.search_dir(self.dirs)
		else:
			self.usage()
		return self.sumary()


if __name__ == '__main__':
	ck = TodoChecker()
	exit(ck.run(sys.argv[1:]))
	# exit(TodoChecker().run(sys.argv[1:]))
