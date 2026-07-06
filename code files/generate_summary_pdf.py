from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import inch

# Create the PDF document
doc = SimpleDocTemplate("summary.pdf", pagesize=letter)
styles = getSampleStyleSheet()

# Custom styles
title_style = styles['Heading1']
section_style = styles['Heading2']
bullet_style = styles['Normal']
bullet_style.leftIndent = 20

# Content list
content = []

# Title
content.append(Paragraph("Summary of Pandas Tips and Tricks Notebooks", title_style))
content.append(Spacer(1, 0.2*inch))

# Notebook 1: 01_pandas.ipynb
content.append(Paragraph("01_pandas.ipynb: Basic Pandas Operations", section_style))
content.append(Spacer(1, 0.1*inch))
content.append(Paragraph("Key Topics:", bullet_style))
content.append(Paragraph("• Importing libraries: pandas, numpy, matplotlib, seaborn", bullet_style))
content.append(Paragraph("• Reading data: CSV with pd.read_csv(), Excel with pd.read_excel()", bullet_style))
content.append(Paragraph("• Writing data: df.to_excel()", bullet_style))
content.append(Paragraph("• Data exploration: df.info(), df.head(), df.tail(), df.describe()", bullet_style))
content.append(Paragraph("• Handling missing values: df.isnull().sum(), percentage, visualization with sns.heatmap()", bullet_style))
content.append(Paragraph("• Unique values: df['column'].unique(), df.nunique()", bullet_style))
content.append(Paragraph("• Value counts: df['column'].value_counts()", bullet_style))
content.append(Paragraph("• Grouping: df.groupby(['col1', 'col2']).size()", bullet_style))
content.append(Paragraph("• Correlation: df[['cols']].corr(), sns.heatmap(), sns.pairplot()", bullet_style))
content.append(Paragraph("• Missing value imputation: drop columns with >70% missing, fill with mean/median/mode", bullet_style))
content.append(Paragraph("• Binning: pd.cut() for age groups", bullet_style))
content.append(Paragraph("• Feature engineering: renaming columns, creating new features", bullet_style))
content.append(Paragraph("• Data filtering: df[df['col'] == value], multiple conditions with &", bullet_style))
content.append(Spacer(1, 0.2*inch))

# Notebook 2: 02_pandas_on_pak_pop.ipynb
content.append(Paragraph("02_pandas_on_pak_pop.ipynb: Pakistani Population Analysis", section_style))
content.append(Spacer(1, 0.1*inch))
content.append(Paragraph("Dataset Description:", bullet_style))
content.append(Paragraph("• Population census data from 2017 and 1998", bullet_style))
content.append(Paragraph("• Features: Province, Division, District, Sub-Division, Area, Urban/Rural Population, Gender, Sex Ratio, Annual Growth Rate", bullet_style))
content.append(Paragraph("• Composition: df.info(), df.head(), pd.set_option() for display", bullet_style))
content.append(Paragraph("• Summary stats: df.describe().T", bullet_style))
content.append(Paragraph("• Population calculations: Total rural/urban, changes from 1998-2017, percentage change", bullet_style))
content.append(Paragraph("• Assignments: Calculate percent change, combine columns by sex", bullet_style))
content.append(Spacer(1, 0.2*inch))

# Notebook 3: 03_ydata_profiling.ipynb
content.append(Paragraph("03_ydata_profiling.ipynb: Automatic EDA with ydata_profiling", section_style))
content.append(Spacer(1, 0.1*inch))
content.append(Paragraph("• Import ydata_profiling as yd", bullet_style))
content.append(Paragraph("• Load dataset: sns.load_dataset('titanic') or CSV", bullet_style))
content.append(Paragraph("• Create profile: profile = yd.ProfileReport(df)", bullet_style))
content.append(Paragraph("• Generate HTML report: profile.to_file('./outputs/filename.html')", bullet_style))
content.append(Paragraph("• Used on Titanic and Pakistani Population datasets", bullet_style))
content.append(Spacer(1, 0.2*inch))

# Notebook 4: 04_kaggle_google_eda.ipynb
content.append(Paragraph("04_kaggle_google_eda.ipynb: Google Play Store EDA", section_style))
content.append(Spacer(1, 0.1*inch))
content.append(Paragraph("• Dataset: Google Play Store apps from Kaggle", bullet_style))
content.append(Paragraph("• Tasks: Download, extract, read CSV, check columns", bullet_style))
content.append(Paragraph("• Define columns: App, Category, Rating, Reviews, Size, Installs, Type, Price, etc.", bullet_style))
content.append(Paragraph("• Data cleaning: Convert Size (K/M to bytes), Installs (remove +, ,), Price (remove $)", bullet_style))
content.append(Paragraph("• Unique values and value counts for Size, Installs, Price", bullet_style))
content.append(Paragraph("• Assignments: Make numeric columns, handle 'Varies with device'", bullet_style))
content.append(Spacer(1, 0.2*inch))

