# MotifDetection
Exact Discovery of Time Series Motifs

Discovery of motifs in 1-D time series using modified method described by http://www.cs.ucr.edu/~mueen/pdf/EM.pdf

  Inputs:
    Time series: a python list or numpy array
    ML: Motif length
    K: Major Factor of Clustor Radius, greater than 1 and X
    X: Minor Factor of Clustor Radius, greater than 1
  Outputs:
    Motifs: in a list of numpy arrays, 
    BSFB: final euclidean distance calculated

# How to use
  Copy md.exe and MotifDetection.py to your project folder, and import MotifDetection.py to your main code.
 
# Example
  Copy the whole folder and run jupyter notebook file produced as an example

# Requirements
  
  1. Numpy
    If not installed(windows):
        pip install numpy
        
  2. Jupyter Notebook, to run example
    If not installed(windows):
        pip install jupyter
     
  3. Plotly, to run example
    If not installed(windows):
        pip install plotly       
      
       
