# Research Methodology

## 1. Study Overview

This project investigates historical trends in cannabis-related substance use among U.S. students.

The analysis focuses on prevalence estimates across educational grades, consumption reporting intervals, and cannabis-related product categories.

**Data Source:** Monitoring the Future (MTF), University of Michigan.

**Geographic Scope:** United States.

**Population:** Students in 8th, 10th, and 12th grades.

**Overall Data Coverage:** 1975–2025.

## 2. Data Collection

The dataset was constructed using 13 CSV files obtained from the Monitoring the Future prevalence database.

Five categories were included:

- Cannabis
- Medical Cannabis
- Vaping Cannabis
- Vaping Flavored Cannabis
- CBD

The original files are preserved in `data/raw/`.

## 3. Data Preparation

The original datasets contained eight columns.

Three columns (`LBYear1`, `LBYear2`, `LBYear3`) contained exclusively missing values and were excluded from the processed dataset.

The remaining variables are:

| Variable | Description |
|---|---|
| drug | Cannabis-related category |
| time | Consumption reporting interval |
| grade | Educational grade |
| estimate | Estimated prevalence percentage |
| year | Survey year |

The cleaned dataset contains 660 observations.

No prevalence estimates were imputed or interpolated.

## 4. Historical Coverage

The Monitoring the Future survey began collecting data from 12th-grade students in 1975.

The study expanded to include 8th- and 10th-grade students in 1991.

Therefore:

- Historical analysis of 12th-grade students may cover 1975–2025.
- Comparisons across all three grades are restricted to 1991–2025.

Product-specific historical coverage varies:

| Category | Available Years |
|---|---|
| Cannabis | 1975–2025 |
| Medical Cannabis | 2017–2025 |
| Vaping Cannabis | 2017–2025 |
| Vaping Flavored Cannabis | 2021–2025 |
| CBD | 2023–2024 |

Some reporting intervals have shorter coverage.

## 5. Prevalence Indicators

The analysis uses four reporting intervals:

- **Lifetime:** Reported use at least once during the respondent's lifetime.
- **12 Month:** Reported use during the previous 12 months.
- **30 Day:** Reported use during the previous 30 days.
- **Daily:** Reported daily or near-daily use, according to the applicable MTF definition.

These indicators represent overlapping populations and must not be added together.

Prevalence estimates represent population-level percentages, not individual-level consumption records.

## 6. Data Quality Assessment

The processed dataset underwent structural validation.

| Validation | Result |
|---|---|
| Total observations | 660 |
| Missing values | 0 |
| Duplicate observations | 0 |
| Invalid prevalence estimates | 0 |
| Invalid survey years | 0 |
| Reporting interval violations | 0 |
| Historical series gaps | 1 |

The only identified historical gap was:

**Medical Cannabis — Lifetime — 12th Grade — 2020.**

No replacement value was generated.

All comparable reporting intervals satisfied the expected ordering:

Lifetime ≥ 12 Month ≥ 30 Day ≥ Daily.

These checks verify structural consistency but do not establish the statistical accuracy of the original estimates.

## 7. Analytical Metrics

The primary metric is estimated consumption prevalence (%).

Additional descriptive metrics include:

- Absolute change in percentage points.
- Relative percentage change.
- Historical maximum prevalence.
- Historical minimum prevalence.
- Historical prevalence range.

Changes are calculated using observed survey estimates.

## 8. Comparative Analysis

Cross-category comparisons use equivalent:

- Survey years.
- Educational grades.
- Reporting intervals.

Product categories may overlap and must not be interpreted as independent populations.

The main historical cross-category comparison covers 2021–2025.

CBD is excluded from that comparison because its available observations cover only 2023–2024.

## 9. Statistical Limitations

The dataset contains aggregated survey estimates rather than individual-level records.

Important limitations include:

- Sampling uncertainty.
- Potential self-reporting bias.
- Differences in historical survey coverage.
- Potential changes in survey methodology.
- Differences in measurement definitions.
- Overlapping cannabis-related product categories.

The downloaded CSV files do not provide the sample sizes, standard errors, or survey design information required for rigorous design-based statistical inference.

Therefore, descriptive differences must not automatically be interpreted as statistically significant.

Correlations must not be interpreted as evidence of causality.

## 10. Reproducibility

The exploratory analysis is documented in:

`notebooks/01_exploratory_data_analysis.ipynb`

The notebook was successfully executed from a restarted kernel without errors.

All visualizations are generated from the processed dataset.

The original source files remain unchanged.

## 11. Research Scope

The findings describe cannabis-related consumption prevalence among the student populations represented by Monitoring the Future.

They do not represent cannabis consumption among the entire U.S. population.

The study does not establish causal effects of legislation, cultural changes, or other external factors.

## 12. Official Methodology Verification

### 12.1 Survey Design and Representativeness

Monitoring the Future (MTF) is a long-running national research study conducted by the University of Michigan with support from the National Institute on Drug Abuse (NIDA).

The study uses probability-based sampling procedures to obtain nationally representative samples of students enrolled in schools in the contiguous United States.

The school-based component surveys students in three educational grades:

