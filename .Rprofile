source("~/.Rprofile")
options(
  browser = local({
    browser <- Sys.getenv("BROWSER")
    if (browser != "") return(browser)
    return(getOption("browser"))
  }),
  blogdown.ext = ".Rmd",
  blogdown.files_filter = function(x, ...) {
    x[!grepl(".*/examples/.*", x)]
  },
  # NOTE: requires hugo-extended e.g., `mise x hugo@extended_0.123.0` -- hugo server
  blogdown.hugo.version = "0.137.1"
)
