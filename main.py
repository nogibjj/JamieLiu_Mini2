import pandas as pd
import matplotlib.pyplot as plt

dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv"

# check = pd.read_csv(dataset)
# print(check.shape)


def load_dataset():
    df = pd.read_csv(dataset)
    return df


def process_mean(df, col):
    return df[col].mean()


def process_median(df, col):
    return df[col].median()


def process_max(df, col):
    return df[col].max()


def process_min(df, col):
    return df[col].min()


def process_std(df, col):
    return df[col].std()


def bar_visual(df, col, jupyter_render):
    """bar graph of a column over all airlines"""
    x = df["airline"]
    y = df[col]
    plt.figure(figsize=(15, 12))
    plt.bar(x, y)
    plt.xlabel("Airlines")
    plt.ylabel(col)
    plt.title(f"{col} over Airlines")
    plt.xticks(rotation=90, fontsize=6)
    if not jupyter_render:
        plt.savefig(f"{col}_over_Airlines.png")
    else:
        plt.show()


def hist_visual(df, col, jupyter_render):
    """histogram of a column over all airlines"""
    plt.figure(figsize=(10, 6))
    plt.hist(df[col])
    plt.xlabel(f"Number of {col}")
    plt.ylabel("Frequency")
    plt.title(f"Frequency of {col}")
    if not jupyter_render:
        plt.savefig(f"Frequency_of_{col}_histogram.png")
    else:
        plt.show()


def g_describe():
    g = load_dataset()
    return g.describe()


def general_viz_combined(general_df, jupyter_render):
    """saves all the figures at once"""
    bar_visual(general_df, "incidents_85_99", jupyter_render)
    hist_visual(general_df, "incidents_85_99", jupyter_render)
    bar_visual(general_df, "fatal_accidents_85_99", jupyter_render)
    hist_visual(general_df, "fatal_accidents_85_99", jupyter_render)
    bar_visual(general_df, "fatalities_85_99", jupyter_render)
    hist_visual(general_df, "fatalities_85_99", jupyter_render)
    bar_visual(general_df, "incidents_00_14", jupyter_render)
    hist_visual(general_df, "incidents_00_14", jupyter_render)
    bar_visual(general_df, "fatal_accidents_00_14", jupyter_render)
    hist_visual(general_df, "fatal_accidents_00_14", jupyter_render)
    bar_visual(general_df, "fatalities_00_14", jupyter_render)
    hist_visual(general_df, "fatalities_00_14", jupyter_render)


def save_to_md():
    """save to markdown"""
    df = load_dataset()
    general_viz_combined(df, False)
    markdown_table = g_describe().to_markdown()
    with open("graph.md", "w", encoding="utf-8") as file:
        file.write("# Report\n\n")
        file.write("## General Description\n\n")
        file.write(f"{markdown_table}\n\n")
        file.write("## Visualizations\n\n")
        file.write("### Incidents 85-99\n\n")
        file.write("![Incidents 85-99](incidents_85_99_over_Airlines.png)\n\n")
        file.write(
            "![Incidents 85-99](Frequency_of_incidents_85_99_histogram.png)\n\n"
        )
        file.write("### Fatal Accidents 85-99\n\n")
        file.write(
            "![Fatal Accidents 85-99](fatal_accidents_85_99_over_Airlines.png)\n\n"
        )
        file.write(
            "![Fatal Accidents 85-99] \
                (Frequency_of_fatal_accidents_85_99_histogram.png)\n\n"
        )
        file.write("### Fatalities 85-99\n\n")
        file.write("![Fatalities 85-99](fatalities_85_99_over_Airlines.png)\n\n")
        file.write(
            "![Fatalities 85-99](Frequency_of_fatalities_85_99_histogram.png)\n\n"
        )
        file.write("### Incidents 00-14\n\n")
        file.write("![Incidents 00-14](incidents_00_14_over_Airlines.png)\n\n")
        file.write(
            "![Incidents 00-14](Frequency_of_incidents_00_14_histogram.png)\n\n"
        )
        file.write("### Fatal Accidents 00-14\n\n")
        file.write(
            "![Fatal Accidents 00-14](fatal_accidents_00_14_over_Airlines.png)\n\n"
        )
        file.write(
            "![Fatal Accidents 00-14] \
                (Frequency_of_fatal_accidents_00_14_histogram.png)\n\n"
        )
        file.write("### Fatalities 00-14\n\n")
        file.write("![Fatalities 00-14](fatalities_00_14_over_Airlines.png)\n\n")
        file.write(
            "![Fatalities 00-14](Frequency_of_fatalities_00_14_histogram.png)\n\n"
        )


if __name__ == "__main__":
    save_to_md()
