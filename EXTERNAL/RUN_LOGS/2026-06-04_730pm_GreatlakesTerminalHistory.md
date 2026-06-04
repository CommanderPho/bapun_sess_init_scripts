7  cd ../pyPhoPlaceCellAnalysis/
8  ls
9  git pull
10  uv lock
11   ../NeuroPy
12  cd ../NeuroPy/
13  git pull
14  uv lock
15  cd ../Spike3D
16  uv lock
17  uv sync --all-extras
18  ./scripts/unix/launch_jupyter_lab_with_remote_access.sh 
19  pwd
20  deactivate
21  source /home/halechr/repos/Spike3D/.venv/bin/activate
22  deactivate
23  uv sync --all-extras
24  uv lock
25  uv remove datoviz
26  source .venv/bin/activate
27  ./scripts/unix/repos_pull_changes.sh 
28  ./scripts/unix/launch_jupyter_lab_with_remote_access.sh 
29  cd ../../
30  ls
31  cd Spike3D_ExploreEnv/
32  ls
33  git status
34  cd Spike3D/
35  git pull
36  git status
37  source /home/halechr/repos/Spike3D/.venv/bin/activate
38  deactivate
39  pwd
40  uv sync --all-extras
41  source .venv/bin/activate
42  jupyter-lab --help
43  jupyter server list
44  htop
45  git status
46  git pull
47  git status
48  pwd
49  ./scripts/unix/launch_jupyter_lab_with_remote_access.sh 
50  pwd
51  git pull
52  source /home/halechr/repos/Spike3D/.venv/bin/activate
53  pwd
54  deactivate
55  uv sync --all-extras
56  uv remove datoviz
57  uv sync --all-extras
58  ./scripts/unix/repos_pull_changes.sh 
59  git status
60  git add pyproject.toml 
61  git add uv.lock 
62  git status
63  git commit -m "GL"
64  git push
65  source .venv/bin/activate
66  source /home/halechr/repos/Spike3D/.venv/bin/activate
67  git stash save GL
68  deactivate
69  source /home/halechr/repos/Spike3D/.venv/bin/activate
70  uv lock
71  uv sync --all-extras
72  for global computations: Performing run_specific_computations_single_context(..., computation_functions_name_includelist=['predictive_decoding_analysis'], ...)...
73  run_specific_computations_single_context(including only 1 out of 16 registered computation functions): active_computation_functions: [<function PredictiveDecodingComputationsGlobalComputationFunctions.perform_predictive_decoding_analysis at 0x1513e5587430>]...
74  Performing _execute_computation_functions(...) with 1 registered_computation_functions...
75  Executing [0/1]: <function PredictiveDecodingComputationsGlobalComputationFunctions.perform_predictive_decoding_analysis at 0x150f7fbae670>
76  [perform_predictive_decoding_analysis] ========== STARTING ==========
77  [perform_predictive_decoding_analysis] Parameters: window_size=2, fine_time_bin_size=0.025, extant_decoded_time_bin_size=0.25
78  [perform_predictive_decoding_analysis] Flags: drop_previous_result_and_compute_fresh=False, enable_masked_filtered_container_before_any_comps=True
79  [perform_predictive_decoding_analysis] Flags: should_perform_first_pass_compute_future_and_past_analysis=True, enable_filter_and_final_result_processing=True
80  [perform_predictive_decoding_analysis] max_workers=1: disabling all parallel execution
81  [perform_predictive_decoding_analysis] WARN: include_includelist: ['sprinkle'] is specified but include_includelist is currently ignored! Continuing with defaults.
82  [perform_predictive_decoding_analysis] Filtering config: should_filter_by_active_spikes=True (min_spikes=5), should_filter_by_position_like_posterior_bins=True (cutoff=0.42)
83  [perform_predictive_decoding_analysis] --- PHASE 1: Loading and masking decoded results ---
84  [perform_predictive_decoding_analysis] Loaded DirectionalDecodersDecoded (deepcopy). spikes_df shape: (14486503, 16)
85  [perform_predictive_decoding_analysis] Applying masks to 1 time bin size(s)...
86  [perform_predictive_decoding_analysis]   Processing time_bin_size 1/1: 0.1s
87  The Kernel crashed while executing code in the current cell or a previous cell. 
88  Please review the code in the cell(s) to identify a possible cause of the failure. 
89  Click here for more info. 
90  pwd
91  tail -f 2026-02-06_mem_log.txt
92  %load_ext memory_profiler
93  from memory_profiler import memory_usage
94  import time
95  def monitor_computation():
96      return run_specific_computations_single_context(...)
97  # Record memory usage every 0.1 seconds
98  mem_use = memory_usage(monitor_computation, interval=0.1)
99  import matplotlib.pyplot as plt
100  plt.plot(mem_use)
101  plt.title('Memory usage over time')
102  plt.xlabel('Time (deciseconds)')
103  plt.ylabel('Memory usage (MiB)')
104  htop -u $USER
105  pwd
106  cd ../
107  cd pyPhoPlaceCellAnalysis/
108  uv add ../bayesian_changepoint_detection
109  pwd
110  cd ../../
111  ls
112  cd Spike3D_ExploreEnv/
113  ls
114  cd Spike3D/
115  git status
116  uv sync --all-extras
117  pwd
118  cd ../
119  git clone https://github.com/estcarisimo/bayesian_changepoint_detection.git
120  cd Spike3D/
121  git add ../bayesian_changepoint_detection
122  uv add ../bayesian_changepoint_detection/
123  tar -xvf Spike3DWorkEnv/
124  tar -xvf Spike3DWorkEnv.tar.gz Spike3DWorkEnv/
125  deactivate
126  ls
127  pwd
128  ./scripts/unix/repos_pull_changes.sh 
129  git stash save "GL"
130  ls
131  pwd
132  source deactivate
133  rm -rf .venv
134  pwd
135  ./scripts/unix/repos_pull_changes.sh 
136  git status
137  git stash save "GL"
138  git pull
139  git pull --force
140  pwd
141  cd ../../
142  ls
143  cd Spike3D_ExploreEnv/
144  cd Spike3D/
145  uv sync --all-extras
146  uv sync
147  uv remove datoviz
148  uv remove datoviz --group testing
149  ./scripts/unix/launch_jupyter_lab_with_remote_access.sh 
150  uv sync
151  uv sync --all-extras
152  source .venv/bin/activate
153  ./scripts/unix/launch_jupyter_lab_with_remote_access.sh 
154  pyenv shell 3.9.13
155  git pull
156  git pull --force
157  git status
158  git push
159  git pull
160  git pull --help
161  pyenv shell 3.9.13
162  git pull
163  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
164  deactivate
165  rm -rf .venv
166  ./scripts/unix/repos_pull_changes.sh 
167  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
168  cd ../
169  ls
170  zip -r Spike3D.zip Spike3D
171  cd Spike3D
172  deactivate
173  ls
174  git pull
175  ./scripts/unix/repos_pull_changes.sh 
176  uv lock
177  pwd
178  exit
179  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
180  cd ../
181  ls
182  git clone https://github.com/CommanderPho/pyPhoCoreHelpers.git
183  cd pyPhoCoreHelpers/
184  pwd
185  uv lock
186   builtin printf "\e[?1049h"
187   if [ "$_termius_integration_installed" = "" ]; then  _termius_integration_installed="yes";  builtin printf "\e]4545;A\a";  _termius_encode() {  builtin echo -n "$1" | command base64;  };  _termius_get_trap() {  builtin local -a terms;  builtin eval "terms=( $(trap -p "${1:-DEBUG}") )";  builtin printf '%s' "${terms[2]:-}";  };  _termius_original_PS1="$PS1";  _termius_custom_PS1="";  _termius_in_command_execution="1";  _termius_current_command="";  _termius_current_cwd() {  builtin printf "\e]4545;SetCwd;%s\a" "$(_termius_encode "$PWD")";  };  _termius_prompt_begins() {  builtin printf "\e]4545;ShellPromptBegins\a";  };  _termius_prompt_ends() {  builtin printf "\e]4545;ShellPromptEnds\a";  };  _termius_wrap_prompt() {  builtin printf "\[$(_termius_prompt_begins)\]%s\[$(_termius_prompt_ends)\]" "$1";  };  _termius_command_started() {  builtin printf "\e]4545;CommandStarted;%s\a" "$(_termius_encode "$1")";  };  _termius_command_exited() {  builtin printf "\e]4545;CommandExited;%s\a" "$1";  };  _termius_update_prompt() {  if [ "$_termius_in_command_execution" = "1" ]; then  if [[ "$_termius_custom_PS1" == "" || "$_termius_custom_PS1" != "$PS1" ]]; then  _termius_original_PS1=$PS1;  _termius_custom_PS1=$(_termius_wrap_prompt "$_termius_original_PS1");  PS1="$_termius_custom_PS1";  fi;  _termius_in_command_execution="0";  fi;  };  _termius_precmd() {  if [ "$_termius_current_command" != "" ]; then  _termius_command_exited "$_termius_status";  fi;  _termius_current_cwd;  _termius_current_command="";  _termius_update_prompt;  };  _termius_preexec() {  if [[ ! "$BASH_COMMAND" =~ ^_termius_prompt* ]]; then  if [[ "$BASH_COMMAND" == *"builtin printf \"\\e[?1049l\""* ]]; then  _termius_current_command=$BASH_COMMAND;  else  _termius_current_command="$(builtin history 1 | sed 's/ *[0-9]* *//')";  fi;  else  _termius_current_command="";  fi;  if [ "$_termius_current_command" != "" ]; then  _termius_command_started "$_termius_current_command";  fi;  };  if [[ -n "${bash_preexec_imported:-}" ]]; then  _termius_preexec_only() {  if [ "$_termius_in_command_execution" = "0" ]; then  _termius_in_command_execution="1";  _termius_preexec;  fi;  };  precmd_functions+=(_termius_prompt_cmd);  preexec_functions+=(_termius_preexec_only);  else  _termius_dbg_trap="$(_termius_get_trap DEBUG)";  if [[ -z "$_termius_dbg_trap" ]]; then  _termius_preexec_only() {  if [ "$_termius_in_command_execution" = "0" ]; then  _termius_in_command_execution="1";  _termius_preexec;  fi;  };  trap '_termius_preexec_only "$_"' DEBUG;  elif [[ "$_termius_dbg_trap" != '_termius_preexec "$_"' && "$_termius_dbg_trap" != '_termius_preexec_all "$_"' ]]; then  _termius_preexec_all() {  if [ "$_termius_in_command_execution" = "0" ]; then  _termius_in_command_execution="1";  builtin eval "${_termius_dbg_trap}";  _termius_preexec;  fi;  };  trap '_termius_preexec_all "$_"' DEBUG;  fi;  fi;  _termius_update_prompt;  _termius_restore_exit_code() {  return "$1";  };  _termius_prompt_cmd_original() {  _termius_status="$?";  _termius_restore_exit_code "${_termius_status}";  for cmd in "${_termius_original_prompt_command[@]}"; do  eval "${cmd:-}";  done;  _termius_precmd;  };  _termius_prompt_cmd() {  _termius_status="$?";  _termius_precmd;  };  _termius_original_prompt_command=$PROMPT_COMMAND;  if [[ -z "${bash_preexec_imported:-}" ]]; then  if [[ -n "$_termius_original_prompt_command" && "$_termius_original_prompt_command" != "_termius_prompt_cmd" ]]; then  PROMPT_COMMAND=_termius_prompt_cmd_original;  else  PROMPT_COMMAND=_termius_prompt_cmd;  fi;  fi;  builtin printf "\e]4545;B\a";  fi
188   builtin printf "\e[?1049l"
189  pwd
190  cd ../../
191  ls
192  cd Spike3D_
193  cd Spike3D_ExploreEnv/
194  cd Spike3D/
195  uv sync --all-extras
196  source .venv/bin/activate
197  ./scripts/unix/launch_jupyter_lab_with_remote_access.sh 
198  pwd
199  uv sync --all-extras
200  uv lock
201  uv remove pyjsoncanvas
202  pwd
203  cd ../../
204  ls
205  cd Spike3D_ExploreEnv/
206  ls
207  cd Spike3D/
208  ./scripts/unix/repos_pull_changes.sh 
209  uv sync --all-extras
210  cd ../../
211  ls
212  cd Spike3D_ExploreEnv/
213  ls
214  cd Spike3D/
215  uv sync --all-extras
216  uv lock
217  source .venv/bin/activate
218  ./scripts/unix/launch_jupyter_lab_with_remote_access.sh 
219  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
220  ls
221  git status
222  cd ../
223  ls
224  cd Spike3D_ExploreEnv/
225  ls
226  git pull
227  git status
228  git pull --force
229  git stash save GL
230  git stash save "GL"
231  cd Spike3D/
232  ls
233  git status
234  git stash save "GL"
235  git rebase --skip
236  git status
237  git pull
238  ./scripts/unix/repos_pull_changes.sh 
239  cd /home/halechr/cloud
240  ls
241  cd locker_dataDen/
242  ls
243  cd ../
244  mount_all_cloud_drives 
245  mount_locker_dataDen_GL 
246  ls
247  cd locker_dataDen/
248  ls
249  cd ../
250  cat mount_locker_dataDen_GL
251  which mount_locker_dataDen_GL
252  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
253  git fsck
254  pyenv shell 3.9.13
255  git status
256  git add SpecificResults/PendingNotebookCode.py 
257  git commit -m "GL good"
258  git hash-object -w src/pyphoplacecellanalysis/GUI/PyVista/InteractivePlotter/InteractivePlaceCellDataExplorer.py
259  pwd
260  cd ../../
261  ls
262  # 1. Delete the corrupted index file
263  rm .git/index
264  # 2. Rebuild the index from your current working directory
265  git reset
266  git status
267  git add src/pyphoplacecellanalysis/SpecificResults/PendingNotebookCode.py 
268  git commit -m "GL"
269  git fsck
270  # 1. Update the file timestamp so Git registers a change
271  touch src/pyphoplacecellanalysis/GUI/PyVista/InteractivePlotter/InteractivePlaceCellDataExplorer.py
272  # 2. Stage the file to overwrite the corrupt index reference with a fresh hash
273  git add src/pyphoplacecellanalysis/GUI/PyVista/InteractivePlotter/InteractivePlaceCellDataExplorer.py
274  # 3. Stage your notebook code
275  git add src/pyphoplacecellanalysis/SpecificResults/PendingNotebookCode.py
276  # 4. Commit again
277  git commit -m "GL"
278  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
279  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
280  cd /home/halechr/cloud/turbo/Data
281  ls
282  cd Bapun/
283  ls
284  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
285  deactivate 
286  uv sync --all-extras
287  uv remove datoviz
288  uv remove datoviz --group testing
289  source .venv/bin/activate
290  ./scripts/unix/repos_pull_changes.sh 
291  git pull
292  ls
293  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
294  pwd
295  git status
296  git stash save "GL"
297  git pull
298  ./scripts/unix/repos_pull_changes.sh 
299  uv sync --all-extras
300  ls
301  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
302  uv sync --all-extras
303  ./scripts/unix/repos_pull_changes.sh 
304  pwd
305  deactivate
306  git pull
307  ./scripts/unix/repos_pull_changes.sh 
308  pwd
309  cd ../
310  git clone https://github.com/CommanderPho/NeuroPy.git"
311  git clone https://github.com/CommanderPho/NeuroPy.git
312  cd NeuroPy/
313  git status
314  ls
315  git checkout feature/safe-advance
316  git pull
317  uv lock
318  pyenv shell 3.9.13
319  ls
320  pwd
321  cd ../../
322  ls
323  git pull
324  git fetch
325  git stash save "GL"
326  git pull
327  cd ../
328  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
329  ./scripts/unix/repos_pull_changes.sh 
330  uv lock
331  uv sync --all-extras
332  pyenv shell 3.9.13
333  git stash save "GL"
334  git pull
335  git pull --force
336  cd ../
337  ls
338  pwd
339  cd ../
340  ls
341  git fetch
342  pwd
343  cd Spike3D
344  git pull
345  git status
346  git stash save "GL"
347  git pull
348  ./scripts/unix/repos_pull_changes.sh 
349  cd ../NeuroPy/
350  git status
351  git fetch
352  git stash save "GL"
353  git
354  git pull --force
355  cd ../
356  ls
357  rm -rf NeuroPy
358  pwd
359  pwd
360  git pull
361  git status
362  ./scripts/unix/repos_pull_changes.sh 
363  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
364  git stash save "GL"
365  pyenv shell 3.9.13
366  pwd
367  cd ../../
368  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/activate
369  /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/python /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/ProcessBatchOutputs_qclus1246789_Only.ipy
370  git pull
371  git status
372  git stash save "GL"
373  git pull
374  pwd
375  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-07_11-26-53/run_kdiba_gor01_one_2006-6-07_11-26-53.sh'
376  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-08_14-26-15/run_kdiba_gor01_one_2006-6-08_14-26-15.sh'
377  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-07_16-40-19/run_kdiba_gor01_two_2006-6-07_16-40-19.sh'
378  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-08_21-16-25/run_kdiba_gor01_two_2006-6-08_21-16-25.sh'
379  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-09_22-24-40/run_kdiba_gor01_two_2006-6-09_22-24-40.sh'
380  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-12_16-53-46/run_kdiba_gor01_two_2006-6-12_16-53-46.sh'
381  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-09_17-29-30/run_kdiba_vvp01_one_2006-4-09_17-29-30.sh'
382  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-10_12-25-50/run_kdiba_vvp01_one_2006-4-10_12-25-50.sh'
383  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-09_16-40-54/run_kdiba_vvp01_two_2006-4-09_16-40-54.sh'
384  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-10_12-58-3/run_kdiba_vvp01_two_2006-4-10_12-58-3.sh'
385  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_17-46-44/run_kdiba_pin01_one_11-02_17-46-44.sh'
386  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_19-28-0/run_kdiba_pin01_one_11-02_19-28-0.sh'
387  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-03_12-3-25/run_kdiba_pin01_one_11-03_12-3-25.sh'
388  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_fet11-01_12-58-54/run_kdiba_pin01_one_fet11-01_12-58-54.sh'
389  git pull
390  git status
391  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-07_11-26-53/run_kdiba_gor01_one_2006-6-07_11-26-53.sh'
392  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-08_14-26-15/run_kdiba_gor01_one_2006-6-08_14-26-15.sh'
393  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-07_16-40-19/run_kdiba_gor01_two_2006-6-07_16-40-19.sh'
394  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-08_21-16-25/run_kdiba_gor01_two_2006-6-08_21-16-25.sh'
395  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-09_22-24-40/run_kdiba_gor01_two_2006-6-09_22-24-40.sh'
396  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-12_16-53-46/run_kdiba_gor01_two_2006-6-12_16-53-46.sh'
397  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-09_17-29-30/run_kdiba_vvp01_one_2006-4-09_17-29-30.sh'
398  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-10_12-25-50/run_kdiba_vvp01_one_2006-4-10_12-25-50.sh'
399  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-09_16-40-54/run_kdiba_vvp01_two_2006-4-09_16-40-54.sh'
400  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-10_12-58-3/run_kdiba_vvp01_two_2006-4-10_12-58-3.sh'
401  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_17-46-44/run_kdiba_pin01_one_11-02_17-46-44.sh'
402  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_19-28-0/run_kdiba_pin01_one_11-02_19-28-0.sh'
403  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-03_12-3-25/run_kdiba_pin01_one_11-03_12-3-25.sh'
404  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_fet11-01_12-58-54/run_kdiba_pin01_one_fet11-01_12-58-54.sh'
405  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-08_14-26-15/run_kdiba_gor01_one_2006-6-08_14-26-15.sh'
406  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-09_1-22-43/run_kdiba_gor01_one_2006-6-09_1-22-43.sh'
407  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-12_15-55-31/run_kdiba_gor01_one_2006-6-12_15-55-31.sh'
408  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-07_16-40-19/run_kdiba_gor01_two_2006-6-07_16-40-19.sh'
409  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-08_21-16-25/run_kdiba_gor01_two_2006-6-08_21-16-25.sh'
410  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-09_22-24-40/run_kdiba_gor01_two_2006-6-09_22-24-40.sh'
411  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-12_16-53-46/run_kdiba_gor01_two_2006-6-12_16-53-46.sh'
412  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-10_12-25-50/run_kdiba_vvp01_one_2006-4-10_12-25-50.sh'
413  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-09_16-40-54/run_kdiba_vvp01_two_2006-4-09_16-40-54.sh'
414  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-10_12-58-3/run_kdiba_vvp01_two_2006-4-10_12-58-3.sh'
415  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_fet11-01_12-58-54/run_kdiba_pin01_one_fet11-01_12-58-54.sh'
416  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_17-46-44/run_kdiba_pin01_one_11-02_17-46-44.sh'
417  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/activate
418  cd Spike3D/
419  ipython ProcessBatchOutputs_qclus1246789_Only.ipy 
420  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/activate
421  uv sync --all-extras
422  cd Spike3D/
423  uv sync --all-extras
424  python ProcessBatchOutputs.ipy
425  ipython ProcessBatchOutputs.ipy
426  pwd
427  source .venv/bin/activate
428  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-08_14-26-15/run_kdiba_gor01_one_2006-6-08_14-26-15.sh'
429  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-09_1-22-43/run_kdiba_gor01_one_2006-6-09_1-22-43.sh'
430  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-12_15-55-31/run_kdiba_gor01_one_2006-6-12_15-55-31.sh'
431  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-07_16-40-19/run_kdiba_gor01_two_2006-6-07_16-40-19.sh'
432  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-08_21-16-25/run_kdiba_gor01_two_2006-6-08_21-16-25.sh'
433  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-09_22-24-40/run_kdiba_gor01_two_2006-6-09_22-24-40.sh'
434  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-12_16-53-46/run_kdiba_gor01_two_2006-6-12_16-53-46.sh'
435  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-10_12-25-50/run_kdiba_vvp01_one_2006-4-10_12-25-50.sh'
436  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-09_16-40-54/run_kdiba_vvp01_two_2006-4-09_16-40-54.sh'
437  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-10_12-58-3/run_kdiba_vvp01_two_2006-4-10_12-58-3.sh'
438  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_fet11-01_12-58-54/run_kdiba_pin01_one_fet11-01_12-58-54.sh'
439  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_17-46-44/run_kdiba_pin01_one_11-02_17-46-44.sh'
440  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/activate
441  /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/python /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/ProcessBatchOutputs_qclus1246789_Only.ipy
442  pwd
443  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-08_14-26-15/run_kdiba_gor01_one_2006-6-08_14-26-15.sh'
444  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-09_1-22-43/run_kdiba_gor01_one_2006-6-09_1-22-43.sh'
445  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-12_15-55-31/run_kdiba_gor01_one_2006-6-12_15-55-31.sh'
446  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-07_16-40-19/run_kdiba_gor01_two_2006-6-07_16-40-19.sh'
447  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-08_21-16-25/run_kdiba_gor01_two_2006-6-08_21-16-25.sh'
448  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-09_22-24-40/run_kdiba_gor01_two_2006-6-09_22-24-40.sh'
449  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-12_16-53-46/run_kdiba_gor01_two_2006-6-12_16-53-46.sh'
450  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-10_12-25-50/run_kdiba_vvp01_one_2006-4-10_12-25-50.sh'
451  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-09_16-40-54/run_kdiba_vvp01_two_2006-4-09_16-40-54.sh'
452  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-10_12-58-3/run_kdiba_vvp01_two_2006-4-10_12-58-3.sh'
453  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_fet11-01_12-58-54/run_kdiba_pin01_one_fet11-01_12-58-54.sh'
454  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_17-46-44/run_kdiba_pin01_one_11-02_17-46-44.sh'
455  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/activate
456  /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/python /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/ProcessBatchOutputs_qclus1246789_Only.ipy
457  ls
458  cd Desktop/
459  ls
460  cd ../
461  ls
462  cd /scratch/kdiba_root/
463  ls
464  cd kdiba99
465  ls
466  cd halechr/
467  ls
468  cd repos/
469  ls
470  cd Spike3DEnv_KDibaVersion/
471  ls
472  cd Spike3D/
473  git status
474  uv sync --all-extras
475  source .venv/bin/activate
476  ipython ProcessBatchOutputs_qclus1246789_Only.ipy 
477  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-08_14-26-15/run_kdiba_gor01_one_2006-6-08_14-26-15.sh'
478  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-09_1-22-43/run_kdiba_gor01_one_2006-6-09_1-22-43.sh'
479  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-12_15-55-31/run_kdiba_gor01_one_2006-6-12_15-55-31.sh'
480  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-07_16-40-19/run_kdiba_gor01_two_2006-6-07_16-40-19.sh'
481  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-08_21-16-25/run_kdiba_gor01_two_2006-6-08_21-16-25.sh'
482  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-09_22-24-40/run_kdiba_gor01_two_2006-6-09_22-24-40.sh'
483  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-12_16-53-46/run_kdiba_gor01_two_2006-6-12_16-53-46.sh'
484  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-10_12-25-50/run_kdiba_vvp01_one_2006-4-10_12-25-50.sh'
485  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-09_16-40-54/run_kdiba_vvp01_two_2006-4-09_16-40-54.sh'
486  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-10_12-58-3/run_kdiba_vvp01_two_2006-4-10_12-58-3.sh'
487  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_fet11-01_12-58-54/run_kdiba_pin01_one_fet11-01_12-58-54.sh'
488  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_17-46-44/run_kdiba_pin01_one_11-02_17-46-44.sh'
489  ipython ProcessBatchOutputs_qclus1246789_Only.ipy 
490  cd /scratch/kdiba_root/kdiba99/halechr/
491  ls
492  cd repos/
493  ls
494  cd Spike3DEnv_KDibaVersion/
495  ls
496  cd Spike3D/
497  source .venv/bin/activate
498  ls
499  chmod +x ProcessBatchOutputs*
500  ls
501  htop
502  git status
503  pwd
504  git status
505  git add ProcessBatchOutputs_*
506  git status
507  git add ProcessBatchOutputs.ipy 
508  git commit -m "GL"
509  nano .gitignore 
510  git status
511  git add .gitignore 
512  git commit -m "ignored slurm outputs""
513  "
514  git status
515  git pull
516  git push
517  nano ProcessBatchOutputs_qclus1246789_Only.ipy 
518  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-08_14-26-15/run_kdiba_gor01_one_2006-6-08_14-26-15.sh'
519  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-09_1-22-43/run_kdiba_gor01_one_2006-6-09_1-22-43.sh'
520  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-12_15-55-31/run_kdiba_gor01_one_2006-6-12_15-55-31.sh'
521  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-07_16-40-19/run_kdiba_gor01_two_2006-6-07_16-40-19.sh'
522  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-08_21-16-25/run_kdiba_gor01_two_2006-6-08_21-16-25.sh'
523  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-09_22-24-40/run_kdiba_gor01_two_2006-6-09_22-24-40.sh'
524  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-12_16-53-46/run_kdiba_gor01_two_2006-6-12_16-53-46.sh'
525  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-10_12-25-50/run_kdiba_vvp01_one_2006-4-10_12-25-50.sh'
526  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-09_16-40-54/run_kdiba_vvp01_two_2006-4-09_16-40-54.sh'
527  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-10_12-58-3/run_kdiba_vvp01_two_2006-4-10_12-58-3.sh'
528  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_fet11-01_12-58-54/run_kdiba_pin01_one_fet11-01_12-58-54.sh'
529  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_17-46-44/run_kdiba_pin01_one_11-02_17-46-44.sh'
530  pwd
531  source .venv/bin/activate
532  ipython ProcessBatchOutputs_qclus1246789_Only.ipy 
533  cd Spike3D
534  git pull
535  ls
536  ./scripts/unix/repos_pull_changes.sh 
537  uv lock
538  uv-deps-switcher dev
539  uv lock
540  uv-deps-switcher dev
541  uv lock
542  uv sync --all-extras
543  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
544  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/activate
545  uv lock
546  uv sync --all-extras
547  pyenv shell 3.9.13
548  pwd
549  ./scripts/unix/repos_pull_changes.sh 
550  uv lock
551  uv sync --all-extras
552  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/activate
553  pyenv shell 3.9.13
554  git stash save "GL"
555  git status
556  pwd
557  ls
558  cd ../../
559  ls
560  git status
561  git pull
562  git pull --force
563  ./scripts/unix/repos_pull_changes.sh 
564  pwd
565  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
566  deactivate
567  uv lock
568  git pull
569  git sdtatus
570  git status
571  git add uv.lock 
572  git commit -m "GL"
573  git pull
574  ./scripts/unix/repos_pull_changes.sh 
575  uv lock
576  uv sync --all-extras
577  source .venv/bin/activate
578  ipython ProcessBatchOutputs_Bapun_Batch.ipy 
579  micromamba activate circus
580  eval "$(micromamba shell hook --shell=bash)"
581  pwd
582  cd Day1Openfield/
583  ls
584  cd spyk-circ/
585  ls
586  rm -rf RatS-Day1Openfield
587  ls
588  micromamba activate circus
589  pwd
590  ls
591  spyking-circus RatS-Day1Openfield.dat -c 32
592  ls
593  cd ~/cloud/turbo/
594  ls
595  cd Bapun/
596  ls
597  cd RatS
598  ls
599  cat README.md 
600  micromamba activate circus
601  eval "$(micromamba shell hook --shell=bash)"
602  micromamba activate circus
603  micromamba install -c conda-forge -c spyking-circus spyking-circus
604  pyenv shell 3.9.13
605  eval "$(micromamba shell hook --shell=bash)"
606  micromamba env list
607  micromamba activate phy2
608  ls
609  cd Day1Openfield/
610  cd spyk-circ/RatS-Day1Openfield
611  ls
612  cd ../
613  pyenv shell 3.9.13
614  history
615  eval "$(micromamba shell hook --shell=bash)"
616  micromamba activate circus
617  pwd
618  ls
619  cd Day1Openfield/
620  ls
621  cd spyk-circ/
622  ls -la
623  spyking-circus RatS-Day1Openfield.dat -c 32
624  spyking-circus RatS-Day1Openfield.dat -c 16
625  spyking-circus RatS-Day1Openfield.dat -c 15
626  pyenv shell 3.9.13
627  cd Day4Openfield/
628  cd spyk-circ/
629  ls
630  ln -s ../_BAK/RatS-Day4Openfield.dat RatS-Day4Openfield.dat
631  mamba
632  micromamba activate circus
633  eval "$(micromamba shell hook --shell=bash)"
634  micromamba activate circus
635  spyking-circus spyking-circus RatS-Day4Openfield.dat --cpu 15
636  spyking-circus RatS-Day4Openfield.dat --cpu 15
637  ls
638  pwd
639  rm -rf RatS-Day4Openfield
640  rm RatS-Day4Openfield.dat 
641  pwd
642  ln -s ../RatS-Day4Openfield.dat RatS-Day4Openfield.dat
643  spyking-circus RatS-Day4Openfield.dat --cpu 20
644  ls
645  pwd
646  rm RatS-Day4Openfield.dat 
647  cp ../RatS-Day4Openfield.dat RatS-Day4Openfield.dat
648  cd /nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/spyk-circ
649  ls
650  cd ../
651  ls
652  chmod +x ConcatenateDatFiles.sh 
653  ./ConcatenateDatFiles.sh 
654  InputFile1=/nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/Raw_data/2020-12-02_10-54-43/experiment1/recording1/continuous/Intan_Rec._Controller-100.0/continuous.dat
655  InputFile2=/nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/Raw_data/2020-12-02_11-37-13/experiment1/recording1/continuous/Intan_Rec._Controller-100.0/continuous.dat
656  InputFile3=/nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/Raw_data/2020-12-02_14-46-16/experiment1/recording1/continuous/Intan_Rec._Controller-100.0/continuous.dat
657  OutputFile=/nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/RatS-Day4Openfield.dat
658  cat ${InputFile1} ${InputFile2} ${InputFile3} > ${OutputFile}
659  cd /nfs/turbo/umms-kdiba/Bapun/RatS/Day1Openfield/spyk-circ
660  mamba activate circus
661  micromamba activate circus
662  eval "$(micromamba shell hook --shell=bash)"
663  micromamba activate circus
664  spyking-circus RatS-Day1Openfield.dat --cpu 30
665  spyking-circus RatS-Day1Openfield.dat --cpu 16
666  ls
667  rm RatS-Day1Openfield.dat
668  cp ../RatS-Day1Openfield.dat RatS-Day1Openfield.dat
669  spyking-circus RatS-Day1Openfield.dat --cpu 15
670  spyking-circus RatS-Day1Openfield.dat --cpu 8
671  pyenv shell 3.9.13
672  micromamba activate circus
673  pwd
674  cd Day4Openfield/
675  cd spyk-circ/
676  cd ../../
677  cd Day1Openfield/
678  cd spyk-circ/
679  spyking-circus RatS-Day1Openfield.dat -m converting -e merged
680  deactivate
681  micromamba deactivate
682  micromamba activate phy2
683  phy template-gui params.py
684  ls
685  pwd
686  phy template-gui
687  ls
688  phy template-gui RatS-Day1Openfield.params 
689  cd /nfs/turbo/umms-kdiba/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI
690  phy template-gui RatS-Day1Openfield.params 
691  phy template-gui params.py 


