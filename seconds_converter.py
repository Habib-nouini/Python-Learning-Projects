total_second = int(input ("please enter the scondes"))
hours = total_second // 3600
remaining_after_hours = total_second % 3600
minutes = remaining_after_hours // 60
second = remaining_after_hours % 60
print (f"{hours} hours and {minutes} minutes and {second} second")