
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "httpx",
#     "pandas",
#     "platformdirs",
#     "python-dotenv",
#     "rich",
#     "seaborn",
#     "requests",
# ]
# ///



import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import json

AIPROXY_TOKEN = os.environ.get("AIPROXY_TOKEN")
if not AIPROXY_TOKEN:
    raise EnvironmentError("AIPROXY_TOKEN environment variable not set.")

PROXY_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {AIPROXY_TOKEN}",
    "Content-Type": "application/json"
}

def load_data(filename):
    """Load dataset with utf-8 or fallback encoding."""
    try:
        df = pd.read_csv(filename, encoding='utf-8')
        return df
    except UnicodeDecodeError:
        print(f"UTF-8 decoding failed. Trying ISO-8859-1 encoding for {filename}.")
        try:
            df = pd.read_csv(filename, encoding='ISO-8859-1')
            return df
        except Exception as e:
            print(f"Error loading file: {e}")
            return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def analyze_data(df):
    """Perform data analysis and return summary."""
    summary_stats = df.describe(include="all").to_dict()
    for col, stats in summary_stats.items():
        for stat, value in stats.items():
            if pd.isnull(value):
                summary_stats[col][stat] = None

    summary = {
        "columns": list(df.columns),
        "types": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "missing_values": df.isnull().sum().to_dict(),
        "summary_stats": summary_stats,
        "correlation_matrix": df.corr(numeric_only=True).fillna(0).to_dict(),
    }
    return summary

def create_visualizations(df, output_dir):
    """Generate and save visualizations."""
    os.makedirs(output_dir, exist_ok=True)

    numeric_cols = df.select_dtypes(include=["number"]).columns
    if numeric_cols.empty:
        print("No numeric columns found for visualizations.")
        return

    # Histogram of numeric columns (limit to 4)
    hist_cols = numeric_cols[:4]
    for col in hist_cols:
        plt.figure()
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f"Distribution of {col}")
        plt.savefig(f"{output_dir}/{col}_histogram.png")
        plt.close()

    # Heatmap of correlations
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig(f"{output_dir}/correlation_heatmap.png")
    plt.close()

def query_llm(prompt):
    """Send a prompt to the LLM through AI Proxy."""
    try:
        payload = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(PROXY_URL, headers=HEADERS, json=payload)

        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"].strip()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return "Error querying LLM."
    except Exception as e:
        print(f"Error querying LLM: {e}")
        return "Error querying LLM."

def generate_markdown_story(df_summary, output_dir):
    """Generate a Markdown story from the data summary."""
    key_insights = {
        "columns": df_summary["columns"][:5],
        "missing": {col: mv for col, mv in df_summary["missing_values"].items() if mv > 0},
        "top_correlations": sorted(
            df_summary.get("correlation_matrix", {}).items(),
            key=lambda x: max(x[1].values()) if isinstance(x[1], dict) else 0,
            reverse=True
        )[:5]
    }

    prompt = (
        f"Provide a concise, insightful narrative based on these data insights: {json.dumps(key_insights)}. "
        "Highlight significant trends, correlations, and missing data. Use Markdown format."
    )
    narrative = query_llm(prompt)

    with open(f"{output_dir}/README.md", "w") as file:
        file.write(narrative)

def run_analysis(input_file):
    """Orchestrate data loading, analysis, visualization, and reporting."""
    cache_file = f"{os.path.splitext(input_file)[0]}_cache.json"

    try:
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as cache:
                summary = json.load(cache)
            print("Cached results loaded.")
            return summary

        if not os.path.exists(input_file):
            print(f"File not found: {input_file}")
            return

        dataset_name = os.path.splitext(os.path.basename(input_file))[0]
        output_dir = dataset_name
        df = load_data(input_file)
        if df is None:
            return

        summary = analyze_data(df)
        with open(cache_file, 'w') as cache:
            json.dump(summary, cache)

        create_visualizations(df, output_dir)
        generate_markdown_story(summary, output_dir)
        print(f"Analysis complete. Outputs saved in {output_dir}/")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = input("Enter the path to your dataset file (e.g., dataset.csv): ")
    run_analysis(input_file)
