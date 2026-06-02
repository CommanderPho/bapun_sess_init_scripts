source /home/halechr/FastData/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
halechr@RDLU0039:~/FastData/Bapun/RatS$ source /home/halechr/FastData/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
(bapun-sess-init-scripts) halechr@RDLU0039:~/FastData/Bapun/RatS$ cd Day1Openfield
(bapun-sess-init-scripts) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield$ ls
dead_times.txt  RatS-Day1Openfield.dat  RatS-Day1Openfield.datetime.csv  RatS-Day1Openfield.eeg  RatS-Day1Openfield.nrs  RatS-Day1Openfield.position.npy  RatS-Day1Openfield.prb  RatS-Day1Openfield.prb.bak  RatS-Day1Openfield.xml  SORTING  spyk-circ
(bapun-sess-init-scripts) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield$ cd spyk-circ/
(bapun-sess-init-scripts) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ$ ls
phy.log             RatS-Day1Openfield-curation_review.csv  RatS-Day1Openfield.dead  RatS-Day1Openfield.nrs     RatS-Day1Openfield-phy-sorting_analyzer  RatS-Day1Openfield.prb.bak                RatS-Day1Openfield-sorting_analyzer
RatS-Day1Openfield  RatS-Day1Openfield.dat                  RatS-Day1Openfield.log   RatS-Day1Openfield.params  RatS-Day1Openfield.prb                   RatS-Day1Openfield-refinement_review.csv  RatS-Day1Openfield.xml
(bapun-sess-init-scripts) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ$ cd RatS-Day1Openfield
(bapun-sess-init-scripts) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield$ ls
RatS-Day1Openfield  RatS-Day1Openfield.basis.hdf5  RatS-Day1Openfield.clusters.hdf5  RatS-Day1Openfield.clusters-merged.hdf5  RatS-Day1Openfield-merged.GUI  RatS-Day1Openfield.overlap.hdf5  RatS-Day1Openfield.result.hdf5  RatS-Day1Openfield.result-merged.hdf5  RatS-Day1Openfield.templates.hdf5  RatS-Day1Openfield.templates-merged.hdf5
(bapun-sess-init-scripts) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield$ cd RatS-Day1Openfield-merged.GUI/
(bapun-sess-init-scripts) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ deactivate
halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ micromamba activate phy
micromamba: command not found
halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ micromamba activate phy2
micromamba: command not found
halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ mamba activate phy2
(phy2) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ phy
Usage: phy [OPTIONS] COMMAND [ARGS]...

  Interactive visualization and manual spike sorting of large-scale ephys
  data.

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  alf-convert        Convert an ephys dataset into ALF.
  extract-waveforms  Extract spike waveforms.
  kwik-describe      Describe a Kwik file.
  kwik-gui           Launch the Kwik GUI on a Kwik file.
  template-describe  Describe a template file.
  template-gui       Launch the template GUI on a params.py file.
  trace-gui          Launch the trace GUI on a raw data file.
(phy2) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ phy template-gui 
amplitudes.npy         channel_positions.npy  cluster_group.tsv      cluster_info.tsv.bak   params.py              pc_features.npy        phy.log                spike_clusters.npy     spike_times.npy        whitening_mat_inv.npy  
channel_map.npy        channel_shanks.npy     cluster_info.tsv       cluster_purity.tsv     pc_feature_ind.npy     .phy/                  similar_templates.npy  spike_templates.npy    templates.npy          whitening_mat.npy      
(phy2) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ phy template-gui params.py 
11:37:57.158 [W] model:668            Skipping spike waveforms that do not exist, they will be extracted on the fly from the raw data as needed.
11:37:57.159 [W] traces:161           Inconsistent number of channels between the params file and the binary dat file
11:44:02.715 [I] supervisor:702       Assigned 736 spikes.
11:44:14.397 [I] supervisor:698       Undo cluster assign.
File
----

Keyboard shortcuts
- exit                                     ctrl+q
- save                                     ctrl+s

View
----

Keyboard shortcuts
- switch_raw_data_filter                   alt+r
- toggle_spike_reorder                     ctrl+r

Help
----

Keyboard shortcuts
- about                                    ?
- show_all_shortcuts                       helpcontents, h

Snippets
--------

Keyboard shortcuts
- enable_snippet_mode                      :

Edit
----

Keyboard shortcuts
- label                                    l (:l)
- merge                                    g (:g)
- move_all_to_good                         ctrl+alt+g
- move_all_to_mua                          ctrl+alt+m
- move_all_to_noise                        ctrl+alt+n
- move_all_to_unsorted                     ctrl+alt+u
- move_best_to_good                        alt+g
- move_best_to_mua                         alt+m
- move_best_to_noise                       alt+n
- move_best_to_unsorted                    alt+u
- move_similar_to_good                     ctrl+g
- move_similar_to_mua                      ctrl+m
- move_similar_to_noise                    ctrl+n
- move_similar_to_unsorted                 ctrl+u
- redo                                     ctrl+shift+z, ctrl+y
- split                                    k (:k)
- split_init                               shift+ctrl+k
- undo                                     ctrl+z

Snippets
- filter                                   :f
- label                                    :l
- merge                                    :g
- select                                   :c
- sort                                     :s
- split                                    :k

Select
------

Keyboard shortcuts
- clear_filter                             esc
- first                                    home
- last                                     end
- next                                     space
- next_best                                down
- previous                                 shift+space
- previous_best                            up
- unselect_similar                         backspace

