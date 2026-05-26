from pathlib import Path
import shutil
import sys
from typing import List, Dict, Tuple, Union, Set


def concatenate_to_output_file(input_paths: List[Path], output_path: Path):
    """ concatenates the binary files in input_paths to a single joined output_path. 
    """
    with open(output_path, "wb") as outfile:
        for path in input_paths:
            with open(path, "rb") as infile:
                shutil.copyfileobj(infile, outfile)
            


def step_perform_concat(found_raw_data_paths: List[Path], spyk_circ_output_dir: Path):
    """ performs the concatenation, creates the output directory if needed
    """
    ## make the "spyk-circ" output directory
    # spyk_circ_output_dir: Path = Path('W:/Data/Bapun/RatS/Day1Openfield/spyk-circ').resolve()
    spyk_circ_output_dir.mkdir(exist_ok=True, parents=True) ## dang I sure hope we're on Windows or I'll add some garbage paths :P
    
    ## Copy the concatenated files to the output directory
    concatenated_file_output_path: Path = spyk_circ_output_dir.joinpath('continuous_combined.dat').resolve() ## do I need to do anything with the adjacent `timestamps.npy` or anything??
    if not concatenated_file_output_path.exists():
        concatenate_to_output_file(input_paths=found_raw_data_paths, output_path=concatenated_file_output_path)
    return concatenated_file_output_path


def step_perform_downsample(concatenated_file_output_path: Path, sampling_frequency=30000, num_chan=200, resample_rate=1250) -> Path:
    import spikeinterface.extractors as se
    import spikeinterface.preprocessing as spre
    from spikeinterface.core import write_binary_recording

    # 1. Map the raw binary file (doesn't load into RAM yet)
    recording = se.read_binary(
        file_paths=concatenated_file_output_path.as_posix(), 
        sampling_frequency=sampling_frequency, 
        num_chan=num_chan, 
        dtype='int16'
    )

    # 2. Set up the downsampling node (applies anti-aliasing filter automatically)
    recording_lfp = spre.resample(recording, resample_rate=resample_rate)

    output_lfp_path: Path = concatenated_file_output_path.with_suffix('.lfp').resolve()
    print(f'trying to write to: "{output_lfp_path.as_posix()}"')
    # 3. Execute and write to a flat binary file in chunks
    # n_jobs=-1 uses all CPU cores for faster processing
    write_binary_recording(
        recording_lfp, 
        file_paths=output_lfp_path.as_posix(), 
        dtype='int16', 
        n_jobs=-1, 
        chunk_duration='1s'
    )
    print(f'\tdone.')
    return output_lfp_path



def main():
    print("Hello from rats!")
    raw_data_path: Path = Path(r'W:/Data/Bapun/RatS/Day1Openfield/Raw_data').resolve()
    print(f'raw_data_path: "{raw_data_path.as_posix()}"')

    ## find all constitutent "continuous.dat" files recurrsively in all subdirectories: "W:\Data\Bapun\RatS\Day1Openfield\Raw_data\2020-11-25_10-24-24\experiment1\recording1\continuous\Rhythm_FPGA-100.0\continuous.dat"
    found_raw_data_paths = ["W:/Data/Bapun/RatS/Day1Openfield/Raw_data/2020-11-25_10-20-27/experiment1/recording1/continuous/Rhythm_FPGA-100.0/continuous.dat",
                            # "W:/Data/Bapun/RatS/Day1Openfield/Raw_data/2020-11-25_10-24-24/experiment1/recording1/continuous/Rhythm_FPGA-100.0/continuous.dat", ## BAD ONE, only has 32 channels, skip
                            "W:/Data/Bapun/RatS/Day1Openfield/Raw_data/2020-11-25_13-02-47/experiment1/recording1/continuous/Rhythm_FPGA-100.0/continuous.dat",
                            "W:/Data/Bapun/RatS/Day1Openfield/Raw_data/2020-11-25_14-30-32/experiment1/recording1/continuous/Rhythm_FPGA-100.0/continuous.dat",
                            "W:/Data/Bapun/RatS/Day1Openfield/Raw_data/2020-11-25_15-06-02/experiment1/recording1/continuous/Rhythm_FPGA-100.0/continuous.dat",
    ]
    ## *-24-24 is a bad one with only 30 good channels!

    ## Iterate through and make proper paths, check their existance
    found_raw_data_paths: List[Path] = [Path(v).resolve() for v in found_raw_data_paths]
    ## could assert that they all exist... but let's NOT!

    ## make the "spyk-circ" output directory
    spyk_circ_output_dir: Path = Path('W:/Data/Bapun/RatS/Day1Openfield/spyk-circ').resolve()
    spyk_circ_output_dir.mkdir(exist_ok=True, parents=True) ## dang I sure hope we're on Windows or I'll add some garbage paths :P
    
    ## Copy the concatenated files to the output directory
    concatenated_file_output_path: Path = step_perform_concat(found_raw_data_paths=found_raw_data_paths, spyk_circ_output_dir=spyk_circ_output_dir)
    print(f'have concatenated_file_output_path: "{concatenated_file_output_path.as_posix()}"')

    output_lfp_path = step_perform_downsample(concatenated_file_output_path=concatenated_file_output_path)

    ## try specific output path
    # output_lfp_path = step_perform_downsample(concatenated_file_output_path=Path(r'W:\Data\Bapun\RatS\Day1Openfield\Raw_data\2020-11-25_13-02-47\experiment1\recording1\continuous\Rhythm_FPGA-100.0\continuous.dat'), num_chan=192)
    print(f'done with saving downsampled lfp')


if __name__ == "__main__":
    main()
