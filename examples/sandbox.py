import idcheckio
import time
import base64

conn = idcheckio.IDCheckIO("example@example.com", "exemple")

# Get the server status
status = conn.healthcheck()
print("{}".format(status.body))

# Get credits on your account
credits = conn.get_credits()
print("{}".format(credits.body))

# Test sandbox MRZ
mrzlist = conn.get_mrzlist()
mrz = conn.get_mrz(mrzlist.body['mrz'][0])
result = conn.analyze_mrz(mrz.body['mrz']['line1'], mrz.body['mrz']['line2'], mrz.body['mrz']['line3'])
print("{}".format(result.body))

# Test sandbox image
imagelist = conn.get_imagelist()
image = conn.get_image(imagelist.body['images'][2]['doc'])
res = conn.analyze_image(image.body['image'])
print("{}".format(res.body))
