import unittest

from sorting import Sort

class TestBubbleSort(unittest.TestCase):

    def test_primera_lista(self):
        primera_lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 7]
        Sort.BubbleSort(self, primera_lista)
        
if __name__ == '__main__':

    unittest.main()
    