import idcheckio
import time

conn = idcheckio.IDCheckIO("example@example.com", "exemple")

# Analyse a identity card with recto and verso.
result = conn.analyse_image("/tmp/recto.jpg", "/tmp/verso.jpg", path=True)

# Finally, get the report
report = conn.get_report(result.uid)
