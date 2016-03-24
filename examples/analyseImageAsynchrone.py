import idcheckio
import time
import base64

# Create connection
conn = idcheckio.IDCheckIO("example@example.com", "exemple")

# Send image for analysis
result = conn.analyse_image("/tmp/recto.jpg", async=True, path=True)

# Client pooling
while 1:
    # Get the status of the task
    status = conn.get_status(result.uid)
    if(status.body["result"] == "OK"):
        # If the task is ended, get the report
        report = conn.get_report(result.uid)
        print(report.body)
        break
    elif "errorMessage" in status.body:
        print(status.body["errorMessage"])
        break
    else:
        time.sleep(1)

# Server waiting
# Encode image in base64
with open("/tmp/recto.jpg", "rb") as recto_file:
    encoded_recto = base64.b64encode(recto_file.read())

# Send the image for analysis
result = conn.analyse_image(encoded_recto, async=True)
# Wait the server return, the best in a different thread
status = conn.get_status(result.uid, wait=20000)
# Finally, get the report
report = conn.get_report(result.uid, path="/tmp/report.pdf")
