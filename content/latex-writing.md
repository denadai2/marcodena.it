Title: Professional paper writing in Latex [2016]
Date: 2016-09-25 10:20
Category: Research
Exceprt: The definite guide to write articles and papers in Latex. This article helps you to design nice tables, avoid errors etc.

I have been through a lot of problems in my early times in academia and even now, I still don't remember some packages or methods to write a good article. For this reason, I here present some technical guidelines to write a paper in LaTex, some I wish I knew from the start. 


## Packages
I don't even try to explain the reason why Latex is so popular in academia. But, if you are still hesitant about it, I suggest to look at these slides before continuing.

### The indispensable

    \usepackage{graphicx} 
	\usepackage[pdftex]{hyperref}
	\usepackage{cleveref}

	\usepackage{booktabs}
	\usepackage{tabularx}

graphicx allows to include, shrink and rotate figures inside the text. It accepts vector files as input.
hyperref is a great tool to include links which I usually add in the text with the `\url` command, appending the accessing date information as well.

    \url{http://www.marcodena.it/blog/wordpress-the-future-is-static/} (accessing date: 09/10/2015)

This allows readers to know the availability of the resource and search for it (maybe in archive.org?). 
If you want to refer to sections, tables and images without even writing the element type name you are referring to, you can use cleveref. For example this code

    \begin{figure}
	   \includegraphics{image.pdf}
	   \label{fig:randomName}
	\end{figure}

	See \cref{fig:randomName}. \Cref{fig:randomName} is really cool!

will generate “See figure 1. Figure 1 is really cool!”. Cool, isn’t it?

#### Tables 
Default tables in Latex are UGLY, writers even worse, because they don't care about the visual aspect of the information they are putting in the tables.
![Latex table comparison](/images/tables_comparison.png)
Which one would you prefer? The second one is very neat, isn't it? However, the information displayed is the same. Hence, the difference stands on some nice visual rules[^3] that have to be applied in (IMHO) every article you write from now to the end of time.

* Avoid vertical lines;
* Avoid lines between rows different from the heading and the footer;
* Avoid the false-fancy-looking double horizontal lines;
* If in doubt, align left.

Hence, the next step is using the [booktabs](http://texcatalogue.sarovar.org/entries/booktabs.html) package, which provides some nice commands for the lines we will add to the tables. Then, we will increase the space between rows with the command `\ra{1.2}` and remove the space to the vertical edges (the first and the last column will not have unnecessary paddings anymore) with the `@{}` in the column specification (`\begin{tabularx}{\columnwidth}{@{}Xccc@{}}`).
Hence, in the header of your document include:

	\usepackage{booktabs}
	\newcommand{\ra}[1]{\renewcommand{\arraystretch}{#1}}

Then make the table in this way:

	\begin{table}[ht]
	    \centering
	    \ra{1.2}
	    \begin{tabularx}{\columnwidth}{@{}Xccc@{}}
	        \midrule
	        \textbf{City} & \textbf{\#Districts} & \textbf{Size (avg)} & \textbf{Population (avg)} \\ \toprule
	        Bologna & 23 & 3.34 & 15,918
	        \\
	        Florence & 21 & 2.89 & 16,633
	        \\
	        Milan & 85 & 1.72 & 14,551
	        \\
	        Palermo & 43 & 2.01 & 15,075 
	        \\
	        Rome & 146 & 3.24 & 17,312 
	        \\
	        Turin & 56 & 2.00 & 15,543 
	        \\
	         \bottomrule
	    \end{tabularx}
	    \caption{Number, average size and population of districts in the analyzed cities.}
	\end{table}

The result is this, instead of the second one:
![Nice table](/images/table_nice.png)
![Not so nice table](/images/table_not_so_nice.png)

### The nice to have
Some packages are not necessary, but still useful for everyday use.

#### Notes
Although there are a lot of websites which allows people to collaborate online and write documents together, I usually have to share PDF documents with my colleagues. Sending PDF documents creates a strange sense of officiality even if the content is still a draft. Thus, the package I personally like the most is todonotes. This package allows to create colored notes all around the pages, enclosed by nice boxes, allowing authors to share ideas, concepts and warnings that are not part of the real content.
![Nice table](/images/latex_todonotes.png)


I usually add this code to the preamble, which creates four commands for different purpose boxes that are self explainable from their names.

	\usepackage{xargs} 
	\usepackage[colorinlistoftodos,prependcaption,textsize=normal]{todonotes}
	\newcommandx{\unsure}[2][1=]{\todo[linecolor=red,backgroundcolor=red!25,bordercolor=red,#1]{#2}}
	\newcommandx{\change}[2][1=]{\todo[linecolor=blue,backgroundcolor=blue!25,bordercolor=blue,#1]{#2}}
	\newcommandx{\info}[2][1=]{\todo[linecolor=OliveGreen,backgroundcolor=OliveGreen!25,bordercolor=OliveGreen,#1]{#2}}
	\newcommandx{\improvement}[2][1=]{\todo[linecolor=Plum,backgroundcolor=Plum!25,bordercolor=Plum,#1]{#2}}
	\newcommandx{\thiswillnotshow}[2][1=]{\todo[disable,#1]{#2}}


#### Microtype

[Microtype](http://ctan.org/tex-archive/macros/latex/contrib/microtype) is one of the most useful packages, but it is known by too few people. It greatly improves general appearance of the text using different techniques, such as margin kerning (protrusion), extra kerning, expansion, tracking, and spacing[^4]. With the default configuration, Microtype optimize the text readability, and you can compare the effect by observing these two texts, where in the second one Microtype was applied:
![Microtype off](/images/latex-writing/Microtype_example_off.png)
![Microtype on](/images/latex-writing/Microtype_example_on.png)

Typesetting experts can observe the total interword spacing and appreciate the improved readability. Others can believe in the more positive effect in the reader when he faces the entire, optimized, document. Moreover, it is important to notice that text takes less space, an important feature when you don't have enough space in your papers.


#### siunitx

Shall you write in your paper km^2 or &#13218;? I prefer the second one. This is where [siunitx](https://www.ctan.org/pkg/siunitx) operates in two ways:

	\SI{10}{\metre}
	\si{\kilogram\metre\per\second} % Note no `\usk' here

and it has many standard units, including the ones coming from Computer science like MB, Gb etc.


## References
Academic references have to be modernized[^2] and the best way is to learn and share some general notions to create a better academia.
First, keep in mind that references in CrossRef, Mendeley and Google Scholar are incomplete and often bloated with unnecessary information[^1]. Then, remember that Google Scholar might be wrong and inconsistent, so don't blindly copy-paste the bibtex items from the website.
So, be sure to collect these details:

* Authors should be listed last name first, followed by a comma and initials (followed by full stops, ‘.’) of given names. This has to be repeated for all the authors up to a limit (usually five), and then use et al.;
* Full title of the book or conference/report/journal article;
* Name of the conference or journal where it is published;
* The date of publication if known, otherwise only the year. For books you can cite only the year;
* The number of publication / volume (for books and journal articles);
* The start page and end page numbers (in full). Write in a transparent way without abbreviations, for instance: pp. 150–179;
* The DOI permanent URL to the commercial text or article. If the open access version is available, put "Also available as...";
* The URL where readers can find the reference. This is (preferably) the author’s home university e-depository version, or other open access version, like [academia.edu](http://academia.edu) or [Research Gate](https://www.researchgate.net/). If the URL is not permanent, then give a shortened, non-permanent URL then add "Accessed on [give full date]".

Moreover, please remember that citations are not words, so instead of "The algorithm performed in [15]", write instead "Gigi et al [15] performed the algorithm". 
Finally, some tips: 

* Use non-breaking spaces before citation, to avoid linebreaks between text and citations: `Gigetti et al.~\cite{gigetti2015}`
* Group multiple citations and order them alphabetically. So, instead of `\cite{gigetti2015}\cite{brunelli1960}` do `\cite{brunelli1960, gigetti2015}`. Always alphabetize grouped citations so they appear in numerical order ([6,13] instead of [13,6]).





[^1]: [How should you be recording citations in the digital era?](https://medium.com/advice-and-help-in-authoring-a-phd-or-non-fiction/how-should-you-be-recording-citations-in-the-digital-era-97550a7c3da6#.heytswkvu).
[^2]: [Academic citation practices need to be modernized so that all references are digital and lead to full texts.](http://blogs.lse.ac.uk/impactofsocialsciences/2014/05/21/academic-citation-practices-need-to-be-modernized/).
[^3]: Rules learned thanks to this [nice presentation](https://www.inf.ethz.ch/personal/markusp/teaching/guides/guide-tables.pdf).
[^4]: I suggest everyone to read [this wounderful post](http://www.khirevich.com/latex/microtype/) about Microtype.


