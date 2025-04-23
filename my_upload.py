from hdfs import InsecureClient
import os

client = InsecureClient('http://localhost:9870', user='hadoop')
local_dir = '/home/nadiia/my_bd/stor_4/'
hdfs_dir = '/user/hadoop/mydir/'
client.makedirs(hdfs_dir)
for filename in os.listdir(local_dir):
    local_file_path = os.path.join(local_dir, filename)
    if os.path.isfile(local_file_path):
        hdfs_path = os.path.join(hdfs_dir, filename)
        print(f'Uploading {filename} to {hdfs_path}...')
        client.upload(hdfs_path, local_file_path)
        print(f'{filename} uploaded.')




