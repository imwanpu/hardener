Get-ChildItem -Path . -Recurse -Include *.py, *.ps1, *.md, *.sh, *.html, *.css, *.js | ForEach-Object {
    Get-Content $_.FullName
} | wc
