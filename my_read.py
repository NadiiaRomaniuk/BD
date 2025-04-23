from hdfs import InsecureClient

client = InsecureClient('http://localhost:9870', user='hadoop')
hdfs_dir = '/user/hadoop/mydir/'
filenames = client.list(hdfs_dir)
print("Файли у директорії:")
for name in filenames:
    print(name)
