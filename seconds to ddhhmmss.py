# Converts seconds to DD:HH:MM:SS format

user_input = int(input("Seconds: "))

days = int(user_input // 60 // 60 // 24 % 365)
hours = int(user_input // 60 // 60 % 24)
mins = int(user_input // 60 % 60)
secs = int(user_input % 60)

dd = str('{:0>2}'.format(days))
hh = str('{:0>2}'.format(hours))
mm = str('{:0>2}'.format(mins))
ss = str('{:0>2}'.format(secs))

result = dd + ':' + hh + ':' + mm + ':' + ss
print(result)