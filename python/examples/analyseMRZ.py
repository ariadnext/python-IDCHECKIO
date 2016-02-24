import idcheckio
import time

conn = idcheckio.IDCheckIO("ariadnext.exemple@ariadnext.com", "exemple@", host="idcheckio.rennes.ariadnext.com", port="9443", verify=False)

# Analyse MRZ
result = conn.analyse_mrz("P<UTOBANDERAS<<LILIAN<<<<<<<<<<<<<<<<<<<<<<<", "01234567894UTO8001014F2501017<<<<<<<<<<<<<06")

# Finally, get the report 
report = conn.get_report(result.uid)
