#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt


# In[2]:


df0 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210501.txt')
df0 = pd.DataFrame(df0)

df1 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210508.txt')
df1 = pd.DataFrame(df1)

df2 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210515.txt')
df2 = pd.DataFrame(df2)

df3 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210522.txt')
df3 = pd.DataFrame(df3)

df4 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210529.txt')
df4 = pd.DataFrame(df4)

df5 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210605.txt')
df5 = pd.DataFrame(df5)

df6 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210612.txt')
df6 = pd.DataFrame(df6)

df7 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210619.txt')
df7 = pd.DataFrame(df7)

df8 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210626.txt')
df8 = pd.DataFrame(df8)

df9 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210703.txt')
df9 = pd.DataFrame(df9)

df10 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210710.txt')
df10 = pd.DataFrame(df10)

df11 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210717.txt')
df11 = pd.DataFrame(df11)

df12 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210724.txt')
df12 = pd.DataFrame(df12)

df13 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210731.txt')
df13 = pd.DataFrame(df13)

df14 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210807.txt')
df14 = pd.DataFrame(df14)

df15 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210814.txt')
df15 = pd.DataFrame(df15)

df16 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210821.txt')
df16 = pd.DataFrame(df16)

df17 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_210828.txt')
df17 = pd.DataFrame(df17)

df18 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200502.txt')
df18 = pd.DataFrame(df18)

df19 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200509.txt')
df19 = pd.DataFrame(df19)

df20 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200516.txt')
df20 = pd.DataFrame(df20)

df21 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200523.txt')
df21 = pd.DataFrame(df21)

df22 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200530.txt')
df22 = pd.DataFrame(df22)

df23 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200606.txt')
df23 = pd.DataFrame(df23)

df24 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200613.txt')
df24 = pd.DataFrame(df24)

df25 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200620.txt')
df25 = pd.DataFrame(df25)

df26 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200627.txt')
df26 = pd.DataFrame(df26)

df27 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200704.txt')
df27 = pd.DataFrame(df27)

df28 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200711.txt')
df28 = pd.DataFrame(df28)

df29 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200718.txt')
df29 = pd.DataFrame(df29)

df30 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200725.txt')
df30 = pd.DataFrame(df30)

df31 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200801.txt')
df31 = pd.DataFrame(df31)

df32 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200808.txt')
df32 = pd.DataFrame(df32)

df33 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200815.txt')
df33 = pd.DataFrame(df33)

df34 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200822.txt')
df34 = pd.DataFrame(df34)

df35 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_200829.txt')
df35 = pd.DataFrame(df35)

df36 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190504.txt')
df36 = pd.DataFrame(df36)

df37 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190511.txt')
df37 = pd.DataFrame(df37)

df38 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190518.txt')
df38 = pd.DataFrame(df38)

df39 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190525.txt')
df39 = pd.DataFrame(df39)

df40 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190601.txt')
df40 = pd.DataFrame(df40)

df41 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190608.txt')
df41 = pd.DataFrame(df41)

df42 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190615.txt')
df42 = pd.DataFrame(df42)

df43 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190622.txt')
df43 = pd.DataFrame(df43)

df44 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190629.txt')
df44 = pd.DataFrame(df44)

df45 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190706.txt')
df45 = pd.DataFrame(df45)

df46 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190713.txt')
df46 = pd.DataFrame(df46)

df47 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190720.txt')
df47 = pd.DataFrame(df47)

df48 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190727.txt')
df48 = pd.DataFrame(df48)

df49 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190803.txt')
df49 = pd.DataFrame(df49)

df50 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190810.txt')
df50 = pd.DataFrame(df50)

df51 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190817.txt')
df51 = pd.DataFrame(df51)

df52 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190824.txt')
df52 = pd.DataFrame(df52)

df53 = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_190831.txt')
df53 = pd.DataFrame(df53)




df2021 = pd.concat([df0, df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17], ignore_index = True)

