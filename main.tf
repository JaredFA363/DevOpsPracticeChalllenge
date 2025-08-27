resource "local_file" "html_file" {
  content = file("build/index.html")
  filename = "output_site/index.html"
}