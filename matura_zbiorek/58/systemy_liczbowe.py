import math

s1 = open("dane_systemy1.txt", "r") #binary input station
s2 = open("dane_systemy2.txt", "r") #quatenary input station
s3 = open("dane_systemy3.txt", "r") #octal input station
results = open("wyniki_systemy.txt", "w") 

s1_hours = []
s2_hours = []
s3_hours = []

s1_temperatures = []
s2_temperatures = []
s3_temperatures = []

#58.1
for lines in s1:
    line = lines.strip().split()
    hour, temperature = line[0], line[1]
    s1_hours.append(int(hour, 2))
    s1_temperatures.append(int(temperature, 2))

for lines in s2:
    line = lines.strip().split()
    hour, temperature = line[0], line[1]
    s2_hours.append(int(hour, 4))
    s2_temperatures.append(int(temperature, 4))

for lines in s3:
    line = lines.strip().split()
    hour, temperature = line[0], line[1]
    s3_hours.append(int(hour, 8))
    s3_temperatures.append(int(temperature, 8))

s1_minimal_temp = bin(min(s1_temperatures)).replace("0b", "")
s2_minimal_temp = bin(min(s2_temperatures)).replace("0b", "")
s3_minimal_temp = bin(min(s3_temperatures)).replace("0b", "")

results.write(f"58.1\n LOWEST REGISTERED TEMPERATURES:\n Station 1: {s1_minimal_temp}\n Station 2: {s2_minimal_temp}\n Station 3: {s3_minimal_temp}\n\n")

#58.2
counter = 0
#since lenght of all files is the same, we can assume len(s1_hours)==len(s2_hours)==len(s3_hours)
#same for temperatures in 58.3
hour_corrector = 12
for i in range(len(s1_hours)): 
    #if s1_hours[i] != hour_corrector and s2_hours[i] != hour_corrector and s3_hours[i] != hour_corrector: 
    # ^ works perfectly fine but I like to complicate my life. Line below also works
    if s1_hours[i]%hour_corrector != 0 and s2_hours[i]%hour_corrector != 0 and s3_hours[i]%hour_corrector != 0:
        counter += 1
    hour_corrector += 24

results.write(f"58.2\n AMOUNT OF HOURS INCORRECTLY READ: \n {counter}\n\n")

#58.3
maxi_s1 = s1_temperatures[0]
maxi_s2 = s2_temperatures[0]
maxi_s3 = s3_temperatures[0]
isRecord = bool
record_days = 1 #first day is always a record day

for i in range(1, len(s1_temperatures)):
    isRecord = False
    if s1_temperatures[i] > maxi_s1:
        maxi_s1 = s1_temperatures[i]
        isRecord = True
    if s2_temperatures[i] > maxi_s2:
        maxi_s2 = s2_temperatures[i]
        isRecord = True
    if s3_temperatures[i] > maxi_s3:
        maxi_s3 = s3_temperatures[i]
        isRecord = True
    if isRecord:
        record_days += 1 
                
results.write(f"58.3\n AMOUNT OF RECORD DAYS:\n {record_days}\n\n")

#58.4
all_jumps = []
r_ij = 0 
temp_jump = 0
for i in range(len(s1_temperatures)):
    for j in range(i+1, len(s1_temperatures)):
        r_ij = (s1_temperatures[i] - s1_temperatures[j])**2
        temp_jump = math.ceil(r_ij / abs(i-j))
        all_jumps.append(temp_jump)
maxi_jump = max(all_jumps)

results.write(f"58.4\n BIGGEST TEMPERATURE JUMP: \n {maxi_jump}")


s1.close()
s2.close()
s3.close()
results.close()