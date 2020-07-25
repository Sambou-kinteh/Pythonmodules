import sys
# creating a mandinka dictionary

mandinka = dict()
#transulation of numbers from engilsh to mandinka(1 to 100)    
mandinka['one'] = "kiling";
mandinka['two'] = "fulla";
mandinka['three'] = "saba";
mandinka['four'] = "nani";
mandinka['five'] = "lulu";
mandinka['six'] = "woroh";
mandinka['seven'] = "woro-wula";
mandinka['eight'] = "seiin";
mandinka['nine'] = "kononto";
mandinka['ten'] = "tang";
mandinka['eleven'] = "tan-nin-kiling";
mandinka['tweleve'] = "tan-nin-fulla";
mandinka['thirteen'] = "tan-nin-saba";
mandinka['fourteen'] = "tan-nin-nani";   
mandinka['fifteen'] = "tan-nin-lulu";
mandinka['sixteen'] = "tan-nin-woroh";
mandinka['senventeen'] = "tan-nin-worowulw";
mandinka['eighteen'] = "tan-nin-seiin";
mandinka['nineteen'] = "tan-nin-kononto";
mandinka['twenty'] = "muwang";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";

#english to mandinka(101 to 200)

mandinka['yes'] = "haa";
mandinka['what'] = "mung";
mandinka['go'] = "ta";
mandinka['come'] = "taa";
mandinka['book'] = "booko";
mandinka['nose'] = "nungo";
mandinka['eye'] = "nyaa";
mandinka['head'] = "kuong";
mandinka['shirt'] = "dendiko";
mandinka['man'] = "keeou";
mandinka['woman'] = "musoo";
mandinka['girl'] = "sunkuto";
mandinka['boy'] = "kangbano";
mandinka['sit'] = "sei";
mandinka['tree'] = "yero";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";

mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";
mandinka[''] = "";

word = input('Enter a word: ')
#print(mandinka.get(''))

'''def Mandinka_word(word, mandinka1):
    #english = word
    for word in mandinka:
        mandinka1 = mandinka.get(word)
    return mandinka.get(word)
print('{0} = {1}'.format(Mandinka_word(word, mandinka1)))'''

def mandinka_word(word):
    mandinka1 = mandinka[word]
    for word in mandinka:
        return mandinka.get(word)
print('{0} = {1}'.format(mandinka_word(word)))    
    














