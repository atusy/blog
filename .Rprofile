if("RSTUDIO" %in% names(Sys.getenv())) {

  #set Tokyo as default CRAN mirror server
  options(repos = structure(c(CRAN = "https://cran.ism.ac.jp/")))
  
  #Check for required packages and install missing ones
  installed <- rownames(utils::installed.packages())
  if(!('devtools' %in% installed))
    utils::install.packages('devtools')
  
  if(!('mytools' %in% installed))
    devtools::install_github('atusy/mytools')

  required <- c(
    'data.table',
    'dplyr',
    'ggplot2',
    'pipeR',
    'purrr',
    'stringr',
    'tidyr',
    'blogdown',
    'knitr'
  )
  
  if(!all(required %in% installed))
    utils::install.packages(
      required[required %in% installed],
      dependency = TRUE
    )
  
  
  #load libraries==============
  options(
    defaultPackages = c(
      getOption("defaultPackages"),
      required,
      'mytools',
      NULL
    )
  )
  
  rm(installed, required)
  
}

