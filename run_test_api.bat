@echo off
chcp 65001 >nul
title Pokemon Price Harvester - Running...
color 0a

echo ======================================================
echo 🚀 正在啟動 Pokemon 卡價收割機...
echo ======================================================

:: 1. 進入代碼所在資料夾 (確保路徑正確)
cd /d "%~dp0"

:: 2. 執行 Python 爬蟲
python test_api.py

:: 3. 檢查執行結果
if %ERRORLEVEL% NEQ 0 (
    color 0c
    echo.
    echo ❌ 程式執行出咗錯！請檢查上面嘅 Error Log。
) else (
    echo.
    echo ✅ 收割任務完成，數據已成功送往 Supabase。
)

echo.
echo --------------------------------------------------
echo 程式已行完。請睇上面有無紅色嘅 Error 字眼。
pause