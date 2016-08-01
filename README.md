# Ranking Highlights in Personal Videos by Analyzing Edited Videos

## Introduction

This is the repository that contains the research code and some meta data for the paper:



## Citation

If you find the code and datasets useful in your research, please cite:

```
```

## Prerequisites

* Python 2.7
* NumPy
* JSON
* SciPy
* mlpy 3.5.0
* scikit-learn 0.17.1

## Contents

|  Folder/Files    | Description |
| ---|---|
| eval/rank.py | train and evaluate by mean average precision (mAP) |
| video*_*meta/vid*_*sel.json | lists of train / test YoutTube IDs for our datasets |
| video*_*meta/HL*_*labels/ | highlight labels for six domains of videos
| models/ | pre-trained Ranking SVM models

## Notations

1. `$Domain`: the keyword for each domain 
2. `$Vid`: video index (a hash key) used by YouTube. The link to the YouTube video is https://www.youtube.com/watch?v=$Vid. 

## Video list

* video*_*meta/vid*_*sel.json

	* The final splitset of our training / testing set 
	* All six domains: `viral`, `dog`, `Gymnastics`, `parkour`, `skiing`, `surfing`, `skating2`. 
	* YouTube IDs and their corresponding domains are formatted in this JSON file as
	
	```
	{"viral": 
			{"test": 
					["_xxORfve_APo", "_77ujXCz2VW0", ...],
			 "train":
					["_S0y-BPrJ9Nk", "_Wa-4HqGeVsQ", ...],
			 "turk":
					["_NLzZlwON9EM", "_jJJTd6ju9As", ...]},
	 ...
	}		
							
	```
	* There are three sets under each domain: `train`, `test` and `turk`. `turk` is a subset of `train` where its highlight moments are  labeled by AMT. 

## Definition of clip

Each clip is defined by [start*_*frame, end*_*frame].
For instance,
	
	[[0.0, 100.0], [50.0, 150.0], [100.0, 200.0]]

contains 3 clips. The first clip starts from frame 0 and ends at frame 100.

## Harvested Highlight
In each folder (e.g., `video_meta/HL_labels/$Domain/hard_labels/`), `$Vid.json` specifies if each clip is *matched* in the edited video (selected by user as highlight).
Label 1 denotes *matched* clip, label -1 denotes *unmatched* clip, and label 0 denotes borderline cases.
For instance,

	[[[0.0, 100.0], [50.0, 150.0], [100.0, 200.0]],[-1, 0, 1]]

means the first clip is not *matched*, the second clip is a borderline cae, and the last clip is a *matched* clip.

## Mturk Highlight
In each folder (e.g., `video_meta/HL_labels/$Domain/soft_labels/`), `Vid.json` specifies how many turkers select a clip as highlight.
For instance,

	[[[0.0, 100.0], [50.0, 150.0], [100.0, 200.0]],[2.0, 3.0, 0.0]]

means the first clip is selected by 2 people, the second clip is selected by 3 people,  and the last clip is not selected.
Note that turkers cast soft votes (i.e., not integer) depending on the coverage between the clip and tuker selected video segment.

 
## References
