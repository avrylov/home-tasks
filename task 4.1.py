import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from scipy.stats import expon
import scipy.stats as sts

#t - время между наступлениями редких событий-
# - 10 часов - интервал между красными бентли возле лубянки в центре москвы, 
#происходящих в среднем с интенсивностью lmbda, тогда величина t 
#имеет экспоненциальное распределение с параметром lmbda. 
lmbda=1./10
#экспоненциальное распределение задается следующим образом expon(loc,scale)
#loc=0 (default parameter)
#The scale parameter is equal to scale = 1.0 / lambda. - взято от сюда 
#https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.expon.html

#первая часть задания

loc=0
scale=1./lmbda
expon_rv = expon(loc, scale)#зададим непрерывное распределение с параметрами loc, scale
r = expon_rv.rvs(size=1000)#1000 случ значений

x = np.linspace(0,40)#задаем числовую ось абцисс, будем пользоваться ей в дальнейших построениях

pdf = expon_rv.pdf(x)#функция исходной плотности случайной величины (rv - random variable)
plt.plot(x, pdf, label='theoretical PDF')#выводим на печать график исходной плотности rv
plt.hist(r, bins=20, normed=True, label='hist of expon')#оцениваем исходную функцию с помощью гисторграммы,
                                                        #по объему случ величин r=1000

#вторая часть задания

n1=5#выборка объема 5
n2=10#выборка объема 10
n3=50#выборка объема 50

norm_mu=1./lmbda #Математическое ожидание по ЦПТ для expon распред(взято из вики),
                    # пригодится для дальнейшего построения графика.
                    #не зависит от объема выборки

h1=[]#откроем пустую матрицу
for i1 in np.arange(1,1001):#сделаем тысячу строк
    sample1 = expon_rv.rvs(n1)#для каждой строки посчитаем rv, объема выборки n1 
    h1.append(sample1)#посчитанные знач для тысячи строк объеденим в пустой матрице
l1=np.array(h1)#получаем матрицу размерности (1000L, 5L), т.е. 1000 строк и 5 столбцов

avrg1=np.mean(l1, axis = 1) #считаем среднее для каждой строки 
                            #и получаем выборочное среднее для объема выборки 5

sigma_in_power1 = (1./lmbda**2)/n1 #Дисперсия по ЦПТ (взято из вики\лекций)
sigma1=sqrt(sigma_in_power1) #Стандартное отклонение по ЦПТ (взято из вики\лекций)

norm_rv1 = sts.norm(norm_mu,sigma1) #нормальное распределения по ЦПТ объема выборки 5

pdf1 = norm_rv1.pdf(x) #функция плотности нормального распределения по ЦПТ объема выборки 5
plt.plot(x, pdf1, label='norm PDF n1') #выводим на печать график плотности rv объма выборки 5
plt.hist(avrg1, bins=15, normed=True, label='hist of expon avrg1') #оцениваем плотности rv объма выборки 5
                                        #с помощью гистограммы по выборочному среднему

#повторяем аналогичные действия для выборок объема n2,n3

h2=[]
for i2 in np.arange(1,1001):
    sample2 = expon_rv.rvs(n2)
    h2.append(sample2)
l2=np.array(h2)

avrg2=np.mean(l2, axis = 1)

sigma_in_power2 = (1./lmbda**2)/n2
sigma2=sqrt(sigma_in_power2)

norm_rv2 = sts.norm(norm_mu,sigma2)

pdf2 = norm_rv2.pdf(x)
plt.plot(x, pdf2, label='norm PDF n2')
plt.hist(avrg2, bins=15, normed=True, label='hist of expon avrg2')



h3=[]
for i3 in np.arange(1,1001):
    sample3 = expon_rv.rvs(n3)
    h3.append(sample3)
l3=np.array(h3)

avrg3=np.mean(l3, axis = 1)

sigma_in_power3 = (1./lmbda**2)/n3
sigma3=sqrt(sigma_in_power3) 

norm_rv3 = sts.norm(norm_mu,sigma3) 

pdf3 = norm_rv3.pdf(x)
plt.plot(x, pdf3, label='norm PDF n3')
plt.hist(avrg3, bins=15, normed=True, label='hist of expon avrg3')


plt.ylabel('$probability not to meet bently$')#подписываем оси
plt.xlabel('$hours$')
plt.legend(loc='upper right')#расположения описания на графике

#Вывод:
#1.Уже при объеме выборки 5 распределение становится унимодальным (один пик, два спуска)
#2.Что распределение выборочных средних хорошо описывается нормальным распределением.
#3.C ростом n - выборочное среднее приближается к математическому ожиданию исходного распределения.
print "Мат ожидание исх-го распред-ия=", norm_mu

sum=0
for i in avrg1:
    sum+=i
avrg1_1=sum/1000.
print "Выборочное среднее объема выборки n1=", round(avrg1_1,3)

sum=0
for i in avrg2:
    sum+=i
avrg2_2=sum/1000.
print "Выборочное среднее объема выборки n2=", round(avrg2_2,3)

sum=0
for i in avrg3:
    sum+=i
avrg3_3=sum/1000.
print "Выборочное среднее объема выборки n3=", round(avrg3_3,3)
#4.Точность аппроксимации распределения выборочных средних нормальным с ростом n - 
#увеличивается и приближается к нормальному.