import pandas as pd
import numpy as np

table= pd.DataFrame()
table['Cb']=''
table['Xb']=''
table['x1']=''
table['x2']=''
table['x3']=''
table['x4']=''
table['x5']=''
table['x6']=''
table['b']=''
table['ratio']=''


z= input('please enter coefficients for expression to be maximized seperated by spaces')
z = list(map(int, z.split()))
a=[[0,0,0,0], [0,0,0,0], [0,0,0,0]]
for i in range(3):
  a[i]= input('please enter constraint '+str(i+1) +' coefficients seperated by spaces')
  a[i] = list(map(int, a[i].split()))


row1= [[], [], []]
row2= [[], [], []]
row3= [[], [], []]
row4= [[], [], []]

for i in range(3):
  row1[i]= [0, i+4 ]
  row2[i]= a[i][:3]
  if (i==0):
      row3[i]= [1,0,0]
  if (i==1):
    row3[i]= [0,1,0]
  if (i==2):
    row3[i]= [0,0,1]
  row4[i]= [a[i][3], 0]

row1[0].extend(row2[0])
row1[0].extend(row3[0])
row1[0].extend(row4[0])
first=row1[0]
row1[1].extend(row2[1])
row1[1].extend(row3[1])
row1[1].extend(row4[1])
second=row1[1]
row1[2].extend(row2[2])
row1[2].extend(row3[2])
row1[2].extend(row4[2])
third=row1[2]
table.loc[len(table)] = first
table.loc[len(table)] = second       
table.loc[len(table)] = third
           

Zj=[0,0,0,0,0,0,0]
for i in range(6):
  Zj[i]= table['Cb'][0]*table['x'+str(i+1)][0]+ table['Cb'][1]*table['x'+str(i+1)][1]+ table['Cb'][2]*table['x'+str(i+1)][2]
Zj[6]= table['Cb'][0]*table['b'][0]+ table['Cb'][1]*table['b'][1]+ table['Cb'][2]*table['b'][2]  
Cj= z+ [0,0,0]
result = [a - b for a, b in zip(Cj, Zj)]
optimized= False


for r in result:
    if (r<=0):
      optimized= True
    else:
      optimized= False
      break

while(optimized== False):
  print(table)
  max, max_index=0, 0
  count=0
  for r in result:
    if (r>max):
      max=r
      max_index= count+1
    count+=1
  pivot_col= table['x'+str(max_index)]
  for i in range(3):
    table['ratio'][i]= float(table['b'][i]/ pivot_col[i])
  min_index=0
  min_value= table['ratio'][0]
  for i in range(3):
    if (table['ratio'][i]<min_value and table['ratio'][i]>=0):
      min_value= table['ratio'][i]
      min_index= i
  pivot_row= table.loc[min_index].values
  pivot_element= table['x'+str(max_index)][min_index]
  for i in range(3):
    if (i==min_index):
      table['Xb'][i]= max_index
      table['Cb'][i]= z[max_index-1]
  for i in range(3):
    if (i==min_index):
      for j in range(6):
        table['x'+str(j+1)][i]= float(table['x'+str(j+1)][i]/pivot_element)
      table['b'][i]= float(table['b'][i]/pivot_element)  
    else:
      for j in range(6):
        table['x'+str(j+1)][i]= table['x'+str(j+1)][i]- float((table['x'+str(j+1)][min_index]*table['x'+str(max_index)][i])/pivot_element) 
      table['b'][i]= table['b'][i]- float((table['b'][min_index]*table['x'+str(max_index)][i])/pivot_element) 
  for i in range(6):
    Zj[i]= table['Cb'][0]*table['x'+str(i+1)][0]+ table['Cb'][1]*table['x'+str(i+1)][1]+ table['Cb'][2]*table['x'+str(i+1)][2]
  Zj[6]= table['Cb'][0]*table['b'][0]+ table['Cb'][1]*table['b'][1]+ table['Cb'][2]*table['b'][2]
  result = [a - b for a, b in zip(Cj, Zj)]
  for r in result:
      if (r<=0):
        optimized= True
      else:
        optimized= False
        break


sum=0
for i in range(3):
  if (table['Xb'][i]<=3):
    n= table['Cb'][i]
    sum+= n*z[table['Xb'][i]-1]
sum  
print('Maximum value of Input expresion is '+ str(sum))     
               
