# scca-classpicker
Class picker for SCCA Solo (Autocross). This provides a web interface to determine
the correct class for a vehicle based on make, model and modifications. While not
exhaustive, it helps newcomers with correctly classing their car without too much hassle.

# Features
- Simplicity - Selecting the modifications made to your vehicle determines your class category (Street, Street Touring, Prepared, etc.)
- Flexibility - Additional Modifications may be simply added by editing a JSON file
- Portability - Once generated, the HTML page may be copied and run without an app server
- Year, make, and model selections to determine the exact class (incomplete)

### Future Features
- Add more vehicles to the vehicle JSON file
- Vehicle features (displacement, body style, etc.) to determine an approximate class 
- PDF parser to update specific vehicle classing (not modifications!)

# How to Use
To view the class picker, go to the [generated HTML page on GitHub Pages](https://danialre.github.io/scca-classpicker/html/classpicker.html) and follow the instructions there.

## Project Requirements
Most of the codebase is written in Python for Python 3.2+.
Specific packages required (through your distribution or pip):
- jinja2
- json
- PyPDF2 (not required at the moment)

## Running the Generator
To generate the HTML page from the Mods JSON file, run `python3 html_generator.py`

# License
Copyright 2018 Danial Ebling

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
