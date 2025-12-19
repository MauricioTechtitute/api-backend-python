$root = Get-Location

Write-Host "`n===== CONTENIDO DE ARCHIVOS PYTHON =====`n"

Get-ChildItem -Recurse -Filter *.py |
Where-Object {
    $_.FullName -notmatch "\\venv\\" -and
    $_.FullName -notmatch "__pycache__"
} |
Sort-Object FullName |
ForEach-Object {
    Write-Host "`n==============================="
    Write-Host "FILE: $($_.FullName.Replace($root.Path + '\',''))"
    Write-Host "==============================="
    Get-Content $_.FullName
}

Write-Host "`n===== FIN DEL DUMP ====="