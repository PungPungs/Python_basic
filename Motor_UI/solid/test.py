period = []
freqs = [100,200,300,400,500]
for freq in freqs:
    period.append((1/(freq/60*1000)) * 1000000)
print(*period)