#!/bin/bash  

# define resource
resource=mutation 

# add the time stamped folder
cd /Users/urnishabhuiyan/Desktop/$resource/

new_dir=$(date +%Y_%m_%d)
mkdir $new_dir

# download files to new folder
cd /Users/urnishabhuiyan/Desktop/$resource/$new_dir

wget http://purl.obolibrary.org/obo/uberon/ext.obo &
wait #wait until all downloads are complete 

# update new folder permissions
chmod -R 775 /Users/urnishabhuiyan/Desktop/$resource/$new_dir/

echo "Download Complete"