#Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых 
# (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
#Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

def bank(start_money,years,percents):
    for i in range(years):
        start_money=start_money+start_money*percents
    return start_money

start_money=int(input('Введите сууму вклада = '))
years=int(input('Введите срок, на который открывается вклад years= '))
percents=float(input('Введите процентную ставку percents= '))
print(float(bank(start_money,years,percents))) 

def bank1(a,years,pr):
        a=a*(1+pr)**years
        return a
a=int(input('Введите сууму вклада а= '))
year=int(input('Введите срок, на который открывается вклад year= '))
pr=float(input('Введите процентную ставку pr= '))
print(float(bank1(a,year,pr))) 

bank=bank(a,years,pr)
def get_money(s)
