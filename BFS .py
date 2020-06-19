import time
def solve(s):
  
    try:
        i  = s.index(0)
    except ValueError: 
        return s

    c = [s[j] for j in range(81)
         if not ((i-j)%9 * (i//9^j//9) * (i//27^j//27 | (i%9//3^j%9//3)))]

    for v in range(1, 10):
        if v not in c:
            r = solve(s[:i]+[v]+s[i+1:])
            if r is not None:
                return r


class Sudoku(list):
        
		
        def __init__(self, content):
            list.__init__(self, [int(i) for i in content.split()] 
                          if isinstance(content, str) else content)
        def __str__(self):
            return '\n'.join(
                ' '.join([(str(j) if j != 0 else '0') 
                          for j in self[i*9:(i+1)*9]]) for i in range(9))
    
	
	# Easy
    problem = Sudoku('''
        0 0 0 0 0 4 0 9 0
        8 0 2 9 7 0 0 0 0
        9 0 1 2 0 0 3 0 0
        0 0 0 0 4 9 1 5 7 
        0 1 3 0 5 0 9 2 0 
        5 7 9 1 2 0 0 0 0 
        0 0 7 0 0 2 6 0 3 
        0 0 0 0 3 8 2 0 5 
        0 2 0 5 0 0 0 0 0
        ''')

	#Hard
	"""
    problem = Sudoku('''
        0 0 0 0 0 0 0 0 2
        0 0 0 0 0 0 9 4 0
        0 0 3 0 0 0 0 0 5
        0 9 2 3 0 5 0 7 4 
        8 4 0 0 0 0 0 0 0 
        0 6 7 0 9 8 0 0 0 
        0 0 0 7 0 6 0 0 0 
        0 0 0 9 0 0 0 2 0 
        4 0 8 5 0 0 3 6 0
        ''')
    """

    start = time.time()
		
    result = Sudoku(solve(problem))
	
    print('==== Problem ====\n{0}\n\n=== Solution ====\n{1}'.format(problem, result))
    
    print ("This puzzle was solved in: ",(time.time()-start),"seconds")
	