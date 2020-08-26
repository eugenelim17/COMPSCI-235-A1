import unittest
from domain.domain import Movie, WatchList

watchlist = WatchList()

class MyTestCase(unittest.TestCase):
    def test_iter_and_next(self):
        watchlist1 = WatchList()
        watchlist1.add_movie(Movie("Moana", 2016))
        watchlist1.add_movie(Movie("Ice Age", 2002))
        watchlist1.add_movie(Movie("Guardians of the Galaxy", 2012))
        it1 = iter(watchlist1)
        self.assertEqual(next(it1), Movie("Moana", 2016))
        self.assertEqual(next(it1), Movie("Ice Age", 2002))
        self.assertEqual(next(it1), Movie("Guardians of the Galaxy", 2012))
        with self.assertRaises(StopIteration):
            next(it1)

if __name__ == '__main__':
    unittest.main()
