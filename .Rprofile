options(
  browser = local({
    browser <- getOption("browser")
    if (is.null(browser) || browser == "") return(Sys.getenv("BROWSER"))
    return(browser)
  }),
  blogdown.ext = ".Rmd",
  blogdown.files_filter = function(x, ...) {
    x[!grepl(".*/examples/.*", x)]
  },
  blogdown.hugo.version = "0.92.1"
)
