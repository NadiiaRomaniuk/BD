from hdfs import InsecureClient

client = InsecureClient('http://localhost:9870', user='hadoop')
local_file_path = '/home/nadiia/my_bd/my_file_2.txt'
hdfs_path = '/user/hadoop/mydir/myfile_2.txt'
client.upload(hdfs_path, local_file_path)