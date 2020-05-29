import sys
import os
import csv
from praatio import tgio
from music21 import *
import re
import numpy as np
import itertools

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def extract_poetry(fn1):
    """
    Return the sanaa number within a recording of each type of poetry form
    """
    row = []
    with open(fn1) as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for rows in reader:
            row.append(rows)

    # Save the number of sanaa in an array depending of the poetry form
    cont = 0
    form_verses={'Qasida':[], 'Moaxaja':[], 'Zejel':[],'Barwala':[]}
    for i in range(len(row)):
        if 'a' in row[i][0]:
            if 'qaṣīdah' in row[i][0]:
                form_verses['Qasida'].append(cont)  
            if 'tawshīḥ' in row[i][0]:
                form_verses['Moaxaja'].append(cont) 
            if 'zajal' in row[i][0]:
                form_verses['Zejel'].append(cont)  
            if 'birūālatin' in row[i][0]:
                form_verses['Barwala'].append(cont) 
            cont +=1
    return form_verses

def extract_data_matrix(fn2):
    """
    Extract onsets of half verses and the corresponding lyric of it from the textgrid file.
    """
    tg = tgio.openTextgrid(fn2)
    structure = tg.tierDict['structure'].entryList # Get all intervals
    structure_start = []
    structure_end = []
    structure_filt = []

    for i in range(len(structure)):
        if re.search('[mi]+[uan]+.[0-9]+.[0-9]+.[0-9]', structure[i][2]):
            structure_start.append(structure[i][0])
            structure_end.append(structure[i][1])
            structure_filt.append(structure[i][2])

    lyrics = tg.tierDict['lyrics'].entryList # the lyrics tier is extracted
    lyrics_filt=[]

    j = 0
    for i in range (len(structure_filt)): # Put together all the lyrics of a whole verse
        while structure_start[i] != lyrics[j][0]:
            j += 1
        lyrics_filt.append(lyrics[j][2])
        k = 0
        while lyrics[j+k][1] != structure_end[i]:
            k += 1
            lyrics_filt[i] += ' ' +lyrics[j+k][2]

    data_matrix = []
    cont = 0
    i =0
    while (i < len(structure_filt)): # If a section of a verse is repeated, the end is taken as the end of the last repeated section
        j = 0                        # results saved in=> data_matrix
        while (structure_filt[i+j]== structure_filt[i]):
            j +=1
            if i+j == len(structure_filt):
                break

        j=j-1
        to_add = [structure_filt[i], lyrics_filt[i], structure_start[i], structure_end[i+j]]
        data_matrix.append(to_add)
        cont += 1
        i += 1 +j

    # Particular case if a section is repeated after one previous that is different. It will be named as mu.1.1.1(1)
    for i in range (len(data_matrix)):
        j=1
        while j<(len(data_matrix)-i):
            if (data_matrix[i][0] == data_matrix[i+j][0]):
                data_matrix[i+j][0] = data_matrix[i+j][0]+'('+str(1)+')'
            j += 1
    return data_matrix

def extract_verses_score(fn3):
    """
    Extract onsets of half verses from the score
    """
    s = converter.parse(fn3)
    p = s.parts[0]
    notes = p.flat.notes.stream()
    sections = ['mu', 'ma', 'in'] 

    annotations = []

    sanaas = {}
        # PROCEDURE
        # Get the segments by looking into the annotated label of the lyrics
    for section in sections:
        for n1 in notes:
            if n1.lyric != None:
                l = n1.lyric
                if re.search(section + '.[0-9]+.[0-9]+.[0-9]+.[se]', l):
                    label = re.findall(section + '.[0-9]+.[0-9]+.[0-9]+.[se]', l)[0]
                    annotations.append([label, n1.offset])


    # Make a list of list call verses with the next information [verse name, start offset, end offset]
    annotations=list(pairwise(annotations))
    annotations = annotations[0::2]
    verses = [[x[0][0][:-2], x[0][1],x[1][1]] for x in annotations]


    i = 0
    verses_filt = []
    # If a section of a verse is repeated, the end is taken as the end of the last repeated section => verses_filt
    while (i < len(verses)):
        j = 0
        while (verses[i+j][0] == verses[i][0]):
            j +=1
            if i+j == len(verses):
                break

        j=j-1
        to_add = [verses[i][0], verses[i][1], verses[i+j][2]]
        verses_filt.append(to_add)
        i += 1 +j

    # Particular case if a section is repeated after one previous that is different. It will be named as mu.1.1.1(1)
    for i in range (len(verses_filt)):
        j=1
        while j<(len(verses_filt)-i):
            if (verses_filt[i][0] == verses_filt[i+j][0]):
                verses_filt[i+j][0] = verses_filt[i+j][0]+'('+str(1)+')'
            j += 1
    
    return verses_filt

