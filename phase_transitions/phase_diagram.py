import filehandling
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import moviepy.editor as mp

from scipy.io.wavfile import read as wavread
from particletracker.general import dataframes

def hex_o(dataframe):
    '''
    Extracts the hexatic order from a pandas dataframe.
    Calculates the magnitude of the order.

    Inputs:
    dataframe : pandas dataframe 

    Outputs : 
    order : array of magnitudes of heaxtic_order param
    '''
    hex_order = dataframe[["hexatic_order"]]
    order = np.abs(hex_order)
    
    return order


def video_to_duty(video_filepath):
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
    clip = mp.VideoFileClip(video_filepath)
    clip.audio.write_audiofile("audio_out.wav") #write audio file from .MP4
    rate, data = wavread("audio_out.wav")   #read audio file
    audio_array = data[:,0] #discard channel information
    
    ft = np.abs(np.fft.fft(audio_array, n=len(audio_array))) #fourier transform audio signal
    freq = np.fft.fftfreq(len(audio_array), 1/rate)
    peak = int(abs(freq[np.argmax(ft)]))    #find peak freq.
    duty = (peak - 1000) / 15   #duty cycle conversion
    duty = float(duty)

    return duty

if __name__ == '__main__':
    path = "videos/exp_2/"
    directory = filehandling.open_directory(path)
    files = filehandling.get_directory_filenames(directory+"/*.hdf5")

    #dataframe = pd.read_hdf("videos/exp_2/19960022.hdf5")
    #print(dataframe)

    dutys = []
    counts = []
    

    if True:
        for file in files:

            filename = os.path.splitext(os.path.split(file)[1])[0]
            
            filepath = path+filename+".hdf5"
        
            dataframe = pd.read_hdf(filepath)

            dataframe.index.name='index'

            hex_order = dataframe[["hexatic_order"]]
            order = np.abs(hex_order)
            
            duty = video_to_duty(path+filename+".MP4")
            count = np.count_nonzero(order>0.85) / len(order)

            counts.append(count)
            dutys.append(duty)

            print(count)
        
        fig, ax = plt.subplots()
        ax.plot(dutys, counts, ".")
        ax.set_xlabel("Duty Cycle, %")
        ax.set_ylabel("Phase Info (ratio crystal)")
        plt.show()
