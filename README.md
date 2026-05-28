https://publish.obsidian.md/dibalabwiki/700+Data+Analysis/720+Spike+Sorting/721+Installation/721.2+Installing+Phy

```ps1
micromamba create -n circus python=3.6
micromamba activate circus
micromamba install -c conda-forge -c spyking-circus spyking-circus

```
spyking-circus file_name.dat -s 100 -p


```ps1
micromamba install pip install . --editable

micromamba pip install . --editable

```

```
process_resample -f 30000,1250 -n 200 continuous.dat continuous.eeg

process_resample -f 30000,1250 -n 200 continuous.dat continuous.eeg


```


don't have process_resample -- downsamples .dat to .eeg/.lfp

## Can't I just:
1. Downsample .dat to .lfp if needed?
2. Concatenate the "good" sessions together so that they can be spike-sorted together
3. 


```python

raw_data_path: Path = Path(r'W:\Data\Bapun\RatS\Day1Openfield\Raw_data').resolve()


'Day1Openfield/Raw_data/2020-11-25_10-24-24',
'Day1Openfield/Raw_data/2020-11-25_13-02-47',
'Day1Openfield/Raw_data/2020-11-25_14-30-32',
'Day1Openfield/Raw_data/2020-11-25_15-06-02',
'Day1Openfield/Raw_data/2020-11-25_10-20-27',



phy template-gui params.py

```



# Pho New 2026

https://github.com/SpikeInterface/spikeinterface/tree/main/installation_tips


# Pho only working on Apogee 2026-05-21
Got working on Apogee using WSL (would not work natively) and the lab-wiki defined micromamba setup.

```bash
micromamba create -n circus python=3.6
micromamba activate circus
micromamba install -c conda-forge -c spyking-circus spyking-circus

```

```bash
eval "$(micromamba shell hook --shell=bash)"
micromamba activate circus
cd spyk-circ
spyking-circus RatS-Day1Openfield.dat -c 8

```

- Ran main export, took about the length of the recording to do processing -- this took about 2 hours
- Ran special export for use with the Phy GUI -- this is taking about 20 minutes


## Starting Phy2 Phase

`cd 'W:\Data\Bapun\RatS\Day1Openfield\spyk-circ\RatS-Day1Openfield\RatS-Day1Openfield-merged.GUI'`
```bash
micromamba env create -f environment.yml
micromamba activate phy2


micromamba env create -f environment_win_WSL.yml
micromamba activate phy2-wsl


cd '/mnt/w/Data/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI'


export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_SCALE_FACTOR=1
export QT_ENABLE_HIGHDPI_SCALING=0
export XCURSOR_SIZE=24 ## this line fixed it, but maybe these Qt fixes fix other things
phy template-gui params.py



export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_SCALE_FACTOR=1
export QT_ENABLE_HIGHDPI_SCALING=0
export XCURSOR_SIZE=24 ## this line fixed it, but maybe these Qt fixes fix other things
LIBGL_ALWAYS_SOFTWARE=1 \
QT_OPENGL=software \
QTWEBENGINE_DISABLE_GPU=1 \
phy template-gui params.py

```


# Pho Interactive NeuroPy Notebook Pipeline

```bash
uv run ipython kernel install --user --name=bapun-sess-init-UV

uv run jupyter-lab --no-browser --port='8889' --ServerApp.ip='0.0.0.0' --ServerApp.allow_origin='*' --ServerApp.disable_check_xsrf=True
http://127.0.0.1:8889/lab?token=5a5da86609475f2e29341b110eecd273fe4e8d5787a83836
```

## on WSL
```ps1
uv run ipython kernel install --user --name=bapun-sess-init-UV-WSL
```


