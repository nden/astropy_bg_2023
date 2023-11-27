import matplotlib.pyplot as plt


def fahr_to_celsius(temp):
  new_temp = ((temp-32)*(5/9))
  return new_temp
    
def celsius_to_kelvin(temp):
  return temp + 273.15

def fahr_to_kelvin(temp):
  """
  This is my special function.
  It takes some values in F degrees
  And returns deg K
  Example: fahr_to_kelvin(212)
  > 373.15
  """

  import numpy as np
  #calculate one thing
  c_temp = fahr_to_celsius(temp) # I'm here

  #calcualate another thing
  k_temp = celsius_to_kelvin(c_temp)
  return k_temp


class LightCurve:
    def __init__(self, times=None, fluxes=None, uncertainties=None, flags=None, name=None):
        self.times = times
        self.fluxes = fluxes
        self.uncertainties = uncertainties
        self.flags = flags
        self.name = name

    def plot(self, color=None):
        """Plot the light curve"""
        plt.errorbar(self.times, self.fluxes, self.uncertainties, fmt='o', color=color)
        plt.xlabel('Time')
        plt.ylabel('Flux')
        plt.title(self.name)