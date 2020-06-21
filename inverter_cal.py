print('Inverter Calculator')
print('Program will calculate: watts hour of a battery, the hours for the battery to ',end='')
print('power a load of certain watts, ',end='')
print('time required to charge the battery, including parallel and series connection')
print('')
print('NOTE: if the values of voltage and current are unknown then multimeter is ',end='')
print('recomemded')
print('')
print('CALCULATING THE WATTS HOUR OF THE BATTERY')
print('')
print('NOTE:If the total value of voltage and current of a solar panel is known ',end='')
print('then the single solar panel option can be chosed')
print('And if the value of voltage and current of each solar panel is known ',end='')
print('then multiple solar panel option can be chosed')
print('')
print('select one option below by pressing the number of option and then press ENTER')
print('1.Single battery')
print('2.Multiple battery')

select=input('option=')
select=int(select)
if select == 1:
    print('Enter the value of voltage below')
    volt_s=input('number of volts=')
    volt_s=float(volt_s)
    print('Enter the value of current below')
    current_s=input('number of current(amphour)=')
    current_s=float(current_s)
    watts_hour=volt_s*current_s
    watts_hour=int(watts_hour)
    print('The amount of watts hour in the battery is', watts_hour,end='')
    print('wh')
    print('')
elif select == 2:
    print('Enter the number of batteries')
    bat_num=input('number of batteries=')
    bat_num=int(bat_num)
    print('Enter the amount of voltage of a single battery below')
    volt_m=input('number of volts=')
    volt_m=float(volt_m)
    print('Enter the amount of current(amphour) of a single battery below')
    current_m=input('number of current(amphour)=')
    current_m=float(current_m)
    print('select one option below by pressing the number of option and then press ENTER')
    print('1.parallel connection')
    print('2.series connection')
    opt=input('option=')
    opt=int(opt)
    if opt == 1:
        current_t=current_m*bat_num
        watts_hour=current_t*volt_m
        watts_hour=int(watts_hour)
        print('The amount of watts hour in the battery is', watts_hour,end='')
        print('wh')
    elif opt == 2:
        volt_t=volt_m*bat_num
        watts_hour=volt_t*current_m
        watts_hour=int(watts_hour)
        print('The amount of watts hour in the battery is',watts_hour,end='')
        print('wh')
    else:
        print('WRONG OPTION, Try again')
else:
    print('WRONG OPTION, Try again')
print('')
print('CALCULATING THE HOURS FOR THE BATTERY TO POWER A LOAD OF CERTAIN WATTS')
print('')
print('Enter the amount of watt of the load')
load_watts=input('amount of load_watt=')
load_watts=int(load_watts)
hours_to_power=watts_hour/load_watts
hours_to_power=float(hours_to_power)
print('The hours that will take a',watts_hour,'wh battery', 'to power a',load_watts,end='')
print('w load is', hours_to_power,'hrs')
print('')
print('CALCULATING HOW LONG WILL IT TAKE THE SOLAR PANELS TO CHARGE',watts_hour,'BATTERY')
print('')
print('NOTE:If the total value of voltage and current of a solar panel is known ',end='')
print('then the single solar panel option can be chosed')
print('And if the value of voltage and current of each solar panel is known ',end='')
print('then multiple solar panel option can be chosed')
print('')
print('select one option below by pressing the number of option and then press ENTER')
print('1.Single solar panel')
print('2.Multiple solar panel')
select_p=input('option=')
select_p=int(select_p)
if select_p == 1:
    print('Enter the value of solar panel voltage below')
    volt_p=input('number of solar panel volts=')
    volt_p=float(volt_p)
    print('Enter the value of solar panel current below')
    current_p=input('number of solar panel current=')
    current_p=float(current_p)
    solar_p_watts=volt_p*current_p
    print('most of solar panels outlet 70% its energy, therefore...')
    solar_p_watts=solar_p_watts*.7
    solar_p_watts=int(solar_p_watts)
    print('The amount of watts hour in the battery is', solar_p_watts,end='')
    print('w')
    print('')
elif select_p == 2:
    print('Enter the number of solar panels')
    panel_num=input('number of solar panels=')
    panel_num=int(panel_num)
    print('Enter the amount of voltage of a single solar panel below')
    volt_p=input('number of solar panel volts =')
    volt_p=float(volt_p)
    print('Enter the amount of current of a single solar panel below')
    current_p=input('number of solar panel current=')
    current_p=float(current_p)
    print('select one option below by pressing the number of option and then press ENTER')
    print('1.parallel connection')
    print('2.series connection')
    opt_p=input('option=')
    opt_p=int(opt_p)
    if opt_p == 1:
        current_st=current_p*panel_num
        solar_p_watts=current_st*volt_p
        print('most of solar panels outlet 70% its energy, therefore...')
        solar_p_watts=solar_p_watts*.7
        solar_p_watts=int(solar_p_watts)
        print('The amount of watts hour contained in the soler panel is', solar_p_watts,end='')
        print('wh')
    elif opt_p == 2:
        volt_st=volt_p*panel_num
        solar_p_watts=volt_st*current_p
        print('most of solar panels outlet 70% its energy, therefore...')
        solar_p_watts=solar_p_watts*.7
        solar_p_watts=int(solar_p_watts)
        print('The amount of watts hour contained in the soler panel is',solar_p_watts,end='')
        print('w')
    else:
        print('WRONG OPTION, Try again')
else:
    print('WRONG OPTION, Try again')

hours_to_charged = watts_hour / solar_p_watts
print('It will take',hours_to_charged,end='')
print('hrs to be charged')
print('END')
    

