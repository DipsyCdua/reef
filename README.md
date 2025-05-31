# Reef03 Github - Reproducible Workflow

Hi! Welcome to Reef03's project repository for our project on exploring ENSO events and heat stress across the GBR. 
This repository is structured for clarity and reproducibility.
It follows a linear workflow from raw data cleaning to final report generation and the shiny app.

# Repository Structure & Navigation

📁 [root]
├── data_cleaning.qmd           # Main data wrangling script (R/Quarto)
├── soi_cleaning.py             # Cleans ENSO index data (Python)
├── FINAL_SHINY.qmd             # Shiny app source code (Quarto)
├── intro_test.md               # Text content for Shiny app's introduction page
├── README.md                   # This file
├── 📁 raw_input_data           # Original source data files
│   ├── enso.txt
│   ├── reef3.zip
│   ├── Great Barrier Reef Bathymetry 2020 100m.zip
│   └── Great_Barrier_Reef_Marine_Park_Boundary_94_*.zip
├── 📁 output_data              # Cleaned, preprocessed datasets (CSV)
├── 📁 model_code_raw           # Code for each model + saved predictions & metrics
│   ├── LR_model.qmd
│   ├── MEM_model.qmd
│   ├── RF_model.qmd
│   ├── GAM_model.qmd
│   └── *.csv (model performance results)
├── 📁 shiny_images             # Static screenshots/images used in the Shiny app
├── 📁 REPORT_folder            # All files required to compile the final PDF report
│   ├── REPORT.qmd              # The main `pinp` report file
│   ├── pinp.bib                # BibTeX references
│   ├── 📁 report_images        # Figures used specifically in the report


# How to Run the Code

Please note that you may run the files in no particular order because everything has been run.
This is just the flow we followed when creating the submission folder.

*1. Data Cleaning*

  * Run `data_cleaning.qmd` and `soi_cleaning.py`.

  * Outputs are already stored as CSVs in `/output_data` (in the CANVAS SUBMISSION).

*2. Modelling*

  * Run each file in `/model_code_raw` to generate predictions and performance metrics 
  
  * Relevant outputs for report & shiny app already saved in relevant subfolders.

  * Does not re-run cleaning!

*3. Shiny App*

  * Run `FINAL_SHINY.qmd`.

  * App is lightweight and uses pre-saved data files from `/output_data` and metrics/figures from other folders.

  * Text content for the intro tab is in `intro_test.md`.

*4. Final Report*

  * Compile the `Reef03_FinalReport.Rmd` file in `/REPORT_folder` using the pinp format.

  * All required images are stored in `/REPORT_folder/report_images`.

  * Already done! Just open `Reef03_FinalReport.Pdf`