Snippets
- filter                                   :f
- label                                    :l
- merge                                    :g
- select                                   :c
- sort                                     :s
- split                                    :k

WaveformView
------------

Keyboard shortcuts
- decrease                                 ctrl+down
- extend_horizontally                      shift+right
- extend_vertically                        shift+up
- increase                                 ctrl+up
- narrow                                   ctrl+left
- next_waveforms_type                      w
- previous_waveforms_type                  shift+w
- shrink_horizontally                      shift+left
- shrink_vertically                        shift+down
- toggle_mean_waveforms                    m
- toggle_show_labels                       ctrl+l
- toggle_waveform_overlap                  o
- widen                                    ctrl+right

Snippets
- change_n_spikes_waveforms                :wn

CorrelogramView
---------------

Keyboard shortcuts
- toggle_normalization                     n

Snippets
- set_bin                                  :cb
- set_refractory_period                    :cr
- set_window                               :cw

ISIView
-------

Snippets
- set_bin_size (ms)                        :isib
- set_n_bins                               :isin
- set_x_max (ms)                           :isimax
- set_x_min (ms)                           :isimin

FeatureView
-----------

Keyboard shortcuts
- decrease                                 ctrl+-
- increase                                 ctrl++
- toggle_automatic_channel_selection       c

AmplitudeView
-------------

Keyboard shortcuts
- next_amplitudes_type                     a
- previous_amplitudes_type                 shift+a

FiringRateView
--------------

Snippets
- set_bin_size (s)                         :frb
- set_n_bins                               :frn
- set_x_max (s)                            :frmax
- set_x_min (s)                            :frmin

TraceView
---------

Keyboard shortcuts
- decrease                                 alt+down
- go_left                                  alt+left
- go_right                                 alt+right
- go_to                                    alt+t (:tg)
- go_to_end                                alt+end
- go_to_next_spike                         alt+pgdown
- go_to_previous_spike                     alt+pgup
- go_to_start                              alt+home
- increase                                 alt+up
- jump_left                                shift+alt+left
- jump_right                               shift+alt+right
- narrow                                   alt++
- switch_origin                            alt+o
- toggle_highlighted_spikes                alt+s
- toggle_show_labels                       alt+l
- widen                                    alt+-

Snippets
- go_to                                    :tg
- shift                                    :ts

ProbeView
---------

ClusterScatterView
------------------

Snippets
- set_size                                 :css
- set_x_axis                               :csx
- set_y_axis                               :csy

11:45:38.315 [I] supervisor:711       Change metadata_group for clusters 129 to good.
11:47:27.600 [I] supervisor:711       Change metadata_q for clusters 129 to 2.
11:50:20.381 [I] supervisor:711       Change metadata_q for clusters 116 to 8.
11:50:23.256 [I] supervisor:711       Change metadata_group for clusters 116 to good.
11:52:19.321 [I] supervisor:711       Change metadata_group for clusters 88 to noise.
(phy2) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ mamba install umap

Looking for: ['umap']

warning  libmamba Cache file "/home/halechr/miniforge3/pkgs/cache/497deca9.json" was modified by another program
warning  libmamba Cache file "/home/halechr/miniforge3/pkgs/cache/09cdf8bf.json" was modified by another program
conda-forge/noarch                                  26.4MB @  55.9MB/s  0.5s
conda-forge/linux-64                                53.9MB @  50.1MB/s  1.2s

Pinned packages:
  - python 3.11.*


Could not solve for environment specs
The following package could not be installed
└─ umap does not exist (perhaps a typo or a missing channel).
(phy2) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ mamba install umap -c conda-forge

Looking for: ['umap']

conda-forge/linux-64                                        Using cache
conda-forge/noarch                                          Using cache

Pinned packages:
  - python 3.11.*


Could not solve for environment specs
The following package could not be installed
└─ umap does not exist (perhaps a typo or a missing channel).
(phy2) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ mamba install -c conda-forge umap-learn

Looking for: ['umap-learn']

conda-forge/linux-64                                        Using cache
conda-forge/noarch                                          Using cache

Pinned packages:
  - python 3.11.*


Transaction

  Prefix: /home/halechr/miniforge3/envs/phy2

  Updating specs:

   - umap-learn
   - ca-certificates
   - certifi
   - openssl


  Package         Version  Build                  Channel          Size
─────────────────────────────────────────────────────────────────────────
  Install:
─────────────────────────────────────────────────────────────────────────

  + tqdm           4.67.3  pyh8f84b5b_0           conda-forge      94kB
  + libhwloc       2.13.0  default_he001693_1000  conda-forge       2MB
  + llvmlite       0.47.0  py311h41a00d4_1        conda-forge      34MB
  + tbb          2023.0.0  hab88423_2             conda-forge     182kB
  + numba          0.65.1  py311h3c884d5_1        conda-forge       6MB
  + pynndescent    0.5.13  pyhd8ed1ab_1           conda-forge      50kB
  + umap-learn     0.5.12  py311h38be061_0        conda-forge     201kB

  Summary:

  Install: 7 packages

  Total download: 43MB

─────────────────────────────────────────────────────────────────────────


