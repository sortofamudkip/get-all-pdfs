# get all pdfs
Gets all the PDFs of a web page. 

## Usage
```
python links.py url [-f]
```
* `url`: The full URL of the website.
* `-f` or `--force`: If specified, the program will force download without asking for a response.

## Example
Without `--force`:
```
python links.py https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/
Download 'file-sample_150kB.pdf'? yes
Download 'file-example_PDF_500_kB.pdf'? yes
Download 'file-example_PDF_1MB.pdf'? yes
```

With `--force`:
```
python links.py https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/ -f
Downloading into current directory: 'file-sample_150kB.pdf'
Downloading into current directory: 'file-example_PDF_500_kB.pdf'
Downloading into current directory: 'file-example_PDF_1MB.pdf'
```

## External modules
Uses `bs4` and `requests`. If you don't have them, you can install them via the following commands:
```
pip install bs4
pip install requests
```