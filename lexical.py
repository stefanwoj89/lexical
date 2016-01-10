import unittest

""" Simple Function Version """
def lexical_order(lex_list, order):
	"""
		Run Time Complexity of O(nlogn) where n is number of elements
		in lex_list
	"""
	look_up = {None: -1}
	for i,l in enumerate(order):
		look_up[l] = i

	def lexical_cmp(word_one, word_two):
		"""
			for k letters in one word, and m letters in the other. Iteration
			and comparison is O(k+m), the look_up table, assuming average case 
			for a robust hash function is constant time.

			Run Time Complexity is therefore O(k+m)
		"""
		for letter_one, letter_two in map(None, word_one, word_two):
		    if letter_one != letter_two:
		    	return look_up[letter_one] - look_up[letter_two]
		return 0

	return sorted(lex_list, cmp=lexical_cmp)


""" Object Oriented Version """
class LexicalOrder:

	def __init__(self, list, order):
		"""
			Assuming average case, dictionary set is constant time,
			therefore building the look up table for n items is O(n)

			Run Time Complexity is therefore O(n)
		"""
		self.look_up = {None: -1}
		self.list = list
		for i,l in enumerate(order):
			self.look_up[l] = i
	
	def sort(self):
		"""
			for n items in the list, time complexity is O(nlogn) bound by
			python's sorted(function).

			Run Time Complexity is therefore O(nlogn)
		"""
		return sorted(self.list, cmp=self.lexical_cmp)

	def lexical_cmp(self, word_one, word_two):
		"""
			for k letters in one word, and m letters in the other. Iteration
			and comparison is O(k+m), the look_up table, assuming average case 
			for a robust hash function is constant time.

			Run Time Complexity is therefore O(k+m)
		"""
		for letter_one, letter_two in map(None, word_one, word_two):
		    if letter_one != letter_two:
		    	return self.look_up[letter_one] - self.look_up[letter_two]
		return 0


""" TESTING """
class TestLexicalFunction(unittest.TestCase):

	def test_natural(self):
		arg_list = ["acb", "abc", "bca"]
		arg_order = "abc"
		result = lexical_order(arg_list, arg_order)
		expected = ["abc","acb","bca"]
		self.assertEqual(result, expected)

	def test_unnatural(self):	
		arg_list = ["acb", "abc", "bca"]
		arg_order = "cba"
		result = lexical_order(arg_list, arg_order)
		expected = ["bca", "acb", "abc"]
		self.assertEqual(result, expected)

	def test_length(self):
		arg_list = ["aaa","aa",""]
		arg_order = "a"
		result = lexical_order(arg_list, arg_order)
		expected = ["", "aa", "aaa"]
		self.assertEqual(result, expected)

class TestLexicalClass(unittest.TestCase):

	def test_natural(self):
		arg_list = ["acb", "abc", "bca"]
		arg_order = "abc"
		x = LexicalOrder(arg_list, arg_order)
		expected = ["abc","acb","bca"]
		result = x.sort()
		self.assertEqual(result, expected)

	def test_unnatural(self):	
		arg_list = ["acb", "abc", "bca"]
		arg_order = "cba"
		x = LexicalOrder(arg_list, arg_order)
		expected = ["bca", "acb", "abc"]
		result = x.sort()
		self.assertEqual(result, expected)

	def test_length(self):
		arg_list = ["aaa","aa",""]
		arg_order = "a"
		x = LexicalOrder(arg_list, arg_order)
		expected = ["", "aa", "aaa"]
		result = x.sort()
		self.assertEqual(result, expected)


if __name__ == "__main__":
	unittest.main()