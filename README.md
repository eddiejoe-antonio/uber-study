# Uber Earnings and Expenses Study 2024

This study calculates the average earnings and expenses per mile for Uber driver's in New York City. Work is underway as part of a contract between [HR&A Advisors](https://www.hraadvisors.com/) and [Uber Technologies](https://www.uber.com/us/en/s/d/kochab/?ad_id=617798783193&adg_id=138827386725&campaign_id=18133742356&cre=617798783193&dev=c&dev_m=&fi_id=&gad_source=1&gclid=CjwKCAjwqMO0BhA8EiwAFTLgILe4f6ko3GWVbHiUSMVgbHAzKbHEobiQhiJjcnVZjemcKMP6GKm5jRoC5LIQAvD_BwE&gclsrc=aw.ds&kw=uber&kwid=kwd-12633382&match=b&net=g&placement=&tar=&utm_campaign=CM2199151-search-google-brand_1_198_US-New%20Jersey_o-d_web_acq_cpc_en_T1_Generic_BM_uber_kwd-12633382_617798783193_138827386725_b_c&utm_source=AdWords_Brand)

To recreate the study, the following datasets are required

- Proprietary data from Uber
- New York City's Taxi and Limousine Comission data
- AAA Maintenance & Depreciation Data
- AAA Cost of Insurance Data
- US DOT Fuel Economy Data
- US Weather Service Data for New York City
- NYSERDA Weekly Average Motor Gasoline Prices Data
- NYSEDRA Cost and Usage Trends for Electric Vehicle Chargers Data
- Local Rental Car Fee Data

# Running the Script

1. To get started, clone the repo using a code editor by running "git clone https://github.com/eddiejoe-antonio/uber-study.git"
3. Download PARQUET datasets from the [TLC](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
4. Re-name files as needed and check the files names and directories to ensure both code files are referencing the correct data. One place to look is cell 2 of Uber_Trip_Processing.ipynb. 
5. At this point, you can eitherload datasets into the Jupyter notebook titled TLC_Trip_Processing.ipynb, running the script cell by cell, or you can run the whole file by typing "python TLC_Trip_Processing.ipynb" into your integrated terminal
6. Use any exports for processing in the Jupyter notebook titled Uber_Trip_Processing.ipynb, once again checking file names and directories against the code and running the script through an integrated terminal or a Jupyter Notebook environment
7. Export processed data to a directory where you can find it, and use as needed!

# Disclaimer

This repo does not reflect any official statements, methodologies, or publication of data from HR&A Advisors or Uber Technologies.
