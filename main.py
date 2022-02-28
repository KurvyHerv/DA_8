import pandas as pd

num1 = input('Enter the starting year: ')
num2 = input('Enter the ending year: ')
usr1 = input('Enter the starting country: ')
usr2 = input('Enter the ending country: ')
country1 = ' ' + usr1 + ' '
country2 = ' ' + usr2 + ' '
df = pd.read_excel('Project_File.xlsx')
dfsplit = df.iloc[:,0].str.split(' ', n = 1, expand = True)
dfsplit = dfsplit[1].str.split(' ', n = 1, expand = True)
df = pd.concat([dfsplit[0], df.iloc[:, 1:]], axis=1)
rowindex1 = df[df.iloc[:,0] == num1].index[1]
rowindex2 = df[df.iloc[:,0] == num2].index[1]
columnindex1 = df.columns.get_loc(country1)
columnindex2 = df.columns.get_loc(country2)
columnindex2 += 1
df = df.iloc[rowindex1:rowindex2, columnindex1:columnindex2]
sumcolumn = df.columns.get_loc(country2)
sumcolumn += 1
countrylist = []
for col in df.columns:
    countrylist.append(col)

i = 0
sumlist = []
while(i < sumcolumn):
    dfsum = df.iloc[:,i].sum()
    sumlist.append(dfsum)
    i+=1

data = [sumlist]
dftotal = pd.DataFrame(data, columns = [countrylist])

top3 = []
x = 0
while(x < 3):
    top = sumlist.index(max(sumlist))
    top3.append(sumlist.pop(top))
    x+=1

b = 0
while(b <= 2):
    countryindex = ((dftotal.iloc[:11] == top3[b]).any()).argmax()
    print(''.join(dftotal.columns[countryindex]) + ' : ' + str(top3[b]))
    b += 1
