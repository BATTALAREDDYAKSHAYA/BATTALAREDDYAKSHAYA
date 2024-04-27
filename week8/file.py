import scipy.io.wavfile as au
[fs,x]=au.read("/home/rguktrkvalley/Downloads/Chorus.wav")
x_revese=x[::-1]
au.write("/home/rguktrkvalley/Downloads/Chorus.wav",fs,x)
