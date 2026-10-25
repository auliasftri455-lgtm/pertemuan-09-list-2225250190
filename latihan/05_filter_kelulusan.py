nilai = [75, 55, 80, 60, 45, 90]
lulus = []

for x in nilai:
    if x >= 60:
        lulus.append(x)

print(f"Semua nilai       = {nilai}")
print(f"Nilai yang lulus  = {lulus}")
print(f"Jumlah yang lulus = {len(lulus)}")