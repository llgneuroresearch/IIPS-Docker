#!/usr/bin/env python3
"""
AVNIR Lab startup banner.
Run at container start, e.g. as the first line of your Docker ENTRYPOINT.
"""

import textwrap

CYAN = "\033[36m"
BOLD = "\033[1m"
YELLOW = "\033[33m"
RESET = "\033[0m"

TITLE = "A V N I R   L A B"
WIDTH = len(TITLE) + 4  # 2 spaces padding each side

top = "╔" + "═" * WIDTH + "╗"
mid = "║" + TITLE.center(WIDTH) + "║"
bot = "╚" + "═" * WIDTH + "╝"

print(f"{CYAN}{BOLD}{top}\n{mid}\n{bot}{RESET}\n")
print("Applied Vascular and Neuroimaging Research (AVNIR) Lab")
print("Laboratoire Clinique de Traitement de l'Image (LCTI)")
print("Centre de Recherche du CHUM (CRCHUM)")
print("Montreal, Quebec, Canada \n")

FUNDING_TEXT = (
    "The development of this tool was supported by the Foundation of the "
    "Radiological Society of North America - Seed Grant (RSD2122) and "
    "Radiology Research Grant (doi.org/10.69777/299979) from the Fonds de "
    "Recherche du Québec en Santé and Fondation de l'Association des "
    "Radiologistes du Québec, internal funding from the 'Support "
    "professoral du Departement de radiologie, radio-oncologie et "
    "medecine nucleaire' de l'Université de Montréal/Bayer and start-up "
    "grants from the Radiology Department Centre Hospitalier de "
    "l'Université de Montréal (CHUM) and CHUM Research Center (CRCHUM). "
    "Laurent Létourneau-Guillon is supported by a Clinical Research "
    "Scholarship–Junior 1 Salary Award (doi.org/10.69777/311203) from "
    "the Fonds de Recherche du Québec en Santé and Fondation de "
    "l'Association des Radiologistes du Québec, and a research funding "
    "from the Quebec Bio-Imaging Network (35450)."
)

ACK_TEXT = (
    "The development of the model was enabled in part by support provided by Calcul "
    "Québec (calculquebec.ca) and the Digital Research Alliance of "
    "Canada (alliancecan.ca)."
)

print("Funding:")
print(textwrap.fill(FUNDING_TEXT, width=71))
print()
print(textwrap.fill(ACK_TEXT, width=71))
print()

CITATION_LINES = [
    "If you found this tool useful, please cite:",
    "",
    "Wu AN, Portafaix A, Pilon D, et al. Multiclass Segmentation of",
    "Intracerebral Hemorrhage, Intraventricular Hemorrhage, and",
    "Perihematomal Edema: Public CT Dataset and Benchmark.",
    "Radiology Advances. 2026;umag036.",
    "https://doi.org/10.1093/radadv/umag036",
]

border = "#" * 71
print(f"{YELLOW}{border}")
for line in CITATION_LINES:
    print(line)
print(f"{border}{RESET}")


DATASET_TEXT = (
    "This model uses images from the 2019 RSNA Intracranial Hemorrhage "
    "Detection dataset, for which we added segmentation masks as "
    "detailed in our paper (see citation above)."
)
 
print("Dataset:")
print(textwrap.fill(DATASET_TEXT, width=71))
print("https://imaging.rsna.org/dataset/1")
print("https://www.kaggle.com/competitions/rsna-intracranial-hemorrhage-detection")



print('\nnnU-Net was used for training this model, see citation below.')
