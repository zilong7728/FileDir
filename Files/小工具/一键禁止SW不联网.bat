@echo off
setlocal enabledelayedexpansion

fltmc >nul 2>&1 || (
    echo 请右键选择【以管理员身份运行】
    pause
    exit
)

set "SW_PATH=I:\Program Files\SOLIDWORKS Corp"

echo 正在批量为目录下所有exe添加防火墙出站+入站阻止规则
echo 目录：%SW_PATH%
echo.

for /r "%SW_PATH%" %%a in (*.exe) do (
    set "FULLPATH=%%a"
    set "RULENAME=!FULLPATH:%SW_PATH%=!"
    set "RULENAME=Block!RULENAME:\=_!"
    set "RULENAME=!RULENAME: =_!"

    netsh advfirewall firewall show rule name="!RULENAME!_OUT" >nul
    if errorlevel 1 (
        netsh advfirewall firewall add rule name="!RULENAME!_OUT" dir=out action=block program="%%a" enable=yes profile=any >nul
        netsh advfirewall firewall add rule name="!RULENAME!_IN" dir=in action=block program="%%a" enable=yes profile=any >nul
        echo 已拦截：%%a
    ) else (
        echo 规则已存在：%%a
    )
)

echo.
echo =================完成=================
echo 如需解除限制，可执行以下命令批量删除本脚本添加的所有规则：
echo netsh advfirewall firewall delete rule name=all ^| findstr /C:"Block" 
echo （或手动：Windows防火墙→高级设置→出站/入站规则，删除所有 Block 开头规则）
pause
