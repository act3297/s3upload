# Copyright (c) 2019 ROBERT WROE BENNETT

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Creator: Robert Bennett
# GitHub: act3297
# Email: opensource-s3upload@robertbennett.info
# Date: 06/21/2019
# Version: 1.0

# This program uploads all the files in a single folder to a bucket in AWS S3. It
# keeps a list of the files (as a readable txt file) so duplicates are not uploaded.

# To use, place s3upload.pyw, config.json, errors.txt, and uploaded_list.txt in the
# folder containing the files to be uploaded. Set the config info in 'config.json',
# then run s3upload.pyw


# IMPORTS: 
import os, json, boto3


# HELPER FUNCTIONS
#upload_files(directory)
def upload_files(directory):
    # Load list of already uploaded files
    already_uploaded = list()
    already_uploaded = open('uploaded_list.txt').read().splitlines()

    # Check each file and upload as needed
    for file in os.listdir(directory):
        # Skip creds/python/list/errors files
        if file == 'config.json' or file == 's3upload.py' or file == 'uploaded_list.txt' or file == 'errors.txt':
            continue

        # Upload file if not in list
        if file not in already_uploaded:
            upload_file_to_s3(file)

#upload_file_to_s3(file)
def upload_file_to_s3(file):
    # Load info from config
    config_info = json.load(open("config.json"))

    # Upload the file using boto3
    try:
        s3client = boto3.client('s3', aws_access_key_id = config_info['access_key'], aws_secret_access_key = config_info['secret_key'])
        s3client.upload_file(file, config_info['target_bucket'], file, ExtraArgs = {"StorageClass": config_info['storage_type']})
        add_to_text_file(file, 'uploaded_list.txt')
    except:
        add_to_text_file(file, 'errors.txt')

#add_to_txt_file(value, file)
def add_to_text_file(value, file):
    list_of_uploads = open(file,'a')
    list_of_uploads.write(value + '\n')
    list_of_uploads.close()


# MAIN FUNCTION
def main():
    # Sets the current/working dir
    os.chdir(os.path.dirname(__file__))
    current_dir = os.getcwd()
    
    # Starts the check and upload process
    upload_files(current_dir)

main()