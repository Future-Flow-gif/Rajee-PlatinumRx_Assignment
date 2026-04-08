def convert_minutes(minutes):
   hrs = minutes // 60
   mins = minutes % 60
  if hrs == 0:
       return f"{mins} minutes"
   elif mins == 0:
       return f"{hrs} hr" if hrs == 1 else f"{hrs} hrs"
   else:
       return f"{hrs} hr{'s' if hrs > 1 else ''} {mins} minutes"

# Examples
print(convert_minutes(130))  
Output:  2 hrs 10 minutes
print(convert_minutes(110))  
Output:  1 hr 50 minutes
