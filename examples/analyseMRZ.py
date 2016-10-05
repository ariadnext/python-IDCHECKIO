import idcheckio
import time

conn = idcheckio.IDCheckIO("example@example.com", "exemple")

# Analyse MRZ
result = conn.analyze_mrz("P<UTOBANDERAS<<LILIAN<<<<<<<<<<<<<<<<<<<<<<<", "01234567894UTO8001014F2501017<<<<<<<<<<<<<06")

# Finally, get the report
report = conn.get_report(result.uid)

print("{}".format(result.body))
