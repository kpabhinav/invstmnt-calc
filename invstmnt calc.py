from re import S


def investment_calculation(P,R,T):
    S = P * (1+ (R/100)*T)
    return S

P = float(input("Enter initial value: "))
R = float(input("Enter the annual interest rate in percentage: "))
T = float(input("Enter the total year of investment: "))

print(investment_calculation(P,R,T), S)