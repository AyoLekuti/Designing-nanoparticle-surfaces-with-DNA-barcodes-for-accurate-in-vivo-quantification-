# Designing-nanoparticle-surfaces-with-DNA-barcodes-for-accurate-in-vivo-quantification

Repository for all code regarding the paper "Designing nanoparticle surfaces with DNA barcodes for accurate in vivo quantification".

# Script for NGS analysis
The file "NGS_analysis_script.py" does the following:
- Quantifies the number of barcodes present in the unique sequences file provided from Azenta's amplicon NGS processing
-    Screens a csv file with the unique sequences provided from Azenta's amplicon NGS processing
-    Applies a Hamming distance correction to the screen. This helps account for errors in sequencing such as substitutions.

All python processing was performed in an Anaconda environment.
