from os.path import abspath, dirname, join

projectName = "hardener"
author = "wan pu"
githubURL = "https://github.com/imwanpu/hardener"
version = "0.1.1"


shellScriptDir = join(dirname(abspath(__file__)), "shellScript")
packageDir = join(dirname(abspath(__file__)), "static")
indexPath = join(dirname(abspath(__file__)), "index.csv")
hostsPath = join(dirname(abspath(__file__)),"hosts.csv")

sourceDir = dirname(abspath(__file__))
targetDir = join("/tmp","hardener")