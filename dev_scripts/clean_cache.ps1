Get-ChildItem -Recurse -Directory | Where-Object { $_.Name -match '__pycache__|.pytest_cache' } | Remove-Item -Recurse -Force