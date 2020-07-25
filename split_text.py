###############################Setting my Dict###########################################

w_dict = {'My':'un',
          'name':'too',
          'is':'mu',
          'i':'nu',
          'am':'teh',
          'in':'ba',
          'grade':'buku',
          '12':'tannin-fula',
          'going':'ka',
          'to':'taa',
          '11':'tannin-kiling',
          'Sambou':'Sambou',
          'kinteh':'kinteh'
    }

text = 'My name is Sambou kinteh i am in grade 12 going to grade 11. Hope you are satisfied'
list = text.split(' ',)
list = list[0:5]
wd1 = str(list[0])
wd2 = str(list[1])
wd3 = str(list[2])
wd4 = str(list[3])
wd5 = str(list[4])
def tansulate():
    w1 = str(w_dict.get(wd1))
    w2 = str(w_dict.get(wd2))
    w3 = str(w_dict.get(wd3))
    w4 = str(w_dict.get(wd4))
    w5 = str(w_dict.get(wd5))
    man_word = w1 + w2 + w3 + w4 + w5
    return man_word

print('{0} {1} {2} {3} {4} = {5}'.format(wd1,wd2,wd3,wd4,wd5, tansulate()))

