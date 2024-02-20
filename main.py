import pandas as pd
import matplotlib.pyplot as plt
import seaborn

df = pd.read_csv('obesity.csv')

print(df.info())

usaData = df[df['Entity'] == 'United States']
russiaData = df[df['Entity'] == 'Russia']

figure = plt.figure(figsize=(10,5))
figure2 = plt.figure(figsize=(10,10))


axes1 = figure.add_subplot(1,2, 1)
axes2 = figure.add_subplot(1,2, 2)
axes3 = figure2.add_subplot()


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


plt.show()


