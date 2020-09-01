import unittest
import pytest
from domain.domain import Movie, WatchList

watchlist = WatchList()
class MyTestCase(unittest.TestCase):
    @pytest.fixture
    def watchlist(self):
        return WatchList()

    def test_no_first_movie_in_watchlist(self):
        watchlist.add_movie(Movie("Moana", 2016))
        assert watchlist.first_movie_in_watchlist() == Movie("Moana", 2016) #with_first_movie
        watchlist.remove_movie(Movie("Moana", 2016))
        assert watchlist.first_movie_in_watchlist() == None #with_no_first_movie

    def test_size(self):
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        assert watchlist.size() == 3

    def test_add_existing_movie_in_watchlist(self):
        watchlist.add_movie(Movie("Moana", 2016)) #add_new_movie_in_watchlist
        assert watchlist.size() == 1
        watchlist.add_movie(Movie("Moana", 2016)) #add_existing_movie_in_watchlist
        assert watchlist.size() == 1

    def test_remove_movie_not_in_watchlist(self):
        watchlist.add_movie(Movie("Moana", 2016))
        assert watchlist.size() == 1
        watchlist.remove_movie(Movie("Parasite", 2019))
        assert watchlist.size() == 1

    def test_select_movie_to_watch(self):
        watchlist.add_movie(Movie("Moana", 2016))
        assert watchlist.first_movie_in_watchlist() == Movie("Moana", 2016)
        assert watchlist.select_movie_to_watch(0) == Movie("Moana", 2016) #when movie in watchlist
        assert watchlist.select_movie_to_watch(watchlist.size() + 2) == None #when movie not in watchlist

if __name__ == '__main__':
    unittest.main()

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
