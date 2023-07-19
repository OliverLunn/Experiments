import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import moviepy.editor as mp
from scipy.io.wavfile import read as wavread


def magnitude_hexatic(dataframe,framenumber):
    '''
    Extracts the hexatic order from a pandas dataframe.
    Calculates the magnitude of the order.

    Inputs:
    dataframe : pandas dataframe 

    Outputs : 
    order : array of magnitudes of heaxtic_order param
    '''
    framedata = dataframe.loc[[framenumber]]
    mag_hexatic = framedata[["hexatic_order_abs"]]
    
    return mag_hexatic

def video_to_duty(video_file_path):
    '''
    Returns duty cycle from audio of .MP4 file
    Extracts audio information from .MP4 file using scipy.io.wavfile and stores
    audio information in a numpy array.
    Extracts duty cycle information from a numpy array of audio information.
    Input:
    video_file_path : a file path to an .MP4 file
    
    Returns:
    duty : duty cycle (as a percentage)

    '''
    clip = mp.VideoFileClip(video_file_path)
    clip.audio.write_audiofile("audio_out.wav") #write audio file from .MP4
    rate, data = wavread("audio_out.wav")   #read audio file
    audio_array = data[:,0] #discard channel information
    
    ft = np.abs(np.fft.fft(audio_array, n=len(audio_array))) #fourier transform audio signal
    freq = np.fft.fftfreq(len(audio_array), 1/rate)
    peak = int(abs(freq[np.argmax(ft)]))    #find peak freq.
    duty = (peak - 1000) / 15   #duty cycle conversion
    return duty


path = "videos/2023_07_19_cooling/set_1/"
framenumber = 2

data_filename_liquid = path+"19950001.hdf5"
data_filename_int = path+"19950040.hdf5"
data_filename_solid = path+"19950075.hdf5"

video_file_l = path+"19950001.MP4"
video_file_i = path+"19950040.MP4"
video_file_s = path+"19950075.MP4"

data_frame_s = pd.read_hdf(data_filename_solid) #read in .hdf5 file
data_frame_l = pd.read_hdf(data_filename_liquid)
data_frame_i = pd.read_hdf(data_filename_int)

data_frame_s.index.name='index' 
data_frame_l.index.name="index"
data_frame_i.index.name="index"

duty_s = video_to_duty(video_file_s)    #calc duty from audio freq
duty_i = video_to_duty(video_file_i)
duty_l = video_to_duty(video_file_l)

order_s = magnitude_hexatic(data_frame_s, framenumber)  #extract magnitude of hexatic order param from dataframe
order_i = magnitude_hexatic(data_frame_i, framenumber)
order_l = magnitude_hexatic(data_frame_l, framenumber)

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharey=True)    #plot distributions of 3 selected videos
ax1.set_title("Distribution of |$\Psi_6$|")
ax1.hist(order_l, bins=100)
ax1.text(0,500,"Duty: "+str(duty_l)+"%")
ax2.hist(order_i, bins=100)
ax2.text(0,500,"Duty: "+str(duty_i)+"%")
ax3.hist(order_s, bins=100)
ax3.text(0,500,"Duty: "+str(duty_s)+"%")

plt.show()
