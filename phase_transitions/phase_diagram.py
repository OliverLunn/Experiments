import filehandling
import numpy as np
import pandas as pd
import os
from tqdm import tqdm
import matplotlib.pyplot as plt
import moviepy.editor as mp
from scipy.io.wavfile import read as wavread


def hexatic(dataframe,framenumber):
    '''
    Extracts the hexatic order from a pandas dataframe.
    Calculates the magnitude of the order.

    Inputs:
    dataframe : pandas dataframe 

    Outputs : 
    order : array of magnitudes of heaxtic_order param
    '''
    framedata = dataframe.loc[[framenumber]]
    hexatic = framedata[["hexatic_order_abs"]]
    return hexatic

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
    peak = abs(freq[np.argmax(ft)])    #find peak freq.
    #peak = int(abs(freq[np.argmax(ft)]))    #find peak freq.
    duty = (peak - 1000) / 15   #duty cycle conversion
    return duty

if __name__ == '__main__':
    path = "videos/2023_07_25_pm/set_3/" #create file directory and select files
    acc_file = "acceleration_data_3.txt"
    data_file = "data_3.txt"
    directory = filehandling.open_directory(path)
    files = filehandling.get_directory_filenames(directory+"/*.hdf5")

    dutys = []  #initalise empty arrays and params
    global_orders = []
    framenumber = 2

    if True:
        for file in tqdm(files):
            #asign filename and filepath
            filename = os.path.splitext(os.path.split(file)[1])[0]
            filepath = path+filename+".hdf5"
            dataframe = pd.read_hdf(filepath)   #read .hdf5 file
            
            dataframe.index.name='index'    #set dataframe index to "index"

            order = hexatic(dataframe, framenumber)   #extract mag of hexatic order param from dataframe
            global_order = np.mean(order)   #calc global order param (mean of local param)

            duty = video_to_duty(path+filename+".MP4")  #calculate duty from freq of audio signal

            global_orders.append(global_order)    #append to arrays
            dutys.append(duty)

        global_orders = np.transpose(np.array([global_orders]))   #create columns of counts and duty data
        dutys = np.transpose(np.array([dutys]))
        acceleration_data = np.loadtxt(path+acc_file, dtype=float)    #load in acc data

        data = np.hstack((global_orders,dutys)) #stack counts and duty data
        np.savetxt(path+data_file, data)    #save .txt file of counts and duty

        fig, (ax1,ax2) = plt.subplots(2,1, sharey=False)    #plotting
        ax1.plot(dutys, global_orders, ".")
        ax1.set_xlabel("Duty Cycle, %")
        ax1.set_ylabel("Average global order parameter")

        ax2.plot(acceleration_data[1:], global_orders[1:], ".")
        ax2.set_xlabel("$\Gamma$")
        ax2.set_ylabel("$\psi$")

        plt.show()
