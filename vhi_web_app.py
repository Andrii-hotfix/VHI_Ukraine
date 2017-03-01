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
        "options": [{"label": year, "value": year} for year in range(1981, 2018)],
        "key": "year",
        "action_id": "update",
     },
     {
        "type": "dropdown",
        "id": "sweek",
        "label": "choose start week",
        "options": [{"label": sweek, "value": sweek} for sweek in range(1, 53)], # fix 1981 and 2017
        "key": "sweek",
        "action_id": "update",
     },
     {
        "type": "dropdown",
        "id": "fweek",
        "label": "choose finish week",
        "options": [{"label": fweek, "value": fweek} for fweek in range(1, 53)],
        "key": "fweek",
        "action_id": "update",
     }
    ]
    outputs = [
     {
        "type": "table",
        "id": "table_year",
        "control_id": "update",
        "tab": "Table"
     },
     {
        "type": "plot",
        "id": "plot",
        "control_id": "update",
        "tab": "Plot",
     }
    ]
    controls = [
     {
        "type": "hidden",
        "id": "update",
     }
    ]
    tabs = [
        "Table",
        "Plot",
    ]

    def getData(self, params):
        filename = params["file"]
        year = int(params["year"])
        sweek = int(params["sweek"])
        fweek = int(params["fweek"])
        df = pd.read_csv("data1/" + filename, sep = ",{1} *| {1,4}", index_col = False, engine = 'python', header = 1)
        df = df.ix[df.year == year]
        return df[(df.week > sweek) & (df.week < fweek)]

    def getPlot(self, params):
        df = self.getData(params).set_index('week')
        df = df[["SMN", "SMT", "VCI", "TCI", "VHI"]]
        # filename = params["file"]
        # year = int(params["year"])
        # sweek = int(params["sweek"])
        # fweek = int(params["fweek"])
        # df = pd.read_csv("data1/" + filename, sep = ",{1} *| {1,4}", index_col = False, engine = 'python', header = 1)
        # df = df.ix[df.year == year, ["week", "VHI"]]
        # df = df[(df.week > sweek) & (df.week < fweek)]
        plt_obj = df.plot()
        plt_obj.set_ylabel("indexes")
        plt_obj.set_title("vegetation indexes for chosen time period")
        return plt_obj.get_figure()




app = vhi_app()
app.launch()
