from scipy.optimize import linprog
import pandas as pd

# Datos ajustados
operators = ["KC", "DH", "HB", "SC", "KS", "NK"]
wage = {"KC": 10.00, "DH": 10.10, "HB": 9.90, "SC": 9.80, "KS": 10.80, "NK": 11.30}
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
max_hours = {
    ("KC","Mon"):6, ("KC","Tue"):0, ("KC","Wed"):6, ("KC","Thu"):0, ("KC","Fri"):6,
    ("DH","Mon"):0, ("DH","Tue"):6, ("DH","Wed"):0, ("DH","Thu"):6, ("DH","Fri"):0,
    ("HB","Mon"):4, ("HB","Tue"):8, ("HB","Wed"):4, ("HB","Thu"):0, ("HB","Fri"):4,
    ("SC","Mon"):5, ("SC","Tue"):5, ("SC","Wed"):5, ("SC","Thu"):0, ("SC","Fri"):5,
    ("KS","Mon"):3, ("KS","Tue"):0, ("KS","Wed"):3, ("KS","Thu"):8, ("KS","Fri"):0,
    ("NK","Mon"):0, ("NK","Tue"):0, ("NK","Wed"):0, ("NK","Thu"):6, ("NK","Fri"):2
}
min_week = {"KC":8, "DH":8, "HB":8, "SC":8, "KS":7, "NK":7}

# Índices
idx = [(i,d) for i in operators for d in days]

# Objetivo
c = [wage[i] for (i,d) in idx]

# Restricciones
A_eq = [[1 if dd==d else 0 for (i,dd) in idx] for d in days]
b_eq = [14]*len(days)

A_ub = [[-1 if ii==i else 0 for (ii,d) in idx] for i in operators]
b_ub = [-min_week[i] for i in operators]

bounds = [(0, max_hours[(i,d)]) for (i,d) in idx]

res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Preparar resultado con 4 decimales
data = {d: [] for d in days}
for i in operators:
    for d in days:
        data[d].append(round(res.x[idx.index((i,d))],4))
df = pd.DataFrame(data, index=operators)
df["Total"] = df.sum(axis=1).round(4)
df.loc["DailySum"] = df.sum(axis=0).round(4)
df.loc["Cost","Total"] = round(res.fun,4)
df
