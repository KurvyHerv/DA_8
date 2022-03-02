import pandas as pd
import matplotlib.pyplot as plt

num1 = input('Enter the starting year: ')
num2 = input('Enter the ending year: ')
usr1 = input('Enter the starting country: ')
usr2 = input('Enter the ending country: ')
country1 = ' ' + usr1 + ' '
country2 = ' ' + usr2 + ' '
df = pd.read_excel('Project_File.xlsx')

#split year and month into 2 columns
dfsplit = df.iloc[:,0].str.split(' ', n = 1, expand = True)
dfsplit = dfsplit[1].str.split(' ', n = 1, expand = True)

#conbine split year into original df
df = pd.concat([dfsplit[0], df.iloc[:, 1:]], axis=1)

#crop df into starting row to ending row and starting column to ending column
rowindex1 = df[df.iloc[:,0] == num1].index[1]
rowindex2 = df[df.iloc[:,0] == num2].index[1]
columnindex1 = df.columns.get_loc(country1)
columnindex2 = df.columns.get_loc(country2)
columnindex2 += 1
df = df.iloc[rowindex1:rowindex2, columnindex1:columnindex2]

#create a list with all the countries in the range
countrylist = []
for col in df.columns:
    countrylist.append(col)

#find out the sum of all values in all countires in the range
sumcolumn = df.columns.get_loc(country2)
sumcolumn += 1
i = 0
sumlist = []
while(i < sumcolumn):
    dfsum = df.iloc[:,i].sum()
    sumlist.append(dfsum)
    i+=1

#create new df with country names and summed values
data = [sumlist]
dftotal = pd.DataFrame(data, columns = [countrylist])

#find out the top3 values of the summed values
top3 = []
x = 0
while(x < 3):
    top = sumlist.index(max(sumlist))
    top3.append(sumlist.pop(top))
    x+=1

#find out which country belongs to which summed value and print
b = 0
countrylist = []
while(b <= 2):
    countryindex = ((dftotal.iloc[:11] == top3[b]).any()).argmax()
    #create list of countries
    countrylist.append(''.join(dftotal.columns[countryindex]))
    print(''.join(dftotal.columns[countryindex]) + ' : ' + str(top3[b]))
    b += 1

#plat bar graph
data = [top3]
dfresult = pd.DataFrame(data, columns = [countrylist])
dfresult.plot.bar(rot=0)
plt.show();
