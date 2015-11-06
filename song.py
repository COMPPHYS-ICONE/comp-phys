'''
Symphony no. 5 in E minor
If you do not enjoy my symphony that is your personal taste, but this is how I intended it
'''

import matplotlib.pyplot as plt
import numpy as np


class Tone:
    def __init__(self):
        self.f = 0
        self.dur = 0
        self.sr = 44100
        self.signal = 0
        self.orig_signal = 0
        self.overtones = {}
        self.OT_num = 0
    def get_tone(self, f, dur, play_sound = False):
        self.f = f
        self.dur = dur
        time_pts = np.linspace(0,dur,dur*self.sr)
        tone_data = (2e4)*np.sin(np.pi*2*f*time_pts)
        self.signal = tone_data
        self.orig_signal = tone_data
        if play_sound == True:
            self.playsound(self.signal, self.sr)
        return tone_data
    def get_overtone(self, multi, play_sound = False):
        time_pts = np.linspace(0,self.dur,self.dur*self.sr)
        tone_data = (2e4)*np.sin(np.pi*2*(self.f*multi)*time_pts)
        if play_sound == True:
            self.playsound(self.sr, tone_data)
        self.overtones[multi] = tone_data
        self.OT_num += 1
        return None
    def comb_tones(self):
        normali = 0
        weight_keys = self.overtones
        for tones in self.overtones:
            normali += (tones**2)
        normalization_factor = (1./((normali)**(1./2)))
        print normalization_factor
        for tones in self.overtones:
            weight_keys[tones] = int(raw_input("please insert a weight")) 
            self.signal += normalization_factor*weight_keys[tones]*self.overtones[tones]
        return self.signal
    def playsound(self, outside_signal = None, sample_rate = 44100, vol = 0.05):
        from scipy.io.wavfile import write
        import os
        if outside_signal == None:
            write('tmp.wav', sample_rate, np.int16(vol*self.signal))
            os.system("afplay tmp.wav") 
            os.system("rm tmp.wav")
        else:
            write('tmp.wav', sample_rate, np.int16(vol*outside_signal))
            os.system("afplay tmp.wav") 
            os.system("rm tmp.wav")
        return
    def plot_fourier(self, freq_lim = 1000., amp_lim = 1e8):
        sample_rate = self.sr
        ft = np.fft.fft(np.float64(self.signal))
        freq = np.fft.fftfreq(self.signal.shape[-1], d = 1./sample_rate)
        plt.figure()
        plt.title('Real')
        plt.plot(freq, ft.real, 'b-')
        plt.xlim([-freq_lim, freq_lim])
        plt.ylim([-amp_lim, amp_lim])
        plt.figure()
        plt.title('Imaginary')
        plt.plot(freq, ft.imag, 'g-')
        plt.xlim([-freq_lim, freq_lim])
        plt.ylim([-amp_lim, amp_lim])
        plt.show()
        return
    def plot_sound(self, fig = None, t_lim = 0.02, s_lim = 'auto', plot_style = 'b-'):
        time_pts = np.linspace(0,self.dur,self.dur*self.sr)
        if fig == None:
            plt.figure()
        plt.title("Combined Tone vs. Time")
        plt.plot(time_pts, self.signal, plot_style)
        plt.xlim([0, t_lim])
        if s_lim  != 'auto':
            plt.ylim([-s_lim, s_lim])
        return 
    
tone = Tone()   
simple_tone = tone.get_tone(440., 1)
tone.get_overtone(2)
tone.get_overtone(3)
tone.get_overtone(4)
tone.playsound(tone.comb_tones())
tone.plot_sound()
tone.plot_fourier(freq_lim = 2000.)