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
  blogdown.hugo.version = "0.92.1"
)
