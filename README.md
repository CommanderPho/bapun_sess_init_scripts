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

