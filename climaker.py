import sys
'''
Definition
'''
'''
example = {'key':{
	'alias' : ['-a','--action'],
	'description' : "This description is printed when launched with --help",
	'numberarguments': range(),

	}
}
'''
class Item(object):
	"""docstring for Item"""
	def __init__(self, arg,defined=True):
		super(Item, self).__init__()
		self.defined = defined
		self.alias = args['alias'] if 'alias' in args.keys() else []
		self.description = args['description'] if 'description' in args.keys() else ""
		self.numargs = args['numargs'] if 'numargs' in args.keys() else 0
		self.values = args['values'] if 'values' in args.keys() else None
		self.position = args['position'] if 'position' in args.keys() else None

	def isDefined(self):
		return self.defined
		

class CliMaker(object):
	"""docstring for CliMaker"""
	def __init__(self,rules=None):
		super(CliMaker, self).__init__()
		self.all = sys.argv.copy()[1:]
		self.rules = rules
	def getAll(self):
		return self.all