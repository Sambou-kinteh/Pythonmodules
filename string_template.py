import string

data = []
data.append({'item' : 'Mango', 'cost' : 5.99, 'qty' : 3})
data.append({'item' : 'Orange', 'cost' : 1.99, 'qty' : 3})
data.append({'item' : 'Banana', 'cost' : 30.99, 'qty' : 3})
data.append({'item' : 'Yam', 'cost' : 10.99, 'qty' : 3})
temp = string.Template('$qty x $item = $cost')
temp.safe_substitute(qty = data['item'] )
print(data)