df2020 =pd.concat([df18, df19, df20, df21, df22, df23, df24, df25, df26, df27, df28, df29, df30, df31, df32, df33, df34, df35], ignore_index = True)

df2019 =pd.concat([df36, df37, df38, df39, df40, df41, df42, df43, df44, df45, df46, df47, df48, df49, df50, df51, df52, df53], ignore_index = True)

df=pd.concat([df2021, df2020, df2019])


# In[3]:


df.info() ####11 kolonumuz var


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


print(df.isnull().sum()) ###null değerleri kontrol ediyoruz


# In[7]:


df.columns


# In[8]:


df.columns=df.columns.str.strip()


# In[9]:


df['TIMESTAMP'] = pd.to_datetime(df['DATE'] + ' ' + df['TIME'])


# In[10]:


df.info()


# In[11]:


df['WEEKDAYS'] = pd.to_datetime(df['DATE']).dt.day_name()
df.head()


# In[12]:


df.info()


# In[13]:


df["TURNSTILE"] = df["C/A"]+"-"+df["UNIT"]+"-"+df["SCP"]


# In[14]:


df.columns


# In[15]:


df.head(5)


# In[16]:


df.shape


# In[17]:


###Duplicate var ise sil
df.drop_duplicates(subset=None, keep="first", inplace=True)


# In[18]:


df.shape


# In[19]:


df.describe()


# In[20]:


df.info()


# In[21]:


df.head()


# In[22]:


df = df[["STATION","TURNSTILE","DATE","TIME", "TIMESTAMP","ENTRIES","EXITS", "WEEKDAYS"]]


# In[23]:


df.info()


# In[24]:


print("Maximum date: ")
print(df["TIMESTAMP"].max())
print()
print("Minimum date: ")
print(df["TIMESTAMP"].min())


# In[25]:


len(df["STATION"].unique())


# In[26]:


len(df["TURNSTILE"].unique())


# In[27]:


print("Row count based on stations (First 10 rows)")
print(df["STATION"].value_counts().sort_values(ascending=False).head(10))


# In[28]:


df['NET_ENTRIES'] = df.ENTRIES.shift(-1) - df.ENTRIES
df['NET_EXITS'] = df.EXITS.shift(-1) - df.EXITS


# In[29]:


df.head(50)


# In[30]:


###Veriyi anlayabilmek için tanımlayıcı istatistiklerine bakalım
print("Descriptive Statistics for NET_ENTRIES column:") 
print(df["NET_ENTRIES"].describe())
print("Descriptive Statistics for NET_EXITS column:")
print(df["NET_EXITS"].describe())


# In[31]:


pd.options.display.float_format='{:.5f}'.format


# In[32]:


df.describe()


# In[33]:


df.columns


# In[34]:


df.shape


# In[35]:


###Negatif değerler NET_ENTRIES ve NET_EXITSte kaç tane var
print("Negative values for NET_ENTRIES column: ")
print(len(df[df["NET_ENTRIES"]<0]))
print("Negative values for NET_EXITS column:")
print(len(df[df["NET_EXITS"]<0]))


# In[36]:


###Boş olanlara 0 ata. Negatif ve de %95 güven aralığının üstünde olan değerlere median değerlerini atadık
df['NET_ENTRIES'][df['NET_ENTRIES'] < 0] = (df["NET_ENTRIES"].median())
df['NET_EXITS'][df['NET_EXITS'] < 0] = (df["NET_EXITS"].median())
df['NET_ENTRIES'][df['NET_ENTRIES'] > (df["NET_ENTRIES"].quantile(0.95))] = (df["NET_ENTRIES"].median()) 
df['NET_EXITS'][df['NET_EXITS'] > (df["NET_EXITS"].quantile(0.95))] = (df["NET_EXITS"].median()) 


# In[37]:


pd.options.display.float_format='{:.5f}'.format


# In[38]:


print("Descriptive Statistics for NET_ENTRIES column:")
print(df["NET_ENTRIES"].describe())
print("Descriptive Statistics for NET_EXITS column:")
print(df["NET_EXITS"].describe())


