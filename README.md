# Arab-Andalusian Music (AAM)
Repository with three main folders:

1. sanaa_lyrics: Compilation of the sanaa lyrics for the Arab Andalusian music collection.
Available in both original script and transliterations, in csv and json format.

2. Scores-MusicXML: directory with the score transcriptions of the corpus recordings, each score named with the MBID (Music Brainz ID) of its corresponding recording.
   	- original_scores:
		the score transcriptions for some of the corpus recordings. In case any of the scores are found to diverge from the available transcription, it should be updated and committed to this directory.
		
	- score_segmented:
		some of the score transcriptions of the original_scores directory. These scores are annotated with their corresponding lyrics, but the actual lyrics are not used. Instead, the ‘code’ given to each line section (eg. mu.1.1.2) is written on the score portion it relates to.

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
6. src: functions used to make the CSV file of the annotations
7. andalusian-VersesCSV.ipynb: Jupyter notebook to generate (8)
8. arab_andalusian_verses.csv: File with all the information from the current annotations
9. metadata-all-nawbas.tsv
This file is different than the metadata.tsv of the lyrics corpus found in https://zenodo.org/record/3337623. metadata-all-nawbas.tsv has metadata on all the recordings that have been processed by the MTG (whether they have lyrics or not). the metadata.csv of the lyrics dataset are only those that correspond to the dataset files.