# Notebook 5: 04a_EDA_google_playstore_data.ipynb
content.append(Paragraph("04a_EDA_google_playstore_data.ipynb: Detailed EDA on Google Play Store", section_style))
content.append(Spacer(1, 0.1*inch))
content.append(Paragraph("• Dataset context: Scraped from Google Play Store", bullet_style))
content.append(Paragraph("• Data loading: pd.read_csv(), set display options", bullet_style))
content.append(Paragraph("• Info and describe: df.info(), df.describe()", bullet_style))
content.append(Paragraph("• Size conversion: Function to convert K/M to bytes, handle 'Varies with device'", bullet_style))
content.append(Paragraph("• Installs: Remove +, ,, convert to int", bullet_style))
content.append(Paragraph("• Price: Remove $, convert to float", bullet_style))
content.append(Paragraph("• Missing values: df.isnull().sum(), percentage, heatmap", bullet_style))
content.append(Paragraph("• Correlation: Numeric cols corr(), heatmap", bullet_style))
content.append(Spacer(1, 0.2*inch))

# Notebook 6: 05_complete_EDA_google_playstore_data.ipynb
content.append(Paragraph("05_complete_EDA_google_playstore_data.ipynb: Complete EDA on Google Play Store", section_style))
content.append(Spacer(1, 0.1*inch))
content.append(Paragraph("• Full data wrangling: Convert Size, Installs, Price to numeric", bullet_style))
content.append(Paragraph("• Installs categories: Binning into Very low, Low, etc.", bullet_style))
content.append(Paragraph("• Missing values handling: Drop rows with few missing, impute Rating based on Installs category", bullet_style))
content.append(Paragraph("• Duplicates: df.duplicated(), df.drop_duplicates()", bullet_style))
content.append(Paragraph("• Insights: Top categories by apps, installs, reviews, ratings", bullet_style))
content.append(Paragraph("• Visualizations: Bar plots for free vs paid, content rating, top apps", bullet_style))
content.append(Paragraph("• Assignments: Make 15 questions and answer with plots", bullet_style))
content.append(Spacer(1, 0.2*inch))

# Notebook 7: 06_data_visualization.ipynb
content.append(Paragraph("06_data_visualization.ipynb: Data Visualization Techniques", section_style))
content.append(Spacer(1, 0.1*inch))
content.append(Paragraph("• Libraries: Pandas, Matplotlib, Seaborn, Plotly", bullet_style))
content.append(Paragraph("• Plot types: Bar, Pie, Histogram, Scatter, Line, Heatmap, Box, Area, Radar, Treemap, Geo Maps, Time Series, Bubble, Violin", bullet_style))
content.append(Paragraph("• Examples: df.plot(kind='bar'), plt.savefig()", bullet_style))
content.append(Paragraph("• Seaborn: sns.barplot(), sns.scatterplot()", bullet_style))
content.append(Paragraph("• Plotly: px.scatter(), fig.show(), fig.write_html(), fig.write_image()", bullet_style))
content.append(Paragraph("• Saving plots: PNG with dpi, SVG, HTML", bullet_style))
content.append(Paragraph("• Assignments: Read docs, make 10 plots each library, interpret", bullet_style))
content.append(Spacer(1, 0.2*inch))

# Notebook 8: 07_plotting_seaborn.ipynb
content.append(Paragraph("07_plotting_seaborn.ipynb: Seaborn Plotting", section_style))
content.append(Spacer(1, 0.1*inch))
content.append(Paragraph("• Grammar of graphics: Data, plot type, x/y, hue, size, color palette, style, interpretation", bullet_style))
content.append(Paragraph("• Scatter plot: sns.scatterplot(), figsize, palette, labels, title, savefig", bullet_style))
content.append(Paragraph("• Box plot: sns.boxplot(), boxenplot", bullet_style))
content.append(Paragraph("• Bar plot: sns.barplot(), capsize", bullet_style))
content.append(Paragraph("• Violin plot: sns.violinplot()", bullet_style))
content.append(Paragraph("• Themes: sns.set_theme(style, font_scale, font)", bullet_style))
content.append(Paragraph("• Saving: plt.savefig() with dpi, format", bullet_style))
content.append(Spacer(1, 0.2*inch))

# Build the PDF
doc.build(content)
print("PDF generated successfully: summary.pdf")
