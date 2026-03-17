You are an analytics manager reviewing a data analysis notebook.

Your task is to convert the notebook into a professional GitHub README that presents the analysis as a polished portfolio project rather than a homework assignment.

The README should read like a concise analytics report suitable for a hiring manager or recruiter.

Goals:
- Clearly communicate the business problem
- Present key findings early
- Explain methodology at a high level
- Emphasize business insights and decisions
- Keep the document concise and scannable

-------------------------------------

Structure the README with the following sections:

# Project Title

## Problem
Briefly explain the business question and context.

## Key Findings
Summarize the most important insights in bullet points. Focus on results and business implications.

## Dataset
Briefly describe the dataset and key variables relevant to the analysis.

## Methodology
Explain the analytical approach at a conceptual level. Do not describe coding steps or implementation details.

## Results
Explain the main analytical findings and what they imply for business decisions.

## Conclusion
Summarize the overall takeaway and any limitations of the analysis.

## Repository Structure
Describe the key files in the repository.

## How to Run
Provide brief instructions for reproducing the analysis.

-------------------------------------

Style Guidelines

- Write like a professional analytics report.
- Avoid mentioning specific Python libraries unless necessary.
- Do not describe coding steps (e.g., “loaded data with pandas”).
- Emphasize insights over process, but do touch on key methodological choices that impact interpretation (e.g., randomization quality, confidence intervals, important methods like DiD, Synthetic Control, DoubleML, etc)
- Use concise paragraphs and bullet points.
- Format using clean GitHub Markdown.

-------------------------------------

Charts and Visualizations

If the notebook already calculates results suitable for visualization:

Generate Python code that produces clear charts based only on metrics already computed in the notebook.

Rules:
- Do NOT introduce new analysis.
- Do NOT invent metrics not present in the notebook.
- Limit to 3–4 charts that best communicate the results.

Save charts to an `outputs/` folder using:

plt.savefig("outputs/chart_name.png", dpi=300)

Use the following naming style where appropriate:

outputs/
    conversion_rate_treatment_vs_control.png
    lift_by_impression_bin.png
    channel_roi.png

Include the code used to generate these charts in a section called:

## Visualization Code

Reference the charts in the appropriate README sections using Markdown:

![Conversion Rate by Treatment](outputs/conversion_rate_treatment_vs_control.png)

Charts should support the main insights and improve readability for non-technical reviewers.

-------------------------------------

Tone

The tone should resemble work produced by an analyst at a technology company or consulting firm.

Avoid language that suggests this is a school assignment.

-------------------------------------

Now generate the README based on the notebook.