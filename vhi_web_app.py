from spyre import server
import pandas as pd
import os

class vhi_app(server.App):
    title = "date ranges"
    inputs = [
     {
        "type": "dropdown",
        "id": "file",
        "label": "choose filename",
        "options": [{"label": filename, "value": filename} for filename in os.listdir("data1")],
        "key": 'file',
        "action_id": "update"
     },
     {
        "type": "dropdown",
        "id": "year",
        "label": "choose year",
        "options": [{"label": year, "value": year} for year in range(1981, 2017)],
        "key": "year",
        "action_id": "update",
     }
    ]
    outputs = [
     {
        "type": "table",
        "id": "table_year",
        "control_id": "update",
     }
    ]
    controls = [
     {
        "type": "hidden",
        "id": "update"
     }
    ]

    def getData(self, params):
        filename = params["file"]
        year = int(params["year"])
        df = pd.read_csv("data1/" + filename, sep = ",{1} *| {1,4}", index_col = False, engine = 'python', header = 1)
        return df.ix[df.year == year, ["week", "VHI"]]


app = vhi_app()
app.launch()
