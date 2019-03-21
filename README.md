# Arab-Andalusian Music (AAM)
Repository with three main folders:

1. sanaa_lyrics: Compilation of the sanaa lyrics for the Arab Andalusian music collection.
Available in both original script and transliterations, in csv and json format.

2. Scores-MusicXML: Containing the scores of the recording named with its MBID (Music Brainz ID)

3. Textgrid: Textgrid file of of the recording named with its MBID (Music Brainz ID). Every Textgrid contains 9 tiers:
      1. Sections (Muassa', Mahzuz or Insiraf)
      2. Vocal/Instrumental sections
      3. Sanaa' numeration
      4. Separation in verses
      5. Separation in half verses
      6. Separation in half verses (redundant)
      7. Lyric
      8. Structure of the melodic content (High level)
      9. Structure of the melodic content (Low level)
      
4. score-annotations: Onsets of every single half verse of the score
5. score-segmented: Scores with the annotations in the lyrics of the file (musicxml)
6. src: modules used to make the CSV of the annotations
7. andalusian-VersesCSV.ipynb: Jupyter notebook to generate (8)
8. arab_andalusian_verses.csv: File with all the information from the current annotations
9. metadata-all-nawbas.csv: 
