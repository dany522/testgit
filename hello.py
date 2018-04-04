# width = input('Please enter width:')
# width = 34
# price_width = 10
# item_width = width-price_width
# header_format = '%-*s%*s'
# format = '%-*s%*.2f'
# print '='*width
# print header_format % (item_width,'Item',price_width,'Price')
# print '-'*width
# # print format % (5,'ert',23,4)
# print format % (item_width,'Apples',price_width,0.4)
#
# print format % (item_width,'Pears',price_width,0.5)
# print format % (item_width,'Cantaloupes',price_width,1.92)
# print format % (item_width,'Dried Apricos (16 oz.)',price_width,8)
# print format % (item_width,'Prunes (4 1bs)',price_width,12)
# print '='*width

# x = {'username':'admin','machines':['foo','bar','baz']}
# y = x.copy()
# y['username'] = 'mlh'
# y['machines'].remove('bar')
# print y

# greeting = 'hello'
# name = 'gumby'
# print greeting+',',name
# def print_params(**params):
#     print params
# print_params(x=1,y=2,z=3)

# def story(**kwds):
#     return 'Once upon a time, there was a ' \
#             '%(job)s called %(name)s' % kwds
# def power(x,y,**others):
#     if others:
#         print 'Received redundant parameters:',others
#     return pow(x,y)
# def interval(start,stop=None,step=1):
#     'Imitates range() for step>0'
#     if stop is None:
#         start,stop = 0,start
#     result = []
#     i = start
#     while i<stop:
#         result.append(i)
#         i+=step
#     return result
# print story(job='king',name='gumby')
# params = {'name':'python','job':'langage'}
# print story(**params)
# print interval(10)

# def multipliter(factor):
#     def multiplyByFactor(number):
#         return number*factor
#     return multiplyByFactor
#
# double = multipliter(2)
# print double(5)

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print factorial(5)

__metaclass__ = type

# class Person:
#     def setName(self,name):
#         self.name = name
#     def getName(self):
#         return self.name
#     def greet(self):
#         print 'hello,world i am %s' % self.name
#
# foo = Person()
# foo.setName('luck')
# foo.name

# class MemberCounter:
#     members = 0
#     def init(self):
#         MemberCounter.members +=1
# m1 = MemberCounter()
# m1.init()
# m2 = MemberCounter()
# m2.init()
# m1.members = 3
# print  m1.members
#
# class Filter:
#     def init(self):
#         self.blocked = []
#     def filter(self,sequence):
#         return [x for x in sequence if x not in self.blocked]
# class SPAMFilter(Filter):
#     def init(self):
#         self.blocked = ['SPAM']

# print issubclass(SPAMFilter,Filter)
# print SPAMFilter.__bases__

# s = SPAMFilter()
# print isinstance(s,SPAMFilter)
# print s.__class__
# s.init()
# print s.filter(['SPAM','GH','SPAM','DKF'])

# try:
#     x = input('enter the first number:')
#     y = input('enter the second number:')
#     print x/y
# except Exception,e:
#     print 'something wrong'

# while True:
#     try:
#         x = input('enter the first number:')
#         y = input('enter the second number:')
#         value = x/y
#         print 'x/y is ',value
#     except:
#         print 'invalid input.please try again'
#     else:
#         break
#
# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#     def setSize(self,size):
#         self.width,self.height = size
#     def getSize(self):
#         return self.width,self.height
#     size = property(getSize,setSize)

import sys,pprint,os
# print os.environ.get('DEV_DATABASE_URL')
pprint.pprint(sys.path)

# import test
# test.hello()


# import MySQLdb
# conn = MySQLdb.Connect(host="localhost",db="mysql",user="root",passwd="jolin1500" )
# curs = conn.cursor()
# sql = "select Host from USER "
#
# curs.execute(sql)
# for row in curs.fetchall():
#     print row
#
# curs.close()
# conn.close()

