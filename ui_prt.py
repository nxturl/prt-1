import json

import streamlit as st

data = json.load(open("v1_post_office_meetings_chunked_reports.json"))
c = 0
new_data = []
for item in data:
    should_include = False
    keep_chunks = []
    for chunk in item["chunks"]:
        report = chunk["report"]
        report = json.loads(report)
        if any([bool(x) for _, x in report.items()]):
            should_include = True
            keep_chunks.append(chunk)
            # with st.expander(label="Report", expanded=True):
            #     items = []
            #     st.write(
            #         "Municipality:",
            #         item["municipality"].replace("_", " ").upper(),
            #     )
            #     for key, value in report.items():
            #         if value:
            #             if isinstance(value, list):
            #                 st.write(key)
            #                 for i, v in enumerate(value):
            #                     st.write(f"{i+1}. {v}")
            #     st.text_area("Reference Text", chunk["text"], height=400)
            #     st.write("Reference URL:", chunk["chunk_url"])
    if should_include:
        item["chunks"] = keep_chunks
        new_data.append(item)

json.dump(new_data, open("./v1_post_office_meetings_chunked_reports_trimmed.json", "w"))
