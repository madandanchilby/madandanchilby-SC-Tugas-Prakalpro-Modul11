def TambahTuple(tupleku):
    List=list(tupleku)
    List.append('Valorant')
    tupleku=tuple(List)
    return tupleku

tupleku=('abiel','itu','beban','tim')
print(TambahTuple(tupleku))
print(type(tupleku))

def hitungnilai(matkul):
    nilai=[]
    for kata in matkul:
        Nilai=int(input(f'masukan nilai mata kuliah {kata}:'))
        nilai.append(Nilai)
    print('nilai rata-rata mata kuliah anda saat ini adalah:',sum(nilai)/len(nilai))

matkul=('pkn','matdis','alpro','prakalpro','jarkom','prajarkom','statiska','Bii','arorkom')
(hitungnilai(matkul))