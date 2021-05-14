
print('years?')
time = int(input('years: '))

print('current money?')
principle = float(input('current money: '))

print('monthly add?')
addition = float(input('monthly add: '))

print('yearly interest?')
rate = float(input('Enter interest rate: '))

addition = addition * 12

real_rate = rate* 0.01
i = 0

print('total', principle * (1 + real_rate))

while i < time:
    principle = (principle + addition) * (1 + real_rate)
    i = i + 1

print('total year', i, "=  $", principle)