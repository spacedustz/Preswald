import preswald
print("Start!")

from preswald import connect, get_df
connect()
df = get_df("dataset")

from preswald import query
sql = "SELECT * FROM dataset WHERE remote_ratio = 100"

filtered_df = query(sql, "dataset")

from preswald import table, text
text("# AI Job Remote ratio")
#table(filtered_df.head(20), title="Fully Remote Jobs (Top 20)")
table(filtered_df[["job_id", "job_title", "salary_usd", "experience_level", "remote_ratio", "company_location"]].head(20),
      title="Remote Jobs Overview (Top 20)")
#table(df, title="전체 데이터")

from preswald import plotly
import plotly.express as px

fig = px.scatter(
    df,
    x="company_location",
    y="salary_usd",
    color="experience_level",
    title="AI Job Salaries by Country and Experience"
)
plotly(fig)