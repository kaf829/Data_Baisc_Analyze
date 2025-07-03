# --------------------------------------------
# PowerShell Script: setup_tensorflow_gpu.ps1
# --------------------------------------------

Write-Host "🎯 Starting TensorFlow GPU environment setup..."

$cudaPath = "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8"
if (!(Test-Path $cudaPath)) {
    Write-Error "❌ CUDA 11.8 path not found: $cudaPath"
    exit
}

# 2. Set environment variables
[System.Environment]::SetEnvironmentVariable("CUDA_PATH", $cudaPath, "Machine")
$envPaths = [System.Environment]::GetEnvironmentVariable("Path", "Machine")

$neededPaths = @(
    "$cudaPath\bin",
    "$cudaPath\libnvvp"
)

foreach ($p in $neededPaths) {
    if ($envPaths -notlike "*$p*") {
        $envPaths += ";$p"
    }
}

[System.Environment]::SetEnvironmentVariable("Path", $envPaths, "Machine")
Write-Host "✅ CUDA environment variables configured."

Write-Host "📦 Downloading and installing Visual C++ Redistributable..."
$vcInstaller = "$env:TEMP\vc_redist.x64.exe"
Invoke-WebRequest "https://aka.ms/vs/17/release/vc_redist.x64.exe" -OutFile $vcInstaller
Start-Process -FilePath $vcInstaller -ArgumentList "/install", "/quiet", "/norestart" -Wait
Remove-Item $vcInstaller
Write-Host "✅ Visual C++ Redistributable installed."

Write-Host "🐍 Creating Python virtual environment (.venv)..."
python -m
