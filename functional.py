# this uses a more cpp style 

''' define empty class '''
class myList(list):
    pass

''' set opinionated functions '''
myList.filter = lambda self, f: myList(filter(f,self))
myList.map = lambda self, f: myList(map(f,self))

''' 
overwrite  built in `list` 
this *should* not cause any Problems
because of the subtype relation
'''
list = myList