692  micromamba activate circus
693  micromamba shell init --shell=bash --prefix=~/micromamba
694  micromamba activate circus
695  eval "$(micromamba shell hook --shell=bash)"
696  micromamba activate circus
697  micromamba
698  mamba
699  eval "$(micromamba shell hook --shell=bash)"
700  micromamba
701  eval "$(micromamba shell hook --shell=bash)"
702  micromamba activate circus
703  spyking-circus RatS-Day1Openfield.dat --cpu 15
704  pwd
705  cd /nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/spyk-circ
706  meval "$(micromamba shell hook --shell=bash)"
707  micromamba activate circus
708  eval "$(micromamba shell hook --shell=bash)"
709  micromamba activate circus
710  ls
711  spyking-circus RatS-Day1Openfield.dat -c 15
712  ls
713  pwd
714  spyking-circus RatS-Day4Openfield.dat -c 15
715  deactivate
716  micromamba deactivate
717  micromamba activate phy
718  micromamba activate phy2
719  ls
720  cd RatS-Day4Openfield
721  ls
722  cd ../
723  ls
724  cd RatS-Day4Openfield
725  ls
726  cd RatS-Day4Openfield
727  ls
728  cd ../
729  micromamba activate circus
730  pwd
731  cd ../
732  spyking-circus RatS-Day4Openfield.dat -m converting -e merged
733  pyenv shell 3.9.13
734  uv lock
735  cd bapun_sess_init_scripts/
736  ls
737  uv lock
738  uv sync --all-extras
739  uv add PyQt5
740  rm uv.lock 
741  uv lock
742  uv sync
743  uv sync --all-extras
744  uv add PyQt6
745  ldd --version
746  uv add "pyside6<6.10"
747  uv add "pyqt6<6.10"
748  uv lock
749  uv add "pyqt6<6.10"
750  uv remove pyside6
751  uv lock
752  pwd
753  uv tool
754  uv tool upgrade
755  uv tool upgrade uv-deps-switcher
756  uv-deps-switcher 
757  uv-deps-switcher dev
758  uv lock
759  uv sync
760  uv-deps-switcher 
761  cd ../
762  ls
763  cd NeuroPy/
764  git status
765  git pull
766  uv lock
767  rm -rf .venv
768  uv lock
769  uv sync --all-extras
770  cd bapun_sess_init_scripts/
771  git pull
772  git stash save "GL"
773  git pull
774  uv lock
775  uv sync --all-extras
776  uv lock
777  uv add pyqt5
778  uv lock
779  uv add pyqt5
780  uv add PyQt5
781  uv lock
782  uv sync --all-extras
783  rm -rf .venv
784  pyenv shell 3.9.13
785  cd bapun_sess_init_scripts/
786  git pull
787  uv lock
788  uv sync
789  uv remove pyside6
790  uv lock
791  uv sync
792  uv lock
793  uv add PyQt5
794  uv lock
795  uv syc
796  uv sync
797  uv remove spikeinterface-gui
798  uv lock
799  uv sync --all-extras
800  pwd
801  uv run ipython kernel install --user --name=bapun-sess-init-UV
802  pyenv shell 3.9.13
803  pwd
804  cd bapun_sess_init_scripts/
805  git status
806  git pull
807  git stash save "GL"


