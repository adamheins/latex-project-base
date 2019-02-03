# How to Write a Paper

## Structure
1. Introduction
  - Motivate the problem
  - Highlight existing approaches. This may also be in a separate related work
    section.
  - Introduce proposed approach
  - Compare proposed approach to existing approach and state why proposed
    approach is an improvement.
  - Indicate novelty of the proposed approach.
  - Describe the organization of the remainder of the paper.
2. Background Information
3. Theory and mathematics of proposed approach
4. Simulation and experimental results using proposed approach
5. Conclusion and discussion

## Appearance
* Do not cram things in - whitespace is your friend. This is especially true
  for equations and tables.
* Generate figures with a specific dimension and then *keep them at that
  size*. If you need to resize them, regenerate the figure.
* Keep your source files organized!
  - Split text across multiple LaTeX files (particularly if you're
    collaborating)
  - Use git to track versions. This way you won't accidentally delete
    anything and won't have to leave messy comments everywhere, and can
    collaborate effectively.
  - Use a bibtex file for references
* Don't label the plots within the figure; this is what the caption is for.
* Save plots in vector formats (PDF, EPS, SVG), so that LaTeX can deal with
  the resizing.

## Tips
1. Remember that plots and figures take the most time to create. Start these
   early!
2. Prefer plots to tables.
3. Pay attention to experimental design (see experimentals.md).
  - Ensure all of the relevant and interesting cases
  - Avoid any suspicious holes in the results, or at least provide reasonable
    explanations
  - Collect and present data in a systematic way
4. Organize all of the data you collect. Organize the hell out of it. Label it
   by content and by timestamp. Document your labeling method. Highlight the
   data that is used in each part of the actual paper. Back it up somewhere,
   along with any documentation or scripts required to interpret it. I cannot
   stress enough how important this is, in order to make your life easier and
   be prepared for any challenges to the research in the future.
