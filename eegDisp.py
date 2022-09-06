"""Example program to show how to read a multi-channel time series from LSL."""

from tkinter import Y
from pylsl import StreamInlet, resolve_stream
import time
import numpy as np
import matplotlib.pyplot as plt
import pygame
from pygame.locals import *
import sys

def main():
    times = np.zeros(0) #store times
    samp = np.zeros((23,0)) #store samples(23 channels)
    i=0
    plt.ion()
    pygame.init() #Initialize Pygame
    screen = pygame.display.set_mode((1000, 100))   # create screen(100×100)
    pygame.display.set_caption("title")         # title
    font = pygame.font.Font(None, 50)              # set Font

    # first resolve an EEG stream on the lab network
    print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])

    while True:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        sample, timestamp = inlet.pull_sample()
        times = np.append(times,i)
        aa = np.zeros((23,1))
        for j in range(23):
            aa[j,0] = sample[j]
        samp = np.append(samp,aa,axis=1)

        screen.fill((0,0,0))            # clear screen
        text = font.render("", False, (255,255,255))   
        screen.blit(text, (10, 10))     # position
        pygame.display.flip()           # renew

        # print("")

        # graph format
        line, = plt.plot(times, samp[0], 'r-',label="sample1") # renew Y-axis
        line.set_ydata(samp[0])
        # line, = plt.plot(times, samp[1], 'b-',label="sample2") # renew Y-axis
        # line.set_ydata(samp[1])
        # line, = plt.plot(times, samp[2], 'g-',label="sample3") # renew Y-axis
        # line.set_ydata(samp[2])
        # line, = plt.plot(times, samp[3], 'c-',label="sample4") # renew Y-axis
        # line.set_ydata(samp[3])
                
        plt.title("Real-time EEG-data about sample1")
        plt.xlabel("Time [s]")
        plt.ylabel("EEG data")
        plt.legend()
        plt.grid()
        plt.xlim([0,50])
        # plt.ylim([0,40])
        plt.pause(.5)
        plt.clf()
        for event in pygame.event.get():
            # Exit when the end button is pressed
            if event.type == QUIT:
                pygame.quit()
                plt.close()
                sys.exit()
        i+=.5


if __name__ == '__main__':
    main()