808  cd /nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/spyk-circ/RatS-Day4Openfield/RatS-Day4Openfield-merged.GUI
809  ls
810  mamba phy2 activate
811  micromamba phy2 activate
812  micromamba activate phy2
813  pwd
814  phy 
815  phy template-gui params.py 



816  pyenv shell 3.9.13
817  cd bapun_sess_init_scripts/
818  uv lock
819  uv sync --all-extras
820  nvidia-smi
821  uv run python -c "import torch; assert torch.cuda.is_available(); print(torch.cuda.get_device_name(0))"
822  uv run si-run-sorter list | grep kilosort4
823  pyenv shell 3.9.13
824  pwd
825  cd bapun_sess_init_scripts/
826  source .venv/bin/activate
827  uv run si-run-sorter list
828  pyenv shell 3.9.13
829  pwd
830  ls
831  cd bapun_sess_init_scripts/
832  ls
833  uv lock
834  uv-deps-switcher dev
835  uv lock
836  uv remove spikeinterface-gui
837  uv sync --all-extras
838  uv lock
839  uv sync --all-extras
840  uv run si-run-sorter list
841  uv run si-run-sorter run   --basedir /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield   --basename RatS-Day4Openfield   --sorter kilosort4   --run-name folder_KS4_v1
842  history
843  pyenv shell 3.9.13
844  ls
845  cd bapun_sess_init_scripts/
846  uv sync --all-extras
847  source .venv/bin/activate
848  uv run si-run-sorter run   --basedir /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield   --basename RatS-Day4Openfield   --sorter spykingcircus2   --run-name folder_SC2   --sorter-params-json '{"job_kwargs": {"n_jobs": 9, "max_threads_per_worker": 1}}'
849  cd /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day1Openfield
850  uv run si-run-sorter run   --basedir /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day1Openfield   --basename RatS-Day1Openfield   --sorter spykingcircus2   --run-name folder_SC2   --export-phy   --phy-export-folder /nfs/turbo/umms-kdiba/Bapun/RatS/Day1Openfield/SORTING/folder_SC2_phy   --n-jobs 9   --sorter-params-json '{"job_kwargs": {"n_jobs": 9, "max_threads_per_worker": 1}}'
851  nvidia-smi
852  uv run python -c "import torch; assert torch.cuda.is_available(); print(torch.cuda.get_device_name(0))"
853  uv run si-run-sorter list | grep kilosort4
854  history
855  history > ../bapun_sess_init_scripts/EXTERNAL/RUN_LOGS/2026-06-02_437pm_GreatlakesCPU_spykingcircus2_run_history.log
856  source /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
857  cd /tmpssd/
858  mkdir halechr
859  cd halechr/
860  ls -la
861  pwd
862  uv run si-run-sorter list --show-default-params   # optional: sorter defaults
863  pwd
864  cd bapun_sess_init_scripts/
865  uv lock
866  uv sync --all-extras
867  uv add pynvml
868  source /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
869  cd /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield
870  ls
871  cd spyk-circ/
872  ls
873  pwd
874  mkdir  /tmpssd/halechr/Day4Openfield
875  cp -R /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield/spyk-circ /tmpssd/halechr/Day4Openfield/spyk-circ
876  rsync -a -W --no-compress --info=progress2 --exclude='*_BAK*' --exclude='*bak' /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield/spyk-circ/ /tmpssd/halechr/Day4Openfield/spyk-circ/
877  nvidia-smi
878  uv run python -c "import torch; assert torch.cuda.is_available(); print(torch.cuda.get_device_name(0))"
879  uv run si-run-sorter list | grep kilosort4
880  source /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
881  uv lock
882  cd bapun_sess_init_scripts/
883  uv sync --all-extras
884  pwd
885  uv run si-run-sorter run --basedir /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield --basename RatS-Day4Openfield --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /home/halechr/FastData/Bapun/RatS/Day4Openfield/SORTING/folder_KS4_v1_phy
886  uv run si-run-sorter run --basedir /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield --basename RatS-Day4Openfield --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield/SORTING/folder_KS4_v1_phy
887  uv run si-run-sorter run --basedir /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield --basename RatS-Day4Openfield --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield/SORTING/folder_KS4_v1_phy --help
888  uv run si-run-sorter run --basedir /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield --basename RatS-Day4Openfield --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield/SORTING/folder_KS4_v1_phy --remove-existing-folder
889  history
890  pyenv shell 3.9.13
891  cd /nfs/dataden/umms-dibalab
892  rm -rf ~/cloud/locker_dataDen
893  mount_all_cloud_drives
894  pwd
895  ls
896  source greatlakes_Helpers/
897  mount_locker_dataDen_GL
898  source greatlakes_Helpers/greatlakes_MOUNT.sh 
899  mount_locker_dataDen
900  mount_locker_dataDen_GL 
901  source /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
902  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/folder_KS4_v1_phy
903  source /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
904  uv lock
905  ls
906  cd bapun_sess_init_scripts/
907  uv lock
908  uv sync --all-extras
909  uv run si-curate-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --run-name folder_KS4_v1 --strategy sua_relaxed_prob --n-jobs 9 --patch-pandas-compat
910  uv run si-curate-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --run-name RatS-Day5TwoNovel-2020-12-04_07-55-09-1.GUI --strategy sua_relaxed_prob --n-jobs 9 --patch-pandas-compat
911  BASE=/nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel
912  BN=RatS-Day5TwoNovel-2020-12-04_07-55-09
913  mkdir -p "$BASE/spyk-circ/$BN"
914  # Phy GUI: pipeline expects .../spyk-circ/{BN}/{BN}-merged.GUI
915  ln -sfn "$BASE/spykcirc/${BN}-1.GUI"        "$BASE/spyk-circ/$BN/${BN}-merged.GUI"
916  # Recording + probe: must exist at these paths (symlink if stored elsewhere)
917  # Check dat_path in your params.py and point accordingly:
918  # ln -sfn <actual_dat> "$BASE/spyk-circ/${BN}.dat"
919  # ln -sfn <actual_prb> "$BASE/spyk-circ/${BN}.prb"
920  # BASE=/nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel
921  BASE=/scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel
922  BN=RatS-Day5TwoNovel-2020-12-04_07-55-09
923  mkdir -p "$BASE/spyk-circ/$BN"
924  # Phy GUI: pipeline expects .../spyk-circ/{BN}/{BN}-merged.GUI
925  ln -sfn "$BASE/spykcirc/${BN}-1.GUI" "$BASE/spyk-circ/$BN/${BN}-merged.GUI"
926  uv run si-refine-phy --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel-2020-12-04_07-55-09 --strategy sua_relaxed_prob --n-jobs 9 --patch-pandas-compat --analyzer-overwrite if_missing
927  uv run si-curate-phy --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel-2020-12-04_07-55-09 --strategy sua_relaxed_prob --n-jobs 9 --patch-pandas-compat --analyzer-overwrite if_missing
928  source /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
929  deactivate
930  mamba
931  micromamba activate phy2
932  phy template-gui /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/spykcirc/RatS-Day5TwoNovel-2020-12-04_07-55-09-1.GUI/params.py
933  rsync -a -W --no-compress --info=progress2 --exclude='*_BAK*' --exclude='*bak' /nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel/spykcirc /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/spykcirc
934  mount_all_cloud_drives 
935  mount_locker_dataDen
936  rsync -a -W --no-compress --info=progress2 --exclude='*_BAK*' --exclude='*bak' /nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel/spykcirc /tmpssd/halechr/Day5TwoNovel/spykcirc
937  mkdir /tmpssd/halechr/Day5TwoNovel
938  cd /tmpssd/halechr
939  cd /
940  ls
941  cd tmp_data
942  ls
943  rclone
944  rclone listremotes
945  rclone mount LockerDDOnGreatlakes:
946  rclone config
947  rclone test
948  rclone
949  rclone selfupdate
950  rclone serve
951  rclone serve http remote:
952  rclone serve http LockerDDOnGreatlakes:
953  cd /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/
954  ls
955  source /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
956  git pull
957  cd bapun_sess_init_scripts/
958  uv lock
959  uv sync --all-extras
960  uv run si-run-sorter run --basedir /nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel/SORTING/folder_KS4_v1_phy
961  cd /nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel
962  ls
963  cd /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel
964  ls
965  ls -la
966  cp RatS-Day5TwoNovel-2020-12-04_07-55-09.dat spyk-circ/RatS-Day5TwoNovel-2020-12-04_07-55-09.dat
967  uv run si-curate-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --run-name RatS-Day5TwoNovel-2020-12-04_07-55-09-1.GUI --strategy sua_relaxed_prob --n-jobs 9 --patch-pandas-compat
968  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/
969  pwd
970  ls
971  cd spyk-circ/
972  ls
973  ls -la
974  ln -s RatS-Day5TwoNovel-2020-12-04_07-55-09.dat RatS-Day5TwoNovel.dat
975  ls
976  ls -la
977  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/
978  pwd
979  ls
980  cd ../
981  ls
982  cd spyk-circ/
983  ln -s ../RatS-Day5TwoNovel-2020-12-04_07-55-09.prb RatS-Day5TwoNovel.prb
984  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/
985  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/ --n-jobs 9
986  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/
987  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel 
988  --sorter spykingcircus2 --run-name folder_SC2 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/folder_SC2_phy --n-jobs 9 --sorter-params-json '{"job_kwargs": {"n_jobs": 9, "max_threads_per_worker": 1}}'
989  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter spykingcircus2 --run-name folder_SC2 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/folder_SC2_phy --n-jobs 9 --sorter-params-json '{"job_kwargs": {"n_jobs": 9, "max_threads_per_worker": 1}}'
990  rsync -a -W --no-compress --info=progress2 --exclude='*_BAK*' --exclude='*bak' /nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel
991  cd /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/spykcirc/RatS-Day5TwoNovel-2020-12-04_07-55-09-1.GUI/
992  ls
993  micromamba activate phy2
994  ls
995  phy 
996  phy template-gui params.py 
997  micromamba activate phy2
998  phy template-gui /nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/spyk-circ/RatS-Day4Openfield/RatS-Day4Openfield-merged.GUI/params.py
999  phy template-gui /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day4Openfield/spyk-circ/RatS-Day4Openfield/RatS-Day4Openfield-merged.GUI/params.py
1000  history
1001  source /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
1002  ls
1003  history
1004  pwd
1005  cd bapun_sess_init_scripts/
1006  history > /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/EXTERNAL/RUN_LOGS/2026-06-04_730pm_GreatlakesTerminalHistory.md
