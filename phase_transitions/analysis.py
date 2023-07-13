import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import moviepy.editor as mp
from scipy.io.wavfile import read as wavread


def hex_order(dataframe, frame_number):
    '''
    Extracts the hexatic order from a pandas dataframe.
    Calculates the magnitude of the order.

    Inputs:
    dataframe : pandas dataframe 
    frame_number : requested frame of video

    Outputs : 
    order : array of magnitudes of heaxtic_order param
    '''
    frame_data = dataframe.loc[frame_number]
    hex_order = frame_data[["hexatic_order"]]
    order = np.abs(hex_order)
    
    return order

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
    duty = float(duty)
    return duty


path = "videos/exp_2/"

data_filename_liquid = path+"19920010.hdf5"
data_filename_solid = path+"19920070.hdf5"
data_filename_int = path+"19920050.hdf5"

video_file_s = path+"19920070.MP4"
video_file_l = path+"19920001.MP4"
video_file_i = path+"19920050.MP4"

data_frame_s = pd.read_hdf(data_filename_solid)
data_frame_l = pd.read_hdf(data_filename_liquid)
data_frame_i = pd.read_hdf(data_filename_int)

data_frame_s.index.name='index'
data_frame_l.index.name="index"
data_frame_i.index.name="index"

duty_s = video_to_duty(video_file_s)
duty_i = video_to_duty(video_file_i)
duty_l = video_to_duty(video_file_l)

frame_number = 10

order_s = hex_order(data_frame_s, frame_number)
order_i = hex_order(data_frame_i, frame_number)
order_l = hex_order(data_frame_l, frame_number)

#count = np.count_nonzero(order > 0.75) / len(hexatic_order)

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, sharey=True)
ax1.set_title("Distribution of |$\Psi_6$|")
ax1.hist(order_l, bins=200)
ax1.text(0,75,"Duty: "+str(duty_l)+"%")
ax2.hist(order_i, bins=200)
ax2.text(0,75,"Duty: "+str(duty_i)+"%")
ax3.hist(order_s, bins=200)
ax3.text(0,75,"Duty: "+str(duty_s)+"%")


plt.show()
