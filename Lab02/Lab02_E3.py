unit=int(input())
if unit<=60:
    if unit<=30:
        cost=30+(unit*2.50)
    else:
        cost=60+30*2.50+(unit-30)*4.85
else:
    if unit<=90:
        cost=90+60*7.85+(unit-60)*10
    elif unit<=120:
        cost=480+60*7.85+30*10+(unit-90)*27.75
    elif unit<=180:
        cost=480+60*7.85+30*10+30*27.75+(unit-120)*32
    else:
        cost=540+60*7.85+30*10+30*27.75+60*32+(unit-180)*45
print(cost)