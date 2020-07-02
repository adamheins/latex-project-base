proj_res_path=~/sw/latex-project-base  # TODO use script path
proj_res_tex_path=$proj_res_path/templates/tex/bare

texme() {
  # -a flag preserves symlinks (among other things)
  cp -a $proj_res_tex_path/bibliography.bib .
  cp -a $proj_res_tex_path/commands.tex .
  cp -a $proj_res_tex_path/content.tex .
  cp -a $proj_res_tex_path/Makefile .
}
