import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('C:/Users/gp/Desktop/ml/StudentsPerformance.csv - StudentsPerformance.csv.csv')
co1=['gender','race/ethnicity','parental level of education','lunch','test preparation course']
col2=['math score','reading score','writing score']
df=data.iloc[:,5:8]


plt.figure(figsize = [20, 20])

plt.subplot(3, 3, 1)
[b,t]=pd.value_counts(data['gender'])
phase1=[b,t]
phase2=['male','female']
plt.title("Gender")
plt.xlabel("Gender")
plt.ylabel("counts")
plt.grid(True)
plt.bar(phase2,phase1,width=0.5)


plt.subplot(3, 3, 2)
[a,B,c,d,e]=pd.value_counts(data['race/ethnicity'])
ph1=[a,B,c,d,e]
ph2=['Group A ','Group B','Group C','Group D','Group E']
plt.title("race/ethnicity")
plt.xlabel("Groups")
plt.ylabel("counts")
plt.grid(True)
plt.bar(ph2,ph1,width=0.5)



plt.subplot(3, 3, 3)
[f,g,h,i,j,k]=pd.value_counts(data['parental level of education'])
pha1=[f,g,h,i,j,k]
pha2=['bachelors degree','some college','masters degree','associates degree','high school','some high school']
plt.title("parental level of education")
plt.xlabel("Education")
plt.ylabel("counts")
plt.grid(True)
plt.bar(pha2,pha1,width=0.5)



plt.subplot(3, 3, 4)
[l,m]=pd.value_counts(data['lunch'])
phas1=[l,m]
phas2=['standard','free/reduced']
plt.title("lunch")
plt.xlabel("TYpes of lunch")
plt.ylabel("counts")
plt.grid(True)
plt.bar(phas2,phas1,width=0.5)


plt.subplot(3, 3, 5)
[n,o]=pd.value_counts(data['test preparation course'])
phas11=[n,o]
phas22=['none','completed']
plt.title("test preparation course")
plt.xlabel("TYpes")
plt.ylabel("counts")
plt.grid(True)
plt.bar(phas22,phas11,width=0.5)


plt.figure(figsize = [20, 20])
plt.subplot(2, 2, 1)
sns.boxplot(x=df['math score'])

plt.subplot(2, 2, 2)
sns.boxplot(x=df['reading score'])

plt.subplot(2, 2, 3)
sns.boxplot(x=df['writing score'])




plt.figure(figsize = [10, 10]) # larger figure size for subplots
bins=[0,10,20,30,40,50,60,70,80,90,100]

# example of somewhat too-large bin size
plt.subplot(2, 2, 1) # 1 row, 2 cols, subplot 1
plt.title("Histogram")
plt.xlabel("Range of Math scores")
plt.ylabel("No of people")
plt.hist(df['math score'],bins,histtype='bar',rwidth=0.9)

plt.subplot(2, 2, 2) # 1 row, 2 cols, subplot 1
plt.title("Histogram")
plt.xlabel("Range of reading scores")
plt.ylabel("No of people")
plt.hist(df['reading score'],bins,histtype='bar',rwidth=0.9)

plt.subplot(2, 2, 3) # 1 row, 2 cols, subplot 1
plt.title("Histogram")
plt.xlabel("Range of Writing scores")
plt.ylabel("No of people")
plt.hist(df['writing score'],bins,histtype='bar',rwidth=0.9)


df['percentage']=round((df['math score'] + df['reading score'] + df['writing score'])/ 3, 2)

data['percentage']=df['percentage']
                      
sns.catplot(x='parental level of education',y=df['percentage'],kind='point',ci=None,order=None ,data=data)
plt.xticks(rotation=90)
plt.show()


plt.figure(figsize = [20, 20])
plt.subplot(2, 2, 1)
sns.barplot(x=data['gender'],y=data['percentage'])


plt.figure(figsize=(10,10))
sns.heatmap(data.corr(),annot=True,fmt='.0%')