```
mv '/home/halechr/FastData/Bapun/RatS/Day4Openfield/RatS-Day4Openfield.eeg' '/home/halechr/FastData/Bapun/RatS/Day4Openfield/RatS-Day4Openfield.eeg.bak'
process_resample -f 30000,1250 -n 200 '/home/halechr/FastData/Bapun/RatS/Day4Openfield/RatS-Day4Openfield.dat' '/home/halechr/FastData/Bapun/RatS/Day4Openfield/RatS-Day4Openfield.eeg'

mv "W:\Data\Bapun\RatS\Day1Openfield\RatS-Day1Openfield.eeg" "W:\Data\Bapun\RatS\Day1Openfield\RatS-Day1Openfield.eeg.bak"
process_resample -f 30000,1250 -n 200 "W:/Data/Bapun/RatS/Day1Openfield/RatS-Day1Openfield.dat" "W:/Data/Bapun/RatS/Day1Openfield/RatS-Day1Openfield.eeg"

process_resample -f 30000,1250 -n 200 "/mnt/w/Data/Bapun/RatS/Day1Openfield/RatS-Day1Openfield.dat" "/mnt/w/Data/Bapun/RatS/Day1Openfield/RatS-Day1Openfield.eeg"

mv "/mnt/w/Data/Bapun/RatS/Day1Openfield/RatS-Day4Openfield.eeg" "/mnt/w/Data/Bapun/RatS/Day1Openfield/RatS-Day4Openfield.eeg.bak"
process_resample -f 30000,1250 -n 200 "/mnt/w/Data/Bapun/RatS/Day1Openfield/RatS-Day4Openfield.dat" "/mnt/w/Data/Bapun/RatS/Day1Openfield/RatS-Day4Openfield.eeg"

```


# Latest Output Apogee 2025-05-26

##############################################
### RatS-Day1Openfield
```bash
mv "/mnt/w/Data/Bapun/RatS/Day1Openfield/RatS-Day1Openfield.eeg" "/mnt/w/Data/Bapun/RatS/Day1Openfield/RatS-Day1Openfield.eeg.bak"
cd '/mnt/w/Data/Bapun/RatS/bapun_sess_init_scripts'
./scripts/process_resample -f 30000,1250 -n 200 "/mnt/w/Data/Bapun/RatS/Day1Openfield/RatS-Day1Openfield.dat" "/mnt/w/Data/Bapun/RatS/Day1Openfield/RatS-Day1Openfield.eeg"
```
#### Output 2026-05-26:
```bash
Input File     : /mnt/w/Data/Bapun/RatS/Day1Openfield/RatS-Day1Openfield.dat
Channels       : 200
Sampling Rate  : 30000.000000
Output file    : /mnt/w/Data/Bapun/RatS/Day1Openfield/RatS-Day1Openfield.eeg
Sampling Rate  : 1250.000000
Freq Ratio     : 0.041667
Converter      : Fastest Sinc Interpolator
Resampling     : 0% ################################################## 100%
Output Frames  : 8708858
```

### IN WSL 2026-05-27:
```bash
cd '/mnt/w/Data/Bapun/RatS/Day1Openfield/spyk-circ'
micromamba activate circus
spyking-circus RatS-Day1Openfield.dat --cpu 15
```

