import json
import pandas as pd
import requests
import streamlit as st


st.title("Catapult")
st.write("Results from tests runs")
st.write("REST endpoint: https://rpqvcjmfyudiehdyx2ykgqzweu0oaxht.lambda-url.eu-west-2.on.aws/")
st.write("GraphQL endpoint: https://6a5dhgnf5yzokyxy46uzz3sija0kwedl.lambda-url.eu-west-2.on.aws/graphql")

res = requests.get("https://rpqvcjmfyudiehdyx2ykgqzweu0oaxht.lambda-url.eu-west-2.on.aws/")

data = json.loads(res.text)
df = pd.DataFrame.from_dict(data, orient="index").reset_index().rename(columns={"index": "result",0:"count"})

df = df.set_index("result")

st.write("---")
st.table(df)
st.write("---")
st.write("Test results")
st.bar_chart(
    df,
    x_label="Status",
    y_label="Results")
