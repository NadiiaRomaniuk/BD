from hdfs import InsecureClient

client = InsecureClient('http://localhost:9870', user='hadoop')
hdfs_file_path = '/user/hadoop/mydir/myfile_2.txt'
client.delete(hdfs_file_path)
print(f'Файл {hdfs_file_path} видалено.')
