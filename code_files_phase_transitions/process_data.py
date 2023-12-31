import filehandling
import numpy as np
import pandas as pd
import os
from tqdm import tqdm
import matplotlib.pyplot as plt
import moviepy.editor as mp
from scipy.io.wavfile import read as wavread

'''
This script requires .hdf5 data files generated from the particle tracking software with specific postprocessing methods:
   
    hexatic_order
    hexatic_order_abs

The .hdf5 files should be saved in the same folder as the .MP4 video files recorded by the camera and the acceleration data
files generated by the experiment code script.

This script will generate and save a .txt file containing columns containing: [global order param] [duty cycle]

'''
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

    path = "videos/08_02_area_f_0.598/set_3/" #specify filepath and file names
    acc_file = "acceleration_data_3.txt"    #acceleration data
    data_file = "data_3.txt"    #name of file to store data in

    directory = filehandling.open_directory(path)   #create file directory and select files
    files = filehandling.get_directory_filenames(directory+"/*.hdf5")
    acceleration_data = np.loadtxt(path+acc_file, dtype=float)    #load in acc data

    dutys = []  #initalise empty arrays and params
    global_orders = []
    framenumber = 0

    if True:
        for file in tqdm(files):
            #asign filename and filepath
            filename = os.path.splitext(os.path.split(file)[1])[0]
            filepath = path+filename+".hdf5"
            dataframe = pd.read_hdf(filepath)   #read .hdf5 file
            
            dataframe.index.name='index'    #set dataframe index to "index"

            order = hexatic(dataframe, framenumber)   #extract mag of hexatic order param from dataframe
            global_order = np.mean(order)   #calc global order param (mean of local param)
            global_orders.append(global_order)    #append to array
            
            duty = video_to_duty(path+filename+".MP4")  #calculate duty from freq of audio signal
            dutys.append(duty)          #append to array
            
        global_orders = np.transpose(np.array([global_orders]))   #create columns of data in numpy arrays
        dutys = np.transpose(np.array([dutys]))

        data = np.hstack((global_orders,dutys)) #stack global order params and duty data
        np.savetxt(path+data_file, data)    #save .txt file of counts and duty
        print("data saved to: ", path+data_file)