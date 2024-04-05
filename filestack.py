from filestack import Client

client = Client('AA3gSNDpNRCKrRI1mTMQ2z')

new_filelink = client.upload(file="path/to/file")
print(new_filelink.url)
