# Arab-Andalusian Music (AAM)
Folder Description:

1. sanaa_lyrics: Compilation of the sanaa lyrics for the Arab Andalusian music collection.
Available in both original script and transliterations, in csv and json format.

2. Scores-MusicXML: directory with the score transcriptions of the corpus recordings, each score named with the MBID (Music Brainz ID) of its corresponding recording.
   	- original_scores:
		the score transcriptions for some of the corpus recordings. In case any of the scores are found to diverge from the available transcription, it should be updated and committed to this directory. 
		
	- score_with_lyrics:
		some of the score transcriptions of the original_scores directory. These scores are annotated with their corresponding lyrics, but the actual lyrics are not used. Instead, the ‘code’ given to each line section (eg. mu.1.1.2) is written on the score portion it relates to.
	
	- sanaa_scores:
		- &lt;mbid&gt;/ contains scores corresponding to the individual san'ai. They are cut according to the annotatated scores from the folder score_with_lyrics. This more granular division facilitates individual san'a analysis. The identifier for each san'a is the same as that given by the TextGrid annotations (in.1, mu.2, etc). To date, the scores of only 2 out of the 5 annotated recordings have been broken into san'aa fragments.
		
3. annotation_csvs: contains all csv annotations and the scripts used to generate them.

	- layer_annotations:
    		- textgrid2csv.praat: praat script used to generate csv documents from layers of the annotated textgrid textgrid. To generate the csvs from a textgrid, modify the textgrid2csv.praat contents to use the number of the layer which you are interested in generating a csv for. This script must be run from within praat.
    		- &lt;mbid&gt;/: folder corresponding to each mbid
        		- &lt;mbid&gt;-vocIns.csv: csv of the Vocal/Instrumental annotations layer
                  	- &lt;mbid&gt;-sections.csv: csv of the sections annotation layer
		  	- &lt;mbid&gt;-contextual.csv: csv of the context annotation layer
		  	- &lt;mbid&gt;-structure.csv: csv of the structure annotation layer
			
	- score_annotations: csv corresponding to the annotated scores. annotations referenced by mbid. The annotations include the locations of lyrics at the level of line sections.
	- arab_andalusian_verses.csv: File with all the information from the current annotations
	- andalusian-VersesCSV.ipynb: Jupyter notebook to generate the above

	

4. Textgrid: Folder with all Textgrid files to-date, each named with the Music Brainz ID (mbid) of the recording it belongs to. Every Textgrid should contain 9 tiers, one provided by Amin Chachoo, and the rest annotated by the MTG. They are:
      1. Sections (Muassa', Mahzuz or Insiraf) (Provided By Amin)
      2. Vocal/Instrumental sections
      3. Sanaa' numeration
      4. Separation in verses
      5. Separation in half verses
      6. Separation in half verses (redundant)
      7. Lyric
      8. Structure of the melodic content (High level)
      9. Structure of the melodic content (Low level)
      
The Arab Andalusian Corpus in Dunya has more TextGrid files available for the recordings, but they only include the first layer. This folder only includes the TextGrids that have been further annotated by the MTG.
      


