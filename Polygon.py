# Read in a WAV and find the freq's
import pyaudio
import wave
import numpy as np

CHUNK = 1024
RATE = 44100
RECORD_SECONDS = 5
FORMAT = pyaudio.paInt16
CHANNELS = 2
chunk = 1024

# open up a wave
# use a Blackman window
window = np.blackman(chunk)
# open stream_outp
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

stream_outp = p.open(format =FORMAT,
                channels =CHANNELS,
                rate = RATE,
                output = True)
swidth = 2
# read some data
while(True):
    data=stream.read(CHUNK)
    # play stream_outp and find the frequency of each chunk
    # write data out to the audio stream_outp
    stream_outp.write(data)
    # unpack the data and times by the hamming window
    indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),data))
    # Take the fft and square each value
    fftData=abs(np.fft.rfft(indata))**2
    # find the maximum
    which = fftData[1:].argmax() + 1
    # use quadratic interpolation around the max
    if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # find the frequency and output it
        thefreq = (which+x1)*RATE/chunk
        #print ("The freq is %f Hz." % (thefreq))
        print(thefreq)

    else:
        thefreq = which*RATE/chunk
        print ("The freq is %f Hz." % (thefreq))
        # read some more data
stream_outp.close()
p.terminate()