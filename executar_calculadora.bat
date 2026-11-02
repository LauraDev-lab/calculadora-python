@echo off
title Calculadora Interativa em Python
cls
echo Iniciando a Calculadora Interativa...
echo.

where python >nul 2>nul
if %errorlevel% equ 0 (
    python main.py
    goto fim
)

where py >nul 2>nul
if %errorlevel% equ 0 (
    py main.py
    goto fim
)

echo [ERRO] O Python nao foi encontrado no PATH do sistema.
echo Certifique-se de que o Python esta instalado no seu computador.
echo.
pause

:fim
