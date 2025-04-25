# km hm dam m dm cm mm
medida = float(input('Distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}dm, {:.0f}cm e {:.0f}mm'.format(medida, dm, cm, mm))
print('A medida de {}m corresponde a {}dam, a {}hm e a {}km'.format(medida, dam, hm, km))