Confirm changes: [Y/n] Y
tbb                                                182.3kB @   3.5MB/s  0.1s
tqdm                                                94.1kB @   1.2MB/s  0.1s
pynndescent                                         49.6kB @ 550.1kB/s  0.0s
libhwloc                                             2.4MB @  22.7MB/s  0.1s
umap-learn                                         201.0kB @   1.2MB/s  0.1s
numba                                                5.9MB @  25.2MB/s  0.2s
llvmlite                                            34.1MB @  76.7MB/s  0.4s

Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(phy2) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ mamba install -c conda-forge umap-learn scikit-learn

Looking for: ['umap-learn', 'scikit-learn']

conda-forge/linux-64                                        Using cache
conda-forge/noarch                                          Using cache

Pinned packages:
  - python 3.11.*


Transaction

  Prefix: /home/halechr/miniforge3/envs/phy2

  All requested packages already installed

(phy2) halechr@RDLU0039:~/FastData/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI$ phy template-gui params.py 
12:45:33.011 [W] model:668            Skipping spike waveforms that do not exist, they will be extracted on the fly from the raw data as needed.
12:45:33.011 [W] traces:161           Inconsistent number of channels between the params file and the binary dat file
12:46:17.555 [I] supervisor:711       Change metadata_group for clusters 2 to good.
12:46:38.613 [I] recluster_v2:156     Processing 14254 spikes with target 4 clusters
/home/halechr/miniforge3/envs/phy2/lib/python3.11/site-packages/umap/umap_.py:1952: UserWarning: n_jobs value 1 overridden to 1 by setting random_state. Use no seed for parallelism.
  warn(
12:46:57.312 [I] recluster_v2:106     Merged clusters 1 and 5 (correlation: 1.000)
12:46:57.322 [I] recluster_v2:106     Merged clusters 1 and 2 (correlation: 1.000)
12:46:57.331 [I] recluster_v2:106     Merged clusters 1 and 4 (correlation: 1.000)
12:46:57.339 [I] recluster_v2:106     Merged clusters 1 and 5 (correlation: 1.000)
12:46:57.345 [I] recluster_v2:106     Merged clusters 1 and 5 (correlation: 1.000)
12:46:57.351 [I] recluster_v2:106     Merged clusters 2 and 3 (correlation: 1.000)
12:46:57.355 [I] recluster_v2:106     Merged clusters 2 and 6 (correlation: 1.000)
12:46:57.359 [I] recluster_v2:106     Merged clusters 1 and 4 (correlation: 1.000)
12:46:57.362 [I] recluster_v2:106     Merged clusters 2 and 3 (correlation: 1.000)
12:46:57.365 [I] recluster_v2:106     Merged clusters 2 and 3 (correlation: 1.000)
12:46:57.365 [I] recluster_v2:188     Created 2 clusters after merging
12:46:57.414 [I] supervisor:702       Assigned 14254 spikes.
12:47:22.348 [I] supervisor:698       Undo cluster assign.
12:48:34.738 [I] supervisor:711       Change metadata_group for clusters 80 to noise.
12:48:39.473 [I] supervisor:711       Change metadata_group for clusters 137 to noise.
12:49:13.474 [I] supervisor:711       Change metadata_group for clusters 69 to good.
12:49:33.138 [I] supervisor:711       Change metadata_group for clusters 134 to good.
12:50:03.681 [I] supervisor:711       Change metadata_group for clusters 127 to good.
12:50:09.713 [I] supervisor:711       Change metadata_group for clusters 128 to good.
12:50:25.497 [I] supervisor:711       Change metadata_q for clusters 127 to 8.
12:50:30.663 [I] supervisor:711       Change metadata_q for clusters 128 to 8.
/home/halechr/.phy/plugins/custom_split_feature3.py:335: FutureWarning: `rcond` parameter will change to the default of machine precision times ``max(M, N)`` where M and N are the input matrix dimensions.
To use the future default and silence this warning we advise to pass `rcond=None`, to keep using the old, explicitly pass `rcond=-1`.
  ri, ri2, ri3, ri4 = np.linalg.lstsq(
12:51:06.137 [I] supervisor:702       Assigned 54451 spikes.
12:51:25.441 [I] supervisor:711       Change metadata_group for clusters 147 to good.
12:51:30.472 [I] supervisor:711       Change metadata_q for clusters 147 to 8.
12:51:39.361 [I] supervisor:711       Change metadata_group for clusters 148 to noise.
12:51:45.281 [I] supervisor:711       Change metadata_group for clusters 11 to good.
12:52:04.368 [I] supervisor:711       Change metadata_group for clusters 93 to good.
12:52:46.833 [I] supervisor:711       Change metadata_group for clusters 49 to good.
12:52:49.600 [I] supervisor:711       Change metadata_group for clusters 26 to good.
12:53:03.616 [I] supervisor:711       Change metadata_group for clusters 16 to good.
12:53:10.016 [I] supervisor:711       Change metadata_group for clusters 91 to good.
12:53:24.640 [I] supervisor:711       Change metadata_group for clusters 5 to good.
12:53:31.081 [I] supervisor:711       Change metadata_group for clusters 118 to good.
12:54:24.639 [I] supervisor:711       Change metadata_group for clusters 50 to good.
12:54:37.056 [I] supervisor:711       Change metadata_group for clusters 41 to good.
12:54:42.656 [I] supervisor:711       Change metadata_group for clusters 107 to good.
12:55:00.672 [I] supervisor:711       Change metadata_group for clusters 125 to good.
12:55:02.784 [I] supervisor:711       Change metadata_group for clusters 21 to good.
12:55:04.607 [I] supervisor:711       Change metadata_group for clusters 110 to good.
12:55:17.903 [I] supervisor:711       Change metadata_group for clusters 19 to good.
12:55:26.143 [I] supervisor:711       Change metadata_group for clusters 136 to good.
12:55:30.927 [I] supervisor:711       Change metadata_group for clusters 38 to good.
12:55:38.351 [I] supervisor:711       Change metadata_group for clusters 13 to good.
12:55:52.223 [I] supervisor:711       Change metadata_group for clusters 35 to good.
12:55:55.887 [I] supervisor:711       Change metadata_group for clusters 29 to good.
12:56:00.863 [I] supervisor:711       Change metadata_group for clusters 90 to noise.
12:56:19.359 [I] supervisor:711       Change metadata_group for clusters 20 to good.
12:56:22.543 [I] supervisor:711       Change metadata_group for clusters 36 to good.
12:56:27.535 [I] supervisor:711       Change metadata_group for clusters 0 to good.
12:56:31.614 [I] supervisor:711       Change metadata_group for clusters 47 to good.
12:56:35.950 [I] supervisor:711       Change metadata_group for clusters 72 to noise.
12:56:39.935 [I] supervisor:711       Change metadata_group for clusters 30 to good.
12:56:45.454 [I] supervisor:711       Change metadata_group for clusters 56 to noise.
12:57:34.654 [I] supervisor:711       Change metadata_group for clusters 64 to noise.
12:57:36.975 [I] supervisor:711       Change metadata_group for clusters 74 to noise.
12:58:00.411 [I] supervisor:700       Merge clusters 82 to 149.
12:58:38.829 [I] supervisor:700       Merge clusters 37 to 150.
12:58:44.582 [I] supervisor:700       Merge clusters 150 to 151.
12:58:54.302 [I] supervisor:711       Change metadata_group for clusters 73 to noise.
12:59:10.318 [I] supervisor:700       Merge clusters 81 to 152.
13:00:24.877 [I] supervisor:711       Change metadata_group for clusters 89 to noise.
13:00:38.733 [I] supervisor:711       Change metadata_group for clusters 47 to noise.
13:01:43.229 [I] supervisor:711       Change metadata_group for clusters 27 to noise.
13:05:38.058 [I] supervisor:711       Change metadata_group for clusters 105 to noise.
13:07:05.803 [I] supervisor:711       Change metadata_group for clusters 112 to good.
13:07:16.481 [I] supervisor:711       Change metadata_q for clusters 112 to 8.
13:07:51.609 [I] supervisor:711       Change metadata_group for clusters 123 to good.
13:09:29.897 [I] supervisor:711       Change metadata_group for clusters 149 to noise.
13:09:37.465 [I] supervisor:711       Change metadata_group for clusters 65 to noise.
13:10:42.538 [I] supervisor:711       Change metadata_group for clusters 92 to noise.
Selected channels =  145 157
13:12:59.331 [I] supervisor:702       Assigned 2987 spikes.
13:13:21.832 [I] supervisor:711       Change metadata_group for clusters 154 to noise.
13:14:54.839 [I] supervisor:711       Change metadata_group for clusters 153 to noise.
13:15:03.150 [I] supervisor:711       Change metadata_q for clusters 153 to 6.
13:20:02.885 [I] supervisor:711       Change metadata_group for clusters 108 to good.
13:21:01.061 [I] recluster_v2:156     Processing 11635 spikes with target 4 clusters
/home/halechr/miniforge3/envs/phy2/lib/python3.11/site-packages/umap/umap_.py:1952: UserWarning: n_jobs value 1 overridden to 1 by setting random_state. Use no seed for parallelism.
  warn(
13:21:06.950 [I] recluster_v2:106     Merged clusters 1 and 6 (correlation: 1.000)
13:21:06.959 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
13:21:06.966 [I] recluster_v2:106     Merged clusters 1 and 6 (correlation: 1.000)
13:21:06.973 [I] recluster_v2:106     Merged clusters 1 and 6 (correlation: 1.000)
13:21:06.978 [I] recluster_v2:106     Merged clusters 1 and 8 (correlation: 1.000)
13:21:06.983 [I] recluster_v2:106     Merged clusters 2 and 3 (correlation: 1.000)
13:21:06.987 [I] recluster_v2:106     Merged clusters 2 and 3 (correlation: 1.000)
13:21:06.989 [I] recluster_v2:106     Merged clusters 2 and 3 (correlation: 1.000)
13:21:06.992 [I] recluster_v2:106     Merged clusters 2 and 3 (correlation: 1.000)
13:21:06.994 [I] recluster_v2:106     Merged clusters 2 and 3 (correlation: 1.000)
13:21:06.994 [I] recluster_v2:188     Created 2 clusters after merging
13:21:07.033 [I] supervisor:702       Assigned 11635 spikes.
13:21:17.069 [I] supervisor:698       Undo cluster assign.
/home/halechr/.phy/plugins/custom_split_feature3.py:335: FutureWarning: `rcond` parameter will change to the default of machine precision times ``max(M, N)`` where M and N are the input matrix dimensions.
To use the future default and silence this warning we advise to pass `rcond=None`, to keep using the old, explicitly pass `rcond=-1`.
  ri, ri2, ri3, ri4 = np.linalg.lstsq(
13:21:27.783 [I] supervisor:702       Assigned 11635 spikes.
13:21:41.252 [I] supervisor:711       Change metadata_group for clusters 158 to noise.
13:22:11.435 [I] supervisor:702       Assigned 11605 spikes.
13:22:19.061 [I] supervisor:698       Undo cluster assign.
Selected channels =  137 138
13:22:46.244 [I] supervisor:702       Assigned 11605 spikes.
13:23:04.056 [I] supervisor:698       Undo cluster assign.
13:23:15.300 [I] supervisor:711       Change metadata_group for clusters 3 to good.
13:24:21.236 [I] supervisor:711       Change metadata_group for clusters 84 to good.
13:24:31.507 [I] supervisor:711       Change metadata_group for clusters 76 to good.
13:24:54.275 [I] supervisor:711       Change metadata_group for clusters 83 to good.
13:25:10.803 [I] supervisor:711       Change metadata_group for clusters 104 to good.
13:25:37.369 [I] recluster_v2:156     Processing 9851 spikes with target 4 clusters
13:25:49.112 [I] recluster_v2:106     Merged clusters 1 and 2 (correlation: 1.000)
13:25:49.120 [I] recluster_v2:106     Merged clusters 1 and 2 (correlation: 1.000)
13:25:49.127 [I] recluster_v2:106     Merged clusters 1 and 2 (correlation: 1.000)
13:25:49.133 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
13:25:49.138 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
13:25:49.142 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
13:25:49.145 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
13:25:49.148 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
13:25:49.150 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
13:25:49.151 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
13:25:49.152 [I] recluster_v2:188     Created 2 clusters after merging
13:25:49.223 [I] supervisor:702       Assigned 9851 spikes.
13:26:05.038 [I] supervisor:698       Undo cluster assign.
13:26:12.643 [I] supervisor:711       Change metadata_group for clusters 33 to good.
13:27:19.203 [I] supervisor:711       Change metadata_group for clusters 96 to good.
13:27:25.058 [I] supervisor:711       Change metadata_group for clusters 14 to good.
13:27:47.746 [I] supervisor:711       Change metadata_group for clusters 53 to good.
13:27:50.499 [I] supervisor:711       Change metadata_group for clusters 58 to good.
13:27:52.898 [I] supervisor:711       Change metadata_group for clusters 44 to good.
13:27:54.306 [I] supervisor:711       Change metadata_group for clusters 70 to good.
13:27:56.738 [I] supervisor:711       Change metadata_group for clusters 75 to good.
13:27:58.115 [I] supervisor:711       Change metadata_group for clusters 86 to good.
13:28:05.106 [I] supervisor:711       Change metadata_group for clusters 17 to good.
13:28:11.378 [I] supervisor:711       Change metadata_group for clusters 94 to good.
13:28:13.938 [I] supervisor:711       Change metadata_group for clusters 101 to good.
13:28:21.394 [I] supervisor:711       Change metadata_group for clusters 51 to good.
13:28:23.314 [I] supervisor:711       Change metadata_group for clusters 60 to good.
13:28:25.938 [I] supervisor:711       Change metadata_group for clusters 62 to good.
13:28:37.474 [I] supervisor:711       Change metadata_group for clusters 1 to good.
13:28:40.658 [I] supervisor:711       Change metadata_group for clusters 135 to good.
13:28:50.706 [I] supervisor:711       Change metadata_group for clusters 10 to good.
13:28:54.881 [I] supervisor:711       Change metadata_group for clusters 114 to good.
13:29:01.666 [I] supervisor:711       Change metadata_group for clusters 131 to good.
13:29:38.242 [I] supervisor:711       Change metadata_group for clusters 68 to good.
13:29:40.738 [I] supervisor:711       Change metadata_group for clusters 97 to good.
13:30:07.649 [I] supervisor:711       Change metadata_group for clusters 23 to good.
13:30:12.353 [I] supervisor:711       Change metadata_group for clusters 87 to noise.
13:30:19.217 [I] supervisor:711       Change metadata_group for clusters 40 to noise.
Selected channels =  185 186
13:30:56.059 [I] supervisor:702       Assigned 9435 spikes.
13:31:03.873 [I] supervisor:711       Change metadata_group for clusters 167 to noise.
Selected channels =  186 187
13:31:45.693 [I] supervisor:702       Assigned 14254 spikes.
13:32:00.529 [I] supervisor:711       Change metadata_group for clusters 171 to noise.
13:32:10.688 [I] supervisor:711       Change metadata_group for clusters 170 to noise.
13:32:14.480 [I] supervisor:711       Change metadata_group for clusters 3 to good.
/home/halechr/.phy/plugins/custom_split_feature3.py:335: FutureWarning: `rcond` parameter will change to the default of machine precision times ``max(M, N)`` where M and N are the input matrix dimensions.
To use the future default and silence this warning we advise to pass `rcond=None`, to keep using the old, explicitly pass `rcond=-1`.
  ri, ri2, ri3, ri4 = np.linalg.lstsq(
13:33:09.947 [I] supervisor:702       Assigned 15694 spikes.
13:33:23.732 [I] supervisor:698       Undo cluster assign.
13:33:29.499 [I] recluster_v2:156     Processing 15694 spikes with target 4 clusters
/home/halechr/miniforge3/envs/phy2/lib/python3.11/site-packages/umap/umap_.py:1952: UserWarning: n_jobs value 1 overridden to 1 by setting random_state. Use no seed for parallelism.
  warn(
13:33:37.836 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
13:33:37.847 [I] recluster_v2:106     Merged clusters 1 and 4 (correlation: 1.000)
13:33:37.857 [I] recluster_v2:106     Merged clusters 1 and 5 (correlation: 1.000)
13:33:37.865 [I] recluster_v2:106     Merged clusters 1 and 2 (correlation: 1.000)
13:33:37.872 [I] recluster_v2:106     Merged clusters 1 and 2 (correlation: 1.000)
13:33:37.877 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
13:33:37.882 [I] recluster_v2:106     Merged clusters 1 and 4 (correlation: 1.000)
13:33:37.886 [I] recluster_v2:106     Merged clusters 1 and 5 (correlation: 1.000)
13:33:37.889 [I] recluster_v2:106     Merged clusters 2 and 3 (correlation: 1.000)
13:33:37.892 [I] recluster_v2:106     Merged clusters 2 and 3 (correlation: 1.000)
13:33:37.892 [I] recluster_v2:188     Created 2 clusters after merging
13:33:37.937 [I] supervisor:702       Assigned 15694 spikes.
/home/halechr/.phy/plugins/custom_split_feature3.py:335: FutureWarning: `rcond` parameter will change to the default of machine precision times ``max(M, N)`` where M and N are the input matrix dimensions.
To use the future default and silence this warning we advise to pass `rcond=None`, to keep using the old, explicitly pass `rcond=-1`.
  ri, ri2, ri3, ri4 = np.linalg.lstsq(
13:55:59.442 [I] supervisor:702       Assigned 736 spikes.
13:56:21.079 [I] supervisor:711       Change metadata_group for clusters 177 to noise.
13:56:57.453 [I] supervisor:702       Assigned 704 spikes.
13:57:09.247 [I] supervisor:698       Undo cluster assign.
13:57:19.031 [I] supervisor:702       Assigned 704 spikes.
13:58:43.250 [I] supervisor:698       Undo cluster assign.
Selected channels =  87 88
14:01:55.077 [I] supervisor:702       Assigned 1939 spikes.
14:02:33.396 [I] supervisor:711       Change metadata_group for clusters 182 to good.
14:04:07.906 [I] supervisor:711       Change metadata_group for clusters 157 to noise.
14:04:10.898 [I] supervisor:711       Change metadata_group for clusters 169 to noise.
Selected channels =  71 72
14:04:37.895 [I] supervisor:702       Assigned 17850 spikes.
14:08:09.729 [I] supervisor:711       Change metadata_group for clusters 100 to noise.
14:08:16.496 [I] supervisor:711       Change metadata_group for clusters 76 to noise.
14:08:36.992 [I] supervisor:711       Change metadata_group for clusters 166 to noise.
14:08:40.273 [I] supervisor:711       Change metadata_group for clusters 168 to noise.
14:08:45.152 [I] supervisor:711       Change metadata_group for clusters 83 to noise.
14:08:46.720 [I] supervisor:711       Change metadata_group for clusters 104 to noise.
Selected channels =  69 70
14:09:23.977 [I] supervisor:702       Assigned 12867 spikes.
14:09:49.248 [I] supervisor:711       Change metadata_group for clusters 186 to noise.
14:09:50.128 [I] supervisor:711       Change metadata_group for clusters 187 to noise.
14:09:52.752 [I] supervisor:711       Change metadata_group for clusters 23 to noise.
14:09:54.704 [I] supervisor:711       Change metadata_group for clusters 69 to noise.
14:09:56.608 [I] supervisor:711       Change metadata_group for clusters 112 to noise.
14:09:58.225 [I] supervisor:711       Change metadata_group for clusters 123 to noise.
14:10:01.361 [I] supervisor:711       Change metadata_group for clusters 9 to noise.
14:10:03.920 [I] supervisor:711       Change metadata_group for clusters 33 to noise.
14:10:10.998 [I] supervisor:711       Change metadata_q for clusters 134 to 8.
14:10:16.704 [I] supervisor:711       Change metadata_group for clusters 55 to noise.
14:10:18.400 [I] supervisor:711       Change metadata_group for clusters 106 to noise.
14:10:41.647 [I] supervisor:711       Change metadata_group for clusters 14 to noise.
14:10:43.695 [I] supervisor:711       Change metadata_group for clusters 54 to noise.
14:10:59.333 [I] supervisor:711       Change metadata_q for clusters 67 to 8.
14:11:05.039 [I] supervisor:711       Change metadata_group for clusters 96 to noise.
14:11:11.631 [I] supervisor:711       Change metadata_group for clusters 120 to noise.
14:11:13.615 [I] supervisor:711       Change metadata_group for clusters 126 to noise.
14:11:16.175 [I] supervisor:711       Change metadata_group for clusters 174 to noise.
14:11:18.287 [I] supervisor:711       Change metadata_group for clusters 175 to noise.
14:11:21.535 [I] supervisor:711       Change metadata_group for clusters 53 to noise.
14:11:43.615 [I] supervisor:711       Change metadata_group for clusters 78 to noise.
14:12:19.700 [I] supervisor:711       Change metadata_q for clusters 58 to 8.
14:12:23.157 [I] supervisor:711       Change metadata_q for clusters 117 to 8.
14:12:46.175 [I] supervisor:711       Change metadata_group for clusters 44 to noise.
14:12:50.863 [I] supervisor:711       Change metadata_group for clusters 70 to noise.
14:12:57.300 [I] supervisor:711       Change metadata_q for clusters 75 to 8.
14:13:02.895 [I] supervisor:711       Change metadata_group for clusters 86 to noise.
14:13:06.479 [I] supervisor:711       Change metadata_group for clusters 113 to noise.
Selected channels =  86 89
14:13:46.919 [I] supervisor:702       Assigned 7732 spikes.
14:14:21.966 [I] supervisor:711       Change metadata_group for clusters 188 to noise.
Selected channels =  71 72
/home/halechr/miniforge3/envs/phy2/lib/python3.11/site-packages/sklearn/base.py:1336: ConvergenceWarning: Number of distinct clusters (1) found smaller than n_clusters (2). Possibly due to duplicate points in X.
  return fit_method(estimator, *args, **kwargs)
14:15:48.826 [I] supervisor:700       Merge clusters 189 to 190.
14:16:02.880 [I] supervisor:698       Undo cluster assign.
Selected channels =  87 88
14:16:16.322 [I] supervisor:702       Assigned 7283 spikes.
14:16:29.197 [I] supervisor:711       Change metadata_group for clusters 191 to noise.
Selected channels =  86 89
14:16:44.607 [I] supervisor:702       Assigned 6710 spikes.
14:16:55.693 [I] supervisor:698       Undo cluster assign.
Selected channels =  88 89
14:17:04.230 [I] supervisor:702       Assigned 6710 spikes.
14:17:09.384 [I] supervisor:698       Undo cluster assign.
14:17:11.868 [I] supervisor:711       Change metadata_group for clusters 192 to good.
14:18:25.708 [I] supervisor:711       Change metadata_group for clusters 28 to good.
14:18:30.734 [I] supervisor:711       Change metadata_q for clusters 28 to 8.
14:19:09.004 [I] supervisor:711       Change metadata_group for clusters 48 to noise.
14:20:46.603 [I] supervisor:711       Change metadata_group for clusters 51 to noise.
14:20:48.203 [I] supervisor:711       Change metadata_group for clusters 60 to noise.
14:20:49.259 [I] supervisor:711       Change metadata_group for clusters 62 to noise.
14:20:50.411 [I] supervisor:711       Change metadata_group for clusters 71 to noise.
14:20:51.499 [I] supervisor:711       Change metadata_group for clusters 93 to noise.
14:20:53.164 [I] supervisor:711       Change metadata_group for clusters 49 to noise.
14:20:53.979 [I] supervisor:711       Change metadata_group for clusters 26 to noise.
14:20:55.339 [I] supervisor:711       Change metadata_group for clusters 79 to noise.
14:20:56.140 [I] supervisor:711       Change metadata_group for clusters 16 to noise.
14:20:58.344 [I] supervisor:709       Undo move.
14:21:11.275 [I] supervisor:711       Change metadata_group for clusters 16 to good.
14:21:18.956 [I] supervisor:711       Change metadata_group for clusters 99 to noise.
14:21:27.308 [I] supervisor:711       Change metadata_group for clusters 130 to noise.
14:21:42.604 [I] supervisor:711       Change metadata_group for clusters 130 to unsorted.
Selected channels =  71 72
14:22:00.508 [I] supervisor:702       Assigned 72407 spikes.
14:22:08.425 [I] supervisor:698       Undo cluster assign.
14:22:16.907 [I] supervisor:711       Change metadata_group for clusters 1 to good.
14:22:19.466 [I] supervisor:711       Change metadata_group for clusters 1 to noise.
14:22:21.947 [I] supervisor:711       Change metadata_group for clusters 5 to noise.
14:22:23.820 [I] supervisor:711       Change metadata_group for clusters 91 to noise.
14:22:25.163 [I] supervisor:711       Change metadata_group for clusters 118 to noise.
14:22:28.971 [I] supervisor:711       Change metadata_group for clusters 135 to noise.
14:22:30.379 [I] supervisor:711       Change metadata_group for clusters 45 to noise.
14:22:33.371 [I] supervisor:711       Change metadata_group for clusters 50 to noise.
14:22:45.338 [I] supervisor:711       Change metadata_group for clusters 59 to noise.
14:22:51.371 [I] supervisor:711       Change metadata_group for clusters 115 to noise.
14:22:57.275 [I] supervisor:711       Change metadata_group for clusters 10 to noise.
14:22:58.522 [I] supervisor:711       Change metadata_group for clusters 114 to noise.
14:23:00.314 [I] supervisor:711       Change metadata_group for clusters 42 to noise.
14:23:01.402 [I] supervisor:711       Change metadata_group for clusters 32 to noise.
14:23:19.667 [I] recluster_v2:156     Processing 42685 spikes with target 4 clusters
/home/halechr/miniforge3/envs/phy2/lib/python3.11/site-packages/umap/umap_.py:1952: UserWarning: n_jobs value 1 overridden to 1 by setting random_state. Use no seed for parallelism.
  warn(
14:23:48.730 [I] recluster_v2:106     Merged clusters 1 and 2 (correlation: 1.000)
14:23:48.755 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
14:23:48.778 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
14:23:48.797 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
14:23:48.813 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
14:23:48.825 [I] recluster_v2:106     Merged clusters 1 and 4 (correlation: 1.000)
14:23:48.835 [I] recluster_v2:106     Merged clusters 1 and 4 (correlation: 1.000)
14:23:48.844 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
14:23:48.852 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
14:23:48.858 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
14:23:48.859 [I] recluster_v2:188     Created 2 clusters after merging
14:23:48.928 [I] supervisor:702       Assigned 42685 spikes.
Selected channels =  87 89
14:24:28.471 [I] supervisor:702       Assigned 38541 spikes.
14:24:38.889 [I] supervisor:711       Change metadata_group for clusters 201 to noise.
14:24:56.506 [I] supervisor:711       Change metadata_group for clusters 202 to noise.
14:24:58.858 [I] supervisor:711       Change metadata_group for clusters 107 to noise.
14:25:00.745 [I] supervisor:711       Change metadata_group for clusters 41 to noise.
14:25:02.781 [I] supervisor:709       Undo move.
14:25:06.425 [I] supervisor:711       Change metadata_group for clusters 41 to noise.
14:25:08.889 [I] supervisor:711       Change metadata_group for clusters 68 to noise.
14:25:09.946 [I] supervisor:711       Change metadata_group for clusters 125 to noise.
14:25:12.106 [I] supervisor:711       Change metadata_group for clusters 21 to noise.
14:25:13.754 [I] supervisor:711       Change metadata_group for clusters 110 to noise.
14:25:15.289 [I] supervisor:711       Change metadata_group for clusters 97 to noise.
14:25:16.553 [I] supervisor:711       Change metadata_group for clusters 19 to noise.
14:25:17.625 [I] supervisor:711       Change metadata_group for clusters 136 to noise.
14:25:19.753 [I] supervisor:711       Change metadata_group for clusters 38 to noise.
14:25:22.191 [I] supervisor:709       Undo move.
14:25:22.862 [I] supervisor:709       Undo move.
14:25:25.420 [I] supervisor:709       Undo move.
14:25:39.401 [I] supervisor:711       Change metadata_group for clusters 13 to noise.
14:25:41.082 [I] supervisor:711       Change metadata_group for clusters 39 to noise.
14:25:41.897 [I] supervisor:711       Change metadata_group for clusters 66 to noise.
14:25:43.241 [I] supervisor:711       Change metadata_group for clusters 35 to noise.
14:25:44.777 [I] supervisor:711       Change metadata_group for clusters 29 to noise.
14:25:45.642 [I] supervisor:711       Change metadata_group for clusters 24 to noise.
14:25:46.809 [I] supervisor:711       Change metadata_group for clusters 20 to noise.
14:25:47.801 [I] supervisor:711       Change metadata_group for clusters 36 to noise.
14:25:49.194 [I] supervisor:711       Change metadata_group for clusters 0 to noise.
14:25:51.625 [I] supervisor:711       Change metadata_group for clusters 30 to noise.
14:25:54.265 [I] supervisor:711       Change metadata_group for clusters 153 to noise.
14:25:56.489 [I] supervisor:711       Change metadata_group for clusters 46 to noise.
14:25:58.585 [I] supervisor:711       Change metadata_group for clusters 152 to noise.
14:26:20.313 [I] supervisor:711       Change metadata_group for clusters 98 to noise.
Selected channels =  71 72
14:27:10.976 [I] supervisor:702       Assigned 72407 spikes.
14:27:19.255 [I] supervisor:698       Undo cluster assign.
/home/halechr/.phy/plugins/custom_split_feature3.py:335: FutureWarning: `rcond` parameter will change to the default of machine precision times ``max(M, N)`` where M and N are the input matrix dimensions.
To use the future default and silence this warning we advise to pass `rcond=None`, to keep using the old, explicitly pass `rcond=-1`.
  ri, ri2, ri3, ri4 = np.linalg.lstsq(
14:27:34.277 [I] supervisor:702       Assigned 72407 spikes.
14:28:48.712 [I] supervisor:711       Change metadata_group for clusters 206 to noise.
14:28:52.808 [I] supervisor:711       Change metadata_group for clusters 15 to good.
14:29:17.689 [I] recluster_v2:156     Processing 71871 spikes with target 4 clusters
/home/halechr/miniforge3/envs/phy2/lib/python3.11/site-packages/umap/umap_.py:1952: UserWarning: n_jobs value 1 overridden to 1 by setting random_state. Use no seed for parallelism.
  warn(
14:30:04.870 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
14:30:04.911 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
14:30:04.945 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
14:30:04.974 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
14:30:04.999 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
14:30:05.021 [I] recluster_v2:106     Merged clusters 1 and 4 (correlation: 1.000)
14:30:05.046 [I] recluster_v2:106     Merged clusters 1 and 4 (correlation: 1.000)
14:30:05.062 [I] recluster_v2:106     Merged clusters 1 and 4 (correlation: 1.000)
14:30:05.075 [I] recluster_v2:106     Merged clusters 1 and 4 (correlation: 1.000)
14:30:05.087 [I] recluster_v2:106     Merged clusters 1 and 3 (correlation: 1.000)
14:30:05.089 [I] recluster_v2:188     Created 2 clusters after merging
14:30:05.194 [I] supervisor:702       Assigned 71871 spikes.
14:30:32.039 [I] supervisor:711       Change metadata_group for clusters 207 to noise.
14:30:32.903 [I] supervisor:711       Change metadata_group for clusters 208 to noise.
14:30:55.084 [I] qt:347               Saved screenshot to /home/halechr/.phy/screenshots/phy_screenshot_20260602143055_ClusterView.png.