#### Run Result:
```bash
pho@Apogee:~$ cd '/mnt/w/Data/Bapun/RatS/Day1Openfield/spyk-circ'
micromamba activate circus
spyking-circus RatS-Day1Openfield.dat --cpu 10

##################################################################
#####             Welcome to the SpyKING CIRCUS              #####
#####                        (1.1.0)                         #####
#####             Written by P.Yger and O.Marre              #####
##################################################################


File          : /mnt/w/Data/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield.dat
Steps         : filtering, whitening, clustering, fitting, merging
Number of CPU : 10/20
Parallel HDF5 : False
Shared memory : True
Hostfile      : /home/pho/spyking-circus/circus.hosts

##################################################################


-------------------------  Informations  -------------------------
| Number of recorded channels : 195
| Number of analyzed channels : 175
| File format                 : RAW_BINARY
| Data type                   : int16
| Sampling rate               : 30000 Hz
| Duration of the recording   : 87 min 28 s 819 ms
| Width of the templates      : 2 ms
| Spatial radius considered   : 120 um
| Threshold crossing          : negative
------------------------------------------------------------------
-------------------------  Informations  -------------------------
| Using only 10 out of 20 local CPUs available (-c to change)
------------------------------------------------------------------
-------------------------  Informations  -------------------------
| Filtering has already been done
------------------------------------------------------------------
Analyzing data to get whitening matrices and thresholds...
Found 15.9538s to compute the whitening matrix...
Because of whitening, need to recompute the thresholds...
Searching spikes to construct the PCA basis...
100%|████████████████████████████████████|[00:33<00:00,  1.02s/it]
Found 140000 waveforms over 140000 requested
-------------------------  Informations  -------------------------
| A basis with 5 dimensions has been built
------------------------------------------------------------------
Searching isolated random spikes to sample amplitudes...
100%|████████████████████████████████████|[06:08<00:00, 11.16s/it]
Found 828206 spikes over 1960000 requested
Estimating amplitudes distributions...
Smart Search of good isolated spikes for the clustering (1/5)...
100%|████████████████████████████████████|[06:42<00:00, 12.20s/it]
Found 761417 isolated spikes over 1960000 requested (199621 rejected)
Computing density estimations...
Searching random spikes to refine the clustering (2/5)...
100%|████████████████████████████████████|[06:39<00:00, 12.10s/it]
Found 158747 spikes over 1960000 requested
Refining density estimations...
Searching random spikes to refine the clustering (3/5)...
100%|████████████████████████████████████|[06:02<00:00, 10.98s/it]
Found 24260 spikes over 1960000 requested
Refining density estimations...
Searching random spikes to refine the clustering (4/5)...
100%|████████████████████████████████████|[05:59<00:00, 10.91s/it]
Found 100 spikes over 1960000 requested
Refining density estimations...
Searching random spikes to refine the clustering (5/5)...
100%|████████████████████████████████████|[05:51<00:00, 10.65s/it]
Found 0 spikes over 1960000 requested
-------------------------  Informations  -------------------------
| No more spikes in the recording, stop searching
------------------------------------------------------------------
Refining density estimations...
Running density-based clustering...
100%|████████████████████████████████████|[01:18<00:00,  4.34s/it]
-------------------------  Informations  -------------------------
| Number of clusters found : 230
| Number of local merges   : 32 (method nd-bhatta, param 2)
------------------------------------------------------------------
Estimating the templates with the median-raw procedure ...
100%|████████████████████████████████████|[00:07<00:00,  2.44it/s]
Removing 125 strongly shifted or noisy/mixture templates...
-------------------------  Informations  -------------------------
| Templates on few channels only (1), cc_merge set to 1 automatically
------------------------------------------------------------------
Removing mixtures of templates...
100%|███████████████████████████████████|[00:00<00:00, 107.28it/s]
100%|███████████████████████████████████|[00:00<00:00, 557.25it/s]
-------------------------  Informations  -------------------------
| Number of global merges    : 0
| Number of mixtures removed : 0
------------------------------------------------------------------
Computing optimal amplitudes for the templates...
100%|████████████████████████████████████|[00:09<00:00,  1.16it/s]
100%|████████████████████████████████████|[00:03<00:00,  4.52it/s]
Pre-computing the overlaps of templates...
100%|███████████████████████████████████|[00:00<00:00, 117.57it/s]
Here comes the SpyKING CIRCUS using 10 CPUs and 105 templates...
100%|████████████████████████████████████|[17:50<00:00,  4.90it/s]
Gathering spikes from 10 nodes...
100%|████████████████████████████████████|[00:01<00:00,  6.77it/s]
-------------------------  Informations  -------------------------
| Number of spikes fitted : 7794413
------------------------------------------------------------------
-------------------------  Informations  -------------------------
| Automatic merging with a threshold of 0.75
------------------------------------------------------------------
Updating the data...
100%|████████████████████████████████████|[00:03<00:00,  2.99it/s]
Deleting 11 noisy templates
Updating the data...
100%|████████████████████████████████████|[00:00<00:00, 54.41it/s]
Updating the data...
100%|████████████████████████████████████|[00:00<00:00, 53.84it/s]
-------------------------  Informations  -------------------------
| We kept 94 templates out of 105 after merging
| As meta merging is still experimental, you need
| to use the extension option to see its results
| >> circus-gui-matlab mydata.dat -e merged
| or
| >> spyking-circus mydata.dat -m converting -e merged
------------------------------------------------------------------
```

