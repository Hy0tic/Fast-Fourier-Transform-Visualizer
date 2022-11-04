import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [16,12]
plt.rcParams.update({'font.size' : 18})

dt = 0.001
t = np.arange(0,1,dt)
f = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)  # sum of 2 frequencies
f_clean = f
f = f + 2.5*np.random.randn(len(t)) # add random noise to the signal


# Compute the Fast Fourier Transform (FFT)
n = len(t)
fhat = np.fft.fft(f,n)
PSD = fhat * np.conj(fhat)/n
freq = (1/(dt*n)) * np.arange(n)
L = np.arange(1,np.floor(n/2),dtype='int')

# Use the PSD to filter out noise
indices = PSD > 100         # Find all frequencies with large power
PSDclean = PSD * indices    # Zero out the frequencies not large enough
fhat = indices * fhat       # Zero out small Fourier coefficients in Y
ffilt = np.fft.ifft(fhat)   # Inverse FFT for filtered signal

# Plots 
fig,axs = plt.subplots(3,1)

    # plot of clean signal vs noisy signal
plt.sca(axs[0])
plt.plot(t,f,color='c',LineWidth=1.5,label="Noisy")
plt.plot(t,f_clean,color='k',LineWidth=2,label="Clean")
plt.xlim(t[0],t[-1])
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

    # plot of denoised signal
plt.sca(axs[1])
plt.plot(t,ffilt,color='k',LineWidth=2,label="Filtered")
plt.xlim(t[0],t[-1])
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

    # plot of FFT result before filted vs after filtered
plt.sca(axs[2])
plt.plot(freq[L],PSD[L],color='c',LineWidth=2,label='Noisy')
plt.plot(freq[L],PSDclean[L],color='k',LineWidth=1.5,label='Filtered')
plt.xlim(freq[L[0]],freq[L[-1]])
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.legend()

plt.show()


