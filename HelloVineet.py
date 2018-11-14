import sys
import collections
def main():
	queue = collections.deque(["Eric", "John", "Michael"])
	queue.append("vineet")
	print queue.popleft()
	print queue

	print "Hello" + sys.argv[1]

if __name__ == '__main__':
	main()