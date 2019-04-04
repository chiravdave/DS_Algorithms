''' 
T9: On old cell phones, users typed on a numeric keypad and the phone would provide a list of words that matched these numbers. Each digit mapped to a set of O - 4 letters. 
    Implement an algorithm to return a list of matching words, given a sequence of digits. You are provided a list of valid words (provided in whatever data structure you'd like).

Phone: {0:'',1:'',2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
'''

class NumberToWords:

	def __init__(self):
		self.phone = {'a':2,'b':2,'c':2,'d':3,'e':3,'f':3,'g':4,'h':4,'i':4,'j':5,'k':5,'l':5,'m':6,'n':6,'o':6,'p':7,'q':7,'r':7,'s':7,'t':8,'u':8,'v':8,'w':9,'x':9,'y':9,'z':9}

	def word_to_num(self, word):
		'''
		This function will give the no. corresponding to the given word
		'''
		num = 0
		for i in word:
			num = num*10 + self.phone[i]
		return num

	def find_words(self, number, matching_words):
		'''
		This function will first generate all possible no.s that could be formed from the given words. Finally, will use the given no. as key to get all the corresponding words.
		'''
		mapping = {}
		for i in matching_words:
			no = self.word_to_num(i)
		if no in mapping:
			mapping[no].append(i)
		else:
			mapping[no] = [i]
		number_int = 0
		for i in number:
			if i != '0' and i !='1':
				number_int = number_int*10 + int(i)
		if number_int in mapping:
			return mapping[number_int]
		else:
			return []

if __name__ == '__main__':
	check = NumberToWords()
	matching_words = ['boy','girl','man','women','box']
	print(check.find_words('12690',matching_words))