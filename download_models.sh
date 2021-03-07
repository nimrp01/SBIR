#! /bin/sh

parse_section()
{
  section="$1"
  param="$2"
  found=false
  while read line
  do
    [[ $found == false && "$line" != "[$section]" ]] && continue
    [[ $found == true && "${line:0:1}" = '[' ]] && break
    found=true
    [[ "${line% =*}" == "$param" ]] && { echo "${line#*= }"; break; }
  done
}
path_aux="/content/SBIR/Models"
if [[ ! -d $path_aux ]]; then
  mkdir $path_aux
fi
############################################# download semantic embeddings #############################################
# echo "Downloading semantic embeddings and pre-trained models (it will take some time)"
echo "Semantic embeddings (it will take some time)"
python3 src/download_gdrive.py 11vmz-iA-U3b2oi6u4bTbXA8PXAcrZdfZ $path_aux/aux_files.zip
echo -n "Unzipping it..."
unzip $path_aux/aux_files.zip -d $path_aux
rm $path_aux/aux_files.zip
echo "Done"
chmod 755 -R $path_aux

