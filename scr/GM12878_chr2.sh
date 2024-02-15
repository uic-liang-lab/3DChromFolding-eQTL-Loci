#!/bin/bash

##parameters
interfile="../sample_data/folding_input/GM_chr2.230805000.231690000.txt"
chrlensfile="../sample_data/folding/human_chrm_sizes"
chrom="chr2"
start=230805000
end=231690000
outfolder="../output"
res=5000
job_prefix="GM_chr2"
threads=20
EXE_PATH="./../bin/sBIF"

##command
cmd="$EXE_PATH -i $interfile -c $chrom -l $chrlensfile -s $start -e $end -o $outfolder -r $res -j $job_prefix -p $threads "
echo $cmd
$cmd 
echo "Done."
