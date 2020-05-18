proj_res_path=~/dev/proj/project-resources  # TODO use script path
proj_res_tex_path=$proj_res_path/templates/tex/bare

texme() {
  cp $proj_res_tex_path/bibliography.bib .
  cp $proj_res_tex_path/commands.tex .
  cp $proj_res_tex_path/content.tex .
  cp $proj_res_tex_path/Makefile .
}

bibme() {
  # TODO autocomplete bib entry types
}
