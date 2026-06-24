# -*- coding: utf-8 -*-
"""Files CFTC : HTML (scraper_static) + PDF (scraper_pdf). Cartographie sec.3.
ExplanatoryNotes deja fait (cot_explanatory, D156-D162) -> exclu.
"""
C = "https://www.cftc.gov"
HTML = [
    ("/MarketReports/CommitmentsofTraders/AbouttheCOTReports/index.htm", "cot_about_reports"),
    ("/ConsumerProtection/EducationCenter/CFTCGlossary/index.htm", "cftc_glossary"),
    ("/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm", "cot_historical_compressed"),
    ("/MarketReports/CommitmentsofTraders/HistoricalViewable/cotvariableslegacy.html", "cot_variables_legacy"),
    ("/MarketReports/CommitmentsofTraders/HistoricalViewable/CFTC_023168.html", "cot_variables_disaggregated"),
    ("/MarketReports/CommitmentsofTraders/HistoricalViewable/cotvariablestfm.html", "cot_variables_tff"),
    ("/MarketReports/CommitmentsofTraders/HistoricalViewable/cotvariablescitsupplement.html", "cot_variables_cit"),
]
PDF = [
    ("/sites/default/files/idc/groups/public/@commitmentsoftraders/documents/file/disaggregatedcotexplanatorynot.pdf", "cot_disaggregated_notes"),
    ("/sites/default/files/idc/groups/public/@commitmentsoftraders/documents/file/tfmexplanatorynotes.pdf", "cot_tff_notes"),
]
with open("queue_cftc_html.tsv", "w", encoding="utf-8") as f:
    for p, n in HTML:
        f.write(f"{C}{p}\t{n}\n")
with open("queue_cftc_pdf.tsv", "w", encoding="utf-8") as f:
    for p, n in PDF:
        f.write(f"{C}{p}\t{n}\n")
print(f"queue_cftc_html.tsv : {len(HTML)} | queue_cftc_pdf.tsv : {len(PDF)}")
