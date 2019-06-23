Creator: Robert Bennett
GitHub: act3297
Email: opensource-s3upload@robertbennett.info
Date: 06/21/2019
Version: 1.0

This program uploads all the files in a single folder to a bucket in AWS S3. It keeps a list of the files (as a readable txt file) so duplicates are not uploaded.

To use, place s3upload.pyw, config.json, errors.txt, and uploaded_list.txt in the folder containing the files to be uploaded. Set the config info in 'config.json', then run s3upload.pyw
