████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▋| 8714/8723 [38:0find spikes (circus-omp) (workers: 9 processes fork): 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▋| 8715/8723 [38:0find spikes (circus-omp) (workers: 9 processes fork): 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 8723/8723 [38:05<00:00,  3.82it/s]
Found 10070422 spikes
Kept 98 units after final merging
spykingcircus2 run time 2557.95s
sorter=spykingcircus2
output_folder=/nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/SORTING/folder_SC2
dry_run=False
num_units=98
num_segments=1
(bapun-sess-init-scripts) bash-4.4$ cd /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day1Openfield
(bapun-sess-init-scripts) bash-4.4$ uv run si-run-sorter run \
>   --basedir /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day1Openfield \
>   --basename RatS-Day1Openfield \
>   --sorter spykingcircus2 \
>   --run-name folder_SC2 \
>   --export-phy \
>   --phy-export-folder /nfs/turbo/umms-kdiba/Bapun/RatS/Day1Openfield/SORTING/folder_SC2_phy \
>   --n-jobs 9 \
>   --sorter-params-json '{"job_kwargs": {"n_jobs": 9, "max_threads_per_worker": 1}}'
/nfs/turbo/umms-kdiba/Bapun/RatS/NeuroPy/neuropy/utils/mixins/time_slicing.py:404: UserWarning: registration of accessor <class 'neuropy.utils.mixins.time_slicing.TimePointEventAccessor'> under name 'time_point_event' for type <class 'pandas.core.frame.DataFrame'> is overriding a preexisting attribute with the same name.
  @pd.api.extensions.register_dataframe_accessor("time_point_event")
Preprocessing the recording (bandpass filtering + CMR + whitening)
Geometry of the probe does not allow 1D drift correction
noise_level (workers: 9 processes fork): 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:00<00:00, 34.38it/s]
write_memory (workers: 9 processes fork): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4371/4371 [03:23<00:00, 21.48it/s]
get protoype waveforms (workers: 9 processes fork): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4371/4371 [00:01<00:00, 3445.85it/s]
detect peaks (matched_filtering) 
engine=process - n_jobs=9 - samples_per_chunk=30,000 - chunk_memory=14.42 MiB - total_memory=129.78 MiB - chunk_duration=1.00s
detect peaks (matched_filtering) (workers: 9 processes fork): 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4371/4371 [00:28<00:00, 156.03it/s]
Kept 619189 peaks for clustering
Fit peaks svd (workers: 9 processes fork): 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4371/4371 [00:01<00:00, 3726.30it/s]
Transform peaks svd (workers: 9 processes fork): 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4371/4371 [00:03<00:00, 1174.52it/s]
split_clusters with local_feature_clustering: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 153/153 [00:06<00:00, 22.69it/s]
/nfs/turbo/umms-kdiba/Bapun/RatS/spikeinterface/src/spikeinterface/core/baserecordingsnippets.py:259: UserWarning: There is no Probe attached to this recording. Creating a dummy one with contact positions
  warn("There is no Probe attached to this recording. Creating a dummy one with contact positions")
Removed 0 empty templates
Removed 0 unaligned templates
Removed 6 templates with too low SNR
Removed 11 templates with too high mean sd / noise ratio
Kept 127 raw clusters
/nfs/turbo/umms-kdiba/Bapun/RatS/spikeinterface/src/spikeinterface/postprocessing/template_similarity.py:345: NumbaTypeSafetyWarning: unsafe cast from uint64 to int64. Precision may be lost.
  overlapping_ids = overlapping_j_list[i]
/nfs/turbo/umms-kdiba/Bapun/RatS/spikeinterface/src/spikeinterface/core/baserecordingsnippets.py:259: UserWarning: There is no Probe attached to this recording. Creating a dummy one with contact positions
  warn("There is no Probe attached to this recording. Creating a dummy one with contact positions")
Kept 122 non-duplicated clusters
/nfs/turbo/umms-kdiba/Bapun/RatS/spikeinterface/src/spikeinterface/core/baserecordingsnippets.py:259: UserWarning: There is no Probe attached to this recording. Creating a dummy one with contact positions
  warn("There is no Probe attached to this recording. Creating a dummy one with contact positions")
Removed 0 empty templates
Removed 0 unaligned templates
Removed 0 templates with too low SNR
Removed 0 templates with too high mean sd / noise ratio
remove_small_cluster: kept  85 removed 37 (min_spike_count 437)
Kept 85 clean clusters
find spikes (circus-omp) 
engine=process - n_jobs=9 - samples_per_chunk=30,000 - chunk_memory=14.42 MiB - total_memory=129.78 MiB - chunk_duration=1.00s
find spikes (circus-omp) (workers: 9 processes fork):  23%|█████████████████████████████████████████████████████████████████████▎                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 find spikes (circus-omp) (workers: 9 processes fork):  23%|█████████████████████████████████████████████████████████████████████▌                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 find spikes (circus-omp) (workers: 9 processes fork): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4371/4371 [27:32<00:00,  2.65it/s]
Found 8618437 spikes
Kept 84 units after final merging
spykingcircus2 run time 2054.78s
estimate_sparsity (no parallelization): 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4371/4371 [02:41<00:00, 27.01it/s]
/nfs/turbo/umms-kdiba/Bapun/RatS/spikeinterface/src/spikeinterface/core/basesorting.py:509: UserWarning: The registered recording will not be persistent on disk, but only available in memory
  warnings.warn("The registered recording will not be persistent on disk, but only available in memory")
compute_waveforms (workers: 9 processes fork): 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1093/1093 [01:31<00:00, 11.99it/s]
/nfs/turbo/umms-kdiba/Bapun/RatS/spikeinterface/src/spikeinterface/exporters/to_phy.py:98: UserWarning: If the sorting_analyzer is sparse the 'sparsity' argument is ignored
  warnings.warn("If the sorting_analyzer is sparse the 'sparsity' argument is ignored")
write_binary (workers: 9 processes fork): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1093/1093 [01:57<00:00,  9.30it/s]
spike_amplitudes (workers: 9 processes fork): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1093/1093 [01:42<00:00, 10.65it/s]
Fitting PCA: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 84/84 [00:58<00:00,  1.44it/s]
Projecting waveforms: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 84/84 [00:00<00:00, 122.92it/s]
extract PCs (workers: 9 processes fork): 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1093/1093 [01:51<00:00,  9.84it/s]
Run:
phy template-gui  /nfs/turbo/umms-kdiba/Bapun/RatS/Day1Openfield/SORTING/folder_SC2_phy/params.py
sorter=spykingcircus2
output_folder=/nfs/turbo/umms-kdiba/Bapun/RatS/Day1Openfield/SORTING/folder_SC2
dry_run=False
num_units=84
num_segments=1
analyzer_folder=/nfs/turbo/umms-kdiba/Bapun/RatS/Day1Openfield/SORTING/folder_SC2_sorting_analyzer
phy_export_folder=/nfs/turbo/umms-kdiba/Bapun/RatS/Day1Openfield/SORTING/folder_SC2_phy
(bapun-sess-init-scripts) bash-4.4$ nvidia-smi
torch.cuda.is_available(); print(torch.cuda.get_device_name(0))"
uv run si-run-sorter list | grep kibash: nvidia-smi: command not found
(bapun-sess-init-scripts) bash-4.4$ uv run python -c "import torch; assert torch.cuda.is_available(); print(torch.cuda.get_device_name(0))"
losort4
Traceback (most recent call last):
  File "<string>", line 1, in <module>
AssertionError
(bapun-sess-init-scripts) bash-4.4$ uv run si-run-sorter list | grep kilosort4
/nfs/turbo/umms-kdiba/Bapun/RatS/NeuroPy/neuropy/utils/mixins/time_slicing.py:404: UserWarning: registration of accessor <class 'neuropy.utils.mixins.time_slicing.TimePointEventAccessor'> under name 'time_point_event' for type <class 'pandas.core.frame.DataFrame'> is overriding a preexisting attribute with the same name.
  @pd.api.extensions.register_dataframe_accessor("time_point_event")
kilosort4: 4.1.7