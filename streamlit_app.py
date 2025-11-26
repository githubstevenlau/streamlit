import json
import pandas as pd
import requests
import streamlit as st


st.title("Test results")
st.write("Results from the test runs are stored in Amazon DynamoDB and can be accessed using the following endpoints:")
st.write("REST endpoint: https://rpqvcjmfyudiehdyx2ykgqzweu0oaxht.lambda-url.eu-west-2.on.aws/")
st.write("GraphQL endpoint: https://6a5dhgnf5yzokyxy46uzz3sija0kwedl.lambda-url.eu-west-2.on.aws/graphql")
st.write("Results can also be sent to Amazon SNS, Amazon SQS or an Apache Kafka instance etc.")
st.write("The following tabulation and graph uses data from the REST endpoint.")

res = requests.get("https://rpqvcjmfyudiehdyx2ykgqzweu0oaxht.lambda-url.eu-west-2.on.aws/")

data = json.loads(res.text)
df = pd.DataFrame.from_dict(data, orient="index").reset_index().rename(columns={"index": "result",0:"count"})

df = df.set_index("result")

st.write("---")
st.table(df)
st.write("---")
st.write("Test suite runs")
st.bar_chart(
    df,
    x_label="Status",
    y_label="Results")