#### Merging for Phy Result:
```bash
(circus) pho@Apogee:/mnt/w/Data/Bapun/RatS/Day1Openfield/spyk-circ$ spyking-circus RatS-Day1Openfield.dat -m converting -e merged

##################################################################
#####             Welcome to the SpyKING CIRCUS              #####
#####                        (1.1.0)                         #####
#####             Written by P.Yger and O.Marre              #####
##################################################################


File          : /mnt/w/Data/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield.dat
Steps         : converting
Number of CPU : 10/20
Parallel HDF5 : False
Shared memory : True
Hostfile      : /home/pho/spyking-circus/circus.hosts

##################################################################


-------------------------  Informations  -------------------------
| Number of recorded channels : 195
| Number of analyzed channels : 175
| File format                 : RAW_BINARY
| Data type                   : int16
| Sampling rate               : 30000 Hz
| Duration of the recording   : 87 min 28 s 819 ms
| Width of the templates      : 2 ms
| Spatial radius considered   : 120 um
| Threshold crossing          : negative
------------------------------------------------------------------
-------------------------  Informations  -------------------------
| Using only 10 out of 20 local CPUs available (-c to change)
------------------------------------------------------------------
-------------------------  Informations  -------------------------
| Exporting data for the phy GUI with 10 CPUs...
------------------------------------------------------------------
100%|████████████████████████████████████|[11:40<00:00, 70.09s/it]
```

## Using Phy
NOTE: must switch to real Windows, not WSL.
Also will need to manually change paths in "W:\Data\Bapun\RatS\Day1Openfield\spyk-circ\RatS-Day1Openfield\RatS-Day1Openfield-merged.GUI\params.py" to Windows Paths
```params.py
dat_path = r"W:/Data/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield.dat"
n_channels_dat = 195
n_features_per_channel = 5
dtype = r"int16"
offset = 0
sample_rate = 30000.0
dir_path = r"W:/Data/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI"
hp_filtered = True
```

```ps1
cd "W:\Data\Bapun\RatS\Day1Openfield\spyk-circ\RatS-Day1Openfield\RatS-Day1Openfield-merged.GUI"
micromamba activate phy2
phy template-gui params.py
```






#############################################
### RatS-Day4Openfield
```bash
mv "/mnt/w/Data/Bapun/RatS/Day4Openfield/RatS-Day4Openfield.eeg" "/mnt/w/Data/Bapun/RatS/Day4Openfield/RatS-Day4Openfield.eeg.bak"
cd '/mnt/w/Data/Bapun/RatS/bapun_sess_init_scripts'
./scripts/process_resample -f 30000,1250 -n 200 "/mnt/w/Data/Bapun/RatS/Day4Openfield/RatS-Day4Openfield.dat" "/mnt/w/Data/Bapun/RatS/Day4Openfield/RatS-Day4Openfield.eeg"
```
#### Output 2026-05-26:
```bash
Input File     : /mnt/w/Data/Bapun/RatS/Day4Openfield/RatS-Day4Openfield.dat
Channels       : 200
Sampling Rate  : 30000.000000
Output file    : /mnt/w/Data/Bapun/RatS/Day4Openfield/RatS-Day4Openfield.eeg
Sampling Rate  : 1250.000000
Freq Ratio     : 0.041667
Converter      : Fastest Sinc Interpolator
Resampling     : 0% ################################################## 100%
Output Frames  : 20443109
```

