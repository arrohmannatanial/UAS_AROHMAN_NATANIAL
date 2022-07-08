
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x_minta = np.arange(0,6000,1)
x_sedia = np.arange(0,700,1)
x_produk = np.arange(0,8000,1)

minta_sd = fuzz.trapmf(x_minta,[0,0,1000,5000])
minta_by = fuzz.trapmf(x_minta,[1000,5000,6000,6000])

sedia_sd = fuzz.trapmf(x_sedia,[0,0,100,600])
sedia_by = fuzz.trapmf(x_sedia,[100,600,700,700])

produk_sd = fuzz.trapmf(x_produk,[0,0,2000,7000])
produk_by = fuzz.trapmf(x_produk,[2000,7000,8000,8000])

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(x_minta, minta_sd, 'b', linewidth=1.5, label='Sedikit')
ax0.plot(x_minta, minta_by, 'g', linewidth=1.5, label='Banyak')
ax0.set_title('Permintaan')
ax0.legend()

ax1.plot(x_sedia, sedia_sd, 'b', linewidth=1.5, label='Sedikit')
ax1.plot(x_sedia, sedia_by, 'g', linewidth=1.5, label='Banyak')
ax1.set_title('Persediaan')
ax1.legend()

ax2.plot(x_produk, produk_sd, 'b', linewidth=1.5, label='Sedikit')
ax2.plot(x_produk, produk_by, 'g', linewidth=1.5, label='Banyak')
ax2.set_title('Produksi')
ax2.legend()

# Turn off top/right axes
for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.tight_layout()

minta = 4000
sedia = 300

in1 = []
in1.append(fuzz.interp_membership(x_minta,minta_sd,minta))
in1.append(fuzz.interp_membership(x_minta,minta_by,minta))
in2 = []
in2.append(fuzz.interp_membership(x_sedia,sedia_sd,sedia))
in2.append(fuzz.interp_membership(x_sedia,sedia_by,sedia))
print("derajat Keanggotaan Permintaan")
if in2[0]>0:
    print("sedikit = "+str(in1[0]))
if in2[1]>0:
    print("Banya = "+str(in1[1]))
    print("derajat Keanggotaan Persedian")
if in1[0]>0:
    print("sedikit = "+str(in2[0]))
if in1[1]>0:
    print("Banya = "+str(in2[1]))


apred1 = np.fmin(in1[1],in2[1])
print ("apred1 = ",apred1)
z1 = 5000*apred1+2000

apred2 = np.fmin(in1[1],in2[0])
print ("apred2 = ",apred2)
z2 = 5000*apred2+2000

apred3 = np.fmin(in1[0],in2[1])
print ("apred3 = ",apred3)
z3 = 7000-(apred3)*5000

apred4 = np.fmin(in1[0],in2[0])
print ("apred4 = ",apred4)
z4 = 7000-(apred4)*5000

print(z1,z2,z3,z4)

z =(apred1*z1+apred2*z2+apred3*z3+apred4*z4)/(apred1+apred2+apred3+apred4)
print("Jadi diperoleh kesimpulan bahwa barang yang harus diproduksi sejumlah "+str(int(z)))