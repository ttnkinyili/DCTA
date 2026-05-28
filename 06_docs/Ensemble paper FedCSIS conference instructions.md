# FedCSIS Conference Paper Template (Markdown version)

> Based on the OpenDocument template for FedCSIS proceedings.
> Follow these instructions closely. Do not modify fonts or spacing in the final submission.

---

**Abstract**---This document describes the rules one should follow to prepare the article for the FedCSIS e-proceedings. The abstract may be up to 150 words. This template was converted from one in the OpenDocument Format. If you are not able to submit your contribution in OpenDocument format, use this document as a template and follow instructions as close as possible. Do not modify any fonts, paragraph formatting attributes, etc. Use corresponding styles for text elements. Do not cite references in the abstract. Do not delete the blank line immediately above the abstract; it sets the footnote at the bottom of this column.

**OpenDocument Template for Preparation of Papers for FedCSIS Conference**

**Index Terms**---FedCSIS, article preparation, open document format.

## Introduction

This document is an OpenDocument template for preparing an article for FedCSIS proceedings and to be placed in IEEE Xplore digital library. To create your own document, from within your favorite text processor, open a file `fedcsis.odt` and replace this text with your own, or simply cut and paste text from another document piece by piece and use markup styles. The style will adjust your fonts and line spacing. ***Do not change the font sizes or line spacing to squeeze more text into a limited number of pages.***

## Styles

The document template contains different styles for appropriate text elements. Most styles are divided into two classes: paragraph styles and symbol styles.

Paragraph styles are applicable to paragraph-like elements of text: paragraphs, headings, picture or table captions, author name and affiliation, etc. To apply a paragraph style just place cursor on the desired element and choose appropriate style from style list.

Symbol styles are applicable to text elements which are not paragraphs, but only certain part of it. For example, URL, file name or the first word in the first paragraph. To apply a text style, select desired element and choose appropriate style from a list.

## Document Structure

### Title

The title of the document is placed in appropriate frame on the top of the document and is formatted with style Title. Do not capitalize short words (a, and, the, and so on).

### Authors

Authors' names and affiliations are input in the table placed under the title. Each author's data are input in separate table cell. Adjust the number of cells. First paragraph in the cell is the author's name (authors' names in case several authors have the same affiliation), style AuthorsN. The second paragraph contains author's affiliation, style AuthorsA. You can use soft line breaks (CTRL+ENTER) if necessary.

### ORCID

Place ORCIDs of all the authors in the line next to author's name. Use the AuthorsA style.

### Abstract

Abstract is placed in the first paragraph. It is formatted with the Abstract style. The length of the abstract should not exceed 150 words. The word "abstract" and the dash should have style Word Abstract applied.

### Keywords

Keywords are placed in the next to the abstract paragraph. It is formatted in the same way as the abstract. Note the usage of *Index Terms* instead of *Keywords*.

### Paragraphs

All the paragraphs should be formatted with the Text style. The first paragraph should be of the First Paragraph style. This style implements the initial drop cap letter.

### Headings

There are standard Heading N styles for headings. Please, use TAB and SHIFT+TAB for adjusting the level of headings numbering. In most text processors you should place cursor just after the number (letter) of the header and hit TAB (SHIFT+TAB) to shift to the next (previous) level. As a rule you should hit tab after selecting the Heading 2 style to input a new heading of level 2.

### Initial Drop Cap Letter

The first letter of a journal paper is a large, capital, oversized letter which descends one line below the baseline. Such a letter is called a "drop cap" letter. The other letters in the first word are rendered in upper case. This effect can be accurately produced using the First Paragraph style for the first paragraph and the First Word style for the letters of the first word.

Note that the second word should also be rendered in upper case if the first word is very short (less than 3 letters).

![Fig 1. Sinusoid](media/image1.png)

**Fig 1. Sinusoid**

## Text Fragments

To emphasize use Emphasis and Strong styles. For code fragments use Code style, for URLs standard Hyperlink style, for file names -- File Name style.

## Figures and Tables

Prepare your figures using vector graphics. Photo pictures should be of high resolution (at least 300 DPI). If your graphical editor is Microsoft Office, try to copy your Excel chart and paste it in OpenOffice Draw. Then use Export as EPS option.

Position figures and tables at the tops and bottoms of columns. Avoid placing them in the middle of columns. Large figures and tables may span across both columns. Figure captions should be below the figures; table captions should be above the tables. Avoid placing figures and tables before their first mention in the text. Use the abbreviation "Fig. 1," even at the beginning of a sentence. Do not abbreviate "Table." Tables are numbered with Roman numerals.

Pay attention that the figure caption is placed *below* the figure, while the table caption is placed *above* the table (cf. Table I). Figures or tables may span both columns, if necessary. If needed, use a copy of the frame of the table I in your article. Otherwise, please delete this entire frame.

**Table I.** Defining characteristics of five early digital computers

