def garis():
    print("------------")

#fungsi bubble sort ascending (dari kecil ke besar)
def sort_asc(array):
     array = sorted(array)
     return(array)

#fungsi bubble sort descending (dari besar ke kecil)
def sort_desc(array):
     array = sorted(array, reverse = True)
     return(array)
    
#fungsi rata rata
def rata_rata(angka):
    return sum(angka)/len(angka)

#input nilai
garis()
print("Masukan tiga buah nilai")
#masukan tipe data interger
nilai_a = int(input("Nilai A : "))
nilai_b = int(input("Nilai B : "))
nilai_c = int(input("Nilai C : "))
#masukan tipe data array

angka = [nilai_a, nilai_b, nilai_c]
garis()
print()

#nilai akhir
print("HASIL AKHIR----")
print("Urutan Angka ascending : ",(sort_asc(angka)))
print("Urutan Angka descending : ",(sort_desc(angka)))

#angka terbesar
print("Angka Terbesar :", max(angka))

#angka terkecil
print("Angka Terkecil :", min(angka))

#rata rata
print("Rata ratanya :", round(rata_rata(angka),2))


