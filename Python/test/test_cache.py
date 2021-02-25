# Import library
from time import sleep
import timeit
from functools import lru_cache
import ttl_cache
from cachetools import cached, LRUCache, TTLCache

def test_timed_cache_lru():
	num = 400
	# Simple fibonacci sequence
	@cached(cache=TTLCache(maxsize=128, ttl=5))
	def fibonacci_cache(num: int) -> int:
		if num <= 1:
			return num
		else:
			return (fibonacci_cache(num-1)+fibonacci_cache(num-2))

	start = timeit.default_timer()
	r2 = fibonacci_cache(num)
	stop = timeit.default_timer()
	print(stop-start)

	start = timeit.default_timer()
	r2 = fibonacci_cache(num)
	stop = timeit.default_timer()
	print(stop - start)

	sleep(6)

	start = timeit.default_timer()
	r2 = fibonacci_cache(num)
	stop = timeit.default_timer()
	print(stop - start)

if __name__ == '__main__':
	test_timed_cache_lru()
