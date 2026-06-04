   66  uv remove datoviz
   67  uv sync --all-extras
   68  ./scripts/unix/repos_pull_changes.sh 
   69  git status
   70  git add pyproject.toml 
   71  git add uv.lock 
   72  git status
   73  git commit -m "GL"
   74  git push
   75  source .venv/bin/activate
   76  source /home/halechr/repos/Spike3D/.venv/bin/activate
   77  git stash save GL
   78  deactivate
   79  source /home/halechr/repos/Spike3D/.venv/bin/activate
   80  uv lock
   81  uv sync --all-extras
   82  for global computations: Performing run_specific_computations_single_context(..., computation_functions_name_includelist=['predictive_decoding_analysis'], ...)...
   83  run_specific_computations_single_context(including only 1 out of 16 registered computation functions): active_computation_functions: [<function PredictiveDecodingComputationsGlobalComputationFunctions.perform_predictive_decoding_analysis at 0x1513e5587430>]...
   84  Performing _execute_computation_functions(...) with 1 registered_computation_functions...
   85  Executing [0/1]: <function PredictiveDecodingComputationsGlobalComputationFunctions.perform_predictive_decoding_analysis at 0x150f7fbae670>
   86  [perform_predictive_decoding_analysis] ========== STARTING ==========
   87  [perform_predictive_decoding_analysis] Parameters: window_size=2, fine_time_bin_size=0.025, extant_decoded_time_bin_size=0.25
   88  [perform_predictive_decoding_analysis] Flags: drop_previous_result_and_compute_fresh=False, enable_masked_filtered_container_before_any_comps=True
   89  [perform_predictive_decoding_analysis] Flags: should_perform_first_pass_compute_future_and_past_analysis=True, enable_filter_and_final_result_processing=True
   90  [perform_predictive_decoding_analysis] max_workers=1: disabling all parallel execution
   91  [perform_predictive_decoding_analysis] WARN: include_includelist: ['sprinkle'] is specified but include_includelist is currently ignored! Continuing with defaults.
   92  [perform_predictive_decoding_analysis] Filtering config: should_filter_by_active_spikes=True (min_spikes=5), should_filter_by_position_like_posterior_bins=True (cutoff=0.42)
   93  [perform_predictive_decoding_analysis] --- PHASE 1: Loading and masking decoded results ---
   94  [perform_predictive_decoding_analysis] Loaded DirectionalDecodersDecoded (deepcopy). spikes_df shape: (14486503, 16)
   95  [perform_predictive_decoding_analysis] Applying masks to 1 time bin size(s)...
   96  [perform_predictive_decoding_analysis]   Processing time_bin_size 1/1: 0.1s
   97  The Kernel crashed while executing code in the current cell or a previous cell. 
   98  Please review the code in the cell(s) to identify a possible cause of the failure. 
   99  Click here for more info. 
  100  pwd
  101  tail -f 2026-02-06_mem_log.txt
  102  %load_ext memory_profiler
  103  from memory_profiler import memory_usage
  104  import time
  105  def monitor_computation():
  106      return run_specific_computations_single_context(...)
  107  # Record memory usage every 0.1 seconds
  108  mem_use = memory_usage(monitor_computation, interval=0.1)
  109  import matplotlib.pyplot as plt
  110  plt.plot(mem_use)
  111  plt.title('Memory usage over time')
  112  plt.xlabel('Time (deciseconds)')
  113  plt.ylabel('Memory usage (MiB)')
  114  htop -u $USER
  115  pwd
  116  cd ../
  117  cd pyPhoPlaceCellAnalysis/
  118  uv add ../bayesian_changepoint_detection
  119  pwd
  120  cd ../../
  121  ls
  122  cd Spike3D_ExploreEnv/
  123  ls
  124  cd Spike3D/
  125  git status
  126  uv sync --all-extras
  127  pwd
  128  cd ../
  129  git clone https://github.com/estcarisimo/bayesian_changepoint_detection.git
  130  cd Spike3D/
  131  git add ../bayesian_changepoint_detection
  132  uv add ../bayesian_changepoint_detection/
  133  tar -xvf Spike3DWorkEnv/
  134  tar -xvf Spike3DWorkEnv.tar.gz Spike3DWorkEnv/
  135  deactivate
  136  ls
  137  pwd
  138  ./scripts/unix/repos_pull_changes.sh 
  139  git stash save "GL"
  140  ls
  141  pwd
  142  source deactivate
  143  rm -rf .venv
  144  pwd
  145  ./scripts/unix/repos_pull_changes.sh 
  146  git status
  147  git stash save "GL"
  148  git pull
  149  git pull --force
  150  pwd
  151  cd ../../
  152  ls
  153  cd Spike3D_ExploreEnv/
  154  cd Spike3D/
  155  uv sync --all-extras
  156  uv sync
  157  uv remove datoviz
  158  uv remove datoviz --group testing
  159  ./scripts/unix/launch_jupyter_lab_with_remote_access.sh 
  160  uv sync
  161  uv sync --all-extras
  162  source .venv/bin/activate
  163  ./scripts/unix/launch_jupyter_lab_with_remote_access.sh 
  164  pyenv shell 3.9.13
  165  git pull
  166  git pull --force
  167  git status
  168  git push
  169  git pull
  170  git pull --help
  171  pyenv shell 3.9.13
  172  git pull
  173  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
  174  deactivate
  175  rm -rf .venv
  176  ./scripts/unix/repos_pull_changes.sh 
  177  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
  178  cd ../
  179  ls
  180  zip -r Spike3D.zip Spike3D
  181  cd Spike3D
  182  deactivate
  183  ls
  184  git pull
  185  ./scripts/unix/repos_pull_changes.sh 
  186  uv lock
  187  pwd
  188  exit
  189  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
  190  cd ../
  191  ls
  192  git clone https://github.com/CommanderPho/pyPhoCoreHelpers.git
  193  cd pyPhoCoreHelpers/
  194  pwd
  195  uv lock
  196   builtin printf "\e[?1049h"
  197   if [ "$_termius_integration_installed" = "" ]; then  _termius_integration_installed="yes";  builtin printf "\e]4545;A\a";  _termius_encode() {  builtin echo -n "$1" | command base64;  };  _termius_get_trap() {  builtin local -a terms;  builtin eval "terms=( $(trap -p "${1:-DEBUG}") )";  builtin printf '%s' "${terms[2]:-}";  };  _termius_original_PS1="$PS1";  _termius_custom_PS1="";  _termius_in_command_execution="1";  _termius_current_command="";  _termius_current_cwd() {  builtin printf "\e]4545;SetCwd;%s\a" "$(_termius_encode "$PWD")";  };  _termius_prompt_begins() {  builtin printf "\e]4545;ShellPromptBegins\a";  };  _termius_prompt_ends() {  builtin printf "\e]4545;ShellPromptEnds\a";  };  _termius_wrap_prompt() {  builtin printf "\[$(_termius_prompt_begins)\]%s\[$(_termius_prompt_ends)\]" "$1";  };  _termius_command_started() {  builtin printf "\e]4545;CommandStarted;%s\a" "$(_termius_encode "$1")";  };  _termius_command_exited() {  builtin printf "\e]4545;CommandExited;%s\a" "$1";  };  _termius_update_prompt() {  if [ "$_termius_in_command_execution" = "1" ]; then  if [[ "$_termius_custom_PS1" == "" || "$_termius_custom_PS1" != "$PS1" ]]; then  _termius_original_PS1=$PS1;  _termius_custom_PS1=$(_termius_wrap_prompt "$_termius_original_PS1");  PS1="$_termius_custom_PS1";  fi;  _termius_in_command_execution="0";  fi;  };  _termius_precmd() {  if [ "$_termius_current_command" != "" ]; then  _termius_command_exited "$_termius_status";  fi;  _termius_current_cwd;  _termius_current_command="";  _termius_update_prompt;  };  _termius_preexec() {  if [[ ! "$BASH_COMMAND" =~ ^_termius_prompt* ]]; then  if [[ "$BASH_COMMAND" == *"builtin printf \"\\e[?1049l\""* ]]; then  _termius_current_command=$BASH_COMMAND;  else  _termius_current_command="$(builtin history 1 | sed 's/ *[0-9]* *//')";  fi;  else  _termius_current_command="";  fi;  if [ "$_termius_current_command" != "" ]; then  _termius_command_started "$_termius_current_command";  fi;  };  if [[ -n "${bash_preexec_imported:-}" ]]; then  _termius_preexec_only() {  if [ "$_termius_in_command_execution" = "0" ]; then  _termius_in_command_execution="1";  _termius_preexec;  fi;  };  precmd_functions+=(_termius_prompt_cmd);  preexec_functions+=(_termius_preexec_only);  else  _termius_dbg_trap="$(_termius_get_trap DEBUG)";  if [[ -z "$_termius_dbg_trap" ]]; then  _termius_preexec_only() {  if [ "$_termius_in_command_execution" = "0" ]; then  _termius_in_command_execution="1";  _termius_preexec;  fi;  };  trap '_termius_preexec_only "$_"' DEBUG;  elif [[ "$_termius_dbg_trap" != '_termius_preexec "$_"' && "$_termius_dbg_trap" != '_termius_preexec_all "$_"' ]]; then  _termius_preexec_all() {  if [ "$_termius_in_command_execution" = "0" ]; then  _termius_in_command_execution="1";  builtin eval "${_termius_dbg_trap}";  _termius_preexec;  fi;  };  trap '_termius_preexec_all "$_"' DEBUG;  fi;  fi;  _termius_update_prompt;  _termius_restore_exit_code() {  return "$1";  };  _termius_prompt_cmd_original() {  _termius_status="$?";  _termius_restore_exit_code "${_termius_status}";  for cmd in "${_termius_original_prompt_command[@]}"; do  eval "${cmd:-}";  done;  _termius_precmd;  };  _termius_prompt_cmd() {  _termius_status="$?";  _termius_precmd;  };  _termius_original_prompt_command=$PROMPT_COMMAND;  if [[ -z "${bash_preexec_imported:-}" ]]; then  if [[ -n "$_termius_original_prompt_command" && "$_termius_original_prompt_command" != "_termius_prompt_cmd" ]]; then  PROMPT_COMMAND=_termius_prompt_cmd_original;  else  PROMPT_COMMAND=_termius_prompt_cmd;  fi;  fi;  builtin printf "\e]4545;B\a";  fi
  198   builtin printf "\e[?1049l"
  199  pwd
  200  cd ../../
  201  ls
  202  cd Spike3D_
  203  cd Spike3D_ExploreEnv/
  204  cd Spike3D/
  205  uv sync --all-extras
  206  source .venv/bin/activate
  207  ./scripts/unix/launch_jupyter_lab_with_remote_access.sh 
  208  pwd
  209  uv sync --all-extras
  210  uv lock
  211  uv remove pyjsoncanvas
  212  pwd
  213  cd ../../
  214  ls
  215  cd Spike3D_ExploreEnv/
  216  ls
  217  cd Spike3D/
  218  ./scripts/unix/repos_pull_changes.sh 
  219  uv sync --all-extras
  220  cd ../../
  221  ls
  222  cd Spike3D_ExploreEnv/
  223  ls
  224  cd Spike3D/
  225  uv sync --all-extras
  226  uv lock
  227  source .venv/bin/activate
  228  ./scripts/unix/launch_jupyter_lab_with_remote_access.sh 
  229  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
  230  ls
  231  git status
  232  cd ../
  233  ls
  234  cd Spike3D_ExploreEnv/
  235  ls
  236  git pull
  237  git status
  238  git pull --force
  239  git stash save GL
  240  git stash save "GL"
  241  cd Spike3D/
  242  ls
  243  git status
  244  git stash save "GL"
  245  git rebase --skip
  246  git status
  247  git pull
  248  ./scripts/unix/repos_pull_changes.sh 
  249  cd /home/halechr/cloud
  250  ls
  251  cd locker_dataDen/
  252  ls
  253  cd ../
  254  mount_all_cloud_drives 
  255  mount_locker_dataDen_GL 
  256  ls
  257  cd locker_dataDen/
  258  ls
  259  cd ../
  260  cat mount_locker_dataDen_GL
  261  which mount_locker_dataDen_GL
  262  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
  263  git fsck
  264  pyenv shell 3.9.13
  265  git status
  266  git add SpecificResults/PendingNotebookCode.py 
  267  git commit -m "GL good"
  268  git hash-object -w src/pyphoplacecellanalysis/GUI/PyVista/InteractivePlotter/InteractivePlaceCellDataExplorer.py
  269  pwd
  270  cd ../../
  271  ls
  272  # 1. Delete the corrupted index file
  273  rm .git/index
  274  # 2. Rebuild the index from your current working directory
  275  git reset
  276  git status
  277  git add src/pyphoplacecellanalysis/SpecificResults/PendingNotebookCode.py 
  278  git commit -m "GL"
  279  git fsck
  280  # 1. Update the file timestamp so Git registers a change
  281  touch src/pyphoplacecellanalysis/GUI/PyVista/InteractivePlotter/InteractivePlaceCellDataExplorer.py
  282  # 2. Stage the file to overwrite the corrupt index reference with a fresh hash
  283  git add src/pyphoplacecellanalysis/GUI/PyVista/InteractivePlotter/InteractivePlaceCellDataExplorer.py
  284  # 3. Stage your notebook code
  285  git add src/pyphoplacecellanalysis/SpecificResults/PendingNotebookCode.py
  286  # 4. Commit again
  287  git commit -m "GL"
  288  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
  289  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
  290  cd /home/halechr/cloud/turbo/Data
  291  ls
  292  cd Bapun/
  293  ls
  294  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
  295  deactivate 
  296  uv sync --all-extras
  297  uv remove datoviz
  298  uv remove datoviz --group testing
  299  source .venv/bin/activate
  300  ./scripts/unix/repos_pull_changes.sh 
  301  git pull
  302  ls
  303  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
  304  pwd
  305  git status
  306  git stash save "GL"
  307  git pull
  308  ./scripts/unix/repos_pull_changes.sh 
  309  uv sync --all-extras
  310  ls
  311  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
  312  uv sync --all-extras
  313  ./scripts/unix/repos_pull_changes.sh 
  314  pwd
  315  deactivate
  316  git pull
  317  ./scripts/unix/repos_pull_changes.sh 
  318  pwd
  319  cd ../
  320  git clone https://github.com/CommanderPho/NeuroPy.git"
  321  git clone https://github.com/CommanderPho/NeuroPy.git
  322  cd NeuroPy/
  323  git status
  324  ls
  325  git checkout feature/safe-advance
  326  git pull
  327  uv lock
  328  pyenv shell 3.9.13
  329  ls
  330  pwd
  331  cd ../../
  332  ls
  333  git pull
  334  git fetch
  335  git stash save "GL"
  336  git pull
  337  cd ../
  338  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
  339  ./scripts/unix/repos_pull_changes.sh 
  340  uv lock
  341  uv sync --all-extras
  342  pyenv shell 3.9.13
  343  git stash save "GL"
  344  git pull
  345  git pull --force
  346  cd ../
  347  ls
  348  pwd
  349  cd ../
  350  ls
  351  git fetch
  352  pwd
  353  cd Spike3D
  354  git pull
  355  git status
  356  git stash save "GL"
  357  git pull
  358  ./scripts/unix/repos_pull_changes.sh 
  359  cd ../NeuroPy/
  360  git status
  361  git fetch
  362  git stash save "GL"
  363  git
  364  git pull --force
  365  cd ../
  366  ls
  367  rm -rf NeuroPy
  368  pwd
  369  pwd
  370  git pull
  371  git status
  372  ./scripts/unix/repos_pull_changes.sh 
  373  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
  374  git stash save "GL"
  375  pyenv shell 3.9.13
  376  pwd
  377  cd ../../
  378  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/activate
  379  /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/python /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/ProcessBatchOutputs_qclus1246789_Only.ipy
  380  git pull
  381  git status
  382  git stash save "GL"
  383  git pull
  384  pwd
  385  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-07_11-26-53/run_kdiba_gor01_one_2006-6-07_11-26-53.sh'
  386  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-08_14-26-15/run_kdiba_gor01_one_2006-6-08_14-26-15.sh'
  387  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-07_16-40-19/run_kdiba_gor01_two_2006-6-07_16-40-19.sh'
  388  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-08_21-16-25/run_kdiba_gor01_two_2006-6-08_21-16-25.sh'
  389  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-09_22-24-40/run_kdiba_gor01_two_2006-6-09_22-24-40.sh'
  390  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-12_16-53-46/run_kdiba_gor01_two_2006-6-12_16-53-46.sh'
  391  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-09_17-29-30/run_kdiba_vvp01_one_2006-4-09_17-29-30.sh'
  392  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-10_12-25-50/run_kdiba_vvp01_one_2006-4-10_12-25-50.sh'
  393  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-09_16-40-54/run_kdiba_vvp01_two_2006-4-09_16-40-54.sh'
  394  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-10_12-58-3/run_kdiba_vvp01_two_2006-4-10_12-58-3.sh'
  395  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_17-46-44/run_kdiba_pin01_one_11-02_17-46-44.sh'
  396  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_19-28-0/run_kdiba_pin01_one_11-02_19-28-0.sh'
  397  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-03_12-3-25/run_kdiba_pin01_one_11-03_12-3-25.sh'
  398  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_fet11-01_12-58-54/run_kdiba_pin01_one_fet11-01_12-58-54.sh'
  399  git pull
  400  git status
  401  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-07_11-26-53/run_kdiba_gor01_one_2006-6-07_11-26-53.sh'
  402  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-08_14-26-15/run_kdiba_gor01_one_2006-6-08_14-26-15.sh'
  403  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-07_16-40-19/run_kdiba_gor01_two_2006-6-07_16-40-19.sh'
  404  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-08_21-16-25/run_kdiba_gor01_two_2006-6-08_21-16-25.sh'
  405  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-09_22-24-40/run_kdiba_gor01_two_2006-6-09_22-24-40.sh'
  406  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-12_16-53-46/run_kdiba_gor01_two_2006-6-12_16-53-46.sh'
  407  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-09_17-29-30/run_kdiba_vvp01_one_2006-4-09_17-29-30.sh'
  408  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-10_12-25-50/run_kdiba_vvp01_one_2006-4-10_12-25-50.sh'
  409  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-09_16-40-54/run_kdiba_vvp01_two_2006-4-09_16-40-54.sh'
  410  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-10_12-58-3/run_kdiba_vvp01_two_2006-4-10_12-58-3.sh'
  411  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_17-46-44/run_kdiba_pin01_one_11-02_17-46-44.sh'
  412  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_19-28-0/run_kdiba_pin01_one_11-02_19-28-0.sh'
  413  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-03_12-3-25/run_kdiba_pin01_one_11-03_12-3-25.sh'
  414  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_fet11-01_12-58-54/run_kdiba_pin01_one_fet11-01_12-58-54.sh'
  415  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-08_14-26-15/run_kdiba_gor01_one_2006-6-08_14-26-15.sh'
  416  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-09_1-22-43/run_kdiba_gor01_one_2006-6-09_1-22-43.sh'
  417  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-12_15-55-31/run_kdiba_gor01_one_2006-6-12_15-55-31.sh'
  418  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-07_16-40-19/run_kdiba_gor01_two_2006-6-07_16-40-19.sh'
  419  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-08_21-16-25/run_kdiba_gor01_two_2006-6-08_21-16-25.sh'
  420  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-09_22-24-40/run_kdiba_gor01_two_2006-6-09_22-24-40.sh'
  421  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-12_16-53-46/run_kdiba_gor01_two_2006-6-12_16-53-46.sh'
  422  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-10_12-25-50/run_kdiba_vvp01_one_2006-4-10_12-25-50.sh'
  423  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-09_16-40-54/run_kdiba_vvp01_two_2006-4-09_16-40-54.sh'
  424  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-10_12-58-3/run_kdiba_vvp01_two_2006-4-10_12-58-3.sh'
  425  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_fet11-01_12-58-54/run_kdiba_pin01_one_fet11-01_12-58-54.sh'
  426  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_17-46-44/run_kdiba_pin01_one_11-02_17-46-44.sh'
  427  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/activate
  428  cd Spike3D/
  429  ipython ProcessBatchOutputs_qclus1246789_Only.ipy 
  430  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/activate
  431  uv sync --all-extras
  432  cd Spike3D/
  433  uv sync --all-extras
  434  python ProcessBatchOutputs.ipy
  435  ipython ProcessBatchOutputs.ipy
  436  pwd
  437  source .venv/bin/activate
  438  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-08_14-26-15/run_kdiba_gor01_one_2006-6-08_14-26-15.sh'
  439  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-09_1-22-43/run_kdiba_gor01_one_2006-6-09_1-22-43.sh'
  440  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-12_15-55-31/run_kdiba_gor01_one_2006-6-12_15-55-31.sh'
  441  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-07_16-40-19/run_kdiba_gor01_two_2006-6-07_16-40-19.sh'
  442  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-08_21-16-25/run_kdiba_gor01_two_2006-6-08_21-16-25.sh'
  443  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-09_22-24-40/run_kdiba_gor01_two_2006-6-09_22-24-40.sh'
  444  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-12_16-53-46/run_kdiba_gor01_two_2006-6-12_16-53-46.sh'
  445  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-10_12-25-50/run_kdiba_vvp01_one_2006-4-10_12-25-50.sh'
  446  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-09_16-40-54/run_kdiba_vvp01_two_2006-4-09_16-40-54.sh'
  447  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-10_12-58-3/run_kdiba_vvp01_two_2006-4-10_12-58-3.sh'
  448  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_fet11-01_12-58-54/run_kdiba_pin01_one_fet11-01_12-58-54.sh'
  449  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_17-46-44/run_kdiba_pin01_one_11-02_17-46-44.sh'
  450  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/activate
  451  /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/python /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/ProcessBatchOutputs_qclus1246789_Only.ipy
  452  pwd
  453  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-08_14-26-15/run_kdiba_gor01_one_2006-6-08_14-26-15.sh'
  454  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-09_1-22-43/run_kdiba_gor01_one_2006-6-09_1-22-43.sh'
  455  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-12_15-55-31/run_kdiba_gor01_one_2006-6-12_15-55-31.sh'
  456  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-07_16-40-19/run_kdiba_gor01_two_2006-6-07_16-40-19.sh'
  457  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-08_21-16-25/run_kdiba_gor01_two_2006-6-08_21-16-25.sh'
  458  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-09_22-24-40/run_kdiba_gor01_two_2006-6-09_22-24-40.sh'
  459  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-12_16-53-46/run_kdiba_gor01_two_2006-6-12_16-53-46.sh'
  460  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-10_12-25-50/run_kdiba_vvp01_one_2006-4-10_12-25-50.sh'
  461  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-09_16-40-54/run_kdiba_vvp01_two_2006-4-09_16-40-54.sh'
  462  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-10_12-58-3/run_kdiba_vvp01_two_2006-4-10_12-58-3.sh'
  463  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_fet11-01_12-58-54/run_kdiba_pin01_one_fet11-01_12-58-54.sh'
  464  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_17-46-44/run_kdiba_pin01_one_11-02_17-46-44.sh'
  465  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/activate
  466  /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/python /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/ProcessBatchOutputs_qclus1246789_Only.ipy
  467  ls
  468  cd Desktop/
  469  ls
  470  cd ../
  471  ls
  472  cd /scratch/kdiba_root/
  473  ls
  474  cd kdiba99
  475  ls
  476  cd halechr/
  477  ls
  478  cd repos/
  479  ls
  480  cd Spike3DEnv_KDibaVersion/
  481  ls
  482  cd Spike3D/
  483  git status
  484  uv sync --all-extras
  485  source .venv/bin/activate
  486  ipython ProcessBatchOutputs_qclus1246789_Only.ipy 
  487  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-08_14-26-15/run_kdiba_gor01_one_2006-6-08_14-26-15.sh'
  488  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-09_1-22-43/run_kdiba_gor01_one_2006-6-09_1-22-43.sh'
  489  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-12_15-55-31/run_kdiba_gor01_one_2006-6-12_15-55-31.sh'
  490  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-07_16-40-19/run_kdiba_gor01_two_2006-6-07_16-40-19.sh'
  491  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-08_21-16-25/run_kdiba_gor01_two_2006-6-08_21-16-25.sh'
  492  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-09_22-24-40/run_kdiba_gor01_two_2006-6-09_22-24-40.sh'
  493  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-12_16-53-46/run_kdiba_gor01_two_2006-6-12_16-53-46.sh'
  494  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-10_12-25-50/run_kdiba_vvp01_one_2006-4-10_12-25-50.sh'
  495  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-09_16-40-54/run_kdiba_vvp01_two_2006-4-09_16-40-54.sh'
  496  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-10_12-58-3/run_kdiba_vvp01_two_2006-4-10_12-58-3.sh'
  497  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_fet11-01_12-58-54/run_kdiba_pin01_one_fet11-01_12-58-54.sh'
  498  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_17-46-44/run_kdiba_pin01_one_11-02_17-46-44.sh'
  499  ipython ProcessBatchOutputs_qclus1246789_Only.ipy 
  500  cd /scratch/kdiba_root/kdiba99/halechr/
  501  ls
  502  cd repos/
  503  ls
  504  cd Spike3DEnv_KDibaVersion/
  505  ls
  506  cd Spike3D/
  507  source .venv/bin/activate
  508  ls
  509  chmod +x ProcessBatchOutputs*
  510  ls
  511  htop
  512  git status
  513  pwd
  514  git status
  515  git add ProcessBatchOutputs_*
  516  git status
  517  git add ProcessBatchOutputs.ipy 
  518  git commit -m "GL"
  519  nano .gitignore 
  520  git status
  521  git add .gitignore 
  522  git commit -m "ignored slurm outputs""
  523  "
  524  git status
  525  git pull
  526  git push
  527  nano ProcessBatchOutputs_qclus1246789_Only.ipy 
  528  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-08_14-26-15/run_kdiba_gor01_one_2006-6-08_14-26-15.sh'
  529  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-09_1-22-43/run_kdiba_gor01_one_2006-6-09_1-22-43.sh'
  530  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_one_2006-6-12_15-55-31/run_kdiba_gor01_one_2006-6-12_15-55-31.sh'
  531  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-07_16-40-19/run_kdiba_gor01_two_2006-6-07_16-40-19.sh'
  532  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-08_21-16-25/run_kdiba_gor01_two_2006-6-08_21-16-25.sh'
  533  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-09_22-24-40/run_kdiba_gor01_two_2006-6-09_22-24-40.sh'
  534  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_gor01_two_2006-6-12_16-53-46/run_kdiba_gor01_two_2006-6-12_16-53-46.sh'
  535  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_one_2006-4-10_12-25-50/run_kdiba_vvp01_one_2006-4-10_12-25-50.sh'
  536  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-09_16-40-54/run_kdiba_vvp01_two_2006-4-09_16-40-54.sh'
  537  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_vvp01_two_2006-4-10_12-58-3/run_kdiba_vvp01_two_2006-4-10_12-58-3.sh'
  538  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_fet11-01_12-58-54/run_kdiba_pin01_one_fet11-01_12-58-54.sh'
  539  sbatch '/nfs/turbo/umms-kdiba/Pho/Output/gen_scripts/run_kdiba_pin01_one_11-02_17-46-44/run_kdiba_pin01_one_11-02_17-46-44.sh'
  540  pwd
  541  source .venv/bin/activate
  542  ipython ProcessBatchOutputs_qclus1246789_Only.ipy 
  543  cd Spike3D
  544  git pull
  545  ls
  546  ./scripts/unix/repos_pull_changes.sh 
  547  uv lock
  548  uv-deps-switcher dev
  549  uv lock
  550  uv-deps-switcher dev
  551  uv lock
  552  uv sync --all-extras
  553  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
  554  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/activate
  555  uv lock
  556  uv sync --all-extras
  557  pyenv shell 3.9.13
  558  pwd
  559  ./scripts/unix/repos_pull_changes.sh 
  560  uv lock
  561  uv sync --all-extras
  562  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3DEnv_KDibaVersion/Spike3D/.venv/bin/activate
  563  pyenv shell 3.9.13
  564  git stash save "GL"
  565  git status
  566  pwd
  567  ls
  568  cd ../../
  569  ls
  570  git status
  571  git pull
  572  git pull --force
  573  ./scripts/unix/repos_pull_changes.sh 
  574  pwd
  575  source /scratch/kdiba_root/kdiba99/halechr/repos/Spike3D_ExploreEnv/Spike3D/.venv/bin/activate
  576  deactivate
  577  uv lock
  578  git pull
  579  git sdtatus
  580  git status
  581  git add uv.lock 
  582  git commit -m "GL"
  583  git pull
  584  ./scripts/unix/repos_pull_changes.sh 
  585  uv lock
  586  uv sync --all-extras
  587  source .venv/bin/activate
  588  ipython ProcessBatchOutputs_Bapun_Batch.ipy 
  589  micromamba activate circus
  590  eval "$(micromamba shell hook --shell=bash)"
  591  pwd
  592  cd Day1Openfield/
  593  ls
  594  cd spyk-circ/
  595  ls
  596  rm -rf RatS-Day1Openfield
  597  ls
  598  micromamba activate circus
  599  pwd
  600  ls
  601  spyking-circus RatS-Day1Openfield.dat -c 32
  602  ls
  603  cd ~/cloud/turbo/
  604  ls
  605  cd Bapun/
  606  ls
  607  cd RatS
  608  ls
  609  cat README.md 
  610  micromamba activate circus
  611  eval "$(micromamba shell hook --shell=bash)"
  612  micromamba activate circus
  613  micromamba install -c conda-forge -c spyking-circus spyking-circus
  614  pyenv shell 3.9.13
  615  eval "$(micromamba shell hook --shell=bash)"
  616  micromamba env list
  617  micromamba activate phy2
  618  ls
  619  cd Day1Openfield/
  620  cd spyk-circ/RatS-Day1Openfield
  621  ls
  622  cd ../
  623  pyenv shell 3.9.13
  624  history
  625  eval "$(micromamba shell hook --shell=bash)"
  626  micromamba activate circus
  627  pwd
  628  ls
  629  cd Day1Openfield/
  630  ls
  631  cd spyk-circ/
  632  ls -la
  633  spyking-circus RatS-Day1Openfield.dat -c 32
  634  spyking-circus RatS-Day1Openfield.dat -c 16
  635  spyking-circus RatS-Day1Openfield.dat -c 15
  636  pyenv shell 3.9.13
  637  cd Day4Openfield/
  638  cd spyk-circ/
  639  ls
  640  ln -s ../_BAK/RatS-Day4Openfield.dat RatS-Day4Openfield.dat
  641  mamba
  642  micromamba activate circus
  643  eval "$(micromamba shell hook --shell=bash)"
  644  micromamba activate circus
  645  spyking-circus spyking-circus RatS-Day4Openfield.dat --cpu 15
  646  spyking-circus RatS-Day4Openfield.dat --cpu 15
  647  ls
  648  pwd
  649  rm -rf RatS-Day4Openfield
  650  rm RatS-Day4Openfield.dat 
  651  pwd
  652  ln -s ../RatS-Day4Openfield.dat RatS-Day4Openfield.dat
  653  spyking-circus RatS-Day4Openfield.dat --cpu 20
  654  ls
  655  pwd
  656  rm RatS-Day4Openfield.dat 
  657  cp ../RatS-Day4Openfield.dat RatS-Day4Openfield.dat
  658  cd /nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/spyk-circ
  659  ls
  660  cd ../
  661  ls
  662  chmod +x ConcatenateDatFiles.sh 
  663  ./ConcatenateDatFiles.sh 
  664  InputFile1=/nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/Raw_data/2020-12-02_10-54-43/experiment1/recording1/continuous/Intan_Rec._Controller-100.0/continuous.dat
  665  InputFile2=/nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/Raw_data/2020-12-02_11-37-13/experiment1/recording1/continuous/Intan_Rec._Controller-100.0/continuous.dat
  666  InputFile3=/nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/Raw_data/2020-12-02_14-46-16/experiment1/recording1/continuous/Intan_Rec._Controller-100.0/continuous.dat
  667  OutputFile=/nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/RatS-Day4Openfield.dat
  668  cat ${InputFile1} ${InputFile2} ${InputFile3} > ${OutputFile}
  669  cd /nfs/turbo/umms-kdiba/Bapun/RatS/Day1Openfield/spyk-circ
  670  mamba activate circus
  671  micromamba activate circus
  672  eval "$(micromamba shell hook --shell=bash)"
  673  micromamba activate circus
  674  spyking-circus RatS-Day1Openfield.dat --cpu 30
  675  spyking-circus RatS-Day1Openfield.dat --cpu 16
  676  ls
  677  rm RatS-Day1Openfield.dat
  678  cp ../RatS-Day1Openfield.dat RatS-Day1Openfield.dat
  679  spyking-circus RatS-Day1Openfield.dat --cpu 15
  680  spyking-circus RatS-Day1Openfield.dat --cpu 8
  681  pyenv shell 3.9.13
  682  micromamba activate circus
  683  pwd
  684  cd Day4Openfield/
  685  cd spyk-circ/
  686  cd ../../
  687  cd Day1Openfield/
  688  cd spyk-circ/
  689  spyking-circus RatS-Day1Openfield.dat -m converting -e merged
  690  deactivate
  691  micromamba deactivate
  692  micromamba activate phy2
  693  phy template-gui params.py
  694  ls
  695  pwd
  696  phy template-gui
  697  ls
  698  phy template-gui RatS-Day1Openfield.params 
  699  cd /nfs/turbo/umms-kdiba/Bapun/RatS/Day1Openfield/spyk-circ/RatS-Day1Openfield/RatS-Day1Openfield-merged.GUI
  700  phy template-gui RatS-Day1Openfield.params 
  701  phy template-gui params.py 
  702  micromamba activate circus
  703  micromamba shell init --shell=bash --prefix=~/micromamba
  704  micromamba activate circus
  705  eval "$(micromamba shell hook --shell=bash)"
  706  micromamba activate circus
  707  micromamba
  708  mamba
  709  eval "$(micromamba shell hook --shell=bash)"
  710  micromamba
  711  eval "$(micromamba shell hook --shell=bash)"
  712  micromamba activate circus
  713  spyking-circus RatS-Day1Openfield.dat --cpu 15
  714  pwd
  715  cd /nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/spyk-circ
  716  meval "$(micromamba shell hook --shell=bash)"
  717  micromamba activate circus
  718  eval "$(micromamba shell hook --shell=bash)"
  719  micromamba activate circus
  720  ls
  721  spyking-circus RatS-Day1Openfield.dat -c 15
  722  ls
  723  pwd
  724  spyking-circus RatS-Day4Openfield.dat -c 15
  725  deactivate
  726  micromamba deactivate
  727  micromamba activate phy
  728  micromamba activate phy2
  729  ls
  730  cd RatS-Day4Openfield
  731  ls
  732  cd ../
  733  ls
  734  cd RatS-Day4Openfield
  735  ls
  736  cd RatS-Day4Openfield
  737  ls
  738  cd ../
  739  micromamba activate circus
  740  pwd
  741  cd ../
  742  spyking-circus RatS-Day4Openfield.dat -m converting -e merged
  743  pyenv shell 3.9.13
  744  uv lock
  745  cd bapun_sess_init_scripts/
  746  ls
  747  uv lock
  748  uv sync --all-extras
  749  uv add PyQt5
  750  rm uv.lock 
  751  uv lock
  752  uv sync
  753  uv sync --all-extras
  754  uv add PyQt6
  755  ldd --version
  756  uv add "pyside6<6.10"
  757  uv add "pyqt6<6.10"
  758  uv lock
  759  uv add "pyqt6<6.10"
  760  uv remove pyside6
  761  uv lock
  762  pwd
  763  uv tool
  764  uv tool upgrade
  765  uv tool upgrade uv-deps-switcher
  766  uv-deps-switcher 
  767  uv-deps-switcher dev
  768  uv lock
  769  uv sync
  770  uv-deps-switcher 
  771  cd ../
  772  ls
  773  cd NeuroPy/
  774  git status
  775  git pull
  776  uv lock
  777  rm -rf .venv
  778  uv lock
  779  uv sync --all-extras
  780  cd bapun_sess_init_scripts/
  781  git pull
  782  git stash save "GL"
  783  git pull
  784  uv lock
  785  uv sync --all-extras
  786  uv lock
  787  uv add pyqt5
  788  uv lock
  789  uv add pyqt5
  790  uv add PyQt5
  791  uv lock
  792  uv sync --all-extras
  793  rm -rf .venv
  794  pyenv shell 3.9.13
  795  cd bapun_sess_init_scripts/
  796  git pull
  797  uv lock
  798  uv sync
  799  uv remove pyside6
  800  uv lock
  801  uv sync
  802  uv lock
  803  uv add PyQt5
  804  uv lock
  805  uv syc
  806  uv sync
  807  uv remove spikeinterface-gui
  808  uv lock
  809  uv sync --all-extras
  810  pwd
  811  uv run ipython kernel install --user --name=bapun-sess-init-UV
  812  pyenv shell 3.9.13
  813  pwd
  814  cd bapun_sess_init_scripts/
  815  git status
  816  git pull
  817  git stash save "GL"
  818  cd /nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/spyk-circ/RatS-Day4Openfield/RatS-Day4Openfield-merged.GUI
  819  ls
  820  mamba phy2 activate
  821  micromamba phy2 activate
  822  micromamba activate phy2
  823  pwd
  824  phy 
  825  phy template-gui params.py 
  826  pyenv shell 3.9.13
  827  cd bapun_sess_init_scripts/
  828  uv lock
  829  uv sync --all-extras
  830  nvidia-smi
  831  uv run python -c "import torch; assert torch.cuda.is_available(); print(torch.cuda.get_device_name(0))"
  832  uv run si-run-sorter list | grep kilosort4
  833  pyenv shell 3.9.13
  834  pwd
  835  cd bapun_sess_init_scripts/
  836  source .venv/bin/activate
  837  uv run si-run-sorter list
  838  pyenv shell 3.9.13
  839  pwd
  840  ls
  841  cd bapun_sess_init_scripts/
  842  ls
  843  uv lock
  844  uv-deps-switcher dev
  845  uv lock
  846  uv remove spikeinterface-gui
  847  uv sync --all-extras
  848  uv lock
  849  uv sync --all-extras
  850  uv run si-run-sorter list
  851  uv run si-run-sorter run --basedir /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield --basename RatS-Day4Openfield --sorter kilosort4 --run-name folder_KS4_v1
  852  history
  853  pyenv shell 3.9.13
  854  ls
  855  cd bapun_sess_init_scripts/
  856  uv sync --all-extras
  857  source .venv/bin/activate
  858  uv run si-run-sorter run   --basedir /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield   --basename RatS-Day4Openfield   --sorter spykingcircus2   --run-name folder_SC2   --sorter-params-json '{"job_kwargs": {"n_jobs": 9, "max_threads_per_worker": 1}}'
  859  cd /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day1Openfield
  860  uv run si-run-sorter run   --basedir /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day1Openfield   --basename RatS-Day1Openfield   --sorter spykingcircus2   --run-name folder_SC2   --export-phy   --phy-export-folder /nfs/turbo/umms-kdiba/Bapun/RatS/Day1Openfield/SORTING/folder_SC2_phy   --n-jobs 9   --sorter-params-json '{"job_kwargs": {"n_jobs": 9, "max_threads_per_worker": 1}}'
  861  nvidia-smi
  862  uv run python -c "import torch; assert torch.cuda.is_available(); print(torch.cuda.get_device_name(0))"
  863  uv run si-run-sorter list | grep kilosort4
  864  history
  865  history > ../bapun_sess_init_scripts/EXTERNAL/RUN_LOGS/2026-06-02_437pm_GreatlakesCPU_spykingcircus2_run_history.log
  866  source /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
  867  cd /tmpssd/
  868  mkdir halechr
  869  cd halechr/
  870  ls -la
  871  pwd
  872  uv run si-run-sorter list --show-default-params   # optional: sorter defaults
  873  pwd
  874  cd bapun_sess_init_scripts/
  875  uv lock
  876  uv sync --all-extras
  877  uv add pynvml
  878  source /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
  879  cd /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield
  880  ls
  881  cd spyk-circ/
  882  ls
  883  pwd
  884  mkdir  /tmpssd/halechr/Day4Openfield
  885  cp -R /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield/spyk-circ /tmpssd/halechr/Day4Openfield/spyk-circ
  886  rsync -a -W --no-compress --info=progress2 --exclude='*_BAK*' --exclude='*bak' /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield/spyk-circ/ /tmpssd/halechr/Day4Openfield/spyk-circ/
  887  nvidia-smi
  888  uv run python -c "import torch; assert torch.cuda.is_available(); print(torch.cuda.get_device_name(0))"
  889  uv run si-run-sorter list | grep kilosort4
  890  source /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
  891  uv lock
  892  cd bapun_sess_init_scripts/
  893  uv sync --all-extras
  894  pwd
  895  uv run si-run-sorter run --basedir /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield --basename RatS-Day4Openfield --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /home/halechr/FastData/Bapun/RatS/Day4Openfield/SORTING/folder_KS4_v1_phy
  896  uv run si-run-sorter run --basedir /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield --basename RatS-Day4Openfield --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield/SORTING/folder_KS4_v1_phy
  897  uv run si-run-sorter run --basedir /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield --basename RatS-Day4Openfield --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield/SORTING/folder_KS4_v1_phy --help
  898  uv run si-run-sorter run --basedir /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield --basename RatS-Day4Openfield --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /nfs/turbo/umms-kdiba/Data/Bapun/RatS/Day4Openfield/SORTING/folder_KS4_v1_phy --remove-existing-folder
  899  history
  900  pyenv shell 3.9.13
  901  cd /nfs/dataden/umms-dibalab
  902  rm -rf ~/cloud/locker_dataDen
  903  mount_all_cloud_drives
  904  pwd
  905  ls
  906  source greatlakes_Helpers/
  907  mount_locker_dataDen_GL
  908  source greatlakes_Helpers/greatlakes_MOUNT.sh 
  909  mount_locker_dataDen
  910  mount_locker_dataDen_GL 
  911  source /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
  912  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/folder_KS4_v1_phy
  913  source /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
  914  uv lock
  915  ls
  916  cd bapun_sess_init_scripts/
  917  uv lock
  918  uv sync --all-extras
  919  uv run si-curate-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --run-name folder_KS4_v1 --strategy sua_relaxed_prob --n-jobs 9 --patch-pandas-compat
  920  uv run si-curate-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --run-name RatS-Day5TwoNovel-2020-12-04_07-55-09-1.GUI --strategy sua_relaxed_prob --n-jobs 9 --patch-pandas-compat
  921  BASE=/nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel
  922  BN=RatS-Day5TwoNovel-2020-12-04_07-55-09
  923  mkdir -p "$BASE/spyk-circ/$BN"
  924  # Phy GUI: pipeline expects .../spyk-circ/{BN}/{BN}-merged.GUI
  925  ln -sfn "$BASE/spykcirc/${BN}-1.GUI"        "$BASE/spyk-circ/$BN/${BN}-merged.GUI"
  926  # Recording + probe: must exist at these paths (symlink if stored elsewhere)
  927  # Check dat_path in your params.py and point accordingly:
  928  # ln -sfn <actual_dat> "$BASE/spyk-circ/${BN}.dat"
  929  # ln -sfn <actual_prb> "$BASE/spyk-circ/${BN}.prb"
  930  # BASE=/nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel
  931  BASE=/scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel
  932  BN=RatS-Day5TwoNovel-2020-12-04_07-55-09
  933  mkdir -p "$BASE/spyk-circ/$BN"
  934  # Phy GUI: pipeline expects .../spyk-circ/{BN}/{BN}-merged.GUI
  935  ln -sfn "$BASE/spykcirc/${BN}-1.GUI" "$BASE/spyk-circ/$BN/${BN}-merged.GUI"
  936  uv run si-refine-phy --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel-2020-12-04_07-55-09 --strategy sua_relaxed_prob --n-jobs 9 --patch-pandas-compat --analyzer-overwrite if_missing
  937  uv run si-curate-phy --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel-2020-12-04_07-55-09 --strategy sua_relaxed_prob --n-jobs 9 --patch-pandas-compat --analyzer-overwrite if_missing
  938  source /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
  939  deactivate
  940  mamba
  941  micromamba activate phy2
  942  phy template-gui /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/spykcirc/RatS-Day5TwoNovel-2020-12-04_07-55-09-1.GUI/params.py
  943  rsync -a -W --no-compress --info=progress2 --exclude='*_BAK*' --exclude='*bak' /nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel/spykcirc /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/spykcirc
  944  mount_all_cloud_drives 
  945  mount_locker_dataDen
  946  rsync -a -W --no-compress --info=progress2 --exclude='*_BAK*' --exclude='*bak' /nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel/spykcirc /tmpssd/halechr/Day5TwoNovel/spykcirc
  947  mkdir /tmpssd/halechr/Day5TwoNovel
  948  cd /tmpssd/halechr
  949  cd /
  950  ls
  951  cd tmp_data
  952  ls
  953  rclone
  954  rclone listremotes
  955  rclone mount LockerDDOnGreatlakes:
  956  rclone config
  957  rclone test
  958  rclone
  959  rclone selfupdate
  960  rclone serve
  961  rclone serve http remote:
  962  rclone serve http LockerDDOnGreatlakes:
  963  cd /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/
  964  ls
  965  source /nfs/turbo/umms-kdiba/Bapun/RatS/bapun_sess_init_scripts/.venv/bin/activate
  966  git pull
  967  cd bapun_sess_init_scripts/
  968  uv lock
  969  uv sync --all-extras
  970  uv run si-run-sorter run --basedir /nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel/SORTING/folder_KS4_v1_phy
  971  cd /nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel
  972  ls
  973  cd /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel
  974  ls
  975  ls -la
  976  cp RatS-Day5TwoNovel-2020-12-04_07-55-09.dat spyk-circ/RatS-Day5TwoNovel-2020-12-04_07-55-09.dat
  977  uv run si-curate-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --run-name RatS-Day5TwoNovel-2020-12-04_07-55-09-1.GUI --strategy sua_relaxed_prob --n-jobs 9 --patch-pandas-compat
  978  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/
  979  pwd
  980  ls
  981  cd spyk-circ/
  982  ls
  983  ls -la
  984  ln -s RatS-Day5TwoNovel-2020-12-04_07-55-09.dat RatS-Day5TwoNovel.dat
  985  ls
  986  ls -la
  987  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/
  988  pwd
  989  ls
  990  cd ../
  991  ls
  992  cd spyk-circ/
  993  ln -s ../RatS-Day5TwoNovel-2020-12-04_07-55-09.prb RatS-Day5TwoNovel.prb
  994  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/
  995  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/ --n-jobs 9
  996  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter kilosort4 --run-name folder_KS4_v1 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/
  997  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel 
  998  --sorter spykingcircus2 --run-name folder_SC2 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/folder_SC2_phy --n-jobs 9 --sorter-params-json '{"job_kwargs": {"n_jobs": 9, "max_threads_per_worker": 1}}'
  999  uv run si-run-sorter run --basedir /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel --basename RatS-Day5TwoNovel --sorter spykingcircus2 --run-name folder_SC2 --export-phy --phy-export-folder /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel/SORTING/folder_SC2_phy --n-jobs 9 --sorter-params-json '{"job_kwargs": {"n_jobs": 9, "max_threads_per_worker": 1}}'
 1000  rsync -a -W --no-compress --info=progress2 --exclude='*_BAK*' --exclude='*bak' /nfs/turbo/umms-kdiba/Bapun/RatS/Day5TwoNovel /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day5TwoNovel
 1001  micromamba activate phy2
 1002  phy template-gui /nfs/turbo/umms-kdiba/Bapun/RatS/Day4Openfield/spyk-circ/RatS-Day4Openfield/RatS-Day4Openfield-merged.GUI/params.py
 1003  phy template-gui /scratch/kdiba_root/kdiba99/halechr/Data/Bapun/RatS/Day4Openfield/spyk-circ/RatS-Day4Openfield/RatS-Day4Openfield-merged.GUI/params.py
 1004  history
(phy2) [halechr@gl3114 ~]$ 
