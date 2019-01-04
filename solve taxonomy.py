#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 13:15:04 2018

@author: nmtarr

Description: Compile taxonomic identifiers for the species concepts of
interest.  

"""
import pandas as pd
from pygbif import species
import config
from pprint import pprint
import sqlite3
import os

sp = config.species

#df = pd.DataFrame(columns=['fws_id', 'gap_code', 'itis_tsn', 'gbif_id', 
#                           'bcb_id', 'common_name', 'scientific_name', 
#                           'start_date', 'end_date'])
#df.index.name='uid'

# Solve taxonomy
name_dict = species.name_backbone(sp)
pprint(name_dict)
#df.loc[1000, 'gbif_key'] = int(name_dict['speciesKey'])


# Connect to or create db
os.chdir('/')
os.chdir(config.workDir)
conn = sqlite3.connect('occurrences.sqlite')
cursor = conn.cursor()
sql1 = """
        INSERT INTO taxa 
        (species_id, gap_code, gbif_id, common_name, scientific_name) 
        VALUES ('bYBCUx0', 'bYBCUx', 2496287, 'Yellow-billed Cuckoo', 
                'Coccyzus americanus');
        """
cursor.execute(sql1)
sql2 = """SELECT * FROM taxa;"""
cursor.execute(sql2).fetchall()
conn.commit()
conn.close()