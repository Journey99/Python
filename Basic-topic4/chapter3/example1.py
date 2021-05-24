# data 폴더의 chicken.txt 파일을 읽어 들이고,
# srtip과 split을 써서 하루평균 매출 출력

with open('data/chicken.txt', 'r') as f:
    total_revenue = 0
    total_day = 0

    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])
        total_revenue += revenue
        total_day += 1

print(total_revenue / total_day)