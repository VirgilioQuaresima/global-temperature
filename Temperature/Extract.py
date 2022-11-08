'''Extract temperature datas'''

import pandas as pd
import plotly.express as px
import datapackage
import pandas as pd

data_url = 'https://datahub.io/core/global-temp/datapackage.json'


class Extract:

    def load():
        package = datapackage.Package(data_url)
        resources = package.resources
        dfs = []
        for resource in resources:
            if resource.tabular:
                data = pd.read_csv(resource.descriptor['path'])
                dfs.append(data)
        return dfs

    def load_from_file(filename):
        return [pd.read_csv('Temperature/data.csv'), pd.read_csv('Temperature/data.csv')]