# In[39]:


df["TRAFFIC"] = df["NET_ENTRIES"] + df["NET_EXITS"]


# In[40]:


df.info()


# In[41]:


df.head(50) 


# In[42]:


df.TRAFFIC.describe()


# In[43]:


df.TRAFFIC.value_counts()


# In[44]:


df['WEEKDAYS_INDEX'] = pd.to_datetime(df['DATE']).dt.weekday
df.head()


# In[45]:


busiest_stations = df.groupby("STATION").sum().sort_values("TRAFFIC", ascending = False).reset_index().head(10)
busiest_stations.head(10)


# In[46]:


plt.figure(figsize=(10,6),dpi=200)
plt.bar(busiest_stations.STATION, busiest_stations.TRAFFIC)
plt.xticks(rotation=45, ha='right');
plt.xlabel("STATIONS")
plt.ylabel("TOTAL TRAFFIC")
plt.title("TOP 10 BUSIEST STATIONS FOR 2019-2021", family='serif',fontsize = 15,loc='center',color='r')


# In[47]:


plt.figure(figsize=(10,6),dpi=200)
plt.barh(busiest_stations.STATION, busiest_stations.TRAFFIC, color=['blue', 'orange', 'orange', 'orange', 'orange','orange','orange','orange','orange','orange']);
plt.gca().invert_yaxis()
plt.xlabel("TOTAL TRAFFIC")
plt.ylabel(" ")
plt.title("TOP 10 BUSIEST STATIONS 2019-2021", family='serif',fontsize = 15,loc='center',color='r')
for index, value in enumerate(busiest_stations.TRAFFIC):
    plt.text(value, index,
             str(value))


# In[48]:


plt.figure(figsize=(10,6),dpi=200)
sns.set_style("whitegrid")
sns.barplot(y = 'STATION', x = 'TRAFFIC', data = busiest_stations)
plt.xlabel("TOTAL TRAFFIC")
plt.ylabel(" ")
plt.title("TOP 10 BUSIEST STATIONS FOR 2019-2021", family='serif',fontsize = 15,loc='center',color='r')
for index, value in enumerate(busiest_stations.TRAFFIC):
    plt.text(value, index,
             str(value))


# In[ ]:


busiest_days = df.groupby("WEEKDAYS").sum().sort_values("WEEKDAYS_INDEX", ascending = True).reset_index()
busiest_days


# In[ ]:


plt.figure(figsize=(10,6),dpi=200)
plt.bar(busiest_days.WEEKDAYS, busiest_days.TRAFFIC, color=['red' if x < 50000000 else 'blue' for x in busiest_days.TRAFFIC.values]);
plt.xlabel(" ")
plt.ylabel("TOTAL TRAFFIC")
plt.title("TOTAL TRAFFIC ACCORDING TO WEEKDAYS 2019-2021", family='serif',fontsize = 15,loc='center',color='r')


# In[ ]:


plt.figure(figsize=(12,8),dpi=200)
sns.set_style("whitegrid")
sns.barplot(x = 'WEEKDAYS', y = 'TRAFFIC', data = busiest_days)
plt.ylabel("TOTAL TRAFFIC")
plt.xlabel(" ")
plt.title("TOTAL TRAFFIC ACCORDING TO WEEKDAYS 2019-2021", family='serif',fontsize = 15,loc='center',color='r')


# In[ ]:


busiest_times = df.groupby("TIME").sum().sort_values("TRAFFIC", ascending = False).reset_index()