### IN WSL 2026-05-27:
```bash
cd '/mnt/w/Data/Bapun/RatS/Day4Openfield/spyk-circ'
micromamba activate circus
spyking-circus RatS-Day4Openfield.dat --cpu 15
```
#### Run Result:
```bash
(circus) pho@Apogee:/mnt/w/Data/Bapun/RatS/Day4Openfield/spyk-circ$ spyking-circus RatS-Day4Openfield.dat --cpu 15

##################################################################
#####             Welcome to the SpyKING CIRCUS              #####
#####                        (1.1.0)                         #####
#####             Written by P.Yger and O.Marre              #####
##################################################################


File          : /mnt/w/Data/Bapun/RatS/Day4Openfield/spyk-circ/RatS-Day4Openfield.dat
Steps         : filtering, whitening, clustering, fitting, merging
Number of CPU : 15/20
Parallel HDF5 : False
Shared memory : True
Hostfile      : /home/pho/spyking-circus/circus.hosts

##################################################################


-------------------------  Informations  -------------------------
| Number of recorded channels : 195
| Number of analyzed channels : 175
| File format                 : RAW_BINARY
| Data type                   : int16
| Sampling rate               : 30000 Hz
| Duration of the recording   : 128 min 16 s 596 ms
| Width of the templates      : 2 ms
| Spatial radius considered   : 120 um
| Threshold crossing          : negative
------------------------------------------------------------------
-------------------------  Informations  -------------------------
| Using only 15 out of 20 local CPUs available (-c to change)
------------------------------------------------------------------
-------------------------  Informations  -------------------------
| Filtering has already been done
------------------------------------------------------------------
Analyzing data to get whitening matrices and thresholds...
Found 10.6359s to compute the whitening matrix...
Because of whitening, need to recompute the thresholds...
Searching spikes to construct the PCA basis...
100%|████████████████████████████████████|[00:39<00:00,  1.25it/s]
Found 139995 waveforms over 139995 requested
-------------------------  Informations  -------------------------
| A basis with 5 dimensions has been built
------------------------------------------------------------------
Searching isolated random spikes to sample amplitudes...
100%|████████████████████████████████████|[10:33<00:00, 12.94s/it]
Found 1266926 spikes over 1959990 requested
Estimating amplitudes distributions...
Smart Search of good isolated spikes for the clustering (1/5)...
100%|████████████████████████████████████|[11:53<00:00, 14.57s/it]
Found 1025546 isolated spikes over 1959990 requested (2444894 rejected)
Computing density estimations...
Searching random spikes to refine the clustering (2/5)...
100%|████████████████████████████████████|[08:57<00:00, 10.97s/it]
Found 537257 spikes over 1959990 requested
Refining density estimations...
Searching random spikes to refine the clustering (3/5)...
100%|████████████████████████████████████|[09:00<00:00, 11.03s/it]
Found 300177 spikes over 1959990 requested
Refining density estimations...
Searching random spikes to refine the clustering (4/5)...
100%|████████████████████████████████████|[08:52<00:00, 10.87s/it]
Found 176938 spikes over 1959990 requested
Refining density estimations...
Searching random spikes to refine the clustering (5/5)...
100%|████████████████████████████████████|[09:27<00:00, 11.57s/it]
Found 103394 spikes over 1959990 requested
Refining density estimations...
Running density-based clustering...
100%|████████████████████████████████████|[01:58<00:00,  9.87s/it]
-------------------------  Informations  -------------------------
| Number of clusters found : 280
| Number of local merges   : 12 (method nd-bhatta, param 2)
------------------------------------------------------------------
Estimating the templates with the median-raw procedure ...
100%|████████████████████████████████████|[00:07<00:00,  1.51it/s]
Removing 198 strongly shifted or noisy/mixture templates...
-------------------------  Informations  -------------------------
| Templates on few channels only (2), cc_merge set to 1 automatically
------------------------------------------------------------------
Removing mixtures of templates...
100%|████████████████████████████████████|[00:00<00:00, 19.05it/s]
100%|███████████████████████████████████|[00:00<00:00, 230.61it/s]
-------------------------  Informations  -------------------------
| Number of global merges    : 0
| Number of mixtures removed : 0
------------------------------------------------------------------
Computing optimal amplitudes for the templates...
100%|████████████████████████████████████|[00:10<00:00,  1.70s/it]
100%|████████████████████████████████████|[00:04<00:00,  2.97it/s]
Pre-computing the overlaps of templates...
100%|████████████████████████████████████|[00:00<00:00, 19.33it/s]
Here comes the SpyKING CIRCUS using 15 CPUs and 82 templates...
100%|██████████████████████████████████|[2:46:13<00:00,  1.94s/it]
Gathering spikes from 15 nodes...
100%|████████████████████████████████████|[00:02<00:00,  5.04it/s]
-------------------------  Informations  -------------------------
| Number of spikes fitted : 10958677
------------------------------------------------------------------
-------------------------  Informations  -------------------------
| Automatic merging with a threshold of 0.75
------------------------------------------------------------------
Updating the data...
100%|█████████████████████████████████|[00:00<00:00, 22651.51it/s]
Deleting 2 noisy templates
Updating the data...
100%|█████████████████████████████████|[00:00<00:00, 37843.34it/s]
Updating the data...
100%|█████████████████████████████████|[00:00<00:00, 51358.82it/s]
-------------------------  Informations  -------------------------
| We kept 80 templates out of 82 after merging
| As meta merging is still experimental, you need
| to use the extension option to see its results
| >> circus-gui-matlab mydata.dat -e merged
| or
| >> spyking-circus mydata.dat -m converting -e merged
------------------------------------------------------------------
```

