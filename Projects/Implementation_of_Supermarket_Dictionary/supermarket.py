# Implementation of Supermarket Dictionary
supermarket = {
                'store1':{
                            'name' : 'Gupta General Store',
                            'items': [
                                        {'name':'soap','quantity':20},
                                        {'name':'brush','quantity':30},
                                        {'name':'paste','quantity':40}
                                    ]
                        },
                'store2':{
                            'name' : 'Gupta Stationary',
                            'items':[
                                        {'name':'Python','quantity':25},
                                        {'name':'Django','quantity':15},
                                        {'name':'Data Structures','quantity':5}
                                    ]
                        }
            }
# print name of the store 1
print(supermarket['store1']['name'])
# Alternatively
print(supermarket.get('store1').get('name'))

# print names of all items present in store 1
for item in supermarket['store1']['items']:
    print(item['name'])
# Alternatively
for item in supermarket.get('store1').get('items'):
    print(item['name'])

# print how many Django books are available
# without using indexing
for item in supermarket['store2']['items']:
    if item['name'] == 'Django':
        print('The Number of Django Books :', item['quantity'])