for i in range(len(busiest_times)):
    
    if busiest_times['TIME'][i] < ('04:00:00'):
        busiest_times['TIME'][i] =  ('00:00 - 04:00')
    
    elif ('04:00:00') <= busiest_times['TIME'][i] < ('08:00:00'):
        busiest_times['TIME'][i] =  ('04:00 - 08:00')
    
    elif ('08:00:00') <= busiest_times['TIME'][i] < ('12:00:00'):
        busiest_times['TIME'][i] =  ('08:00 - 12:00')
    
    elif ('12:00:00') <= busiest_times['TIME'][i] < ('16:00:00'):
        busiest_times['TIME'][i] =  ('12:00 - 16:00')
    
    elif ('16:00:00') <= busiest_times['TIME'][i] < ('20:00:00'):
        busiest_times['TIME'][i] =  ('16:00 - 20:00')
    
    elif ('20:00:00') <= busiest_times['TIME'][i]:
        busiest_times['TIME'][i] =  ('20:00 - 00:00')
        
    i = i + 1

busiest_times


# In[ ]:


busiest_times = busiest_times.groupby("TIME").sum().sort_values("TRAFFIC", ascending = False).reset_index()
busiest_times


# In[ ]:


plt.figure(figsize=(10,6),dpi=200)
sns.set_style("whitegrid")

sns.barplot(x = 'TIME', y = 'TRAFFIC', data = busiest_times, order = ['00:00 - 04:00', '04:00 - 08:00', '08:00 - 12:00', '12:00 - 16:00', '16:00 - 20:00', '20:00 - 00:00'])
plt.xlabel(" ")
plt.ylabel("TOTAL TRAFFIC")
plt.title("TOTAL TRAFFIC ACCORDING TO TIMES OF DAY 2019-2021", family='serif',fontsize = 15,loc='center',color='r')



# In[ ]:


plt.figure(figsize=(12,8),dpi=200)
plt.pie(busiest_times.TRAFFIC,labels= busiest_times.TIME, autopct='%.0f%%', explode = [.1,0,0,0,0,0])
plt.title("TOTAL TRAFFIC ACCORDING TO TIMES OF DAY 2019-2021", family='serif',fontsize = 15,loc='center',color='r')


# In[ ]:


busiest_stations_weekdays = df.groupby(['STATION','WEEKDAYS',"WEEKDAYS_INDEX"]).agg({'TRAFFIC':'sum'}).reset_index()[["STATION","WEEKDAYS","TRAFFIC","WEEKDAYS_INDEX"]]
busiest_stations_weekdays


# In[ ]:


station1 = busiest_stations_weekdays[ busiest_stations_weekdays.loc[: , "STATION"] == "34 ST-PENN STA" ].sort_values("WEEKDAYS_INDEX",ascending = True)
station1


# In[ ]:


station2 = busiest_stations_weekdays[ busiest_stations_weekdays.loc[: , "STATION"] == "23 ST" ].sort_values("WEEKDAYS_INDEX",ascending = True)
station2


# In[ ]:


station3 = busiest_stations_weekdays[ busiest_stations_weekdays.loc[: , "STATION"] == "FULTON ST" ].sort_values("WEEKDAYS_INDEX",ascending = True)
station3


# In[ ]:


station4 = busiest_stations_weekdays[ busiest_stations_weekdays.loc[: , "STATION"] == "86 ST" ].sort_values("WEEKDAYS_INDEX",ascending = True)
station4


# In[ ]:


station5 = busiest_stations_weekdays[ busiest_stations_weekdays.loc[: , "STATION"] == "125 ST" ].sort_values("WEEKDAYS_INDEX",ascending = True)
station5


# In[ ]:


station6 = busiest_stations_weekdays[ busiest_stations_weekdays.loc[: , "STATION"] == "34 ST-HERALD SQ" ].sort_values("WEEKDAYS_INDEX",ascending = True)
station6


# In[ ]:


station7 = busiest_stations_weekdays[ busiest_stations_weekdays.loc[: , "STATION"] == "GRD CNTRL-42 ST" ].sort_values("WEEKDAYS_INDEX",ascending = True)
station7


# In[ ]:


station8 = busiest_stations_weekdays[ busiest_stations_weekdays.loc[: , "STATION"] == "TIMES SQ-42 ST" ].sort_values("WEEKDAYS_INDEX",ascending = True)
station8


