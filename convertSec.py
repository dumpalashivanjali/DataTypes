# Question: Convert total seconds into hours, minutes, and seconds.
# Input: - Total seconds = 3672
# Output: - Hours: 1 - Minutes: 1 - Seconds: 12

def convertSec(seconds):
    hours=seconds//3600
    seconds=seconds%3600
    minutes=seconds//60
    seconds=seconds%60
    return (hours,minutes,seconds)

h,m,s =convertSec(3672)
print(f"Hours: {h} - Minutes: {m} - Seconds: {s}")