| Computer | First operation | Place | Decimal/Binary | Electronic | Programmable | Turing complete |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Zuse Z3 | May 1941 | Germany | binary | No | By punched film stock | Yes (1998) |
| Atanasoff-Berry Computer | Summer 1941 | USA | binary | Yes | No | No |
| Colossus | 1943–1944 | UK | binary | Yes | Partially, by rewiring | No |
| Harvard Mark I–IBM ASCC | 1944 | USA | decimal | No | By punched paper tape | Yes (1998) |
| ENIAC | 1944 | USA | decimal | Yes | Partially, by rewiring | Yes |
| | 1948 | USA | decimal | Yes | By Function Table ROM | Yes |

## Math

Mathematical equations should be typeset using MathML markup. For displayed equation use an equation paragraph style. Place the equation after the first tab and equation number, if any, after the second. Number equations consecutively with equation numbers in parentheses.

$$
\frac{1}{\sqrt{2\pi}}\int e^{\frac{-x^{2}}{2}}dx = 1 \qquad (1)
$$

## References

Number citations consecutively in square brackets [1]. The sentence punctuation follows the brackets [2]. Multiple references [2], [3] are each numbered with separate brackets [1]–[3]. When citing a section in a book, please give the relevant page numbers [2]. In sentences, refer simply to the reference number, as in [3]. Do not use "Ref. [3]" or "reference [3]" except at the beginning of a sentence: "Reference [3] shows ... ." Type the reference list at the end of the paper using the "References" style.

Please note that the references at the end of this document are in the preferred referencing style. Give all authors' names; do not use "*et al.*" unless there are six authors or more. Use a space after authors' initials. Papers that have not been published should be cited as "unpublished" [4]. Papers that have been submitted for publication should be cited as "submitted for publication" [5]. Papers that have been accepted for publication, but not yet specified for an issue should be cited as "to be published" [6]. Please give affiliations and addresses for private communications [7].

Capitalize only the first word in a paper title, except for proper nouns and element symbols. If you are short of space, you may omit paper titles. However, paper titles are helpful to your readers and are strongly recommended. For papers published in translation journals, please give the English citation first, followed by the original foreign-language citation [8].

### DOI

Please, add a DOI information to your bibliography using the format of the reference [24].

## Abbreviations and Acronyms

Define abbreviations and acronyms the first time they are used in the text, even after they have already been defined in the abstract. Abbreviations such as IEEE, SI, ac, and dc do not have to be defined. Abbreviations that incorporate periods should not have spaces: write "C.N.R.S.," not "C. N. R. S." Do not use abbreviations in the title unless they are unavoidable (for example, "IEEE" in the title of this article).

## Other Recommendations

Use one space after periods and colons. Hyphenate complex modifiers: "zero-field-cooled magnetization." Avoid dangling participles, such as, "Using (1), the potential was calculated." [It is not clear who or what used (1).] Write instead, "The potential was calculated by using (1)," or "Using (1), we calculated the potential."

Use a zero before decimal points: "0.25," not ".25."

A parenthetical statement at the end of a sentence is punctuated outside of the closing parenthesis (like this). (A parenthetical sentence is punctuated within the parentheses.) In American English, periods and commas are within quotation marks, like "this period." Other punctuation is "outside"! Avoid contractions; for example, write "do not" instead of "don't." The serial comma is preferred: "A, B, and C" instead of "A, B and C."

If you wish, you may write in the first person singular or plural and use the active voice ("I observed that ..." or "We observed that ..." instead of "It was observed that ..."). Remember to check spelling. If your native language is not English, please get a native English-speaking colleague to proofread your paper.

Number footnotes separately in superscripts (Insert | Footnote).[^2] Place the actual footnote at the bottom of the column in which it is cited; do not put footnotes in the reference list (endnotes).

Use manual column break for column balancing if necessary.

## Some Common Mistakes

The word "data" is plural, not singular.

Be aware of the different meanings of the homophones "affect" (usually a verb) and "effect" (usually a noun), "complement" and "compliment," "discreet" and "discrete," "principal" (e.g., "principal investigator") and "principle" (e.g., "principle of measurement"). Do not confuse "imply" and "infer."

Prefixes such as "non," "sub," "micro," "multi," and "ultra" are not independent words; they should be joined to the words they modify, usually without a hyphen. There is no period after the "et" in the Latin abbreviation "*et al.*" (it is also italicized). The abbreviation "i.e.," means "that is," and the abbreviation "e.g.," means "for example" (these abbreviations are not italicized).

Microsoft Office is not a graphical editor.

An excellent style manual and source of information for science writers is [9]. A general IEEE style guide, *Information for Authors,* is available at <http://www.ieee.org/organizations/pubs/transactions/information.htm>

## Conclusion

A conclusion section is not required. Although a conclusion may review the main points of the paper, do not replicate the abstract as the conclusion. A conclusion might elaborate on the importance of the work or suggest applications and extensions.

## Submission

Submitting the article, please, provide

- Reviewing:
  - PDF file with the article. PDF will be sent to the referees.

- Final version:
  - PDF file with the article.
  - The source of the article.

## Appendix

Appendixes, if needed, appear before the acknowledgment.

