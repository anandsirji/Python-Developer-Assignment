import pandas as pd

#Creating the first dataframe of sheet=2
df1=pd.read_excel("Python_Assignment.xlsx",sheet_name=1,usecols="D:G")
df1=df1.iloc[9:31]
df1.index=range(len(df1))
df1.columns=df1.iloc[0]
df1=df1.drop(index=0)

#Creating the first dataframe of sheet=3
df2=pd.read_excel("Python_Assignment.xlsx",sheet_name=2,usecols="C:G")
df2=df2.iloc[6:30]
df2.columns=df2.iloc[0]
df2.drop(index=6,inplace=True)
df2.index=range(len(df2))
df2.columns=["S No","Name","User ID","total_statements","total_reasons"]

#Merging the two data frames into one
df=pd.merge(left=df1,right=df2,on=["S No","Name","User ID"])

#Taking part of data frame for team ranking
s1=df[["S No","Team Name","total_statements","total_reasons"]]
s2=s1["Team Name"]
s2.drop_duplicates(keep="first")
t_statements=[]
t_reasons=[]
for i in s2:
    t_statements.append(round(s1[s1.eq(i).any(axis=1)]["total_statements"].mean(),ndigits=2))
    t_reasons.append(round(s1[s1.eq(i).any(axis=1)]["total_reasons"].mean(),ndigits=2))
s2.index=range(len(s2))
s3=pd.DataFrame({"Team_Name":s2,"Average_Statements":t_statements,"Average Reasons":t_reasons},index=range(len(s2)))
s3.sort_values(by=["Average_Statements","Average Reasons"],ascending=False,inplace=True)

#Taking part of data frame for indivisual ranking

df.sort_values(by=["total_statements","total_reasons"],ascending=False,inplace=True)
df.index=range(len(df))
df.index.name="Rank"
r_df=df[["Name","User ID","total_statements","total_reasons"]]

#Using both data frames two create output sheets in a single excel file
with pd.ExcelWriter('output.xlsx') as writer:
    s3.to_excel(writer, sheet_name='Sheet_name_1')
    r_df.to_excel(writer, sheet_name='Sheet_name_2')
