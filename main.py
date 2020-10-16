#!/usr/bin/python

import web
from servicio_fibonacci import fibonacci


urls = (
    "/", "index",
    "/fibonacci/(.*)", "fibonacc"
)

class fibonacc:
	def GET(self, num):
		try:
			num = int(num)
			series = fibonacci(num)
		except ValueError as e:
			return """{\n"Exception":"%s"\n}""" % (e) 

		return "%s" % (series)

def main():
	serv = web.application(urls, globals())
	serv.run()

if __name__ == '__main__':
    main()