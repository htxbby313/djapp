@echo off
title DJ Streaming App Setup
echo ============================================
echo  🚀 Setting up DJ Streaming App...
echo ============================================
echo.

:: Check if Docker is installed
where docker >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker is not installed. Please install Docker first.
    pause
    exit
)

cd %~dp0

echo 🔹 Building Docker Containers...
docker-compose up -d --build

echo ✅ Setup Complete!
pause
exit
