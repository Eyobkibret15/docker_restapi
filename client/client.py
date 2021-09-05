# #!/usr/bin/env python3
#
# # Import of python system library.
# # This library is used to download the 'index.html' from server.
# # You don't have to install anything special, this library is installed with Python.
# import urllib.request
#
# # This variable contain the request on 'http://localhost:1234/'.
# # You must wondering what is 'http://localhost:1234'?
# # localhost: This means that the server is local.
# # 1234: Remember we define 1234 as the server port.
# fp = urllib.request.urlopen("http://localhost:1337/home/")
#
# # 'encodedContent' correspond to the server response encoded ('index.html').
# # 'decodedContent' correspond to the server response decoded (what we want to display).
# encodedContent = fp.read()
# decodedContent = encodedContent.decode("utf8")
#
# # Display the server file: 'index.html'.
# print(decodedContent)
#
# # Close the server connection.
# fp.close()

import requests
r = requests.get("http://localhost:1111/api/")
print("new 111111111111111111111111111111")
print(r.text)
assert r.status_code == 200
