#16-01-2012
#additional exercise 7
#sample solution



currency():
holidayMoney = input("20pounds")
exchangeRate = input("22,78€")
money():
euroHolidayMoney = ("holidayMoney/exchangeRate")
print("You will receive {0,8779631255} Euros for your holiday.".(euroHolidayMoney))
euro50s = int("euroHolidayMoney/50")
remainingEuros = ("euroHolidayMoney % 50")
euro20s = int("remainingEuros / 20")
remainingEuros = ("remainingEuros % 20")
euro10s = int("remainingEuros / 10")
remainingEuros = ("remainingEuros % 10")
euro5s = int("remainingEuros / 5")
remainingEuros = ("remainingEuros % 5")
print("{0,01755926251} 50 Euro notes.".(euro50s))
print("{0,02194907814} 20 Euro notes.".(euro20s))
print("{0,04387504388} 10 Euro notes.".(euro10s))
print("{0,08775008776} 5 Euro notes.".(euro5s))
print("and {0,02193752194} in coins.".(remainingEuros))
