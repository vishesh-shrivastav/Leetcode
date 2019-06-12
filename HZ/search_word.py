board =[['A', 'B', 'E', 'R', 'T'],['K', 'A', 'I', 'O', 'P']]
 
# // 
 
def search_word(board, word):
if not board or len(board)==0 or len(board[0])==0:
return False
if not word:
return True
# DFS: find the word, explore its neighbor
def find_the_word(i,j, word, visited):
ch = board[i][j]
if (i,j) in visited:
return False
         
if ch == word[0]:
visited.add((i,j))
if len(word)==1:
return True
else:
#keep searching its neighbor
for neighbor in [(0,1), (1,0), (-1,0) , (0,-1)]:
next_i, next_j = i+neighbor[0], j+neighbor[1]
# validate the boundary
if 0<=next_i<len(board) and 0<=next_j<len(board[0]):
if find_the_word(next_i, next_j, word[1:], set(visited)):
return True
 
     
# iterate each cell on this board
for i in range(len(board)):
for j in range(len(board[0])):
if find_the_word(i,j, word, set()):
return True
             
# could not find
return False
 
# M: num of row
# N: num of cols
# TIME: O(MN*MN)
#
 
# Test 
 
import unittest
class MyTestCase(unittest.TestCase):
     
def test_something(self):
self.assertEqual(False, search_word(board, 'AA'))
     
     
def test_should_find_word(self):
self.assertEqual(True, search_word(board, 'BERTP'))
         
def test_should_find_word_4(self):
self.assertEqual(False, search_word(board, 'BERTPBERTPBERTPBERTPBERTPBERTPBERTPBERTP')) 
         
         
def test_should_not_find_word(self):
self.assertEqual(False, search_word(board, 'PTP')) 
         
def test_should_not_find_word2(self):
self.assertEqual(True, search_word(board, 'P')) 
         
def test_should_not_find_word3(self):
self.assertEqual(True, search_word(board, '')) 
         
         
# check empty board
     
def test_should_not_find_word6(self):
self.assertEqual(False, search_word(None, '')) 
         
def test_should_not_find_word7(self):
self.assertEqual(False, search_word([], '')) 
         
def test_should_not_find_word8(self):
self.assertEqual(False, search_word([[]], '')) 
         
# // []
# // [[]]
         
         
unittest.main()
