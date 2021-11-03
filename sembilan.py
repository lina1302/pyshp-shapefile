import shapefile
print(1194030 % 8)
# Karena angka kedua terakhir npm saya adalah 3 maka saya akan membuat 3 trapesium

w = shapefile.Writer("soal10", shapeType=shapefile.POLYGON)
w.shapeType


w.field("kolom1", "C")
w.field("kolom2", "C")

w.record("Petrolina Anastasia ", "Gatto")
w.record("Black", "Pink")


w.poly([[[3, 1], [9, 1], [6, 5], [3, 1]]])

w.poly([[[10, 1], [13, 1], [17, 5], [10, 1]]])


w.close()