## Acknowledgment

The preferred spelling of the word "acknowledgment" in American English is without an "e" after the "g." Use the singular heading even if you have many acknowledgments. Avoid expressions such as "One of us (S. B. A.) would like to thank ... ." Instead, write "F. A. Author thanks ... ." ***Sponsor and financial support acknowledgments are placed in the unnumbered footnote on the first page.***

## References

1.  G. O. Young, "Synthetic structure of industrial plastics (Book style with paper title and editor)," in *Plastics*, 2nd ed. vol. 3, J. Peters, Ed. New York: McGraw-Hill, 1964, pp. 15–64.
2.  W.-K. Chen, *Linear Networks and Systems* (Book style). Belmont, CA: Wadsworth, 1993, pp. 123–135.
3.  H. Poor, *An Introduction to Signal Detection and Estimation*. New York: Springer-Verlag, 1985, ch. 4.
4.  B. Smith, "An approach to graphs of linear forms (Unpublished work style)," unpublished.
5.  E. H. Miller, "A note on reflector arrays (Periodical style---Accepted for publication)," *IEEE Trans. Antennas Propagat.*, to be published.
6.  J. Wang, "Fundamentals of erbium-doped fiber amplifiers arrays (Periodical style---Submitted for publication)," *IEEE J. Quantum Electron.*, submitted for publication.
7.  C. J. Kaufman, Rocky Mountain Research Lab., Boulder, CO, private communication, May 1995.
8.  Y. Yorozu, M. Hirano, K. Oka, and Y. Tagawa, "Electron spectroscopy studies on magneto-optical media and plastic substrate interfaces (Translation Journals style)," *IEEE Transl. J. Magn.Jpn.*, vol. 2, Aug. 1987, pp. 740–741 [*Dig. 9th Annu. Conf. Magnetics* Japan, 1982, p. 301].
9.  M. Young, *The Technical Writers Handbook.* Mill Valley, CA: University Science, 1989.
10. J. U. Duncombe, "Infrared navigation---Part I: An assessment of feasibility (Periodical style)," *IEEE Trans. Electron Devices*, vol. ED-11, pp. 34–39, Jan. 1959.
11. S. Chen, B. Mulgrew, and P. M. Grant, "A clustering technique for digital communications channel equalization using radial basis function networks," *IEEE Trans. Neural Networks*, vol. 4, pp. 570–578, July 1993.
12. R. W. Lucky, "Automatic equalization for digital communication," *Bell Syst. Tech. J.*, vol. 44, no. 4, pp. 547–588, Apr. 1965.
13. S. P. Bingulac, "On the compatibility of adaptive controllers (Published Conference Proceedings style)," in *Proc. 4th Annu. Allerton Conf. Circuits and Systems Theory*, New York, 1994, pp. 8–16.
14. G. R. Faulhaber, "Design of service systems with priority reservation," in *Conf. Rec. 1995 IEEE Int. Conf. Communications*, pp. 3–8.
15. W. D. Doyle, "Magnetization reversal in films with biaxial anisotropy," in *1987 Proc. INTERMAG Conf.*, pp. 2.2-1–2.2-6.
16. G. W. Juette and L. E. Zeffanella, "Radio noise currents in short sections on bundle conductors (Presented Conference Paper style)," presented at the IEEE Summer Power Meeting, Dallas, TX, June 22–27, 1990, Paper 90 SM 690-0 PWRS.
17. J. G. Kreifeldt, "An analysis of surface-detected EMG as an amplitude-modulated noise," presented at the 1989 Int. Conf. Medicine and Biological Engineering, Chicago, IL.
18. J. Williams, "Narrow-band analyzer (Thesis or Dissertation style)," Ph.D. dissertation, Dept. Elect. Eng., Harvard Univ., Cambridge, MA, 1993.
19. N. Kawasaki, "Parametric study of thermal and chemical nonequilibrium nozzle flow," M.S. thesis, Dept. Electron. Eng., Osaka Univ., Osaka, Japan, 1993.
20. J. P. Wilkinson, "Nonlinear resonant circuit devices (Patent style)," U.S. Patent 3 624 12, July 16, 1990.
21. *IEEE Criteria for Class IE Electric Systems* (Standards style), IEEE Standard 308, 1969.
22. *Letter Symbols for Quantities*, ANSI Standard Y10.5-1968.
23. R. E. Haskell and C. T. Case, "Transient signal propagation in lossless isotropic plasmas (Report style)," USAF Cambridge Res. Lab., Cambridge, MA Rep. ARCRL-66-234 (II), 1994, vol. 2.
24. Ghosh, M.K., M.L. Harter. 2003. "A viral mechanism for remodeling chromatin structure in G0 cells." *Mol. Cell.* 12:255–260, http://dx.doi.org/10.1016/S1097-2765(03)00225-9

---

[^1]: This work was not supported by any organization

[^2]: It is recommended that footnotes be avoided (except for the unnumbered footnote with the receipt date on the first page). Instead, try to integrate the footnote information into the text.