#### Merging for Phy Result:
```bash
(circus) pho@Apogee:/mnt/w/Data/Bapun/RatS/Day4Openfield/spyk-circ$ spyking-circus RatS-Day4Openfield.dat -m converting -e merged

##################################################################
#####             Welcome to the SpyKING CIRCUS              #####
#####                        (1.1.0)                         #####
#####             Written by P.Yger and O.Marre              #####
##################################################################


File          : /mnt/w/Data/Bapun/RatS/Day4Openfield/spyk-circ/RatS-Day4Openfield.dat
Steps         : converting
Number of CPU : 10/20
Parallel HDF5 : False
Shared memory : True
Hostfile      : /home/pho/spyking-circus/circus.hosts

##################################################################


-------------------------  Informations  -------------------------
| Number of recorded channels : 195
| Number of analyzed channels : 175
| File format                 : RAW_BINARY
| Data type                   : int16
| Sampling rate               : 30000 Hz
| Duration of the recording   : 128 min 16 s 596 ms
| Width of the templates      : 2 ms
| Spatial radius considered   : 120 um
| Threshold crossing          : negative
------------------------------------------------------------------
-------------------------  Informations  -------------------------
| Using only 10 out of 20 local CPUs available (-c to change)
------------------------------------------------------------------
-------------------------  Informations  -------------------------
| Exporting data for the phy GUI with 10 CPUs...
------------------------------------------------------------------
100%|███████████████████████████████████|[25:19<00:00, 189.90s/it]
```

## Using Phy
NOTE: must switch to real Windows, not WSL.
Also will need to manually change paths in "W:\Data\Bapun\RatS\Day4Openfield\spyk-circ\RatS-Day4Openfield\RatS-Day4Openfield-merged.GUI\params.py" to Windows Paths
Example `params.py` file:
```params.py
dat_path = r"W:/Data/Bapun/RatS/Day4Openfield/spyk-circ/RatS-Day4Openfield.dat"
n_channels_dat = 195
n_features_per_channel = 5
dtype = r"int16"
offset = 0
sample_rate = 30000.0
dir_path = r"W:/Data/Bapun/RatS/Day4Openfield/spyk-circ/RatS-Day4Openfield/RatS-Day4Openfield-merged.GUI"
hp_filtered = True
```

```ps1
cd "W:\Data\Bapun\RatS\Day4Openfield\spyk-circ\RatS-Day4Openfield\RatS-Day4Openfield-merged.GUI"
micromamba activate phy2
phy template-gui params.py
```
