import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('obesity.csv')

print(df.info())

usaData = df[df['Entity'] == 'United States']
russiaData = df[df['Entity'] == 'Russia']

figure = plt.figure(figsize=(10,10))
figure2 = plt.figure(figsize=(10,10))
figure3 = plt.figure(figsize=(10,10))

axes1 = figure.add_subplot(2,2, 1)
axes2 = figure.add_subplot(2,2, 2)
axes3 = figure2.add_subplot()
axes4 = figure3.add_subplot()

axes3.plot(usaData['Year'], usaData['Indicator:Prevalence of obesity among adults, BMI &GreaterEqual; 30 (crude estimate) (%) - Sex:Both sexes'],
           label='США',
           color='red',
           linewidth=2)
axes3.plot(russiaData['Year'], russiaData['Indicator:Prevalence of obesity among adults, BMI &GreaterEqual; 30 (crude estimate) (%) - Sex:Both sexes'],
           label='Россия',
           color='blue',
           linewidth=2)
axes3.set_title('Сравнение ожирения в США и России')
axes3.set_xlabel('Год')
axes3.set_ylabel('Ожирение (%)')
axes3.grid()
axes3.legend()

axes1.plot(usaData['Year'], usaData['Indicator:Prevalence of obesity among adults, BMI &GreaterEqual; 30 (crude estimate) (%) - Sex:Both sexes'],
           color='red',
           linewidth=2,
           label='США')
axes1.set_title('США')
axes1.set_xlabel('Год')
axes1.set_ylabel('Ожирение (%)')
axes1.grid()
axes1.legend()

axes2.plot(russiaData['Year'], russiaData['Indicator:Prevalence of obesity among adults, BMI &GreaterEqual; 30 (crude estimate) (%) - Sex:Both sexes'],
           linewidth=2,
           label='Россия',
           color='blue')
axes2.set_title('Россия')
axes2.set_xlabel('Год')
axes2.set_ylabel('Ожирение (%)')
axes2.grid()
axes2.legend()

russiaData = russiaData.drop(columns=['Code', 'Entity'])
russiaData = russiaData.rename(columns={"Indicator:Prevalence of obesity among adults, BMI &GreaterEqual; 30 (crude estimate) (%) - Sex:Both sexes": "BMI RUS"}).reset_index()
print('Данные russiaData ниже:')
russiaData = russiaData.reset_index(drop=True) # new
print(russiaData.head(10))

usaData = usaData.drop(columns=['Entity', 'Code', 'Year'])
usaData = usaData.rename(columns={"Indicator:Prevalence of obesity among adults, BMI &GreaterEqual; 30 (crude estimate) (%) - Sex:Both sexes": "BMI USA"}).reset_index()
usaData = usaData.reset_index(drop=True) # new
print('Данные usaData ниже:')
print(usaData.head(10))


hopelessData = pd.concat([russiaData, usaData])
hopelessData['BMI USA'] = usaData['BMI USA']
print('Данные ниже с RU and USA:')
print(hopelessData.head(10))


print("Проверка")
hopelessData = hopelessData.drop(columns=['index'])
print(hopelessData.info())
print(hopelessData.head(10))
corrData = hopelessData.corr()
print(corrData)


# hopelessData.index = pd.MultiIndex.from_tuples(hopelessData.values.tolist(), names=hopelessData.colums) # не работает MultiIndex


# print('Данные ниже х2:')
# print(combined_data.head(10))
#print("%%%")

# Создание тепловой карты
sns.heatmap(corrData, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1,vmax=1) # работает, но не так как надо
axes4.set_title('Корреляция')


plt.show()