| Educational Grade | Approximate Age | Initial Survey Year |
|---|---|---|
| 8th Grade | 13–14 | 1991 |
| 10th Grade | 15–16 | 1991 |
| 12th Grade | 17–18 | 1975 |

The study uses repeated cross-sectional samples. Consequently, annual observations generally represent different groups of students rather than the same individuals followed over time.

Students who have left school or are absent during survey administration may not be represented.

### 12.2 Survey Disruptions During 2020

The COVID-19 pandemic interrupted MTF data collection in March 2020.

Consequently, the number of participating students was substantially lower than in typical survey years.

Some estimates were unavailable because the number of respondents was insufficient.

Our processed dataset contains one historical gap:

- Category: Medical Cannabis
- Reporting interval: Lifetime
- Grade: 12th Grade
- Year: 2020

No interpolation or imputation was performed.

The reduced sample size and unusual collection conditions must be considered when interpreting estimates from 2020.

### 12.3 Survey Administration Changes in 2021

In 2021, MTF adapted survey administration to accommodate remote and hybrid educational environments.

Students could complete web-based questionnaires using electronic devices.

MTF considers substance-use prevalence estimates broadly comparable across the transition in administration methods.

Nevertheless, the change in survey mode and the extraordinary circumstances surrounding the COVID-19 pandemic should be acknowledged when interpreting historical changes.

The observed prevalence declines in 2021 cannot be attributed exclusively to the pandemic using the available aggregated data.

### 12.4 Sampling and Questionnaire Changes in 2024

MTF updated its sampling procedures in 2024.

Changes were also introduced to the wording of several substance-use questions, including questions related to marijuana and cannabis.

These methodological adjustments must be considered when evaluating trends extending across 2024.

The analysis retains the published prevalence estimates without applying undocumented adjustments.

Additional question-level verification would be required to quantify the effects of specific questionnaire changes on individual prevalence indicators.

### 2024 Survey Comparability Assessment

The Monitoring the Future study introduced methodological changes in 2024, including updates to its sampling procedures and the wording of selected substance-use questions.

These changes included questions related to marijuana/cannabis prevalence across lifetime, past-year, and past-month reporting intervals.

**Implications for this research:**

- Historical prevalence estimates are retained as officially published.
- Comparisons involving 2024 and 2025 require methodological caution.
- Changes in survey estimates cannot automatically be attributed to changes in consumption behavior.
- The potential effects of question wording and sampling modifications have not been quantified in this analysis.
- Linear regression and correlation results covering 2021–2025 are interpreted as descriptive and exploratory.

**Additional verification required:**

Question-level documentation should be examined to determine whether specific cannabis-related indicators were affected differently by the 2024 methodological changes.

**Official references:**

- ICPSR Study 39444 — Monitoring the Future, 12th Grade, 2024.
- ICPSR Study 39445 — Monitoring the Future, 8th and 10th Grades, 2024.
- Monitoring the Future — Official Prevalence Footnotes.

### 12.5 Interpretation of Daily Cannabis Use

MTF reporting definitions distinguish between daily or near-daily cannabis consumption and actual daily use measured for certain vaping indicators.

Daily or near-daily cannabis use is generally defined as use on at least 20 occasions during the previous 30 days.

Vaping indicators may use a distinct daily-use measurement definition.

Consequently, the interpretation of the Daily category must be linked to the applicable survey question and reporting methodology.

Direct comparisons between daily cannabis use and daily cannabis vaping require consideration of these differences.

### 12.6 Statistical Uncertainty

MTF prevalence estimates originate from complex survey samples.

The processed dataset contains published prevalence estimates but does not include the variable-specific standard errors, sample sizes, or complex survey design information necessary for rigorous design-based statistical inference.

Therefore:

- Historical differences are descriptive.
- Regression slopes describe fitted historical trends.
- Pearson correlations describe exploratory associations.
- Statistical significance cannot be established from the available CSV files alone.
- Causal relationships cannot be inferred.

Additional official documentation and suitable survey design information would be necessary for formal statistical inference.

### 12.7 Implications for Research Conclusions

The findings should be interpreted as descriptive evidence of historical changes in reported cannabis-related prevalence.

Particular caution is required when evaluating:

1. Historical differences involving the 2020 survey.
2. Large changes observed around 2021.
3. Comparisons extending across the 2024 methodological updates.
4. Associations involving overlapping cannabis product categories.
5. Statistical relationships calculated from short time series.

These considerations do not invalidate the exploratory analysis.

They establish the boundaries within which the results can be interpreted responsibly.

### 12.8 Official References

The following official sources support this methodological assessment:

1. University of Michigan — Monitoring the Future: About the Study.
2. Centers for Disease Control and Prevention — Monitoring the Future: Health, United States.
3. Monitoring the Future — Prevalence/Trends and Official Footnotes.
4. ICPSR — Monitoring the Future, 2020 Student Surveys.
5. ICPSR — Monitoring the Future, 2024 Student Surveys.
6. Monitoring the Future — Annual Reports and Methodological Documentation.

These references should be consulted when interpreting methodological changes and the comparability of historical survey estimates.