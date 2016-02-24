import idcheckio
import time

conn = idcheckio.IDCheckIO("ariadnext.exemple@ariadnext.com", "exemple@", host="idcheckio.rennes.ariadnext.com", port="9443", verify=False)

# Analyse a identity card with recto and verso.
result = conn.analyse_image("/tmp/recto.jpg", "/tmp/verso.jpg", path=True)

# Finally, get the report
report = conn.get_report(result.uid)
