# pdfmerge

a small script to merge .pdf files

## usage

The script looks for a configuration file in the current directory in which the order of pdf files is specified. This configuration file is just a plain .txt file. The default name is 'config.txt'. You can provide a different name using the `-c ` flag.
```
>pdfmerge -c order.txt 
```

You can also set the name of the output file using the `-o` flag.

```
>pdfmerge -o merged_file
```
Example configuration file:
```
pdf_1.pdf
pdf_2.pdf
pdf_3.pdf
```