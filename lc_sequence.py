
"""
DSP 539: Assignment 4
Submitted by: Archana Chittoor

This script, when run using the command line, outputs the linguistic complexity of each
sequence in a file of sequences. The file will be specified by the end user as a command line
argument.

Usage: python lc_sequence.py <filename>
"""

import pandas as pd
import sys 
import matplotlib.pyplot as plt

def count_obs_kmer(Seq,k):
    """
    Summary line: Counts the number of observed kmers for a sequence, for a specific k value
    
    Extended description: This function takes k and a sequence Seq as input arguments and determines the number of observed k-mers 
    for a particular k-value
    
    Parameters: 
    Seq: the input sequence for which the k-mers need to be determined
    k: the input value, ranges from 1 to length of sequence 
    
    Return:
    obs_kmers: the number of kmers observed
    """
    lk_pos = []
    for i in range(0,len(Seq)-k+1):
        lk_pos.append(Seq[i:i+k])

    lk_obs = list(set(lk_pos))
    return len(lk_obs)

def count_pos_kmer(Seq,k):
    """
    Summary line: Counts the number of possible kmers for a sequence, for a specific k value
    
    Extended description: This function takes k and a sequence Seq as input arguments and determines the number of possible/expected k-mers 
    for a particular k-value
    
    Parameters: 
    Seq: the input sequence for which the number of k-mers need to be determined
    k: the input value, ranges from 1 to length of the sequence 
    
    Return:
    pos_kmers: the number of kmers possible
    """
    
    lk_pos = []
    if k == 1:
        return 4;
    else:
        for i in range(0,len(Seq)-k+1):
            lk_pos.append(Seq[i:i+k])
            
        return len(lk_pos)
    
def create_kmer_df(Seq):
    """
    Summary line: Creates a data frame with k values, observed number of kmers and possible number of kmers as columns. 
    
    Extended description: This function takes a sequence Seq as input argument and returns a pandas data frame 
    which has columns k value, observed kmer count and possible kmer count.
        
    Parameters: 
    Seq: the input sequence for which the kmer data frame needs to be created
    
    Return:
    kmer_df: kmer data drame
    """
    #import pandas as pd
    k = []
    k_pos_list = []
    k_obs_list = []
    k = list(range(1,len(Seq)+1))
    
    for i in k:
        k_pos = count_pos_kmer(Seq,i)
        k_pos_list.append(k_pos)
    
    for i in k:
        k_obs = count_obs_kmer(Seq,i)
        k_obs_list.append(k_obs)
    
    kmer_df = pd.DataFrame(     # create the data frame
    {
         'k':k,
         'Observed kmers':k_obs_list,
         'Possible kmers':k_pos_list
    }
    )
    return kmer_df

def plot_kmer_prop(Seq):
    """
    Summary line: Creates a graph for proportion of each observed kmer
    
    Extended description: This function takes a sequence Seq as input argument and produces a plot for the proportion of each observed kmers 
    with respect to the number of possible kmers
        
    Parameters: 
    Seq: the input sequence for which the kmer proportion graph needs to be created
    
    Return:
    None
    """
    
    
    kmer_df = create_kmer_df(Seq)
    kmer_prop = kmer_df['Observed kmers']/kmer_df['Possible kmers'] # calculate the kmer proportion
    plt.plot(kmer_df['k'],kmer_prop)
    plt.title('Proportion of Observed kmers')
    plt.xlabel('k value')
    plt.ylabel('Observed/Possible kmers')
    plt.show()
    
def linguistic_complexity(Seq):
    """
    Summary line: Calculates the lingusitic complexity of a given sequence
    
    Extended description: This function takes a sequence Seq as input argument and produces the linguistic complexity, 
    the proportion of k-mers that are observed compared to the total number that are theoretically possible
        
    Parameters: 
    Seq: the input sequence for which the linguistic complexity needs to be determined
    
    Return:
    lc: linguistic complexity
    """
    
    kmer_df = create_kmer_df(Seq)
    tot_obs_kmer = sum(kmer_df['Observed kmers'])
    tot_pos_kmer = sum(kmer_df['Possible kmers'])
    lc = tot_obs_kmer/tot_pos_kmer
    return lc

if __name__=='__main__':
    
    myfile = sys.argv[1]
    with open(myfile,'r') as current_file:
        text = current_file.read()
    seq = text.split() # split sequences
    for i in range(0,len(seq)):
        #print(seq[i])
        lc_seq = linguistic_complexity(seq[i])
        print(lc_seq) # print the linguistic complexity
        #plot_kmer_prop(seq[i]) # produce the plot for kmer proportion
        
    