# In[ ]:


station9 = busiest_stations_weekdays[ busiest_stations_weekdays.loc[: , "STATION"] == "42 ST-PORT AUTH" ].sort_values("WEEKDAYS_INDEX",ascending = True)
station9


# In[ ]:


station10 = busiest_stations_weekdays[ busiest_stations_weekdays.loc[: , "STATION"] == "59 ST" ].sort_values("WEEKDAYS_INDEX",ascending = True)
station10


# In[ ]:


stations = [station1, station2, station3 ,station4 ,station5]
stations_for_tourists = pd.concat(stations)
stations_for_tourists


# In[ ]:


fig, ax = plt.subplots(figsize=(12,8))

sns.lineplot(data=stations_for_tourists, x="WEEKDAYS", y="TRAFFIC", hue="STATION")

ax.axvspan("Wednesday", "Thursday", alpha=0.15, color='blue')

plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)

plt.title("TOTAL TRAFFIC OF TOP 5 STATIONS BY WEEKDAYS FOR 2019-2021", family='serif',fontsize = 15,loc='center',color='r')


# In[ ]:


Most_Busiest_Station = df[df['STATION'] == '34 ST-PENN STA']
Most_Busiest_Station


# In[ ]:


for i in range(len(Most_Busiest_Station['TIME'].index)):
    
    if Most_Busiest_Station['TIME'][Most_Busiest_Station['TIME'].index[i]] < ('04:00:00'):
        Most_Busiest_Station['TIME'][Most_Busiest_Station['TIME'].index[i]] =  ('00:00 - 04:00')
    
    elif ('04:00:00') <= Most_Busiest_Station['TIME'][Most_Busiest_Station['TIME'].index[i]] < ('08:00:00'):
        Most_Busiest_Station['TIME'][Most_Busiest_Station['TIME'].index[i]] =  ('04:00 - 08:00')
    
    elif ('08:00:00') <= Most_Busiest_Station['TIME'][Most_Busiest_Station['TIME'].index[i]] < ('12:00:00'):
        Most_Busiest_Station['TIME'][Most_Busiest_Station['TIME'].index[i]] =  ('08:00 - 12:00')
    
    elif ('12:00:00') <= Most_Busiest_Station['TIME'][Most_Busiest_Station['TIME'].index[i]] < ('16:00:00'):
        Most_Busiest_Station['TIME'][Most_Busiest_Station['TIME'].index[i]] =  ('12:00 - 16:00')
    
    elif ('16:00:00') <= Most_Busiest_Station['TIME'][Most_Busiest_Station['TIME'].index[i]] < ('20:00:00'):
        Most_Busiest_Station['TIME'][Most_Busiest_Station['TIME'].index[i]] =  ('16:00 - 20:00')
    
    elif ('20:00:00') <= Most_Busiest_Station['TIME'][Most_Busiest_Station['TIME'].index[i]]:
        Most_Busiest_Station['TIME'][Most_Busiest_Station['TIME'].index[i]] =  ('20:00 - 00:00')
        
    i = i + 1
    
Most_Busiest_Station


# In[ ]:


BT_of_MBS = Most_Busiest_Station.groupby(["TIME","WEEKDAYS","WEEKDAYS_INDEX"]).agg({'TRAFFIC':'sum'}).reset_index()[["TIME","WEEKDAYS","TRAFFIC","WEEKDAYS_INDEX"]]
BT_of_MBS


# In[1]:


plt.figure(figsize=(12,8),dpi=200)

revels = BT_of_MBS.pivot("TIME", "WEEKDAYS_INDEX", "TRAFFIC")

revels.columns = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

ax = sns.heatmap(revels, linewidths=0.4, cmap="Oranges")

ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
plt.xlabel(' ')
plt.ylabel(' ')

plt.title("BUSIEST DAYS AND TIMES FOR 34 ST-PENN STATION 2019-2021", family='serif',fontsize = 15,loc='center',color='Red')
plt.show()


# In[ ]:




