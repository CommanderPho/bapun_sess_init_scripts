#! /bin/bash


InputFile1=/run/media/bapung/mercik/RatS/Day2NSD/2020-11-27_10-22-29/experiment1/recording1/continuous/Rhythm_FPGA-100.0/continuous.dat
InputFile2=/run/media/bapung/mercik/RatS/Day2NSD/2020-11-27_11-07-48/experiment1/recording1/continuous/Rhythm_FPGA-100.0/continuous.dat
InputFile3=/run/media/bapung/mercik/RatS/Day2NSD/2020-11-27_12-22-42/experiment1/recording1/continuous/Rhythm_FPGA-100.0/continuous.dat
InputFile4=/run/media/bapung/mercik/RatS/Day2NSD/2020-11-27_16-14-48/experiment1/recording1/continuous/Rhythm_FPGA-100.0/continuous.dat
InputFile5=/run/media/bapung/mercik/RatS/Day2NSD/2020-11-27_18-44-47/experiment1/recording1/continuous/Rhythm_FPGA-100.0/continuous.dat
InputFile6=/run/media/bapung/mercik/RatS/Day2NSD/2020-11-27_21-12-51/experiment1/recording1/continuous/Rhythm_FPGA-100.0/continuous.dat

OutputFile=/data/Clustering/SleepDeprivation/RatS/Day2NSD/RatS-Day2NSD-2020-11-27_10-22-29.dat

cat ${InputFile1} ${InputFile2} ${InputFile3} ${InputFile4} ${InputFile5} ${InputFile6} > ${OutputFile}


Recipient="bapun.k.giri@gmail.com"
Subject="ExtractingFinished"
Message="Finshed"
`mail -s $Subject $Recipient <<< $Message`
