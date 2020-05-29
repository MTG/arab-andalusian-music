# Line segmentation

Folder containing annotations at line level for both audio and score.

1. intermediary_files:
	- recording_annotations: Audio annotated at line livel in TextGrid format. Every Textgrid should contain 9 tiers, one provided by Amin 		Chachoo, and the rest annotated by the MTG. They are:
      1. Sections (Muassa', Mahzuz or Insiraf) (Provided By Amin)
      2. Vocal/Instrumental sections
      3. Sanaa' numeration
      4. Separation in verses
      5. Separation in half verses
      6. Separation in half verses (redundant)
      7. Lyric
      8. Structure of the melodic content (High level)
      9. Structure of the melodic content (Low level)

	- score_annotations: Score annotated at line level following the structure mu.1.1.1.s, to represent the start of the muassa for the 	first sana, for the first verse, for the firt line.

2. arab_andalusian_verses.csv: File with all the information from the line annotations
3. andalusian-VersesCSV.ipynb: Jupyter notebook to generate arab_andalusian_verses.csv
