# Set the output log file name
$outputFile = "mic_usage_log.txt"

# Announce where the log is being stored
Write-Host "Logging microphone usage to $outputFile..."

# Start monitoring, print to the shell, and log to the file
adb logcat | Select-String -Pattern "AudioRecord" | Select-String -Pattern "set()" | ForEach-Object {
    $line = $_.Line
    Write-Host $line
    $line | Out-File -Append -FilePath $outputFile
}
